# Field & Hearth — GitHub Pages deploy

A self-contained static scrollytelling site (Dutch). No build step, no framework — just an `index.html`, a `frames/` image sequence, and Google Fonts loaded over the network.

## What's in this folder

```
deploy/
├── index.html      ← the whole site (HTML + inline CSS + vanilla JS)
├── frames/         ← f00.jpg … f63.jpg, the 64-frame scroll film
├── .nojekyll       ← tells GitHub Pages to serve all files as-is
└── README.md       ← this file
```

`index.html` is fully standalone — it does **not** depend on `support.js` or any `.dc.html` file in the parent project. Everything it needs is in this folder. Deploy this folder, nothing else.

## Deploy to GitHub Pages

### Option A — project site from a `/docs` or root folder
1. Create a repo and copy the **contents of this folder** to the repo root (so `index.html` sits at the top level).
2. Commit and push to `main`.
3. Repo → **Settings → Pages** → Source: **Deploy from a branch** → Branch `main`, folder `/ (root)` → Save.
4. Wait ~1 min. Site is live at `https://<user>.github.io/<repo>/`.

### Option B — GitHub Actions (no branch juggling)
Add `.github/workflows/pages.yml`:

```yaml
name: Deploy to Pages
on:
  push:
    branches: [main]
permissions:
  contents: read
  pages: write
  id-token: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/checkout@v4
      - uses: actions/configure-pages@v5
      - uses: actions/upload-pages-artifact@v3
        with:
          path: deploy        # upload this folder
      - id: deployment
        uses: actions/deploy-pages@v4
```
Then Settings → Pages → Source: **GitHub Actions**.

## Notes
- **All paths are relative** (`frames/f00.jpg`), so it works at any sub-path — no base-URL config needed.

## Lead-capture form
Pressing **"Bestel een brood"** opens a modal that collects name, email, phone (optional), preferred pickup day, and an explicit GDPR consent checkbox. It includes a privacy/processing notice and links to the full **privacy policy** (`privacy.html`, in Dutch).

The form is wired to **Formspree**. One step remains before it works live:
1. Create a (free) form at https://formspree.io and copy its endpoint ID (looks like `https://formspree.io/f/abcdwxyz`).
2. In `index.html`, find `var FORM_ENDPOINT = 'https://formspree.io/f/YOUR_FORM_ID';` and replace `YOUR_FORM_ID` with your real ID.
3. In Formspree, set the form's allowed domain to `fieldandhearth.nl` and confirm the notification email.

Submissions then POST via AJAX and land in your Formspree inbox; the user sees a Dutch thank-you screen. A hidden honeypot field (`_gotcha`) and a `_subject` line are already included.

**GDPR housekeeping:**
- The controller details and `privacy@fieldandhearth.nl` are set throughout (modal notice + `privacy.html`).
- `privacy.html` is a complete Dutch privacy policy (controller, data, purpose/legal basis, retention, processors incl. Formspree/GitHub/Google Fonts + US-transfer safeguards, rights, AP complaint route). Review it with your own counsel before going live and confirm Formspree's DPA covers your use.

- **Custom domain:** add a `CNAME` file next to `index.html` containing your domain, and point DNS per GitHub's docs.
- The 64 frames preload on load; a progress bar covers the screen until they're ready. Total ~ a few MB — fine for Pages.
- Fonts (Cormorant Garamond, Jost) load from Google Fonts. To go fully offline, self-host the woff2 files and swap the `<link>` for `@font-face`.
- Content language is Dutch (`<html lang="nl">`). Address is fictional: Korenmolenstraat 12, Oude Markt, Tilburg.
