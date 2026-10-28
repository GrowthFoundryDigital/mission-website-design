# MISSION homepage review site

The client review site: lanes D3, G3, C3 and H2 (the plain-language ELI15 versions), each on desktop and mobile, in one viewer. `public/` is the finished static site; `wrangler.jsonc` deploys it as a Cloudflare Worker with static assets. The same site is also published as a claude.ai artifact: https://claude.ai/artifact/Bcfv2oZ3wHrJGKY6svUfGJ

## Deploy on Cloudflare

**From GitHub (no local tools):** in the Cloudflare dashboard, go to Workers & Pages, choose Create, then Import a repository. Pick `growthfoundrydigital/mission-website-design` and the branch, set the root directory to `review-site`, and leave the build command empty (the deploy command is `npx wrangler deploy`). Cloudflare redeploys on every push to that branch. The site is served at `mission-homepage-review.<your-subdomain>.workers.dev`, and a custom domain can be added under the Worker's Settings, Domains & Routes.

**From a computer with Node:** `cd review-site && npx wrangler login && npx wrangler deploy`.

**Keeping it private:** the pages carry `noindex`, but anyone with the link can open them. To limit it to the client, turn on Cloudflare Access for the Worker (Settings, Domains & Routes, enable Cloudflare Access on the workers.dev route) and allow their email addresses.

## Files

- `public/index.html`: the viewer (lane and desktop/mobile switches, a Divider On/Off switch that appears for Lane H2 and drives the page's hero divider, an "Open full page" link, a link per view such as `#d3-desktop`). It is `index.html` wrapped in a page skeleton (doctype, head, body).
- `public/pages/*.html`: one standalone page per lane and device, generated from the canvas boards.
- **Comments (claude.ai copy only):** on the claude.ai review artifact, comments can be pinned to exact spots inside each design. Turn on claude.ai's comment mode, then click a spot. Each pin is anchored to the lane, device and the point in the design's own pixels (for example `H2 desktop @219,6771`), with a label naming the section and nearby text, so it stays on its spot at any zoom and while scrolling; opening a thread from the comment list switches to that design and scrolls to it. The page only positions pins; claude.ai stores and shows every thread. On Cloudflare there is no claude.ai comment system, so the layer stays off and the site is view-only.
- `public/rt.js`: a small runtime that runs the boards' component scripts (carousels, the typing hero, the button toggle).
- `public/img/`: the images the pages use.
- `index.html`, `rt.js`, `build.cjs`: the sources. `build.cjs` regenerates the pages from the canvas `.dc.html` files; after a rebuild, copy the output into `public/` and push.
