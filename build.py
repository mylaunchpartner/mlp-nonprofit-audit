#!/usr/bin/env python3
"""Build every nonprofit audit funnel page for every partner in partners/.

Funnel steps (one GHL funnel per partner, one Code element per step):
  1. audit      - landing page + claim form          dist/<SLUG>-audit.js
  2. thank-you  - claim received, link to step 3     dist/<SLUG>-thank-you.js
  3. book       - book the audit walkthrough call    dist/<SLUG>-book.js

Each step also gets a paste-in version (dist/<SLUG>-<step>.html) and a preview inside a
narrow fake GHL row (preview/<SLUG>-<step>.html). index.html lists the previews.

Run:  python3 build.py
"""
import datetime
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "src"
SHARED_HEAD = (SRC / "MLP-TEMPLATE-shared-head.html").read_text().split("\n", 1)[1]
STEPS = {
    "audit": "MLP-TEMPLATE-nonprofit-audit.html",
    "thank-you": "MLP-TEMPLATE-thank-you.html",
    "book": "MLP-TEMPLATE-book.html",
}
PAGES_BASE = "https://mylaunchpartner.github.io/mlp-nonprofit-audit"

# Shared runtime for every page.
RUNTIME_JS = r"""
function mlpnpUnclip(el){
  for(var p=el.parentElement;p&&p!==document.body;p=p.parentElement){
    var cs=getComputedStyle(p);
    if(cs.overflowX==='hidden'||cs.overflowX==='clip'||cs.overflow==='hidden'){p.style.overflow='visible';}
  }
}
function mlpnpEmbedScript(){
  if(!document.querySelector('script[src*="form_embed.js"]')){
    var s=document.createElement('script');
    s.src='https://link.msgsndr.com/js/form_embed.js';
    document.body.appendChild(s);
  }
}
function mlpnpForm(root,formId,partner){
  var box=root.querySelector('[data-mlpnp-form]');
  if(!box)return;
  if(!formId||/PASTE|YOUR_/i.test(formId)){
    box.innerHTML='<p class="mlpnp-formnote">The claim form opens soon. Keep your donation receipt handy and check back shortly.</p>';
    return;
  }
  var f=document.createElement('iframe');
  f.src='https://api.leadconnectorhq.com/widget/form/'+encodeURIComponent(formId)+'?partner_nonprofit='+encodeURIComponent(partner);
  f.id='inline-'+formId;
  f.title='Claim your free audit';
  f.setAttribute('data-layout',"{'id':'INLINE'}");
  f.setAttribute('data-trigger-type','alwaysShow');
  f.setAttribute('data-trigger-value','');
  f.setAttribute('data-activation-type','alwaysActivated');
  f.setAttribute('data-activation-value','');
  f.setAttribute('data-deactivation-type','neverDeactivate');
  f.setAttribute('data-deactivation-value','');
  f.setAttribute('data-layout-iframe-id','inline-'+formId);
  f.setAttribute('data-form-id',formId);
  box.appendChild(f);
  mlpnpEmbedScript();
}
function mlpnpCalendar(root,slug){
  var box=root.querySelector('[data-mlpnp-calendar]');
  if(!box||!slug)return;
  var f=document.createElement('iframe');
  f.src='https://api.leadconnectorhq.com/widget/bookings/'+encodeURIComponent(slug)+(location.search||'');
  f.id=slug+'_mlpnp';
  f.title='Book your audit walkthrough';
  f.setAttribute('scrolling','no');
  box.appendChild(f);
  mlpnpEmbedScript();
}
function mlpnpKeepQuery(root){
  if(!location.search)return;
  var links=root.querySelectorAll('[data-mlpnp-keepquery]');
  for(var i=0;i<links.length;i++){
    var h=links[i].getAttribute('href')||'';
    links[i].setAttribute('href',h+(h.indexOf('?')>-1?'&':'?')+location.search.slice(1));
  }
}
function mlpnpMount(root,cfg){
  mlpnpUnclip(root);
  mlpnpKeepQuery(root);
  mlpnpForm(root,cfg.formId,cfg.partner);
  mlpnpCalendar(root,cfg.calendarSlug);
}
"""


def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def render(step, p):
    e = lambda s: html.escape(str(s), quote=True)
    end = p.get("endDate", "").strip()
    days = str(p.get("turnaroundDays", "")).strip()
    vals = {
        "sharedHead": SHARED_HEAD,
        "partner": e(p["partner"]),
        "donateUrl": e(p["donateUrl"]),
        "partnerUrl": e(p["partnerUrl"]),
        "bookUrl": e(p.get("bookUrl", "")),
        "partnerBlurbHtml": "\n        ".join(f"<p>{e(x)}</p>" for x in p["partnerBlurb"]),
        "legalLine": e(p["legalLine"]),
        "cap": e(p["cap"]),
        "endLine": f" Ends {fmt_date(end)} at 11:59 PM MST (Arizona time)." if end else "",
        "endFine": f", or until 11:59 PM MST (Arizona time) on {fmt_date(end)}, whichever comes first" if end else "",
        "turnaroundLine": f" within {e(days)} business days" if days else "",
    }
    out = (SRC / STEPS[step]).read_text()
    for k, v in vals.items():
        out = out.replace("{{" + k + "}}", v)
    assert "{{" not in out, f"unfilled token in {step} template"
    return out.split("\n", 1)[1]


def cfg_js(p, step):
    return json.dumps({
        "partner": p["partner"],
        "formId": p.get("ghlFormId", "") if step == "audit" else "",
        "calendarSlug": p.get("calendarSlug", "") if step == "book" else "",
    })


def build_js(p, step, page):
    slug = p["slug"]
    return f"""/* {slug} | Nonprofit audit funnel, step "{step}". Built by build.py, do not edit by hand.
   GHL snippet (one Code element in a full-width, 0-padding section):
   <div id="mlpnp-audit"></div>
   <script src="{PAGES_BASE}/dist/{slug}-{step}.js"></script>
*/
(function(){{
  var HTML={json.dumps(page)};
  var CFG={cfg_js(p, step)};
{RUNTIME_JS}
  var me=document.currentScript;
  var host=document.getElementById('mlpnp-audit');
  if(!host){{host=document.createElement('div');host.id='mlpnp-audit';if(me&&me.parentNode){{me.parentNode.insertBefore(host,me);}}else{{document.body.appendChild(host);}}}}
  host.innerHTML=HTML;
  var attr=(host.getAttribute('data-form-id')||'').trim();
  if(attr&&!/PASTE|YOUR_/i.test(attr)){{CFG.formId=attr;}}
  mlpnpMount(host.querySelector('#mlpnp-root'),CFG);
}})();
"""


def build_paste(p, step, page):
    slug = p["slug"]
    return f"""<!-- {slug} | Nonprofit audit funnel, step "{step}", FULL PAGE paste-in version. Paste into ONE Code element in a full-width, 0-padding section. Built by build.py. -->
{page}
<script>
(function(){{
  var CFG={cfg_js(p, step)};
{RUNTIME_JS}
  mlpnpMount(document.getElementById('mlpnp-root'),CFG);
}})();
</script>
"""


def build_preview(p, step):
    slug = p["slug"]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p["partner"])} {step} preview</title>
<style>
body{{margin:0;font-family:system-ui,sans-serif;background:#e8e8e8}}
.fake-ghl-header{{background:#fff;padding:20px;text-align:center;border-bottom:1px solid #ccc}}
.fake-ghl-row{{max-width:640px;margin:0 auto;padding:30px;background:#fafafa;overflow:hidden}}
.fake-ghl-row p{{color:#555;font-size:14px;margin:0 0 12px}}
</style>
</head>
<body>
<div class="fake-ghl-header">Preview of step "{step}" inside a 640px boxed row with padding and overflow hidden, like a default GHL section. It should still fill the whole window width.</div>
<div class="fake-ghl-row">
<p>[GHL row starts here]</p>
<div id="mlpnp-audit"></div>
<script src="../dist/{slug}-{step}.js"></script>
<p>[GHL row ends here]</p>
</div>
</body>
</html>
"""


def main():
    (ROOT / "dist").mkdir(exist_ok=True)
    (ROOT / "preview").mkdir(exist_ok=True)
    links = []
    for f in sorted((ROOT / "partners").glob("*.json")):
        p = json.loads(f.read_text())
        slug = p["slug"]
        for step in STEPS:
            page = render(step, p)
            (ROOT / "dist" / f"{slug}-{step}.js").write_text(build_js(p, step, page))
            (ROOT / "dist" / f"{slug}-{step}.html").write_text(build_paste(p, step, page))
            (ROOT / "preview" / f"{slug}-{step}.html").write_text(build_preview(p, step))
            links.append(f'<li><a href="preview/{slug}-{step}.html">{html.escape(p["partner"])}: {step}</a></li>')
        print("built", slug)
    (ROOT / "index.html").write_text(
        "<!doctype html><html lang=\"en\"><head><meta charset=\"utf-8\">"
        "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
        "<title>MLP nonprofit audit pages</title></head>"
        "<body style=\"font-family:system-ui,sans-serif;max-width:640px;margin:40px auto;padding:0 16px\">"
        "<h1>MLP nonprofit audit pages</h1><p>Previews:</p><ul>" + "".join(links) + "</ul></body></html>\n"
    )


if __name__ == "__main__":
    main()
