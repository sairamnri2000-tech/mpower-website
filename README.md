# MPOWER GROUP AUSTRALIA Website

Static website for MPOWER GROUP AUSTRALIA (ABN 36 694 585 512), hosted on GitHub Pages.

## Files

| File | Purpose |
|---|---|
| `index.html` | Home page (Hero, Mission, Why Choose Us, Contact with map) |
| `privacy.html` | Privacy policy |
| `404.html` | "Page not found" page |
| `favicon.svg` | Browser tab icon ("M" logo mark) |
| `robots.txt` | Lets search engines index the site |
| `fetch_images.py` | Downloads the images into `images/` so the site doesn't depend on Pexels |

## Go live on GitHub Pages (test URL)

1. Run `python3 fetch_images.py` in this folder. This creates `images/` and updates `index.html`.
2. Create a public GitHub repo, for example `mpower-website`.
3. Upload all files and the `images/` folder to the repo root (don't upload `index.html.bak`).
4. In the repo, open **Settings → Pages**. Set Source to **Deploy from a branch**, Branch to `main` and folder to `/ (root)`, then save.
5. After 1–2 minutes the site is live at `https://<your-username>.github.io/mpower-website/`.

## Still to add (when available)

- **Email or phone:** there's a TODO comment in the contact section of `index.html`. Add a "Drop Us a Line!" `mailto:` button there.
- **Opening hours:** not on the current site, so left out.
- **"Why Choose Us" text:** written from the mission statement. The owner should approve it.

## Later: custom domain

1. Verify the domain first: **GitHub account Settings → Pages → Add a domain**.
2. At the domain registrar, add:
   - 4 A records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - A CNAME record: `www` → `<your-username>.github.io`
   - **Do not touch MX records** (email).
3. In **Repo Settings → Pages → Custom domain**, enter the domain. Once the certificate is ready (up to 24h), tick **Enforce HTTPS**.
4. Only after the new site works on HTTPS, delete the old GoDaddy website. Check what else is on that GoDaddy plan (domain, email) before cancelling it.

## Image credits

Photos from Pexels (free to use under the Pexels license).
