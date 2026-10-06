# Relume wireframe review: MISSION Accounting

Prepared by Growth Foundry · 6 Oct 2026
Reviewed against: the Website Brief (Oct 2026), MISSION's Business DNA, and the Migration Overview discovery artifact.
Sources: `relume/relume-export-part-1.md` to `relume/relume-export-part-4.md`

> **Status: complete.** All 23 pages, the navbar, the footer and the Relume style guide are reviewed. 34 of the 103 content sections are empty placeholders in Relume: the Partner Program and its four subpages, the Blog, and the Legal pages. Those are reviewed against what they need to contain.

Relume copy is placeholder. This review judges structure, intent, facts and tone, not final wording. Growth Foundry's copywriter writes the final copy. Nothing here is a design decision.

---

## Summary: the biggest gaps

1. **Invented facts.** Several claims appear in no source. They include MISSION founded in 2007, "three principals" owning every file, Bernard as a CFO "since the 1990s", a fixed-fee cleanup, office hours, a one-business-day reply promise, and a range of timelines. The full list is in section 5.
2. **The copy contradicts how MISSION delivers.** "Not a junior with your file", "every file is owned by one of the three of us" and "you will reach one of the partners" all clash with the Business DNA. Account managers do the recurring work, and growing them into advisory is a stated goal.
3. **Products is an advice page, not a catalog.** The brief calls for a browsable display-only catalog of the 22 products in 7 categories, with a quote request. Relume has a six-item lineup, no product pages, no categories, and no quote form. It also omits hosting and POS. One FAQ answer says MISSION doesn't earn more from bigger versions, which sits awkwardly beside the Partner Program's published Intuit commission.
4. **A third of the site has no wireframe.** The Partner Program and its four subpages, the Blog, and Legal are empty placeholders. The Partner Program is a live revenue line the brief says to keep working.
5. **Contact doesn't do the one job the brief gives it.** The brief makes Contact the "Schedule a free consultation" page. The page never uses that phrase, the submit button says "Send message", and the form doesn't qualify on revenue, complexity or trigger.
6. **The tier-1 page is the weakest page.** Bookkeeping & Accounting sits outside Services, at a URL that collides with a legacy blog path. Its hero is service-first, it adds a Connecticut-only filter the ICP rules out, and it carries no proof.
7. **Qualification is uneven.** Setup never mentions spreadsheets or NetSuite. Fractional CFO never says it's limited. "Which service do I need?" sends nobody to Bookkeeping & Accounting and omits the strongest trigger, "our bookkeeper left".
8. **Every service page lacks proof.** None has a testimonial, a case study, a "who this is for" block, related articles, or a link to the next step in the client journey.
9. **The style guide isn't the brand palette.** Relume built a blue-only scheme, adding Cerulean and Navy and dropping Growth Green, Action Blue, Partner Amber and the neutral greys. Its primary button color fails AA contrast for normal-size text. Typefaces are still undecided.
10. **Depth proof is missing everywhere.** The named extended network, Bernard's full credentials, Google reviews and the three "beliefs" sections are absent.

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
| Products index | `/products` | ⚠️ Exists, but isn't a catalog |
| Single product (display-only) | Missing | ❌ Needed for the 22 products |
| Product category | Missing | ❌ Needed for the 7 categories, or a filter on the index |
| Partner Program + 4 subpages | `/partner-program` + 4 | ⚠️ All four kept, all empty |
| Blog index | `/blog` | ⚠️ Empty |
| Single post | Missing | ❌ Template, carries the article CTAs and related-service blocks |
| Blog category | Missing | ❌ Template |
| Contact | `/contact` | ⚠️ General contact page rather than the consultation page |
| Legal: Terms, Privacy, Cookies, Returns | `/legal/*` | ✅ Structure fine, content empty |
| Legal index | `/legal` | Extra. Harmless, optional |
| 404 | Missing | ❌ Template, in the brief and the SEO plan |
| Industry pages, Join Our Team | Not present | ✅ Correctly deferred to later phases |

Relume models pages, not templates. Single post, blog category, single product, product category and 404 still need designing even though they won't appear in Relume's sitemap.

### Service order

- **The nav dropdown, the footer and the Services index cards are correct.** All three run Bookkeeping & Accounting, QuickBooks Cleanup, QuickBooks Setup & Integration, Advisory, Fractional CFO, Custom Reporting, Point-of-Sale Support.
- **The sitemap tree is not.** Bookkeeping & Accounting is a top-level sibling of Services, listed after the other six. Move it to `/services/bookkeeping-accounting` as the first child.

### URL issues to settle before design

- **`/bookkeeping-accounting` collides with a legacy path.** The current site has a `/bookkeeping-accounting/` blog category holding about ten duplicate articles. Those need to redirect to their canonical posts, and a new service page at the same path would clash with those redirects.
- **The old service URLs need mapping.** The current pages are `/services/bookkeeping`, `/services/quickbooks-setup-services`, `/services/quickbooks-reports`, `/services/point-of-sale-software` and `/services/fractional-cfo-services`. Each needs a 301 to its new page.
- **The Partner Program moves from `/partners` to `/partner-program`.** Either keep `/partners` or add it to the redirect map.
- **The partner subpage slugs repeat themselves.** `/partner-program/partner-program-faq` and `/partner-program/apply-to-partner-program` would read better as `/partner-program/faq` and `/partner-program/apply`.
- **Product URLs.** A few `/product/` pages carry backlinks. The single product template needs URLs that those pages can redirect to cleanly.
- **Pages from the current site with no new home:** Testimonials and QuickBooks Enterprise Features. Testimonials could redirect to About. Enterprise Features could redirect to Products or a blog post.

### QuickBooks Training

The brief's offer table lists QuickBooks Training. It has no page in either the approved sitemap or Relume. That's consistent, because Setup and Products both cover training. The Bookkeeping & Accounting page should mention it too, since the Business DNA lists training as part of that service.

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
- **Align the Products label.** The nav says "Products" and the footer says "QuickBooks Products". The footer label is clearer. Use one in both places.

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
| Dark logo | Not uploaded | ⚠️ A reversed wordmark is needed for the dark color schemes |

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
- **Services.** The seven-card carousel hides most services behind arrows and gives every tier equal weight. The brief's tiers need a layout where Bookkeeping & Accounting leads and Fractional CFO reads as limited. The Setup card must qualify on maturity, for example "for established businesses moving off spreadsheets or down from NetSuite".
- **Tenure.** "Still on the books today" about the 2007 client is not verified, since the testimonial comes from a page last updated in 2020. Say "one since 2007" without claiming it's current, or confirm with MISSION. "29 reviews" will date quickly, so it needs to be easy to update or pulled live.
- **Testimonials.** The brief pairs tenure with testimonials and says to lead with Google reviews. Add the Google rating, a link to the Google profile, and two or three short review excerpts if MISSION approves. The rating isn't in our materials yet.
- **Industries.** Nonprofits are the highest-volume industry and the first industry page to come, so list them first. The cards will need to link out to industry pages later. "Labour" should be "labor".
- **Team.** "MISSION is a small core team on purpose" leans small. The brief says to read as established without claiming to be large. Lead with the bench instead. Confirm Rob's public title, since the Business DNA gives his responsibilities but no title.
- **Latest articles.** "More than 300 articles" will be wrong after triage, which keeps about 170 pages. The same claim appears on About and in the Blog meta description. Use a number that stays true, or none.
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
- **The named extended network.** The brief calls the fifteen specialists, named on the current About page with headshots, the main depth proof. A network section with names, firms and credentials is needed.
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
- **The hero's three situations leave out the biggest one.** "Our bookkeeper left, someone has to take over" maps to Bookkeeping & Accounting and is the strongest trigger.
- **"Which service do I need?" sends nobody to Bookkeeping & Accounting.** Add a situation that starts there, with Cleanup first if the books are behind.
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
- **"Senior certified people, not a junior with your file."** This contradicts the account-manager model. The bench promise is the accurate version of this claim.
- **Check the included list against the Business DNA.** Chart of accounts, revenue and expense analysis, tax-information preparation, and QuickBooks setup and training are in the DNA but missing here. Payroll coordination, sales tax by jurisdiction, a fixed close calendar and statements "on the same date each month" are here but not in the DNA. Confirm the added items before they become promises.
- **"A handful of minutes a month."** This is an unverified claim. Soften it or confirm it.

**Missing**
- **Anything that shows "Accounting".** Tier 1 is bookkeeping and accounting equally, but the page reads as bookkeeping only. The accounting side, such as financial statements, year-end, analysis and lender-ready numbers, needs its own block.
- **The bench differentiator, testimonials, and the industries served.** This is the page most referrals will land on after the homepage. It needs the most proof, and today it has none.

### QuickBooks Cleanup

**Keep**
- **The hero "Months behind, and nobody wants to open QuickBooks".** It's trigger-led and written in the visitor's own words.
- **The six "What a cleanup covers" items.** Specific, with real fixes named: suspense accounts, chart of accounts, inventory and job costs.
- **FAQ 1, "There is no threshold we turn away",** which matches "we prefer the hard jobs". **FAQ 5,** which routes to monthly bookkeeping without pressure.
- **The CTA**, "scope, fee and timeline, in writing, before anything starts".

**Change**
- **The process stops at step 3.** It has no ending. A step 4 is needed: the CPA-ready handoff and the move to monthly bookkeeping.
- **"No lecture about how it happened" sits awkwardly beside FAQ 4,** which promises to show where the process broke. Both can be true. Say it without blame, but keep the root-cause promise.
- **Unconfirmed pricing and timing:** "a fixed project fee… not an open hourly meter", "usually a matter of weeks", and "six months… three years". The pricing model is a commercial decision, so confirm it before it's published.

**Missing**
- **"Who it's for."** The brief asks for it explicitly. Name the bookkeeper-left and inherited-books situations, plus the overdue-taxes and lender angles.
- **A timeline section.** The brief asks for process and timeline. Timing appears only inside an FAQ.
- **Proof.**
- **Landing-page strength.** This is the most likely destination for ads and search, so it has to convert on its own: proof near the top and the CTA repeated.

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
- **"A senior advisor / Who runs it."** The Business DNA says advisory is increasingly delivered by account managers. Confirm how MISSION wants this described.
- **The CFO column in the comparison should say "Limited availability".**
- **"Several days a month" for the CFO here, but "a few days a month" on the CFO page.** Pick one, and confirm it.
- **"Tax and structure questions"** should stay clearly framed as questions to take to the CPA, as the copy does now.

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
- **Limited availability, stated on the page.** The brief and the Business DNA both say it's offered to a limited number of clients, and the page never says so. It belongs in the hero.
- **Bernard's credentials.** This service is Bernard, so the page should show him: Harvard MBA, École Polytechnique, manufacturing and defense, 20+ years of consulting, ProAdvisor Elite.
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
- **FAQ 4, "We stay independent of the hardware".** The brief lists POS among the Intuit products MISSION resells. Confirm what MISSION sells before claiming independence.
- **FAQ 1, "the major retail and restaurant systems".** It's vague. Naming the systems MISSION actually supports would be stronger and better for search.

**Missing**
- **Proof,** and a link to the Restaurants industry content.

### Products

**Keep**
- **The hero idea**, "Buy the QuickBooks that fits, not the one that is easiest to sell". It turns the reseller relationship into advice, which suits the voice.
- **"Why buy it through the people who keep your books"**, especially "One call for software and books". This is differentiator 2 from the brief, stated well.
- **FAQ 1, "Can we buy it ourselves…? Of course"** and **FAQ 4** on owning the wrong version. Balanced, and they say when MISSION isn't needed.
- **No prices and no cart,** as the brief and Intuit's reseller rules require.

**Change**
- **"Independent advice, not a push toward a cheaper tier."** The logic is inverted. A reseller's conflict would push toward a more expensive tier.
- **FAQ 2, "Do you make money by recommending a bigger version? No."** MISSION earns an Intuit commission, and the Partner Program publishes that it shares 50% of it. If the commission scales with the order, this answer is inaccurate. Reword it around putting the right fit ahead of the commission, and confirm with MISSION.
- **The lineup must be checked against Intuit's current range.** Intuit stopped selling new QuickBooks Desktop Pro and Premier subscriptions in the US in 2024, and it retired QuickBooks Desktop Point of Sale in 2023. Enterprise is still sold. Verify the Desktop line and the POS items in today's 22-product catalog before any of them is published.
- **Simple Start is described as "the right starting point for a very small operation".** That's fine for a catalog entry, but it shouldn't be featured. It speaks to the startups the brief wants to filter out.
- **The CTA goes to the consultation.** The brief's secondary conversion here is "request a QuickBooks quote". Both have a place, but the quote request is the page's primary action.
- **"Call for pricing" appears only in the meta description.** It needs to be visible on the page and on every product.

**Missing**
- **The catalog itself.** The brief calls for today's 22 products in 7 categories as a browsable, display-only catalog with titles, images and "call for pricing".
- **Hosting, POS and payroll as categories.** The brief lists Online, Desktop, Enterprise, hosting, POS and payroll. Relume covers Online, Desktop and payroll only.
- **The single product and category templates.** See section 1.
- **A quote request form,** with product, number of users and a contact field at minimum.
- **A link to the Returns Policy.** It exists specifically for Intuit products.

### Partner Program (overview + 4 pages)

All five pages are empty placeholders. Only the section names and SEO fields exist. The SEO descriptions state the terms correctly: 50% of MISSION's Intuit commission on referred orders, 25% on a referred colleague's first order, paid monthly, free to join with approval.

**What the pages need, per the brief and the current `/partners` pages:**
- **Overview:** who the program is for, the terms stated plainly, how a referral works, an FAQ, and the apply CTA.
- **How It Works:** the steps from introduction to monthly payment, and what a partner is responsible for.
- **Commission Examples:** worked examples on real order types. The figures must come from MISSION, since product prices aren't published. One option is to show percentages on an example order value rather than real prices.
- **FAQ:** joining, approval, payment timing and method, tracking.
- **Apply:** the application form and what happens after applying.

**Issues to settle before these are wireframed**
- **What does the program pay for?** The terms cover Intuit software orders. The How It Works SEO description says "referring a client to MISSION", which suggests bookkeeping clients too. Referrals are MISSION's main source of new clients, so this distinction matters.
- **Who are the partners?** The audience changes the tone and the form. It could be other accountants, IT consultants, or existing clients.
- **Tracking arrives in Phase 4.** Until then, referrals are tracked by hand. The application and referral forms should capture what Phase 4 will need, such as a partner ID or referral source.
- **Copy source.** The current four pages already hold the terms, examples and FAQ. Use them as the starting point rather than writing from scratch.

### Blog

All four content sections are empty placeholders.

**What the page needs**
- **"Browse by the problem you have"** is a good idea and should stay. It maps the blog to the six triggers instead of the old taxonomy.
- **Categories.** The current site uses technology, planning, customers, expenses and staffing, plus duplicates under bookkeeping-accounting, quickbooks and cfo. The triage should settle the new category set before the category template is designed.
- **Podcast.** The feed is preserved, and the brief lists subscribing as a secondary conversion. The Blog has no podcast block.
- **Newsletter.** "Get the monthly email" conflicts with the weekly newsletter in discovery.
- **The SEO description says "300+ articles… written by our team".** The count will be about 170 after triage, and most articles are bylined by Bernard.
- **Single post template.** The brief says every article needs contextual CTAs and related-service blocks. The template also needs an author block for Bernard, breadcrumbs, and Article schema.

### Contact

**Keep**
- **The SEO title, "Schedule a Free Consultation".** It's the right framing.
- **The H1 "Tell us where your books stand".** It's situation-led.
- **The FAQ.** "Who will I actually speak to? Bernard or Rob" matches onboarding. "A recent profit and loss statement helps" is practical.
- **The error state that offers the phone number.** Good fallback.

**Change**
- **The page never says "Schedule a free consultation".** The brief makes Contact the consultation page, and every CTA on the site points here. The H2 says "Send us a message" and the button says "Send message". Both should name the consultation.
- **The form doesn't qualify.** It asks for name, email, a service topic and a message. The brief says to qualify on maturity and complexity. Phone, company and annual revenue band are missing, and so is the trigger, the "what's going on" question.
- **The topic options are service-led.** The brief says to lead with the trigger. Options such as "Our bookkeeper left" or "We're behind" would match the site's own homepage.
- **"You will reach one of the partners, not a call centre."** Only Bernard is a partner. "Centre" is British.
- **Office hours, visits by appointment, longer hours in tax season, and "within one business day".** All unconfirmed. A published response time becomes a promise, so confirm it with Rob.
- **"Office: Westport, Connecticut."** Use the full address, 36 Cross Highway, Westport, CT 06880, since it's already public in the footer.
- **"We use your details only to reply to your enquiry."** This stops being true in Phase 2, when leads go into a CRM with email and SMS follow-up. "Enquiry" is British.

**Missing**
- **The consultation slot.** See section 6.
- **A separate route for product quotes and partner applications,** so those don't land in the consultation pipeline.

### Legal

The index and all four policy pages are empty placeholders. The structure is right, and the SEO descriptions are accurate.

- **The Returns Policy is specific to Intuit products.** It should link from Products and from every product page.
- **The Cookie Policy must match the consent tool.** Discovery lists CookieYes.
- **The Privacy Policy must cover Phase 2.** It needs to describe CRM storage, email and SMS follow-up, and SMS consent before GoHighLevel goes live.
- **The policy text comes from MISSION or its counsel.** It isn't placeholder copy for the copywriter.

---

## 5. Voice

Checked: all 23 pages, the navbar and the footer.

| Check | Result |
|---|---|
| Banned phrases | None found |
| "I" instead of "we" | None outside client quotes |
| Startup-SaaS tone | None. Consultative and plain throughout |
| Fake testimonials or names | None. All testimonials are verbatim and correctly attributed |
| Spelling | British usage to correct: labour, authorised, "trading", till, reorganisation, judgement, categorised, centre, enquiry |
| Register | Home and some service pages use contractions; About, Bookkeeping, Fractional CFO, Products and Contact mostly don't. Pick one |
| Size signal | "Small core team on purpose" and "Small on purpose" lean against "read as more established" |

### Invented or unconfirmed claims

Each of these needs confirming with MISSION or cutting before the copy is final.

| Claim | Where | Status |
|---|---|---|
| Founded in 2007, "closing books since 2007" | About | ❌ Not in any source. 2007 is the longest client relationship |
| Three "principals" own every file; "not passed down to a junior" | About | ❌ Contradicts the account-manager model |
| "Senior certified people, not a junior with your file" | Bookkeeping | ❌ Same contradiction |
| "You will reach one of the partners" | Contact | ❌ Only Bernard is a partner |
| Bernard has been a CFO "since the 1990s" | Fractional CFO | ❌ Source says 20+ years of consulting |
| "CFOs on the bench" | About | ❌ No CFOs in the network list |
| "Connecticut" / "local" businesses | Bookkeeping, About | ❌ The ICP isn't a geography filter |
| "300+ articles" | Home, About, Blog meta | ❌ About 170 survive triage |
| No extra money from bigger versions | Products | ❌ Likely inaccurate given the Intuit commission |
| The 2007 client is "still on the books today" | Home | ⚠️ Testimonial is from a page last updated in 2020 |
| MISSION doesn't prepare taxes; "we prepare, they file" | About, Services, Bookkeeping, CFO | ⚠️ Unconfirmed. DNA lists tax-information preparation |
| Cleanup is a fixed project fee | Cleanup | ⚠️ Pricing model unconfirmed |
| Start "within a week or two"; setup "two to three weeks"; cleanup "a matter of weeks"; reports "a couple of weeks"; "weeks, not months" | Services, Setup, Cleanup, Reporting | ⚠️ Unconfirmed timelines |
| CFO "a few days a month" vs "several days a month" | CFO, Advisory | ⚠️ Inconsistent and unconfirmed |
| "A handful of minutes a month" | Bookkeeping | ⚠️ Unconfirmed |
| "Most accountants we deal with prefer it" | Services | ⚠️ Unconfirmed |
| Independent of POS hardware | POS | ⚠️ May conflict with the reseller catalog |
| Office hours 9 to 5, longer in tax season; visits by appointment; reply within one business day | Contact | ⚠️ Unconfirmed |
| QuickBooks Desktop Pro and Premier on sale | Products | ⚠️ Check against Intuit's current lineup |

What works and should carry into final copy: the six trigger cards; "That's the work we prefer"; "If your operation is simple, a good solo bookkeeper will serve you well"; "We're built to be the last bookkeeper change a business has to make"; "Standard reports answer the accountant's questions. Custom reporting answers yours"; "Your file stays yours… nothing holding you in"; and "Buy the QuickBooks that fits, not the one that is easiest to sell". These match the brief's voice: specific, balanced, and willing to say "you don't need us".

---

## 6. Phase 2 readiness (GoHighLevel booking)

Phase 1 launches on native forms. Phase 2 replaces them with GoHighLevel forms and a booking calendar. These are the requirements the wireframe has to meet for that swap to be cheap.

- **One destination for every consultation CTA.** The navbar, the heroes, the final CTA bands and the service pages all use the same two buttons today. They should all point to one place on Contact. Then the swap happens once, not on 23 pages.
- **The consultation area on Contact has to hold either a form or a calendar.** At launch it's a short qualifying form. In Phase 2 the same area holds a GoHighLevel calendar embed, which needs roughly 650–750px of height on desktop and full width on mobile. Both states need to be planned now.
- **The launch form should collect what GoHighLevel will need.** Name, email, phone, company, annual revenue band, and the trigger. Those map directly to CRM custom fields later. Today's form collects only name, email, topic and message.
- **Carry the source page into the form.** Each service CTA should pass which page it came from. At launch that tells Rob why the person is calling. In Phase 2 it becomes a field for routing and follow-up.
- **SMS consent.** Phase 2 adds SMS follow-up, and A2P registration requires explicit consent language at the point of capture. Leave room for a consent checkbox and short disclosure under the phone field.
- **Keep the phone button beside every booking CTA.** It's the fallback when the embed fails to load, and a secondary conversion either way.
- **Treat the other forms the same way.** The footer newsletter, the Products quote request and the Partner application all move to GoHighLevel later. If they share one form pattern, each replacement is a swap rather than a redesign.
- **Keep the final CTA bands verbal.** The "Single Path Verbal" CTA has buttons only and no inline form. That pattern survives the swap untouched.
- **Update the privacy line with the swap.** "We use your details only to reply" has to change when leads enter the CRM.

---

## 7. Open questions that change the design

1. **Bookkeeping & Accounting URL.** Move it to `/services/bookkeeping-accounting`? This is the recommendation, and it avoids the legacy category path.
2. **Founding year and team framing.** When was MISSION founded? Can we say "account managers" publicly, or does MISSION prefer another term? This decides the About hero, the stats, and the "who does the work" lines on every page.
3. **Taxes.** Does MISSION prepare or file any returns, or is it strictly books plus a hand-off to the CPA? This claim appears on four pages and shapes the overdue-taxes messaging.
4. **Pricing and timelines.** Is cleanup quoted as a fixed fee? Which timelines, office hours and response times is MISSION willing to publish? This decides whether process and contact sections show durations.
5. **Products catalog.** Which of the 22 products are still current under Intuit's lineup? Should the page lead with the catalog and a quote request, or with advice and a consultation?
6. **Partner Program scope.** Does it pay only on Intuit software orders, or also on referred bookkeeping clients? Who is it for? This decides the content of all five partner pages.
7. **Brand palette and type.** Should the site use the provided palette, with Growth Green, Action Blue and Partner Amber, rather than Relume's blue-only scheme? Is Navy an approved addition? Which typefaces does Growth Foundry's brand kit specify?
8. **Newsletter and podcast.** Weekly or monthly? Is the podcast active enough to promote, or is the feed only preserved for SEO?
9. **Intuit badges.** Do we have the ProAdvisor Elite, Advanced and reseller badge files, and permission to use them?
10. **Google reviews.** What's the current rating, and can we quote reviews on the site?
11. **Extended network.** Can all fifteen names, firms and headshots from the current About page be reused?
12. **POS.** Which POS systems does MISSION support, and does it sell any POS products?

---

## Appendix: Relume style guide vs the brand palette

This records what Relume set up. It is not a design recommendation.

### Colors

| Brand palette (provided) | In Relume |
|---|---|
| Mission Blue #0087C0, primary | ✅ As "Neutral", and as the base of the neutral ramp |
| Growth Green #66B653, secondary | ❌ Absent |
| Action Blue #1E73BE, accent | ❌ Absent. Relume uses Cerulean #0082C1, a near-duplicate of Mission Blue |
| Partner Amber #E09506 | ❌ Absent |
| Headline Black #111111, Ink #333333, Slate #666666 | ❌ Replaced by blue-tinted darks: headings #00141D, text #004866 |
| Mist #F4F4F4, Hairline #EEEEEE, White | ⚠️ White kept. Greys replaced by pale blues #EFF7FB and #EDF7FB |
| — | ➕ Navy #0A3352 added. Not in the brand palette |

The result is a single-hue blue scheme. The brand palette is a blue primary with a green secondary, a separate action blue, amber, and true neutral greys.

### Contrast, measured with WCAG 2 ratios

| Pair | Ratio | Normal text (4.5:1) |
|---|---|---|
| White on Relume Cerulean #0082C1, the primary button | 4.23 | ❌ Fails |
| White on Mission Blue #0087C0 | 4.02 | ❌ Fails |
| White on Action Blue #1E73BE | 4.94 | ✅ Passes |
| Cerulean #0082C1 link text on white | 4.23 | ❌ Fails |
| Relume accent #006798 on white | 6.19 | ✅ Passes |
| Relume body text #004866 on white | 9.91 | ✅ Passes |
| Ink #333333 on white | 12.63 | ✅ Passes |
| Growth Green #66B653 on white | 2.51 | ❌ Fails |
| Partner Amber #E09506 on white | 2.48 | ❌ Fails |
| Headline Black #111111 on Growth Green | 7.54 | ✅ Passes |
| Headline Black #111111 on Partner Amber | 7.62 | ✅ Passes |

Relume's button is 16px at weight 500, which counts as normal text, so its primary button and link color fail AA. Action Blue passes AA for normal text with white, at 4.94:1. That corrects my earlier note, which said it passed only for large text. Growth Green and Partner Amber can't carry white or colored text on white, but dark text on them passes comfortably.

### Typography

- **Relume assigned Open Sans at weight 800 for headings and Source Sans 3 for body.** Source Serif 4 is loaded but unused.
- **These are Relume's choices.** The brief says Growth Foundry holds the brand typography, and it hasn't been supplied yet. Treat these as unconfirmed.

### Logo

- **Only the light, blue wordmark is uploaded.** Relume's dark schemes 3 and 4 and any dark footer need a reversed white version. The supplied SVG is single-color, so a white version is straightforward to produce.
