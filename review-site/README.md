# MISSION homepage review site

The client review site: lanes D3, G3, C3 and H2 (the plain-language ELI15 versions), each on desktop and mobile, in one viewer. `public/` is the finished static site; `wrangler.jsonc` deploys it as a Cloudflare Worker with static assets. The same site is also published as a claude.ai artifact: https://claude.ai/artifact/Bcfv2oZ3wHrJGKY6svUfGJ

## Deploy on Cloudflare

**From GitHub (no local tools):** in the Cloudflare dashboard, go to Workers & Pages, choose Create, then Import a repository. Pick `growthfoundrydigital/mission-website-design` and the branch, set the root directory to `review-site`, and leave the build command empty (the deploy command is `npx wrangler deploy`). Cloudflare redeploys on every push to that branch. The site is served at `mission-homepage-review.<your-subdomain>.workers.dev`, and a custom domain can be added under the Worker's Settings, Domains & Routes.

**From a computer with Node:** `cd review-site && npx wrangler login && npx wrangler deploy`.

**Keeping it private:** the pages carry `noindex`, but anyone with the link can open them. To limit it to the client, turn on Cloudflare Access for the Worker (Settings, Domains & Routes, enable Cloudflare Access on the workers.dev route) and allow their email addresses.

## Files

- `public/index.html`: the viewer. It always opens on the **Overview** (9 Nov, by request; the address no longer records the design on show, so an old link ending such as `#j-desktop` is ignored). The Overview shows all five lanes side by side, D3, G3, C3, H2 and then J (J was left out of it from 9 to 12 Nov), and the lane switcher lists all five lanes in their original order (D3, G3, C3, H2, then J; D3 and G3 left the lineup on 8 Nov and were brought back on 9 Nov, by request, for another reviewer, to be hidden again after that review) side by side, each a column up to 300 px wide holding the whole desktop page scaled down (about 21%), scrollable on its own, with the lane name, its one-line look and an Open link; clicking a column opens that lane. The review switches bar is hidden inside the overview previews, and the previews share each lane's switch channel, so a tweak changed in a lane shows there too. Below 900 px wide the columns become a sideways-scrolling row. One top bar holds the Lane switch (Overview, J, C3, H2), the desktop/mobile switch and an "Open full page" link (both hidden on the overview); a link per view such as `#d3-desktop` still opens that design directly. Comments are pinned inside a design, so on the overview, comment mode shows a note to open a design first. H2's Divider and Blue switches live only in the page's own review bar. It is `index.html` wrapped in a page skeleton (doctype, head, body).
- `public/pages/*.html`: one standalone page per lane and device, generated from the canvas boards.
- **Comments (claude.ai copy only):** on the claude.ai review artifact, comments can be pinned to exact spots inside each design. Turn on claude.ai's comment mode, then click a spot. Each pin is anchored to the lane, device and the point in the design's own pixels (for example `H2 desktop @219,6771`), with a label naming the section and nearby text, so it stays on its spot at any zoom and while scrolling; opening a thread from the comment list switches to that design and scrolls to it. The page only positions pins; claude.ai stores and shows every thread. On Cloudflare there is no claude.ai comment system, so the layer stays off and the site is view-only.
- `public/rt.js`: a small runtime that runs the boards' component scripts (carousels, the typing hero, the button toggle).
- `public/img/`: the images the pages use.
- `index.html`, `rt.js`, `build.cjs`: the sources. `build.cjs` regenerates the pages from the canvas `.dc.html` files; after a rebuild, copy the output into `public/` and push.
