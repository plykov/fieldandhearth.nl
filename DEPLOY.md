# Deploy Field & Hearth to GitHub Pages — step by step

Everything you need lives in this `deploy/` folder. Follow these in order.

---

## Step 1 — Formspree (already wired)
The form is connected to `https://formspree.io/f/mbdvyaey`. Just two things in your Formspree dashboard:
1. Add `fieldandhearth.nl` as an **allowed domain** for this form.
2. Confirm the **notification email** so submissions reach you.

(If you ever swap forms, change `var FORM_ENDPOINT = '…'` near the bottom of `index.html`.)

---

## Step 2 — Put the files in a GitHub repo
You want the **contents of this `deploy/` folder** at the **root** of the repo (so `index.html` is at the top level, not inside a `deploy/` subfolder).

**Option A — web upload (no command line):**
1. On GitHub, click **New repository**, name it e.g. `field-and-hearth`, set it **Public**, create it.
2. On the repo page click **Add file → Upload files**.
3. Drag in everything from this folder: `index.html`, `privacy.html`, `README.md`, `CNAME`, `.nojekyll`, and the whole `frames/` folder.
4. Click **Commit changes**.

**Option B — command line:**
```bash
cd deploy
git init
git add .
git commit -m "Field & Hearth site"
git branch -M main
git remote add origin https://github.com/<your-user>/field-and-hearth.git
git push -u origin main
```

---

## Step 3 — Turn on GitHub Pages
1. Repo → **Settings** → **Pages** (left sidebar).
2. Under **Source**, choose **Deploy from a branch**.
3. Branch: **main**, folder: **/ (root)**. Click **Save**.
4. Wait ~1 minute. A green box appears with your live URL: `https://<your-user>.github.io/field-and-hearth/`.
5. Open it and scroll — confirm the film plays and the order form opens.

---

## Step 4 — Connect your domain (fieldandhearth.nl)
The `CNAME` file in this folder already tells Pages to use `fieldandhearth.nl`.

1. **At your domain registrar / DNS provider**, add these records:

   For the apex domain `fieldandhearth.nl`, add four **A** records pointing to GitHub:
   ```
   185.199.108.153
   185.199.109.153
   185.199.110.153
   185.199.111.153
   ```
   (Optional) also add an **AAAA** set for IPv6:
   ```
   2606:50c0:8000::153
   2606:50c0:8001::153
   2606:50c0:8002::153
   2606:50c0:8003::153
   ```
   And for `www`, add a **CNAME** record pointing to `<your-user>.github.io`.

2. Back in repo **Settings → Pages → Custom domain**, enter `fieldandhearth.nl` and **Save** (it may already be filled from the CNAME file). Let the DNS check pass — this can take from a few minutes up to 24 hours.

3. Once verified, tick **Enforce HTTPS**. Your site is now live on `https://fieldandhearth.nl`.

---

## Step 5 — Test the live form
1. Open `https://fieldandhearth.nl`, scroll to the end, press **Bestel een brood**.
2. Fill it in, tick the consent box, submit.
3. The first real submission triggers a Formspree confirmation email — confirm it once. After that, submissions arrive in your Formspree inbox.

---

## Updating the site later
Edit the files and push again (or re-upload via **Add file → Upload files**). Pages redeploys automatically within a minute.

## Before going fully live
- Have the privacy policy (`privacy.html`) reviewed by counsel.
- Confirm Formspree's data-processing agreement covers your use.
- Replace the placeholder address/email only if your real details differ from what's set.
