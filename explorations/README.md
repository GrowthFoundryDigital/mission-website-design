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
- **Angles, no pills (7 Oct):** after Mobbin research, with Later and Greptile as the closest references, the user asked for more angles and no pill buttons. The angle comes from the MISSION logo's diagonal strokes and the blog wedges, always rising left to right. Every rounded shape is now square with one diagonal cut at the bottom-right: 14 px on buttons and the footer email field, 7 px on tags and icon squares, and 28 px on cards and the team photo. The navy hero, triggers banner and contact section meet their neighbors on a rising diagonal, 72 px on desktop and 36 px on mobile. The hero photo has a slanted edge. Headshots stay round because they are faces. The style sheet shows the system.
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

## Button color review toggle (7 Oct 2026)

Lanes C, D and E each have a review bar at the top of the desktop homepage: "Review · button color" with Blue and Green #C1F432. It switches every solid button between its original color and the inspiration's green, with navy text. Growth Foundry chose a toggle over duplicate boards, so the client can switch it themselves once there's a way for them to review.

- **Covered buttons:** every filled button. That's 9 in Lane C (including the white "Read all articles" and "Subscribe"), 7 in Lane D and 8 in Lane E. Carousel arrows, text links, tags and cards don't change.
- **Default:** Blue, which is each lane's original.
- **Scope:** desktop and mobile. The bar adds 40 px, so the desktop boards are now 7,008 px (C), 7,736 px (D) and 7,996 px (E).
- **Mobile:** the first mobile board and the continuation board each have their own bar. The boards of one lane stay in step through a browser broadcast channel, so a click on any of them switches that lane's desktop and both mobile boards. If the canvas blocks the channel, each board still toggles on its own. The mobile boards are now interactive so the bar can be clicked.
- **Green hover:** the same #C1F432 at 90% opacity, with no brightening.
- **Mobile heights, measured:** C 10,465 px, D 11,943 px, E 11,457 px including the bar. The continuation boards are 2,625 px (C), 4,103 px (D) and 3,617 px (E). Lane C's continuation board had been sized from an estimate of about 13,240 px and showed roughly 2,800 px of blank space below the footer; it now fits.
- **Before launch:** the bar is a review control, not part of the design. Remove it, or hide it, for any client-facing build.

## Lane G decisions (9 Oct 2026)

Built from `content-baseline.md` on inspiration 7, a security consultancy homepage on near-black, white and one royal blue band. Content only; the look comes from the inspiration. Lane G carries the button color review toggle on desktop and both mobile boards, the calendar icon on Schedule buttons and the blue MISSION logo.

- **Type:** Inter Tight for headings and Inter for text. The hero headline is uppercase Semibold with the second line stepped in, as in the inspiration. A sky square stands in for the period. Every other heading is Inter Tight Medium in one color. The inspiration's two-tone headings were not used, because headings stay one color.
- **Color:** ink #070D17 for the hero, the team section (dark by request), call to action and footer, after the inspiration's near-black. Action Blue replaces its royal blue on buttons, the featured card and the certifications band. Light sections alternate white and mist #F1F3F6. Square corners throughout.
- **Header button:** a ghost outline at rest that fills solid on hover and focus, Action Blue in blue mode and #C1F432 in green mode, by request. The fill fades in over 0.35 s with a soft ease; the nav link style had been cutting the transition to text color only.
- **Secondary links:** every arrow link (All services, Client reviews, See client reviews, Meet the team, Not on the list?, Read all articles) is a ghost button that fills solid on hover like the header button, by request. The phone number stays a plain link.
- **Imagery:** photos run in grayscale, as the inspiration's do. The hero photo fills the right 46% with a blue tint, where the inspiration shows its architecture render. It is framed so the man sits to the right of the headline rather than under it, by request.
- **Section order:** hero, with the certifications card where the inspiration shows "A clear place to start" → software strip where it shows client logos → value statement and the services as a carousel of eight cards that runs off the right edge (by request): four full cards and half of a fifth on desktop, one and a half on mobile: Bookkeeping in blue, Cleanup and Setup on a photo, Advisory on a photo, Fractional CFO in light grey and marked limited, Point-of-Sale Support in navy, Custom Reporting on a photo, QuickBooks software in white, and a near-black "Not sure which you need?" card with the Schedule button. Square arrow buttons step one card at a time. The CTA card headline is drafted wording with no new facts → certifications on the blue band, the eight badges as a four-by-two grid of light grey tiles on a white sheet like the inspiration's report (the grid replaced a named list and the tilt was removed, by request) → testimonials in two rows of three, by request: the three Relume quotes (Jacquie Herz, Richard Cipolla, Mary Iaffaldano) alternating with 10+, 5.0 with the headshots, and 2007, under "Clients stay for years." Naming clients still needs MISSION's confirmation → the six triggers as numbered rows → the bench, with the team photo in black and white like the founder portrait → how we work, with the five industries and their descriptors → FAQ → blog as photo cards → call to action with three steps → white footer.
- **Judgment calls to check:** the certifications moved after the services, so the blue band can sit where the inspiration has its. The call to action splits the approved line "Bring your situation as it is. We'll tell you what we'd do first, and what it would take." into the inspiration's three steps. The founder block shows the team, because Rob's title and naming people are still open.
- **Logo:** the MISSION blue logo in the header is 28 px tall on desktop and 22 px on mobile, enlarged by request. The badge sheet and footer logos are unchanged.
- **Call to action:** the Schedule button and phone link sit at the right of the heading row, top-aligned with "Your next step", by request; the three steps run the full width below the line. Mobile stays stacked.
- **Footer:** the Lane F footer layout restyled for Lane G, by request: description and the QuickBooks tips signup, phone and address, Services, Company, then Follow with Legal under it. Below them the MISSION logo runs the full content width as a blue (#0087C0) outline, and a bottom bar holds the copyright and Back to top. The Intuit badges were left out. It sits on ink #070D17, like the call to action above it, with a faint hairline between the two and square corners (dark mode, by request).
- **Trigger icons:** each of the six trigger rows leads with a thin Action Blue line icon matched to its content, with no background tile, by request: a person with a minus (bookkeeper left), a shield alert (lost confidence), a clock turning back (behind), a document with an x (taxes unfiled), a bank (clean financials), stacked layers (outgrew our help). The five industry rows under How we work got icons in the same style, also by request: a heart (nonprofits), a hard hat (construction), a fork and knife (restaurants), a building (property management), a factory (manufacturing).
- **Numbers removed, by request:** no "01"-style labels anywhere: section eyebrows, the badge list, the trigger rows, the call-to-action steps and the carousel counter. Stats such as 10+, 2007 and 5.0 stay.
- **Heights, measured:** desktop 7,926 px with the new footer and the trigger icons, under the 8,000 px board limit (padding had earlier been trimmed on the testimonial grid and the FAQ). Mobile 10,595 px; the continuation board is 2,755 px including its 40 px toggle bar.
- **Changed on the canvas by Growth Foundry:** the hero eyebrow now reads "Is your accounting Complicated?". Removed: the square after the hero headline, the note under the hero button, the certifications card in the hero, the navy sheet behind the badge sheet, the hairline above the certifications button, the "Intuit ProAdvisor certifications" label on the badge sheet, the dark band with Jane Didona's quote (both boards), and the QuickBooks tags row in the bench section. The "Does this sound like you?" heading was enlarged to 54 px on desktop.

## Schedule buttons lead with a calendar (7 Oct 2026)

On every lane, A to F, each solid button that says Schedule and carried an icon now shows a calendar icon on the left instead of an arrow on the right. The calendar takes the text color. Lane D's calendar has square corners, and the arrow's hover nudge is off for these buttons. Text links and cards that mention scheduling keep their arrows: Lane D's "Not on the list?" link and navy CTA card, and Lane E's text link and sky tile.

## Lane F decisions (7 Oct 2026, rebuilt the same day)

The first Lane F, built on inspiration 5 (a fintech homepage on cream with a ringed gradient and pill buttons), was rejected and replaced. The current Lane F is built from `content-baseline.md` on inspiration 6, a mobile wallet homepage that alternates near-black and white sections. Content only; the look comes from the inspiration. Lane D's refinements stay out, as with Lane E. The button color review toggle is on desktop and both mobile boards.

- **Not used, on request:** the inspiration's angled section dividers. Every section edge is straight.
- **Call button:** the hero's outline button shows a phone icon and the number, without "Or call", by request. The line beside the form's submit button still reads "Or call".
- **Logo:** the MISSION blue logo (#0087C0) in the header and the footer, on the navy, by request. The white logo is not used in this lane.
- **Buttons:** sky with a plain navy arrow after the label. The navy square the inspiration puts behind the arrow was removed on request, in both toggle modes.
- **Dark sections:** Deep Navy #081E3A replaces the near-black, as chosen. Sky #7CB8F0 takes the place of the inspiration's lime: buttons, the floating cards, the checks and the eyebrows on navy. Mission Navy is the button text and arrow, the dark cards and the phone-shaped frames.
- **Type:** Plus Jakarta Sans, after the inspiration's rounded grotesk. Headings Bold, one color, left-aligned. The inspiration's faint vertical column guides were tried and removed on request.
- **Hero visual:** Growth Foundry's monitor mockup (a finance dashboard), with its white background cut out, sits in the right column on a faint sky glow. A floating ProAdvisor Elite card and a floating "Since 2007" card sit over the monitor, both white with navy text, by request. On mobile the monitor runs full width and the two cards sit side by side over its base. The mockup's sample figures and greeting are illustration, not MISSION data. The 5.0 Google rating with the three headshots sits under the buttons, where the inspiration shows its avatars.
- **Stats:** the inspiration's stat slots are kept. Confirmed numbers fill them where they fit (10+, 2007, 5.0, eight certifications, around fifteen on the bench). The three slots in the blog section are clearly marked placeholders for MISSION to confirm: articles in the library, podcast episodes, newsletter readers. They render as dashed tiles with a "Placeholder · confirm" tag so nobody mistakes them for data.
- **Section order:** header and hero on navy → proof on white (the "clients stay for years" heading, the bench copy, 10+ and 5.0, Jane Didona's quote on a sky card with the inspiration's prev/next) → value statement with inline marks on navy, then the two stat cards (8 certifications on sky, 2007 on the team photo) and the three-column catch up / keep accurate / clarity row → services on white: the six service checks, Fractional CFO limited, and a card listing the six places clients arrive from → the six triggers around a tall photo frame on navy, with a faint MISSION watermark → how we work on white, with the five industries as checks and the eight badges in a card → the bench on navy, with the team photo, a "~15" floating card and Jacquie Herz's quote → blog on white with the three placeholder stats → FAQ on navy, first answer open → call to action on white with the form → footer on navy with the newsletter field, three badge circles and a big logo, as in the inspiration.
- **Judgment calls to check:** the trigger section's photo is a mood image. The "six places clients arrive from" card restates the tier rows from the baseline with a short line each. The footer's big logo follows the inspiration; drop it if it reads as self-serving.
- **Heights, measured:** desktop 7,629 px, after the hero edits made on the canvas (a 76 px headline, a larger monitor, the two cards moved). Mobile 10,811 px; the continuation board is 2,971 px including its 40 px toggle bar.

## Lane E decisions (7 Oct 2026)

Built from `content-baseline.md` on inspiration 4, a fintech homepage. Content only carried from the baseline; the look comes from the inspiration. Lane D's later refinements (six industry cards, the removed stats band, the dark hero, the angle system) were left out so each lane stays a clean comparison.

- **Type:** Inter for everything, after the inspiration's geometric sans. Headings are one weight and one color, centered in most sections. Big stat numbers are Inter Semibold 72 px in Action Blue.
- **Color:** a deep navy to Mission Navy gradient stands in for the inspiration's near-black purple on the hero, the bento and the footer. Action Blue replaces the purple on buttons, eyebrows, big numbers and the featured tile. Sky #7CB8F0 replaces the lime on the call-to-action block, the header button, the hero chip and the "Not on the list?" tile. Light grey panels alternate with white.
- **Shapes:** 8 px radius on buttons, 10 to 14 px on cards, tiles and chips. Floating white chips with a deep shadow straddle section edges, as the inspiration's product cards do.
- **Section order:** header and hero on one navy ground → the hero photo as a card straddling into the white, with floating proof chips (5.0 Google rating with headshots, ProAdvisor Elite, 2007) → software strip where the inspiration has its logo strip → value proposition as three cards with photo panels → certifications as the inspiration's connected icon constellation, the Elite badge at the center and a navy "ProAdvisor directory" tile → the six triggers as a dark bento, trigger 06 as the tall blue center tile with the construction photo, plus a sky "Not on the list?" tile → services in tier order as the inspiration's alternating big-number rows (01 start, 02 the core, 03 beyond), each with a "Services for this stage" list → team and proof, copy left, photo card with floating testimonials right, with the three stats as small cards → FAQ in two columns → blog as three cards → sky call-to-action block straddling into the footer → footer.
- **Buttons:** Lane E's original keeps blue buttons, with a sky header button. The green #C1F432 version moves to a separate B comparison, decided 7 Oct. A nav color rule had been overriding the header button's navy text; that's fixed.
- **Hero:** the outlined "Our services" button was removed. The gap between the hero CTA and the photo card grew by 64 px on desktop and 40 px on mobile.
- **Judgment calls to check:** the contact form is replaced by the inspiration's simple call-to-action block with a button and the phone number. The six services are regrouped into three tiers, which merges the baseline's six problem-to-fix cards.
- **Heights:** desktop measured 7,956 px by a local render, with section paddings tightened from 96 to 72 px to stay under the 8,000 px board limit. Mobile measured 11,417 px; the continuation artboard is 3,537 px.

## Lane D decisions (7 Oct 2026)

**Status:** the user called Lane D good enough on 7 Oct. Lane E comes next, from a new inspiration screenshot.

Built from `content-baseline.md` on inspiration 3. Content only carried from Lane C; the look comes from the inspiration.

- **Type:** DM Sans for everything. The inspiration's italic serif second line was tried and dropped: headings are one weight and one color, with no italic line, and the two-tone grey-and-navy statements are plain navy. Stat numbers and row numbers are DM Sans Semibold.
- **Color:** Mission Navy stands in for the inspiration's forest green (dark panels, tiles, headings). Action Blue is the buttons, links, icons and row numbers. Sky #7CB8F0 stands in for the inspiration's lime on navy, for eyebrows and numbers. The cream ground #F6F5F0 is kept.
- **Angles, no pills (7 Oct):** after Mobbin research, with Later and Greptile as the closest references, the user asked for more angles and no pill buttons. The angle comes from the MISSION logo's diagonal strokes and the blog wedges, always rising left to right. Every rounded shape is now square with one diagonal cut at the bottom-right: 14 px on buttons and the footer email field, 7 px on tags and icon squares, and 28 px on cards and the team photo. The navy hero, triggers banner and contact section meet their neighbors on a rising diagonal, 72 px on desktop and 36 px on mobile. The hero photo has a slanted edge. Headshots stay round because they are faces. The style sheet shows the system.
- **Section order:** hero → stats band → value proposition (three numbered rows) → certifications (badges in the white card, industries row below) → the six triggers as glass cards on a navy-tinted photo banner → services as six numbered rows with service tags → team card with two testimonials → contact form on navy with the FAQ beside it → blog as the inspiration's four-column strip with diagonal photo wedges → footer. The stats moved up under the hero and the FAQ moved beside the form because the inspiration's layouts fit them there.
- **Second testimonial:** Jacquie Herz, Jornik Manufacturing, from the Relume export. Initials circles stand in for reviewer photos, since the three headshots aren't identified.
- **Photos:** hero at the right of the hero; the old laptop hero in the stats band; reviewing-papers tinted behind the triggers; the team photo in the team card; consultation desk, thinking-at-laptop and construction crew as the blog wedges.
- **Stats band:** removed at the user's request, on desktop and mobile. It had held 10+, the laptop photo, 2007 and 5.0. The 5.0 Google rating stays in the hero, and the tenure proof now lives only in Jacquie Herz's testimonial.
- **Industries row:** rebalanced after Mobbin research into six equal cards: the five industries plus a navy CTA card, "Schedule a free consultation". Each industry card has an icon, the name and the Relume one-line descriptor, with "labor" spelled the US way. Nonprofits comes first, labeled "Our largest industry". The "Not on the list?" consultation link sits directly under the paragraph. Desktop is a 3 by 2 grid, and mobile stacks the cards in one column. Three predicted industries (retail, wholesale and distribution, franchise groups) were tried and removed. The twin-chevron marks above the triggers banner and the contact section were removed.
- **Hero:** dark mode at the user's request, on desktop and mobile. It has a Mission Navy ground, white headline, light body text, and sky-blue eyebrow and checks. The header stays cream for now.
- **Hover effects (7 Oct):** every clickable element responds on hover, keyboard focus and tap, with motion off for reduced-motion users.
  - Cut buttons brighten, and their arrow nudges up and right. Button arrows are plain white with no square behind them, at the user's request. The CTA card keeps its icon square to match the industry cards.
  - The CTA card brightens and its arrow moves.
  - Service tags fill sky tint with a blue edge.
  - Footer social squares turn navy.
  - Nav links turn blue with an underline. Footer links and the phone links also respond.
  - Text links slide their arrow right.
  - FAQ questions turn sky blue, and closed items rotate their plus.
  - Service rows turn the title blue and fill the arrow square.
  - Blog posts underline the title on top of the wedge animation.
  - Form fields show a sky underline on focus.
- **Blog strip (desktop):** detached from the contact section by an 88 px cream gap. "Read all articles" sits directly under the heading. On hover or keyboard focus, each post's diagonal photo cut tips the other way over 0.7 s, and the motion is off for reduced-motion users. The board is set to interactive so the hover works on the canvas. Mobile already had both changes and was left alone.
- **Style sheet:** the twin chevrons were removed from the sample stat tile, matching the homepage.
- **Desktop height:** the board's auto-fill setting does not grow it to fit, so the stored height must match the page. A local render at 1,440 px measured Lane D at 7,908 px, then 7,996 px with the blog gap, and Lane C at 6,967 px. The boards are now 7,696 px (after the stats band was removed) and 6,968 px; both had been 6,900 px and were clipping the footer.
- **Mobile height:** measured by a local render at 11,903 px; the continuation artboard is 4,023 px.
- **Not carried:** the green highlighter, the typing animation, the mesh gradients and the carousel.
