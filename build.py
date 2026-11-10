#!/usr/bin/env python3
"""Build the nonprofit audit page for every partner in partners/.

For each partners/<SLUG>.json this writes:
  dist/<SLUG>-audit.js    the embed loader (what the GHL snippet points to)
  dist/<SLUG>-audit.html  the same page as one paste-in block (no hosting needed)
  preview/<SLUG>.html     the page inside a narrow fake GHL row, to check the breakout
and refreshes index.html.

Run:  python3 build.py
"""
import datetime
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
TEMPLATE = (ROOT / "src" / "MLP-TEMPLATE-nonprofit-audit.html").read_text()
PAGES_BASE = "https://mylaunchpartner.github.io/mlp-nonprofit-audit"

# Shared runtime: frees GHL wrappers that clip the breakout, then mounts the GHL form.
RUNTIME_JS = r"""
function mlpnpUnclip(el){
  for(var p=el.parentElement;p&&p!==document.body;p=p.parentElement){
    var cs=getComputedStyle(p);
    if(cs.overflowX==='hidden'||cs.overflowX==='clip'||cs.overflow==='hidden'){p.style.overflow='visible';}
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
  if(!document.querySelector('script[src*="form_embed.js"]')){
    var s=document.createElement('script');
    s.src='https://link.msgsndr.com/js/form_embed.js';
    document.body.appendChild(s);
  }
}
"""


def fmt_date(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def render(p):
    e = lambda s: html.escape(str(s), quote=True)
    end = p.get("endDate", "").strip()
    days = str(p.get("turnaroundDays", "")).strip()
    vals = {
        "partner": e(p["partner"]),
        "donateUrl": e(p["donateUrl"]),
        "partnerUrl": e(p["partnerUrl"]),
        "partnerBlurbHtml": "\n        ".join(f"<p>{e(x)}</p>" for x in p["partnerBlurb"]),
        "legalLine": e(p["legalLine"]),
        "cap": e(p["cap"]),
        "endLine": f" Ends {fmt_date(end)} at 11:59 PM MST (Arizona time)." if end else "",
        "endFine": f", or until 11:59 PM MST (Arizona time) on {fmt_date(end)}, whichever comes first" if end else "",
        "turnaroundLine": f" within {e(days)} business days" if days else "",
    }
    out = TEMPLATE
    for k, v in vals.items():
        out = out.replace("{{" + k + "}}", v)
    assert "{{" not in out, "unfilled token in template"
    # Drop the template's own header comment; each output gets its own label.
    return out.split("\n", 1)[1]


def build_js(p, page):
    slug = p["slug"]
    return f"""/* {slug} | Nonprofit audit page embed loader. Built by build.py, do not edit by hand.
   GHL snippet:
   <div id="mlpnp-audit" data-form-id="YOUR_GHL_FORM_ID"></div>
   <script src="{PAGES_BASE}/dist/{slug}-audit.js"></script>
*/
(function(){{
  var HTML={json.dumps(page)};
  var DEFAULT_FORM={json.dumps(p.get("ghlFormId", ""))};
  var PARTNER={json.dumps(p["partner"])};
{RUNTIME_JS}
  var me=document.currentScript;
  var host=document.getElementById('mlpnp-audit');
  if(!host){{host=document.createElement('div');host.id='mlpnp-audit';if(me&&me.parentNode){{me.parentNode.insertBefore(host,me);}}else{{document.body.appendChild(host);}}}}
  host.innerHTML=HTML;
  var root=host.querySelector('#mlpnp-root');
  mlpnpUnclip(root);
  var attr=(host.getAttribute('data-form-id')||'').trim();
  if(!attr||/PASTE|YOUR_/i.test(attr)){{attr=DEFAULT_FORM;}}
  mlpnpForm(root,attr,PARTNER);
}})();
"""


def build_paste(p, page):
    slug = p["slug"]
    form = json.dumps(p.get("ghlFormId", ""))
    return f"""<!-- {slug} | Nonprofit audit page, FULL PAGE paste-in version. Paste into ONE Code element in a full-width, 0-padding section.
     Built by build.py. Set "ghlFormId" in partners/{slug}.json and rebuild, or edit FORM_ID below. -->
{page}
<script>
(function(){{
  var FORM_ID={form};
{RUNTIME_JS}
  var root=document.getElementById('mlpnp-root');
  mlpnpUnclip(root);
  mlpnpForm(root,FORM_ID,{json.dumps(p["partner"])});
}})();
</script>
"""


def build_preview(p):
    slug = p["slug"]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(p["partner"])} audit page preview</title>
<style>
body{{margin:0;font-family:system-ui,sans-serif;background:#e8e8e8}}
.fake-ghl-header{{background:#fff;padding:20px;text-align:center;border-bottom:1px solid #ccc}}
.fake-ghl-row{{max-width:640px;margin:0 auto;padding:30px;background:#fafafa;overflow:hidden}}
.fake-ghl-row p{{color:#555;font-size:14px;margin:0 0 12px}}
</style>
</head>
<body>
<div class="fake-ghl-header">Preview: the page sits in a 640px boxed row with padding and overflow hidden, like a default GHL section. It should still fill the whole window width.</div>
<div class="fake-ghl-row">
<p>[GHL row starts here]</p>
<div id="mlpnp-audit" data-form-id=""></div>
<script src="../dist/{slug}-audit.js"></script>
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
        page = render(p)
        (ROOT / "dist" / f"{slug}-audit.js").write_text(build_js(p, page))
        (ROOT / "dist" / f"{slug}-audit.html").write_text(build_paste(p, page))
        (ROOT / "preview" / f"{slug}.html").write_text(build_preview(p))
        links.append(f'<li><a href="preview/{slug}.html">{html.escape(p["partner"])}</a></li>')
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
