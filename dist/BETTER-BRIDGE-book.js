/* BETTER-BRIDGE | Nonprofit audit funnel, step "book". Built by build.py, do not edit by hand.
   GHL snippet (one Code element in a full-width, 0-padding section):
   <div id="mlpnp-audit"></div>
   <script src="https://mylaunchpartner.github.io/mlp-nonprofit-audit/dist/BETTER-BRIDGE-book.js"></script>
*/
(function(){
  var HTML="<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n<link rel=\"preconnect\" href=\"https://fonts.gstatic.com\" crossorigin>\n<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Space+Grotesk:wght@500;600;700&display=swap\">\n<style>\n/* Full-width breakout: escapes GHL's boxed row/column no matter how narrow it is. */\nhtml,body{overflow-x:clip}\n.mlpnp{position:relative;left:50%;width:100vw;max-width:100vw;margin-left:-50vw!important;margin-right:0!important}\n.mlpnp,.mlpnp *,.mlpnp *::before,.mlpnp *::after{box-sizing:border-box}\n.mlpnp{\n  --np-navy:#102a42;--np-navy-deep:#0a1b2b;--np-amber:#e9a25b;--np-amber-deep:#b8692a;--np-brown:#6b4a1f;\n  --np-cream:#f6f4ef;--np-line:#d9d3c7;--np-ink:#1c2430;--np-muted-on-navy:#d5dde6;--np-foot:#c7d0da;\n  --np-display:'Space Grotesk',system-ui,sans-serif;--np-body:'Inter',system-ui,-apple-system,'Segoe UI',sans-serif;\n  font-family:var(--np-body);font-size:17px;line-height:1.55;color:var(--np-ink);background:var(--np-cream);\n  text-align:left;-webkit-font-smoothing:antialiased\n}\n.mlpnp p,.mlpnp h1,.mlpnp h2,.mlpnp h3,.mlpnp ul,.mlpnp li{margin:0;padding:0;color:inherit;font-family:inherit;font-size:inherit;font-weight:inherit;line-height:inherit;letter-spacing:normal;text-transform:none;text-align:left}\n.mlpnp h1,.mlpnp h2,.mlpnp h3{font-weight:600}\n.mlpnp a{color:var(--np-navy)}\n.mlpnp a:hover{color:var(--np-navy-deep)}\n.mlpnp :focus-visible{outline:3px solid var(--np-amber);outline-offset:3px}\n.mlpnp .mlpnp-wrap{width:100%;max-width:1120px;margin:0 auto;padding:0 24px}\n.mlpnp .mlpnp-display{font-family:var(--np-display)}\n\n.mlpnp .mlpnp-top{background:var(--np-navy);color:var(--np-cream)}\n.mlpnp .mlpnp-bar{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;padding-top:18px;padding-bottom:18px}\n.mlpnp .mlpnp-brand{font:600 18px/1.3 var(--np-display);letter-spacing:.01em}\n.mlpnp .mlpnp-brand span{color:var(--np-amber)}\n.mlpnp .mlpnp-top .mlpnp-bar a{color:var(--np-cream);font-weight:600;font-size:15px;text-underline-offset:4px}\n\n.mlpnp .mlpnp-hero{display:flex;flex-wrap:wrap;gap:48px;align-items:center;padding-top:72px;padding-bottom:88px}\n.mlpnp .mlpnp-hero-main{flex:999 1 520px;min-width:0}\n.mlpnp .mlpnp-eyebrow{font-size:14px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--np-amber);margin-bottom:16px!important}\n.mlpnp .mlpnp-h1{font:700 clamp(40px,6vw,64px)/1.05 var(--np-display);margin-bottom:20px!important;color:var(--np-cream)}\n.mlpnp .mlpnp-lede{font-size:19px;max-width:560px;color:var(--np-muted-on-navy);margin-bottom:32px!important}\n.mlpnp .mlpnp-ctas{display:flex;flex-wrap:wrap;gap:12px}\n.mlpnp .mlpnp-btn{display:inline-flex;align-items:center;min-height:48px;padding:0 24px;border-radius:6px;font-weight:600;font-size:16px;text-decoration:none}\n.mlpnp .mlpnp-btn--amber{background:var(--np-amber);color:var(--np-navy)}\n.mlpnp .mlpnp-btn--amber:hover{background:#f0b375;color:var(--np-navy)}\n.mlpnp .mlpnp-btn--ghost{border:2px solid var(--np-cream);color:var(--np-cream)}\n.mlpnp .mlpnp-btn--ghost:hover{background:rgba(246,244,239,.1);color:var(--np-cream)}\n.mlpnp .mlpnp-card{flex:1 1 300px;background:var(--np-cream);color:var(--np-ink);border-radius:10px;padding:28px}\n.mlpnp .mlpnp-card-kicker{font-size:13px;font-weight:600;letter-spacing:.1em;text-transform:uppercase;color:var(--np-brown);margin-bottom:6px!important}\n.mlpnp .mlpnp-card-num{font:700 44px/1.1 var(--np-display);color:var(--np-navy);margin-bottom:4px!important}\n.mlpnp .mlpnp-card-sub{font-size:16px;margin-bottom:20px!important}\n.mlpnp .mlpnp-card-note{font-size:15px;padding-top:16px;border-top:1px solid var(--np-line)}\n\n.mlpnp .mlpnp-section{padding-top:80px;padding-bottom:80px}\n.mlpnp .mlpnp-white{background:#fff}\n.mlpnp .mlpnp-h2{font:600 36px/1.15 var(--np-display);color:var(--np-navy);margin-bottom:40px!important}\n.mlpnp .mlpnp-steps{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:24px}\n.mlpnp .mlpnp-step{background:#fff;border-radius:10px;padding:28px}\n.mlpnp .mlpnp-step .mlpnp-step-num{font:700 40px/1 var(--np-display);color:var(--np-amber-deep);margin-bottom:16px!important}\n.mlpnp .mlpnp-step h3{font-size:20px;color:var(--np-navy);margin-bottom:8px}\n.mlpnp .mlpnp-step p{font-size:16px}\n\n.mlpnp .mlpnp-split{display:flex;flex-wrap:wrap;gap:48px}\n.mlpnp .mlpnp-split > div{flex:1 1 380px;min-width:0}\n.mlpnp .mlpnp-list{padding-left:20px!important;font-size:17px;display:flex;flex-direction:column;gap:12px}\n.mlpnp .mlpnp-list li{list-style:disc}\n.mlpnp .mlpnp-why{background:var(--np-cream);border-radius:10px;padding:32px}\n.mlpnp .mlpnp-why .mlpnp-h2{font-size:28px;margin-bottom:16px!important}\n.mlpnp .mlpnp-why p{font-size:17px;margin-bottom:14px!important}\n.mlpnp .mlpnp-why a{display:inline-block;margin-top:6px;font-weight:600;font-size:16px}\n\n.mlpnp #mlpnp-claim{scroll-margin-top:90px}\n.mlpnp .mlpnp-claim{max-width:760px;margin:0 auto}\n.mlpnp .mlpnp-claim .mlpnp-h2{margin-bottom:8px!important}\n.mlpnp .mlpnp-claim-lede{font-size:17px;margin-bottom:28px!important}\n.mlpnp .mlpnp-formbox{background:#fff;border-radius:10px;padding:12px;min-height:200px}\n.mlpnp .mlpnp-formbox iframe{width:100%;border:0;display:block;min-height:820px}\n.mlpnp .mlpnp-formnote{padding:28px;font-size:16px;color:var(--np-ink)}\n\n.mlpnp .mlpnp-foot{background:var(--np-navy);color:var(--np-foot);font-size:14px}\n.mlpnp .mlpnp-foot .mlpnp-wrap{display:flex;flex-direction:column;gap:12px;padding-top:40px;padding-bottom:40px}\n.mlpnp .mlpnp-foot strong{color:var(--np-cream)}\n.mlpnp .mlpnp-foot a{color:var(--np-cream)}\n\n/* Step tracker (thank-you + booking pages) */\n.mlpnp .mlpnp-steps-track{display:flex;flex-direction:column;gap:14px;max-width:760px;margin:0 auto}\n.mlpnp .mlpnp-track{display:flex;gap:18px;align-items:flex-start;background:#fff;border-radius:10px;padding:22px 24px;border:2px solid transparent}\n.mlpnp .mlpnp-track--now{border-color:var(--np-amber)}\n.mlpnp .mlpnp-track--next{opacity:.75}\n.mlpnp .mlpnp-badge{flex:none;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font:700 17px/1 var(--np-display);background:var(--np-cream);color:var(--np-navy)}\n.mlpnp .mlpnp-track--done .mlpnp-badge{background:var(--np-navy);color:var(--np-cream)}\n.mlpnp .mlpnp-track--now .mlpnp-badge{background:var(--np-amber);color:var(--np-navy)}\n.mlpnp .mlpnp-track .mlpnp-kicker{font-size:12px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--np-brown);margin-bottom:4px!important}\n.mlpnp .mlpnp-track h3{font-size:19px;color:var(--np-navy);margin-bottom:4px}\n.mlpnp .mlpnp-track p{font-size:16px}\n.mlpnp .mlpnp-track .mlpnp-btn{margin-top:14px}\n.mlpnp .mlpnp-cal{max-width:860px;margin:0 auto;background:#fff;border-radius:10px;padding:12px;min-height:640px}\n.mlpnp .mlpnp-cal iframe{width:100%;border:0;display:block;min-height:640px}\n.mlpnp .mlpnp-follow{text-align:center}\n.mlpnp .mlpnp-follow p,.mlpnp .mlpnp-follow .mlpnp-h2{text-align:center}\n.mlpnp .mlpnp-follow p{margin-bottom:16px!important}\n.mlpnp .mlpnp-hero--short{padding-bottom:64px}\n\n@media (max-width:600px){\n  .mlpnp .mlpnp-hero{padding-top:48px;padding-bottom:56px;gap:32px}\n  .mlpnp .mlpnp-section{padding-top:56px;padding-bottom:56px}\n  .mlpnp .mlpnp-h2{font-size:30px;margin-bottom:28px!important}\n  .mlpnp .mlpnp-btn{width:100%;justify-content:center}\n}\n</style>\n\n\n<div class=\"mlpnp\" id=\"mlpnp-root\" data-partner=\"Better Bridge\">\n  <div class=\"mlpnp-top\">\n    <div class=\"mlpnp-wrap mlpnp-bar\">\n      <p class=\"mlpnp-brand\">My Launch Partner <span>\u00d7</span> Better Bridge</p>\n    </div>\n    <div class=\"mlpnp-wrap mlpnp-hero mlpnp-hero--short\">\n      <div class=\"mlpnp-hero-main\">\n        <p class=\"mlpnp-eyebrow\">Last step</p>\n        <h1 class=\"mlpnp-h1\">Book your audit walkthrough.</h1>\n        <p class=\"mlpnp-lede\">30 minutes with Samantha. We'll go over your audit and the fastest fixes. Pick any time that works below.</p>\n      </div>\n    </div>\n  </div>\n\n  <div class=\"mlpnp-section\">\n    <div class=\"mlpnp-wrap\">\n      <div class=\"mlpnp-steps-track\" style=\"margin-bottom:40px\">\n        <div class=\"mlpnp-track mlpnp-track--done\">\n          <span class=\"mlpnp-badge\" aria-hidden=\"true\">\u2713</span>\n          <div>\n            <p class=\"mlpnp-kicker\">Done</p>\n            <h3>Donated to Better Bridge</h3>\n          </div>\n        </div>\n        <div class=\"mlpnp-track mlpnp-track--done\">\n          <span class=\"mlpnp-badge\" aria-hidden=\"true\">\u2713</span>\n          <div>\n            <p class=\"mlpnp-kicker\">Done</p>\n            <h3>Receipt received</h3>\n            <p>Your audit lands in your inbox within 3 business days.</p>\n          </div>\n        </div>\n        <div class=\"mlpnp-track mlpnp-track--now\">\n          <span class=\"mlpnp-badge\" aria-hidden=\"true\">03</span>\n          <div>\n            <p class=\"mlpnp-kicker\">Do this now \u00b7 1 min</p>\n            <h3>Pick a time for your walkthrough</h3>\n          </div>\n        </div>\n      </div>\n      <div class=\"mlpnp-cal\" data-mlpnp-calendar></div>\n    </div>\n  </div>\n\n  <div class=\"mlpnp-section mlpnp-white\">\n    <div class=\"mlpnp-wrap mlpnp-follow\">\n      <h2 class=\"mlpnp-h2\" style=\"margin-bottom:12px!important\">While you wait</h2>\n      <p>We post memes about running a business that are a little too accurate.</p>\n      <div class=\"mlpnp-ctas\" style=\"justify-content:center\">\n        <a class=\"mlpnp-btn mlpnp-btn--amber\" href=\"https://www.instagram.com/mylaunchpartner/\" target=\"_blank\" rel=\"noopener\">Follow @mylaunchpartner</a>\n      </div>\n    </div>\n  </div>\n\n  <div class=\"mlpnp-foot\">\n    <div class=\"mlpnp-wrap\">\n      <p>Questions? Message us on Instagram at <a href=\"https://www.instagram.com/mylaunchpartner/\" target=\"_blank\" rel=\"noopener\">@mylaunchpartner</a>.</p>\n      <p>Better Bridge is a DBA of Bridge to Better Living Financial Advocacy Group Inc., a 501(c)(3) nonprofit, EIN 33-3035880.</p>\n      <p>My Launch Partner LLC \u00b7 Sedona, Arizona</p>\n    </div>\n  </div>\n</div>\n";
  var CFG={"partner": "Better Bridge", "formId": "", "calendarSlug": "nonprofit-audit-walkthrough"};

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

  var me=document.currentScript;
  var host=document.getElementById('mlpnp-audit');
  if(!host){host=document.createElement('div');host.id='mlpnp-audit';if(me&&me.parentNode){me.parentNode.insertBefore(host,me);}else{document.body.appendChild(host);}}
  host.innerHTML=HTML;
  var attr=(host.getAttribute('data-form-id')||'').trim();
  if(attr&&!/PASTE|YOUR_/i.test(attr)){CFG.formId=attr;}
  mlpnpMount(host.querySelector('#mlpnp-root'),CFG);
})();
