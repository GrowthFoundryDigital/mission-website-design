# Design explorations: working rules

Standing rules for the MISSION homepage explorations, agreed with Growth Foundry on 6 Oct 2026. They apply to every lane and every round.

## Canvas

All lanes live on one Design canvas: https://claude.ai/artifact/3vmvJuakcT7WR5rU2gbeLw

| Lane | Round | Status |
|---|---|---|
| A | 1 | Homepage desktop, mobile and style sheet published 6 Oct 2026 |
| B | 1 | Homepage desktop and mobile published 7 Oct 2026. Same inspiration as Lane A, so the lanes isolate the content variable |
| C | 1 | Homepage desktop, mobile and style sheet published 7 Oct 2026. Inspiration 2, with the section gradients in `assets/backgrounds` |

## The inspirations lead the design

- **The layouts and design of the inspiration screenshots are the point.** Each lane should feel like its inspiration: its grid, rhythm, density, typography and section shapes.
- **When a layout doesn't fit MISSION's content, adapt the content to the layout.** Don't drop the layout. Find a creative way to express MISSION's content in the shape the inspiration uses.
- **Examples of adapting.** A product-feature grid can become the six trigger moments. A pricing table can become the service tiers, with no prices. A logo wall can become credentials and tenure. A metrics strip can become tenure proof. A case-study carousel can become client situations.
- **Adapting never means inventing.** Facts, testimonials and credentials stay true to the brief and the Business DNA. Anything unconfirmed becomes a visible placeholder such as [CONFIRM FOUNDING YEAR].

## The lanes

| Lane | Inspiration | Content source |
|---|---|---|
| A | First screenshot supplied | Relume structure and copy, minus the invented facts flagged in `reviews/relume-wireframe-review.md` |
| B | Same first screenshot (decided 7 Oct 2026) | Brief and Business DNA only. Relume ignored. Free to restructure. Shares Lane A's type and color so only content changes |
| C | Inspiration 2 (`assets/inspiration/inspiration-2.webp`) with the 12 gradient backgrounds, one per section | The inspiration's own copy where accurate, corrected against the brief: no invented stats, logos or testimonials |

## Color

- **The blues are fixed in every lane, whatever the inspiration uses.** Mission Blue #0087C0 and Action Blue #1E73BE carry the brand. Where an inspiration uses another main color, the blues take its place.
- **Other colors are allowed when they make groups read better.** Examples include telling service tiers apart, marking the Partner Program, or separating sections. Growth Green, Partner Amber and the neutral greys come first. A color from the inspiration is fine if it does the job better.
- **Supporting colors support.** They never replace blue as the brand color.
- **Contrast still applies.** White text goes on Action Blue, not on Mission Blue, Green or Amber. Green and Amber carry dark text, or work as fills and accents.

## Constants across lanes

- The MISSION wordmark and the color rules above.
- Typefaces come from each inspiration, matched with a similar web font.
- The CTA label "Schedule a free consultation", with the phone number beside it.
- Real testimonials only, word for word.
- Text contrast of at least 4.5:1, or 3:1 for large text.
- Photos from `assets/photos`, never captioned as MISSION staff.

## Round one scope

Homepage at desktop and mobile width, plus a small style sheet per lane.

## Content baseline

The next lane starts from [`content-baseline.md`](content-baseline.md). It lists every addition, change and removal since the original materials, with the source of each. Where it disagrees with the brief, the Business DNA or the Relume export, it wins.

## Lane C decisions (7 Oct 2026)

Agreed on the canvas, to carry into later rounds of Lane C:

- **Hero photo:** the man working on a laptop, matching the inspiration's hero.
- **Call to action:** merged into the dark footer, which has rounded top corners, as in the inspiration. The light call-to-action background is unused.
- **Buttons:** Action Blue with a 10 px corner radius, not pills. Tags and chips stay pill-shaped.
- **Headings and stat numbers:** Source Serif 4 Bold.
- **Navy:** kept only for the first journey step card and the avatar circle.
- **Hero headline:** "We handle *the messy work.*", all in near-black (#111111), with the italic phrase kept. Tight line height: 0.84 on desktop, 0.86 on mobile.
- **Hero overlay:** a white gradient that runs from solid white over the bottom 20% to transparent at the top.
- **Trust strip:** a plain white background, with no gradient.
- **Highlighter:** a hand-drawn Growth Green swipe (#B6E2BC) behind the lower half of the words. It's used on the hero phrase and on one phrase in every other section heading: "manage its books", "long clients stay", "complicated operations" and "Plain-English answers". It's never used on dark backgrounds, and never on more than one phrase per section.
- **Google reviews:** show the 5.0 average, never the total. In the hero, three overlapping headshots replace the star icon, with the starred headshot last, on top, at the right. The proof stat tile reads "5.0 · Average rating across our Google reviews".
- **Hero photo:** no quote card over it.
- **Section backgrounds:** the trust strip, From behind to ahead, the stats, the team story and the blog are plain white. Value proposition fades to white over the bottom 20%. Clear books, How it works and the FAQ fade to white at the top and bottom edges. How it works and the FAQ keep a 50% white veil in the middle, and the FAQ gradient is mirrored left to right.
- **Journey cards and stat tiles:** soft mesh gradients (the three proof stat tiles use the sky, white and green meshes), made of three layered radial glows over each card's existing color (navy, sky, white, green), as in inspiration 2. Text colors are unchanged. White text on the navy card stays above about 6:1 contrast at its lightest point.
- **Team section (desktop):** photo on the left, text on the right. The stats section sits after the team section on desktop and mobile.
- **"Does this sound like you?":** uses Lane A's layout. The heading and button sit on top. On desktop, the heading, intro, button and photo (tagged "Where clients start", no badge) stack on the left, and a bordered 2 × 3 grid sits on the right. It holds of the six triggers, each with an icon, a title and one line of description, using the same copy as Lane A. On mobile, the photo sits above the six triggers stacked as rows.
- **Services carousel ("From behind to ahead"):** six mesh cards, each pairing a problem with the service that fixes it. In order: Cleanup and Setup & Integration, Bookkeeping & Accounting, Point-of-Sale Support, Custom Reporting, Advisory, and Fractional CFO (limited). The cards bleed off the right edge, with arrows between them, as in Lane A. On desktop the row runs to both page edges as you scroll, with the first card lined up with the content. The prev and next buttons scroll the row about one card per click (in Play mode). Card tones repeat navy, sky, green, white, so the six run navy, sky, green, white, navy, sky. The new POS and Reporting copy comes from the Relume service lines. The "Alongside any stage" line is now just "Also available: QuickBooks software, call for pricing". On mobile, the cards are a swipe row.
- **Proof section copy:** the heading is "Clients stay for years." (highlighter on "stay for years"). The body is just "Several clients have worked with us for more than a decade."
- **Blog cards:** photos in 16:9 frames. They're the old laptop hero, the consultation-desk photo and the construction crew.
- **Team photo testimonial:** a light white-mesh quote card instead of the dark glass strip.
- **Hero typing animation:** "We handle" stays fixed. The highlighted line types and deletes through "the messy work.", "the hard part.", "the backlog.", "the cleanup." and "the numbers.", with a blinking Action Blue caret. Screen readers get the static first phrase, and so does anyone with reduced motion turned on. The eyebrow above it is now "Accounting for complicated businesses" (Growth Foundry's edit).
- **Certifications section:** Growth Foundry moved it to sit right after "You didn't build a business…". On desktop, the badges are in padded white tiles in the wider left column (four across), and the text is on the right: the eyebrow "Certified by Intuit", the heading "QuickBooks credentials you can check." and a link to Intuit's ProAdvisor directory (Bernard's profile, new tab). On mobile, the tiles are three across. There are eight badges: 4 × 2 on desktop, 3 × 3 on mobile.
- **Footer social links:** three round outline icon buttons under the address, opening in a new tab. Facebook (MissionAccounting) and LinkedIn (company/mission-quickbooks) are company pages. X (twitter.com/BernardRoesch) is Bernard's personal profile, and its label says so.

## Lane D decisions (7 Oct 2026)

Built from `content-baseline.md` on inspiration 3. Content only carried from Lane C; the look comes from the inspiration.

- **Type:** DM Sans for everything. The inspiration's italic serif second line was tried and dropped: headings are one weight and one color, with no italic line, and the two-tone grey-and-navy statements are plain navy. Stat numbers and row numbers are DM Sans Semibold.
- **Color:** Mission Navy stands in for the inspiration's forest green (dark panels, tiles, headings). Action Blue is the buttons, links, icons and row numbers. Sky #7CB8F0 stands in for the inspiration's lime on navy, for eyebrows and numbers. The cream ground #F6F5F0 is kept.
- **Buttons:** pills with a white circled arrow, as in the inspiration. Lane C's 10 px radius was a Lane C decision only.
- **Section order:** hero → stats band → value proposition (three numbered rows) → certifications (badges in the white card, industries row below) → the six triggers as glass cards on a navy-tinted photo banner → services as six numbered rows with service tags → team card with two testimonials → contact form on navy with the FAQ beside it → blog as the inspiration's four-column strip with diagonal photo wedges → footer. The stats moved up under the hero and the FAQ moved beside the form because the inspiration's layouts fit them there.
- **Second testimonial:** Jacquie Herz, Jornik Manufacturing, from the Relume export. Initials circles stand in for reviewer photos, since the three headshots aren't identified.
- **Photos:** hero at the right of the hero; the old laptop hero in the stats band; reviewing-papers tinted behind the triggers; the team photo in the team card; consultation desk, thinking-at-laptop and construction crew as the blog wedges.
- **Stats band icons:** the circle and chevron shapes were removed. Each stat tile now carries an icon in the same treatment (Action Blue at 35% opacity, oversized and cropped off the bottom-right corner): a calendar for 10+ years, a handshake for the 2007 relationship, and the Google G silhouette for the 5.0 Google rating. The G is one color, so check Google's brand rules before launch; their guidelines ask for the full-color G when the mark itself is used.
- **Industries row:** rebalanced after Mobbin research into six equal cards: the five industries plus a navy CTA card, "Schedule a free consultation". Each industry card has an icon, the name and the Relume one-line descriptor, with "labor" spelled the US way. Nonprofits comes first, labeled "Our largest industry". The "Not on the list?" consultation link sits directly under the paragraph. Desktop is a 3 by 2 grid, and mobile stacks the cards in one column. Three predicted industries (retail, wholesale and distribution, franchise groups) were tried and removed. The triggers banner lost its twin-chevron mark.
- **Mobile height:** measured by a local render at 12,335 px; the continuation artboard is 4,455 px.
- **Not carried:** the green highlighter, the typing animation, the mesh gradients and the carousel.
