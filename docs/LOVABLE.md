# Putting OrbitGuard Defence on a Lovable site

The console is one plain HTML file (`index.html`, about 180 KB). Lovable apps are React projects, so the simplest route is to serve the file as a static page from the project's `public/` folder. Don't ask Lovable's AI to rebuild it in React.

## Option A: paste it in the code editor

1. Open the Lovable project and switch to the code view (Dev Mode).
2. In the `public/` folder, create a file named `defence.html`.
3. Paste the entire contents of `index.html` from this repo and save.
4. Also upload `favicon.png` into `public/`, or delete the `<link rel="icon" …>` line near the top of the file.
5. Publish. The console is then at `https://<your-domain>/defence.html`, for example `https://orbitguard.live/defence.html`.

Then send Lovable this prompt to link to it:

> Add a "Launch console" button to the hero section and a "Console" link to the navbar. Both should be plain links to `/defence.html` that open in the same tab. Do not edit, move, rename or wrap `public/defence.html`; it is a standalone static page and must be served exactly as it is.

## Option B: through GitHub

1. In Lovable, connect the project to GitHub.
2. In that repository, add this repo's `index.html` as `public/defence.html` (plus `favicon.png`) and push.
3. Lovable syncs the change. Send the same prompt as above for the links.

## Check after publishing

- The top bar should switch from "Demo catalog" to "Live · CelesTrak" within about 30 seconds. If it stays on Demo catalog, CelesTrak and the proxies were unreachable from that browser, and the app keeps working on the simulated catalogue.
- The Earth texture loads from jsDelivr. If the globe looks black, check that the site's Content Security Policy allows `cdn.jsdelivr.net`, `cdnjs.cloudflare.com` and `fonts.googleapis.com`.
