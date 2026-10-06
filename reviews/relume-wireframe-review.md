# Relume wireframe review: MISSION Accounting

Prepared by Growth Foundry · 6 Oct 2026
Reviewed against: the Website Brief (Oct 2026), MISSION's Business DNA, and the Migration Overview discovery artifact.
Source: `relume/relume-export-part-1.md`

> **Status: draft, Part 1 of 4 reviewed.** Part 1 contains the full sitemap, the navbar, the footer, Home and About. Parts 2 to 4 (Services, the service pages, Bookkeeping & Accounting, Products, Partner Program, Blog, Contact, Legal) are not yet received. Sections marked **PENDING** are judged from section names only and will be finished when the rest of the export arrives.

Relume copy is placeholder. This review judges structure, intent, facts and tone, not final wording. Growth Foundry's copywriter writes the final copy.

---

## Summary: the biggest gaps so far

1. **Invented facts on About.** The page says MISSION was founded in 2007 and that three "principals" own every client file. Neither is in the source material. 2007 is the longest client relationship, not the founding date, and recurring work is done by account managers.
2. **Bookkeeping & Accounting sits outside Services.** Its URL `/bookkeeping-accounting` also collides with an existing blog category path on the current site, which carries legacy articles and redirects.
3. **Services on the homepage are a seven-card carousel.** That flattens the confirmed tiers and hides most services behind arrows. Tier 1 should dominate and Fractional CFO should sit visibly smaller.
4. **The extended network is missing.** The brief's main depth proof is the named network of about fifteen specialists. Relume only mentions it in one sentence.
5. **"300+ articles" will be false after launch.** Content triage keeps about 170 pages.
6. **Newsletter cadence conflicts.** Relume says monthly. Discovery says the newsletter is weekly. The podcast is not mentioned anywhere.
7. **Google reviews are a number, not proof.** The brief says to lead with Google reviews. Relume shows "29 reviews" as a stat with no link, rating or review excerpts.

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

Relume models pages, not templates. Single post, blog category, single product, product category and 404 still need to be designed even though they won't appear in Relume's sitemap.

### Service order

- **The nav dropdown and footer are correct.** Both list Bookkeeping & Accounting, QuickBooks Cleanup, QuickBooks Setup & Integration, Advisory, Fractional CFO, Custom Reporting, Point-of-Sale Support.
- **The sitemap tree is not.** Bookkeeping & Accounting is a top-level sibling of Services, listed after the six other services. Move it to `/services/bookkeeping-accounting` as the first child.

### URL issues to settle before design

- **`/bookkeeping-accounting` collides with a legacy path.** The current site has a `/bookkeeping-accounting/` blog category holding about ten duplicate articles. Those need to redirect to their canonical posts. A new service page at the same path will clash with those redirects.
- **The old service URLs need mapping.** The current pages are `/services/bookkeeping`, `/services/quickbooks-setup-services`, `/services/quickbooks-reports`, `/services/point-of-sale-software` and `/services/fractional-cfo-services`. Each needs a 301 to its new page.
- **The Partner Program moves from `/partners` to `/partner-program`.** That's fine with redirects. Either keep `/partners` or add it to the redirect map.
- **The partner subpage slugs repeat themselves.** `/partner-program/partner-program-faq` and `/partner-program/apply-to-partner-program` would read better as `/partner-program/faq` and `/partner-program/apply`.
- **Pages from the current site with no new home:** Testimonials and QuickBooks Enterprise Features. Both need a redirect target. Testimonials could point to About. Enterprise Features could point to Products or a blog post.

### QuickBooks Training

The brief's offer table lists QuickBooks Training. It has no page in either the approved sitemap or Relume. Training is already folded into Setup and Bookkeeping, so leaving it out is consistent. It should be named on the Setup page.

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
- **Consider a grouped dropdown.** A flat list of seven gives equal weight to every service. Grouping them as core services and specialist services would reflect the tiers without changing the order.

### Footer

| Need | Relume | Verdict |
|---|---|---|
| Legal links | Terms, Privacy, Cookies, Returns | ✅ |
| Partner Program | In the Company column | ✅ |
| Newsletter | "QuickBooks tips, once a month" | ⚠️ Discovery says the newsletter is weekly |
| Podcast | Missing | ❌ The feed is preserved, and subscribing is a secondary conversion |
| Join Our Team | Missing | ⚠️ Phase 4. Reserve the slot in the Company column now |
| Consultation CTA | Missing | ⚠️ Add a short CTA row above the footer columns or in the contact block |
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

- **Hero.** Keep the trigger headline, the three proof bullets and the phone button. The body quotes "$1M to $10M a year", but the brief calls that range a guide, not a cutoff. In the hero it reads as a hard filter. Lead with maturity and complexity, and keep the number for the About fit section.
- **Credibility strip.** It currently shows Logoipsum placeholders. It's only worth keeping if it shows the real ProAdvisor Elite, Advanced Certified and Intuit reseller badges. Confirm that MISSION has the badge files and may use them under Intuit's rules. If not, cut the strip and put the credentials into the team section.
- **Services.** Replace the carousel with a tiered layout. Bookkeeping & Accounting gets the largest card. Cleanup sits beside it as the entry point. Setup and Advisory form a second row. Fractional CFO appears as a smaller, clearly limited card. Custom Reporting and POS become compact links. The Setup card must qualify on maturity, for example "for established businesses moving off spreadsheets or down from NetSuite". Today it reads as a general setup offer, which the brief warns attracts startups.
- **Tenure.** "Still on the books today" about the 2007 client is not verified. The testimonial comes from a page last updated in 2020. Use "one since 2007" without claiming it's current, or confirm with MISSION. "29 reviews" will date quickly, so plan for it to be updated or pulled live.
- **Testimonials.** Merge the tenure stats into this section as the brief suggests. Add the Google rating and a link to the Google profile, plus two or three short Google review excerpts if MISSION approves. The rating itself isn't in our materials, so don't design around a star figure until we have it.
- **Industries.** Nonprofits are the highest-volume industry and the first industry page to come, so list them first. Design each card so it can link out later without a layout change. "Labour" should be "labor".
- **Team.** "MISSION is a small core team on purpose" leans small. The brief says to read as established without claiming to be large. Lead with the bench instead, for example "A core team of ProAdvisors, with a bench of specialists behind them." Confirm Rob's public title, since the Business DNA describes his responsibilities but gives no title.
- **Latest articles.** "More than 300 articles" will be wrong after triage, which keeps about 170 pages. Use a number that stays true, or none. The card titles will come from the live feed. The first title doesn't match a known article name and is only a placeholder.
- **Final CTA.** Keep it. "A free consultation with Bernard or Rob" matches how onboarding actually works.

---

## 4. Page by page

### Home
Covered in section 3.

### About

**Keep**
- The fit section "What we are, and what we're not". It does the qualifying the brief asks for, especially "Straight about fit".
- The bench paragraph, "Around fifteen CPAs, controllers and accounting-firm owners".
- The team cards and the final CTA.

**Change**
- **H1 and the "2007 / In practice since" stat.** The founding year isn't in any source. 2007 is when the longest-running client started. Remove "Founded in Westport… since 2007" unless MISSION confirms the year.
- **"Three principals" throughout.** The Business DNA names one co-founder and Managing Partner, a Director of Operations, and a pipeline and onboarding lead. Account managers deliver the recurring work. "Every file is owned by one of the three of us, not passed down to a junior" contradicts that, and it works against the plan to grow account managers into advisory. Reframe around a named core team plus account managers plus the bench.
- **"CPAs, controllers and CFOs on the bench."** The network lists CPAs, controllers, ProAdvisors and firm owners. No CFOs. Drop "CFOs".
- **"Not your tax preparer."** This is a strong positioning claim with no source. The Business DNA lists "tax-information preparation", and Carol has a tax-preparation background. Confirm what MISSION does and doesn't file before this stands.
- **"How we work with your CPA and your team."** The structure is useful. The specifics, such as the trial balance hand-off and "reconstructed in March", are invented process claims. The copywriter should confirm them with MISSION.
- **Testimonials.** These are the same three as the homepage. Use different ones here. Jane Didona's "Bernard and Gina have been a great team" is the best proof of the bench, since Gina Palacio is in the network. Kristin Fine's ten-year quote also works.
- **Spelling and tone.** "Authorised", "labour" and "trading past $1M" are British usage. The About page also drops contractions ("we do not", "we will") where the homepage uses them. Pick one register, preferably the homepage's.

**Missing**
- **The named extended network.** The brief says the fifteen specialists are named on the current About page with headshots, and that this is the main depth proof. Add a network grid with names, firms and credentials.
- **"Why MISSION": the three beliefs.** The brief gives each belief a section: complicated work is worth doing, the right team beats the biggest firm, and a bookkeeper leaving is a chance to upgrade. None appear on Home or About.
- **Bernard's full credentials.** École Polytechnique, the manufacturing and defense background, and the Fractional CFO specialties.
- **Real certification badges.** The section shows Logoipsum placeholders.

### Services index, all service pages, Bookkeeping & Accounting
**PENDING.** From section names only:
- **The structure is consistent and sensible.** Each page has a hero, what's included, the process, an FAQ and a CTA.
- **Missing from every service page:** a "who this is for, and who it isn't" block, a proof block with a testimonial or case study, and related articles. The brief calls for contextual CTAs and related-service blocks, and for qualifying on maturity.
- **Cleanup should look like a landing page,** not a standard service page. It's the trigger-event page and the most likely ad and search destination. The brief asks for "what a cleanup involves, who it's for, process and timeline". Timeline isn't visible in the section names.
- **Advisory and Fractional CFO each include a comparison section.** That's a good way to keep Fractional CFO in proportion, provided the CFO page states limited availability clearly.

### Products
**PENDING.** No single product page or category page yet. Check for no prices, no cart, "call for pricing" and a quote request form. "Talk to us before you buy" needs to resolve to a quote request, not the consultation form.

### Partner Program (overview + 4 pages)
**PENDING.** All four required pages exist. Check that the terms are exactly 50% of MISSION's Intuit commission per order, 25% on a referred colleague's first order, paid monthly, free to join with approval.

### Blog
**PENDING.** "Get the monthly email" conflicts with the weekly newsletter. A podcast block is missing. "Browse by the problem you have" is a good idea, since it maps the blog to the triggers.

### Contact
**PENDING.** The brief says Contact is the "Schedule a free consultation" page. "Send us a message" suggests a general enquiry form. The page should lead with the consultation request, with phone and address second.

### Legal
**PENDING.** Structure is fine.

---

## 5. Voice

Checked so far: Home, About, navbar and footer.

| Check | Result |
|---|---|
| Banned phrases | None found |
| "I" instead of "we" | None outside client quotes |
| Startup-SaaS tone | None. The tone is consultative and plain |
| Invented facts or stats | **Yes.** Founded 2007, three principals owning every file, "still on the books today", "CFOs on the bench", "not your tax preparer", the year-end process details, "300+ articles" after triage |
| Fake testimonials or names | None. All three testimonials are verbatim and correctly attributed |
| Spelling | British spellings to correct: labour, authorised, "trading" |
| Register | Home uses contractions; About doesn't. Align them |
| Size signal | "Small core team on purpose" and "Small on purpose" lean against "read as more established" |

What works well and should carry into final copy: the six trigger cards, "That's the work we prefer", "If your operation is simple, a good solo bookkeeper will serve you well", and "We're built to be the last bookkeeper change a business has to make". These match the brief's voice: specific, balanced, and willing to say "you don't need us".

---

## 6. Phase 2 readiness (GoHighLevel booking)

Phase 1 launches on native forms. Phase 2 replaces them with GoHighLevel forms and a booking calendar. To make that swap cheap:

- **One destination for every consultation CTA.** The navbar, hero, final CTA band and service page CTAs should all point to one place, such as `/contact#schedule` or a dedicated `/schedule` page. Then the swap happens once, not on 23 pages.
- **Design the consultation block as a slot.** At launch it holds a short form: name, email, phone, company, annual revenue band, and "what's going on". In Phase 2 the same slot holds a GoHighLevel calendar embed, which needs roughly 650–750px of height on desktop and full width on mobile. Design both states now.
- **Keep the revenue band and trigger fields.** They qualify leads at launch and become GoHighLevel custom fields later.
- **Keep the phone button beside every booking CTA.** It's the fallback when the embed fails to load, and it's a secondary conversion either way.
- **Treat other forms the same way.** The footer newsletter, the Products quote request and the Partner application all move to GoHighLevel in later phases. Use a consistent form component so the replacement is a swap, not a redesign.
- **Keep the final CTA bands verbal.** The current "Single Path Verbal" CTA has buttons only and no inline form. That's the right pattern, because it survives the swap untouched.

---

## 7. Open questions that change the design

1. **Bookkeeping & Accounting URL.** Move it to `/services/bookkeeping-accounting`? This is the recommendation, and it avoids the legacy category path.
2. **Founding year and team framing.** When was MISSION founded? Can we say "account managers" publicly, or does MISSION prefer another term? This decides the About hero and stats.
3. **Taxes.** Does MISSION prepare or file any returns, or is it strictly books plus a hand-off to the CPA? This decides the "Not your tax preparer" block and the overdue-taxes messaging.
4. **Newsletter and podcast.** Weekly or monthly? Is the podcast still active enough to promote, or is the feed only preserved for SEO?
5. **Intuit badges.** Do we have the ProAdvisor Elite, Advanced and reseller badge files, and permission to use them? If not, the credibility strip goes.
6. **Google reviews.** What's the current rating, and can we quote reviews on the site? This decides whether testimonials lead with Google or with the on-site quotes.
7. **Extended network.** Can all fifteen names, firms and headshots from the current About page be reused?

---

*Parts 2 to 4 of the export will complete sections 1, 4, 5 and 6 for the remaining pages.*
