# Relume wireframe review: MISSION Accounting

Prepared by Growth Foundry · 6 Oct 2026
Reviewed against: the Website Brief (Oct 2026), MISSION's Business DNA, and the Migration Overview discovery artifact.
Sources: `relume/relume-export-part-1.md`, `-part-2.md`, `-part-3.md`

> **Status: draft, Parts 1–3 of 4 reviewed.** Reviewed in full: sitemap, navbar, footer, Home, About, Services index and all seven service pages. **Not yet received:** Products, Partner Program and its four subpages, Blog, Contact, Legal. Those sections are marked **PENDING** and are judged from section names only.

Relume copy is placeholder. This review judges structure, intent, facts and tone, not final wording. Growth Foundry's copywriter writes the final copy.

---

## Summary: the biggest gaps so far

1. **Invented facts.** Several claims appear in no source: MISSION founded in 2007, "three principals" owning every file, Bernard as a CFO "since the 1990s", a fixed-fee cleanup model, and specific start times and timelines. The full list is in section 5.
2. **The copy contradicts how MISSION actually delivers.** "Not a junior with your file" and "every file is owned by one of the three of us" clash with the Business DNA. Account managers do the recurring work, and growing them into advisory is a stated goal.
3. **A geography filter crept in.** Bookkeeping & Accounting says "established Connecticut businesses" and About says "established local businesses". Discovery says plainly that the ICP is a revenue and maturity filter, not a geography filter.
4. **The tier-1 page is the weakest page.** Bookkeeping & Accounting sits outside Services, at a URL that collides with a legacy blog path. Its hero is service-first rather than trigger-first. It carries no proof, no team and no "bench".
5. **Setup doesn't qualify on maturity.** The page never mentions spreadsheets or NetSuite, the two entry routes the brief names. The "established businesses, not startups" line appears only in the meta description.
6. **Fractional CFO never says it's limited.** The Services index and Advisory pages say "limited capacity". The CFO page itself doesn't.
7. **Service pages share one thin template.** Every service page is hero, what's included, process, FAQ and CTA. None has proof, a "who this is for, and who it isn't" block, related articles, or a link to the next step in the client journey.
8. **"Which service do I need?" sends nobody to Bookkeeping & Accounting.** It also leaves out "our bookkeeper left", the strongest trigger in six years of testimonials.
9. **The homepage services block is a seven-card carousel.** That flattens the confirmed tiers.
10. **Missing depth proof.** The named extended network, Bernard's full credentials, Google reviews and the three "beliefs" sections are absent.

---

## 1. Sitemap and IA

### Page list vs the approved sitemap

| Approved page | In Relume | Verdict |
|---|---|---|
| Home | `/` | ✅ |
| About | `/about` | ✅ Content issues below |
| Services index | `/services` | ✅ |
| Bookkeeping & Accounting | `/bookkeeping-accounting`, top level | ⚠️ Wrong place. Move under Services |
| QuickBooks Cleanup | `/services/quickbooks-cleanup` | ✅ |
| QuickBooks Setup & Integration | `/services/quickbooks-setup-integration` | ✅ |
| Advisory | `/services/advisory` | ✅ |
| Fractional CFO | `/services/fractional-cfo` | ✅ |
| Custom Reporting | `/services/custom-reporting` | ✅ |
| Point-of-Sale Support | `/services/point-of-sale-support` | ✅ |
| Products index | `/products` | ✅ PENDING content |
| Single product (display-only) | Missing | ❌ Needed for the 22 products |
| Product category | Missing | ❌ Needed for the 7 categories, or a filter on the index |
| Partner Program + 4 subpages | `/partner-program` + 4 | ✅ All four kept |
| Blog index | `/blog` | ✅ |
| Single post | Missing | ❌ Template, carries the article CTAs and related-service blocks |
| Blog category | Missing | ❌ Template |
| Contact | `/contact` | ⚠️ Reads as a general contact page. See page notes |
| Legal: Terms, Privacy, Cookies, Returns | `/legal/*` | ✅ |
| Legal index | `/legal` | Extra. Harmless, optional |
| 404 | Missing | ❌ Template, in the brief and the SEO plan |
| Industry pages, Join Our Team | Not present | ✅ Correctly deferred to later phases |

Relume models pages, not templates. Single post, blog category, single product, product category and 404 still need designing even though they won't appear in Relume's sitemap.

### Service order

- **The nav dropdown, the footer and the Services index cards are correct.** All three run Bookkeeping & Accounting, QuickBooks Cleanup, QuickBooks Setup & Integration, Advisory, Fractional CFO, Custom Reporting, Point-of-Sale Support.
- **The sitemap tree is not.** Bookkeeping & Accounting is a top-level sibling of Services, listed after the other six. Move it to `/services/bookkeeping-accounting` as the first child.

### URL issues to settle before design

- **`/bookkeeping-accounting` collides with a legacy path.** The current site has a `/bookkeeping-accounting/` blog category holding about ten duplicate articles. Those need to redirect to their canonical posts. A new service page at the same path will clash with those redirects.
- **The old service URLs need mapping.** The current pages are `/services/bookkeeping`, `/services/quickbooks-setup-services`, `/services/quickbooks-reports`, `/services/point-of-sale-software` and `/services/fractional-cfo-services`. Each needs a 301 to its new page.
- **The Partner Program moves from `/partners` to `/partner-program`.** Either keep `/partners` or add it to the redirect map.
- **The partner subpage slugs repeat themselves.** `/partner-program/partner-program-faq` and `/partner-program/apply-to-partner-program` would read better as `/partner-program/faq` and `/partner-program/apply`.
- **Pages from the current site with no new home:** Testimonials and QuickBooks Enterprise Features. Testimonials could redirect to About. Enterprise Features could redirect to Products or a blog post.

### QuickBooks Training

The brief's offer table lists QuickBooks Training. It has no page in either the approved sitemap or Relume. That's consistent, because Setup now covers training well. The Bookkeeping & Accounting page should mention it too, since the Business DNA lists training as part of that service.

---

## 2. Navigation and footer

### Navbar

| Approved | Relume | Verdict |
|---|---|---|
| Home | Logo links home | ✅ Fine |
| About | About | ✅ |
| Services ▾ | Services ▾, 7 items in the right order | ✅ |
| Products | Products | ✅ |
| Partner Program | Partner Program | ✅ |
| Blog | Blog | ✅ |
| Contact | Contact | ✅ |
| CTA button | Schedule a free consultation | ✅ |

- **Add a phone number to the navbar.** Calling the office is a secondary conversion, and this audience calls. A visible number in a utility bar or beside the CTA supports that.
- **Consider a grouped dropdown.** A flat list of seven gives every service equal weight. Grouping them as core services and specialist services would reflect the tiers without changing the order.

### Footer

| Need | Relume | Verdict |
|---|---|---|
| Legal links | Terms, Privacy, Cookies, Returns | ✅ |
| Partner Program | In the Company column | ✅ |
| Newsletter | "QuickBooks tips, once a month" | ⚠️ Discovery says the newsletter is weekly |
| Podcast | Missing | ❌ The feed is preserved, and subscribing is a secondary conversion |
| Join Our Team | Missing | ⚠️ Phase 4. Reserve the slot in the Company column now |
| Consultation CTA | Missing | ⚠️ Add a short CTA row above the footer columns |
| Credentials | "Image List", 3 items, hidden | ⚠️ Turn it on for the ProAdvisor and Intuit reseller badges |
| Social links | Hidden | ❓ Confirm which profiles exist. Google Business Profile at least, for reviews |
| Copyright | No © and no year | ⚠️ Add both |
| Email address | Missing | ❓ Only phone and address. Confirm whether a public email exists |

---

## 3. Homepage

| # | Brief's suggested order | Relume | Verdict |
|---|---|---|---|
| 1 | Trigger-led hero + consultation CTA | Hero: "Your bookkeeper left and the books are months behind." | ✅ Strong. Leads with the strongest trigger |
| — | — | Credibility logo strip, placeholder logos | Extra. Keep only with real Intuit badges |
| 2 | "Does this sound like you?" (six triggers) | Present, all six | ✅ Matches the brief one to one |
| 3 | Services in tier order | Seven-card carousel in the right order | ⚠️ Right order, wrong form |
| — | — | "Tenure in numbers" stats | Moved. The brief pairs tenure with testimonials |
| 4 | "A bench, not just a bookkeeper" | Present, three differentiators | ✅ |
| 5 | Industries | Present, five industries, ecommerce left out | ✅ |
| 6 | Testimonials + tenure + Google reviews | Three real testimonials, no Google reviews | ⚠️ Missing the Google proof |
| 7 | Team and credentials | Three team members + bench note | ✅ Credentials could be fuller |
| 8 | Latest articles | Three cards + "Read all articles" | ✅ Article count claim needs fixing |
| 9 | Final CTA | "Let's look at your books" | ✅ |

### Homepage section notes

- **Hero.** Keep the trigger headline, the three proof bullets and the phone button. The body quotes "$1M to $10M a year", but the brief calls that range a guide, not a cutoff. In the hero it reads as a hard filter. Lead with maturity and complexity, and keep the number for the fit sections.
- **Credibility strip.** It shows Logoipsum placeholders. Keep it only with the real ProAdvisor Elite, Advanced Certified and Intuit reseller badges, used under Intuit's rules. Otherwise cut it and put the credentials into the team section.
- **Services.** Replace the carousel with a tiered layout. Bookkeeping & Accounting gets the largest card, with Cleanup beside it as the entry point. Setup and Advisory form a second row. Fractional CFO appears as a smaller card marked as limited. Custom Reporting and POS become compact links. The Setup card must qualify on maturity, for example "for established businesses moving off spreadsheets or down from NetSuite".
- **Tenure.** "Still on the books today" about the 2007 client is not verified, since the testimonial comes from a page last updated in 2020. Say "one since 2007" without claiming it's current, or confirm with MISSION. "29 reviews" will date quickly, so plan for it to be updated or pulled live.
- **Testimonials.** Merge the tenure stats into this section as the brief suggests. Add the Google rating, a link to the Google profile, and two or three short review excerpts if MISSION approves. The rating isn't in our materials, so don't design around a star figure until we have it.
- **Industries.** Nonprofits are the highest-volume industry and the first industry page to come, so list them first. Design each card so it can link out later without a layout change. "Labour" should be "labor".
- **Team.** "MISSION is a small core team on purpose" leans small. The brief says to read as established without claiming to be large. Lead with the bench instead. Confirm Rob's public title, since the Business DNA gives his responsibilities but no title.
- **Latest articles.** "More than 300 articles" will be wrong after triage, which keeps about 170 pages. Use a number that stays true, or none. The card titles will come from the live feed.
- **Final CTA.** Keep it. "A free consultation with Bernard or Rob" matches how onboarding actually works.

---

## 4. Page by page

### Pattern across all seven service pages

Every service page uses the same five sections: hero, what's included, process, FAQ and CTA. The consistency is good for build and for SEO. The template is missing four things the brief asks for:

- **Who it's for, and who it isn't.** The brief says to qualify on maturity and complexity on every page so startups self-select out. Only the Services index FAQ does this today.
- **Proof.** No service page has a testimonial, a case study or the Google rating. The material exists: ten testimonials and four case-study articles. A suggested mapping is below.
- **Related articles.** The brief says the blog is the traffic and the service pages are the conversion, so every page should link both ways.
- **The next step in the journey.** Cleanup should lead to Bookkeeping & Accounting, Bookkeeping to Advisory, and Advisory to Fractional CFO. Today each page ends at its own CTA.

Three hero list blocks render empty, on Fractional CFO, Custom Reporting and POS. Either fill them on every page or drop them from the template.

| Page | Best proof on file |
|---|---|
| Bookkeeping & Accounting | Jacquie Herz, "over 10 years"; Kristin Fine, "10 years" |
| QuickBooks Cleanup | A bookkeeper-left story. None is attributed on file yet, so ask MISSION |
| Setup & Integration | Barbara Steadman, moved from Peachtree to QuickBooks; Gavin Heatly, QuickBooks upgrade; the construction Enterprise case study |
| Advisory | "Bernard gave me insights to grow sales, enhance cash flow, profitability." |
| Fractional CFO | Bernard's full credentials, plus the same quote if not used on Advisory |
| Custom Reporting | The bakery and jewelry Enterprise case studies |
| POS Support | None on file. Ask MISSION for a retail or restaurant client |

### Home
Covered in section 3.

### About

**Keep**
- The fit section "What we are, and what we're not", especially "Straight about fit".
- The bench paragraph, "Around fifteen CPAs, controllers and accounting-firm owners".
- The team cards and the final CTA.

**Change**
- **The H1 and the "2007 / In practice since" stat.** No source gives a founding year. 2007 is when the longest-running client started. Remove the founding claim unless MISSION confirms the year.
- **"Three principals" throughout.** The Business DNA names a co-founder and Managing Partner, a Director of Operations, and a pipeline and onboarding lead. Account managers deliver the recurring work. "Every file is owned by one of the three of us, not passed down to a junior" contradicts that. Reframe around the core team, the account managers and the bench.
- **"Established local businesses."** Drop "local". The ICP is not a geography filter.
- **"CPAs, controllers and CFOs on the bench."** The network has CPAs, controllers, ProAdvisors and firm owners, and no CFOs. Drop "CFOs".
- **"Not your tax preparer."** This is a strong positioning claim with no source, and it repeats on Services, Bookkeeping and Fractional CFO. The Business DNA lists "tax-information preparation", and Carol has a tax-preparation background. Confirm before it stands.
- **"How we work with your CPA and your team."** The structure is useful. The trial balance hand-off and "reconstructed in March" are invented process claims for the copywriter to confirm.
- **Testimonials.** These are the same three as the homepage. Use different ones. Jane Didona's "Bernard and Gina have been a great team" is the best proof of the bench, since Gina Palacio is in the network.

**Missing**
- **The named extended network.** The brief calls the fifteen specialists, named on the current About page with headshots, the main depth proof. Add a network grid with names, firms and credentials.
- **"Why MISSION", the three beliefs.** Complicated work is worth doing, the right team beats the biggest firm, and a bookkeeper leaving is a chance to upgrade. None appear on any page.
- **Bernard's full credentials.** École Polytechnique, the manufacturing and defense background, and his specialties.
- **Real certification badges** in place of the Logoipsum placeholders.

### Services index

**Keep**
- **The hero "Where are your books right now?"** It's situation-led, which fits the brief.
- **The cards in tier order,** with "Nearly every client starts here" on Bookkeeping and "Limited capacity" on Fractional CFO.
- **The four-step "How an engagement starts".** It sets expectations well. The named person accountable for each file fits the account-manager model.
- **FAQ 5 on minimum size.** It qualifies cleanly and politely, exactly as the brief asks. FAQ 1, "A conversation, not a pitch", also works.

**Change**
- **The hero's three situations leave out the biggest one.** "Our bookkeeper left, someone has to take over" maps to Bookkeeping & Accounting and is the strongest trigger. Add it as a fourth situation or swap it in.
- **"Which service do I need?" sends nobody to Bookkeeping & Accounting.** Add a "We need someone to take over the books" column that starts at Bookkeeping & Accounting, with Cleanup first if the books are behind.
- **The "software is the problem" column describes fixing a bad setup.** The brief's Setup entry routes are spreadsheets and NetSuite. Name both.
- **Unconfirmed specifics:** "Weeks, not months" for setup, "usually within a week or two" to start, "most accountants we deal with prefer it", and the file-review step before the scope. Confirm them with Rob, who runs onboarding.

**Missing**
- **Proof,** for example one long-tenure testimonial and the Google rating.

### Bookkeeping & Accounting (tier 1)

**Keep**
- **The eight "What's included" items.** They're specific and close to the Business DNA list.
- **FAQ 3**, "Yes, and it is the work we prefer", and **FAQ 5**, "Your file stays yours… nothing holding you in". Both are strong trust builders.
- **FAQ 4,** which routes behind-on-books visitors to Cleanup.

**Change**
- **Move it to `/services/bookkeeping-accounting`.** See section 1.
- **The hero is service-first.** "Your books closed on schedule, by a team that knows QuickBooks" names the service, not the moment. The brief says lead with the trigger. The Business DNA's "built for" line gives the angle: books that are more than one bookkeeper can handle, or a bookkeeper who just left.
- **"Established Connecticut businesses."** Drop the geography.
- **"Senior certified people, not a junior with your file."** This contradicts the account-manager model. Replace it with the bench promise, for example "A team of ProAdvisors, with specialists when the work needs them."
- **Check the included list against the Business DNA.** Chart of accounts, revenue and expense analysis, tax-information preparation, and QuickBooks setup and training are in the DNA but missing here. Payroll coordination, sales tax by jurisdiction, a fixed close calendar and statements "on the same date each month" are here but not in the DNA. Confirm the added items before they become promises.
- **"A handful of minutes a month."** This is an unverified claim. Soften it or confirm it.

**Missing**
- **Anything that shows "Accounting".** Tier 1 is bookkeeping and accounting equally, but the page reads as bookkeeping only. Add a block on the accounting side, such as financial statements, year-end, analysis and lender-ready numbers.
- **The bench differentiator, testimonials, and the industries served.** This is the page most referrals will land on after the homepage. It needs the most proof, and today it has none.

### QuickBooks Cleanup

**Keep**
- **The hero "Months behind, and nobody wants to open QuickBooks".** It's trigger-led and written in the visitor's own words.
- **The six "What a cleanup covers" items.** Specific, with real fixes named: suspense accounts, chart of accounts, inventory and job costs.
- **FAQ 1, "There is no threshold we turn away",** which matches "we prefer the hard jobs". **FAQ 5,** which routes to monthly bookkeeping without pressure.
- **The CTA**, "scope, fee and timeline, in writing, before anything starts".

**Change**
- **The process stops at step 3.** It has no ending. Add step 4: the CPA-ready handoff and the move to monthly bookkeeping.
- **"No lecture about how it happened" sits awkwardly beside FAQ 4,** which promises to show where the process broke. Both can be true. Say it without blame, but keep the root-cause promise.
- **Unconfirmed pricing and timing:** "a fixed project fee… not an open hourly meter", "usually a matter of weeks", and "six months… three years". Pricing model is a commercial decision. Confirm it before it's published.

**Missing**
- **"Who it's for."** The brief asks for it explicitly. Name the bookkeeper-left and inherited-books situations, plus the overdue-taxes and lender angles.
- **A timeline section.** The brief asks for process and timeline. Timing appears only inside an FAQ.
- **Proof.**
- **Landing-page treatment.** This is the most likely destination for ads and search, so it should work as a standalone landing page. That means a stronger hero, proof near the top, and a repeated CTA, all within the standard template.

### QuickBooks Setup & Integration

**Keep**
- **The six setup items and the four-stage process.** Specific and credible. Testing with a full cycle of real transactions is a good detail.
- **FAQ 1, "Can it be fixed instead of replaced? Usually yes".** **FAQ 2,** "you can buy it through us or anywhere else". This is the balanced advice the brief asks for, and it ties Setup to the reseller catalog.

**Change**
- **The hero never qualifies on maturity.** The brief says to qualify hard: an established business still on spreadsheets, or stepping down from NetSuite. Neither word appears on the page. "For established businesses, not startups" exists only in the meta description.
- **"Typically live within two to three weeks."** Unconfirmed.

**Missing**
- **A "who this is for, and who it isn't" block.** This is the page most likely to attract the startups MISSION doesn't want, so it needs the strongest filter of any page.
- **The migration routes,** named plainly: spreadsheets to QuickBooks, NetSuite to QuickBooks, Desktop to Online. Desktop-to-Online migration guides are among the site's top blog traffic.
- **A link to the Products catalog** from the version recommendation.
- **Proof:** the Peachtree and upgrade testimonials and the construction Enterprise case study.

### Advisory

**Keep**
- **The hero "The books are clean. Now what do they mean?"** It sets the prerequisite neatly.
- **The six advisory areas.** Concrete and useful.
- **The Advisory-or-CFO comparison.** It's the right tool for keeping Fractional CFO in proportion.
- **The CTA**, "sometimes the books come first".

**Change**
- **"A senior advisor / Who runs it."** The Business DNA says advisory is increasingly delivered by account managers. Confirm how MISSION wants this described. "Your account team, with Bernard's oversight" may be more accurate.
- **The CFO column in the comparison should say "Limited availability".**
- **"Several days a month" for the CFO here, but "a few days a month" on the CFO page.** Pick one, and confirm it.
- **"Tax and structure questions"** should stay clearly framed as questions to take to the CPA, as the copy does now. Keep that boundary when the copy is rewritten.

**Missing**
- **Who it's for.** The Business DNA says advisory is built for existing bookkeeping and accounting clients. State that clean, current books come first, and link to Bookkeeping and Cleanup.
- **The proof quote** about growing sales, cash flow and profitability.
- **An FAQ.** Every other service page has one.

### Fractional CFO (tier 3)

**Keep**
- **The structure, and the CFO-vs-full-time-hire comparison.** It positions the service clearly.
- **"It starts once the numbers are clean".** It ties CFO back to the core service.
- **The CTA:** "whether it needs a CFO, an advisor, or nothing at all yet". It routes visitors down to Advisory, which is the right proportion.

**Change**
- **"Bernard has held that seat for owners since the 1990s."** This isn't in any source. The Business DNA says 20+ years of consulting with a manufacturing and defense background. Use that.
- **The six areas only partly match Bernard's stated specialties.** Forecasting is there. Integrated performance measures, cash-flow valuation and business-unit planning are missing, though the meta description mentions two of them. Lender packages, pricing, structure, owner pay and board reporting are plausible but unconfirmed.
- **"A few days a month."** Confirm, and align it with the Advisory page.
- **British spellings:** "reorganisation" and "judgement".

**Missing**
- **Limited availability, stated on the page.** The brief and the Business DNA both say it's offered to a limited number of clients, and the page never says so. Put it in the hero.
- **Bernard's credentials block.** This service is Bernard, so the page should show him: headshot, Harvard MBA, École Polytechnique, manufacturing and defense, 20+ years of consulting, ProAdvisor Elite.
- **Proof.**

### Custom Reporting

**Keep**
- **The hero line** "Standard reports answer the accountant's questions. Custom reporting answers yours." It's one of the best lines in the export.
- **The six report types and FAQ 3, "Will anyone actually read it?"** These are specific and practical, in MISSION's voice.

**Change**
- **"Within a couple of weeks of your monthly close."** Unconfirmed.
- **The hero list is empty.**

**Missing**
- **Proof:** the bakery and jewelry Enterprise case studies fit this page.
- **Related articles.**

### Point-of-Sale Support

**Keep**
- **The six coverage items and the mapping-first process.** Tips, gift cards, processor fees and payouts are named. That's the specificity the brief asks for.
- **FAQ 2, "normally a mapping problem rather than a software problem".**

**Change**
- **"Till" appears in the H1, a section heading, an item and the FAQ intro.** It's British. Use "register" or "point of sale".
- **FAQ 4, "We stay independent of the hardware".** MISSION resells Intuit products, and POS appears in the reseller list in the brief. Confirm what MISSION sells before claiming independence. Also check the POS products in the current catalog: Intuit has retired QuickBooks Desktop Point of Sale, so those listings may be out of date.
- **FAQ 1, "the major retail and restaurant systems".** It's vague. Naming the systems MISSION actually supports would be stronger and better for search.

**Missing**
- **Proof,** and a link to the Restaurants industry content.

### Products
**PENDING.** No single product page or category page exists yet. Check for no prices, no cart, "call for pricing" and a quote request form. "Talk to us before you buy" needs to resolve to a quote request, not the consultation form. Check the POS listings against what Intuit still sells.

### Partner Program (overview + 4 pages)
**PENDING.** All four required pages exist. Check that the terms are exactly 50% of MISSION's Intuit commission per order, 25% on a referred colleague's first order, paid monthly, free to join with approval.

### Blog
**PENDING.** "Get the monthly email" conflicts with the weekly newsletter. A podcast block is missing. "Browse by the problem you have" is a good idea, since it maps the blog to the triggers.

### Contact
**PENDING.** The brief says Contact is the "Schedule a free consultation" page. "Send us a message" suggests a general enquiry form. Lead with the consultation request, with phone and address second.

### Legal
**PENDING.** Structure is fine.

---

## 5. Voice

Checked so far: navbar, footer, Home, About, Services and all seven service pages.

| Check | Result |
|---|---|
| Banned phrases | None found |
| "I" instead of "we" | None outside client quotes |
| Startup-SaaS tone | None. Consultative and plain throughout |
| Fake testimonials or names | None. All testimonials are verbatim and correctly attributed |
| Spelling | British usage to correct: labour, authorised, "trading", till, reorganisation, judgement, categorised |
| Register | Home and some service pages use contractions; About, Bookkeeping and Fractional CFO mostly don't. Pick one |
| Size signal | "Small core team on purpose" and "Small on purpose" lean against "read as more established" |

### Invented or unconfirmed claims

Each of these needs confirming with MISSION or cutting before the copy is final.

| Claim | Where | Status |
|---|---|---|
| Founded in 2007, "closing books since 2007" | About | ❌ Not in any source. 2007 is the longest client relationship |
| Three "principals" own every file; "not passed down to a junior" | About | ❌ Contradicts the account-manager model |
| "Senior certified people, not a junior with your file" | Bookkeeping | ❌ Same contradiction |
| Bernard has been a CFO "since the 1990s" | Fractional CFO | ❌ Source says 20+ years of consulting |
| The 2007 client is "still on the books today" | Home | ⚠️ Testimonial is from a page last updated in 2020 |
| "CFOs on the bench" | About | ❌ No CFOs in the network list |
| "Connecticut" / "local" businesses | Bookkeeping, About | ❌ The ICP isn't a geography filter |
| MISSION doesn't prepare taxes; "we prepare, they file" | About, Services, Bookkeeping, CFO | ⚠️ Unconfirmed. DNA lists tax-information preparation |
| Cleanup is a fixed project fee | Cleanup | ⚠️ Pricing model unconfirmed |
| Start "within a week or two"; setup "two to three weeks"; cleanup "a matter of weeks"; reports "a couple of weeks"; "weeks, not months" | Services, Setup, Cleanup, Reporting | ⚠️ Unconfirmed timelines |
| CFO "a few days a month" vs "several days a month" | CFO, Advisory | ⚠️ Inconsistent and unconfirmed |
| "A handful of minutes a month" | Bookkeeping | ⚠️ Unconfirmed |
| "Most accountants we deal with prefer it" | Services | ⚠️ Unconfirmed |
| Independent of POS hardware | POS | ⚠️ May conflict with the reseller catalog |
| "300+ articles" | Home, About | ❌ About 170 survive triage |

What works and should carry into final copy: the six trigger cards; "That's the work we prefer"; "If your operation is simple, a good solo bookkeeper will serve you well"; "We're built to be the last bookkeeper change a business has to make"; "Standard reports answer the accountant's questions. Custom reporting answers yours"; and "Your file stays yours… nothing holding you in". These match the brief's voice: specific, balanced, and willing to say "you don't need us".

---

## 6. Phase 2 readiness (GoHighLevel booking)

Phase 1 launches on native forms. Phase 2 replaces them with GoHighLevel forms and a booking calendar. To make that swap cheap:

- **One destination for every consultation CTA.** The navbar, the heroes, the final CTA bands and the service pages should all point to one place, such as `/contact#schedule` or a dedicated `/schedule` page. Every page uses the same two buttons today, so this is easy to enforce.
- **Design the consultation block as a slot.** At launch it holds a short form: name, email, phone, company, annual revenue band, and "what's going on". In Phase 2 the same slot holds a GoHighLevel calendar embed, which needs roughly 650–750px of height on desktop and full width on mobile. Design both states now.
- **Carry the source page into the form.** Each service CTA should pass which page it came from, for example as a hidden field or a URL parameter. At launch that tells Rob why the person is calling. In Phase 2 it becomes a GoHighLevel custom field for routing and follow-up.
- **Keep the revenue band and trigger fields.** They qualify leads at launch and become GoHighLevel custom fields later.
- **Keep the phone button beside every booking CTA.** It's the fallback when the embed fails to load, and a secondary conversion either way.
- **Treat other forms the same way.** The footer newsletter, the Products quote request and the Partner application all move to GoHighLevel later. Use one form component so each replacement is a swap, not a redesign.
- **Keep the final CTA bands verbal.** The "Single Path Verbal" CTA has buttons only and no inline form. That pattern survives the swap untouched.

---

## 7. Open questions that change the design

1. **Bookkeeping & Accounting URL.** Move it to `/services/bookkeeping-accounting`? This is the recommendation, and it avoids the legacy category path.
2. **Founding year and team framing.** When was MISSION founded? Can we say "account managers" publicly, or does MISSION prefer another term? This decides the About hero, the stats, and the "who does the work" lines on every service page.
3. **Taxes.** Does MISSION prepare or file any returns, or is it strictly books plus a hand-off to the CPA? This claim appears on four pages and shapes the overdue-taxes messaging.
4. **Pricing and timelines.** Is cleanup quoted as a fixed fee? Which timelines is MISSION willing to publish? This decides whether the process sections show durations.
5. **Newsletter and podcast.** Weekly or monthly? Is the podcast active enough to promote, or is the feed only preserved for SEO?
6. **Intuit badges.** Do we have the ProAdvisor Elite, Advanced and reseller badge files, and permission to use them? If not, the credibility strip goes.
7. **Google reviews.** What's the current rating, and can we quote reviews on the site? This decides whether testimonials lead with Google or with the on-site quotes.
8. **Extended network.** Can all fifteen names, firms and headshots from the current About page be reused?
9. **POS.** Which POS systems does MISSION support, and does it sell any POS products? This decides the POS FAQ and the POS listings in the catalog.

---

*Part 4 of the export will complete Products, Partner Program, Blog, Contact and Legal.*
