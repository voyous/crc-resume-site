# Cloud Resume Site

This is Chaska Ananiev's resume website, built for the Cloud Resume Challenge. It's a static site made with HTML, CSS, and JavaScript, and it shows a live count of total visitors.

**[View the live site](https://resume.voyous.dev)**

## Architecture

- **Frontend:** Vercel serves the static site at the custom domain `resume.voyous.dev`.
- **Backend:** An Azure Function App runs the visitor-counter API. The site calls it from `scripts/counter.js`.

## Deploying to Vercel

Vercel serves the site exactly as it is in the repository. The settings are in `vercel.json`: it uses no framework, has no install or build step, publishes the project root, and turns on clean URLs.

### Option 1: Git integration (recommended)

1. Push the repository to GitHub.
2. In the [Vercel dashboard](https://vercel.com/new), select **Add New → Project** and import the repository.
3. Keep the default settings, since `vercel.json` already sets them, and select **Deploy**.
4. From then on, every push to `main` triggers a production deployment, and pushes to other branches get preview deployments.

### Option 2: Vercel CLI

```bash
npm install -g vercel
vercel login
vercel          # create a preview deployment (links the project on first run)
vercel --prod   # deploy to production
```

### Custom domain

1. In the Vercel project, go to **Settings → Domains** and add `resume.voyous.dev`.
2. At your DNS provider, add the record Vercel shows you, usually a `CNAME` pointing to `cname.vercel-dns.com`.
3. Wait for the DNS change to take effect. Vercel issues the TLS certificate automatically.

> **Note:** The Azure Function App's CORS settings must allow the site's origin (for example, `https://resume.voyous.dev`). Otherwise, the visitor counter won't load.

## Tests

`tests/test_api.py` runs against the deployed API and website. It checks that:

- `GET /api/get_visits` returns HTTP 200 and an integer visitor count.
- `POST /api/visits` increases the visitor count by one.
- Reloading the website increases the displayed visitor count by one.

### Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
```

Install Playwright's browsers and system dependencies:

```bash
playwright install
playwright install-deps
```

### Running

From the project root:

```bash
pytest
```
