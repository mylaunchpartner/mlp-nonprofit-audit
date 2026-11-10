# MLP nonprofit audit pages (GHL embed)

The landing page for My Launch Partner's nonprofit partner program: donate $5+ to the partner nonprofit, upload the receipt, get a free SEO audit. One template, one config file per partner.

Live previews: https://mylaunchpartner.github.io/mlp-nonprofit-audit/

## What's here

```
src/MLP-TEMPLATE-nonprofit-audit.html   the page template (edit copy and styles here)
partners/<SLUG>.json                    one file per nonprofit partner
build.py                                rebuilds dist/ and preview/ after any edit
dist/<SLUG>-audit.js                    embed loader the GHL snippet points to
dist/<SLUG>-audit.html                  same page as a paste-in block (no hosting)
preview/<SLUG>.html                     the page inside a narrow fake GHL row
```

## Put it in GHL

1. Add a section to the page. Set it to **full width** and **0 padding** (it breaks out to full width anyway, but this avoids extra space above and below).
2. Add a **Code / Custom HTML** element and paste the snippet:

```html
<div id="mlpnp-audit" data-form-id="YOUR_GHL_FORM_ID"></div>
<script src="https://mylaunchpartner.github.io/mlp-nonprofit-audit/dist/BETTER-BRIDGE-audit.js"></script>
```

3. Replace `YOUR_GHL_FORM_ID` with the ID of the "Nonprofit Audit Claim" form (Sites > Forms > the form > Integrate; it's the code after `/widget/form/`). Until it's set, the form area says the form opens soon.
4. In that form, set the **Partner Nonprofit** field's query key to `partner_nonprofit`. The page passes the partner name through the URL, so the field fills itself.

Edits pushed here show up on the live page within about 10 minutes (GitHub Pages cache).

## Add a new partner

1. Copy `partners/BETTER-BRIDGE.json` to `partners/<NEW-SLUG>.json` and fill it in.
   - `endDate`: `YYYY-MM-DD`, or blank to hide it. Shown as 11:59 PM MST (Arizona time) on that date.
   - `turnaroundDays`: a number, or blank to hide it.
   - `ghlFormId`: optional default; the snippet's `data-form-id` overrides it.
2. Run `python3 build.py`.
3. Use the snippet above with `dist/<NEW-SLUG>-audit.js`.
