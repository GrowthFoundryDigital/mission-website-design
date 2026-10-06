# Relume export: MISSION Accounting — Part 1 of 4

Source: Relume site project 01a11228-6bb8-701a-98d0-9237559ed619 (wireframe mode), extracted with Claude in Chrome, 6 Oct 2026. Stored verbatim as received. Relume copy is placeholder: it shows intent and length, not final text.

## Sitemap

Every page in the order Relume shows it. Nesting comes from the sitemap tree and the URL paths. Each page lists its section cards in order. Section cards in this project show only a name. There is no description text on them: selecting a card shows just "Name" and "Tagging: Default". No pages or sections are marked disabled or hidden.

1. Home (/)
   Navbar · Hero — Schedule a free consultation · Credibility / Logo List · Does this sound like you? · Services in tier order · Tenure in numbers · A bench, not just a bookkeeper · Industries we're comfortable in · Client testimonials · The team behind your books · Latest articles · Schedule a free consultation · Footer
2. Home > About (/about)
   Navbar · About MISSION hero · What we are, and what we're not · Where we've been · The people you'll work with · How we work with your CPA and your team · Certifications and partner status · What clients say · Schedule a free consultation · Footer
3. Home > Services (/services)
   Navbar · Services — where to start · All services in tier order · How an engagement starts · Which service do I need? · Questions before the first call · Schedule a free consultation · Footer
   1. Services > QuickBooks Cleanup (/services/quickbooks-cleanup)
      Navbar · QuickBooks Cleanup hero · What a cleanup covers · The cleanup, step by step · Cleanup questions we get asked · Schedule a free consultation · Footer
   2. Services > QuickBooks Setup & Integration (/services/quickbooks-setup-integration)
      Navbar · QuickBooks Setup & Integration hero · What we set up and integrate · From decision to a working system · Setup questions we get asked · Schedule a free consultation · Footer
   3. Services > Advisory (/services/advisory)
      Navbar · Advisory hero · What advisory looks at · How an advisory relationship runs · Advisory or fractional CFO? · Schedule a free consultation · Footer
   4. Services > Fractional CFO (/services/fractional-cfo)
      Navbar · Fractional CFO hero · What a fractional CFO owns · Taking the financial seat · Fractional CFO or a full-time hire? · Schedule a free consultation · Footer
   5. Services > Custom Reporting (/services/custom-reporting)
      Navbar · Custom Reporting hero · Reports we build · From question to report · Reporting questions we get asked · Schedule a free consultation · Footer
   6. Services > Point-of-Sale Support (/services/point-of-sale-support)
      Navbar · Point-of-Sale Support hero · What POS support covers · Connecting the till to the books · POS questions we get asked · Schedule a free consultation · Footer
4. Home > Bookkeeping & Accounting (/bookkeeping-accounting). This page sits at top level, not under Services. See Extraction notes.
   Navbar · Bookkeeping & Accounting hero · What's included every month · How the monthly cycle runs · Questions we get about monthly books · Schedule a free consultation · Footer
5. Home > Products (/products)
   Navbar · Products hero · The QuickBooks line, and who each version suits · Why buy through MISSION · Product questions we get asked · Talk to us before you buy · Footer
6. Home > Partner Program (/partner-program)
   Navbar · Partner Program hero · The terms in numbers · How a referral works · Partner questions we get asked · Apply to the partner program · Footer
   1. Partner Program > How It Works (/partner-program/how-it-works)
      Navbar · How It Works header · From introduction to payment · What a partner is responsible for · Referral questions we get asked · Apply to the partner program · Footer
   2. Partner Program > Commission Examples (/partner-program/commission-examples)
      Navbar · Commission Examples header · What the commission looks like on real orders · Commission questions we get asked · Apply to the partner program · Footer
   3. Partner Program > Partner Program FAQ (/partner-program/partner-program-faq)
      Navbar · Partner Program FAQ header · Questions about joining and getting paid · Apply to the partner program · Footer
   4. Partner Program > Apply to Partner Program (/partner-program/apply-to-partner-program)
      Navbar · Apply header · Application form · After you apply · Footer
7. Home > Blog (/blog)
   Navbar · Blog header · Latest articles · Browse by the problem you have · Get the monthly email · Footer
8. Home > Contact (/contact)
   Navbar · Contact header · Send us a message · Call or visit us · Before you get in touch · Footer
9. Home > Legal (/legal)
   Navbar · Legal header · Our policies · Footer
   1. Legal > Terms of Service (/legal/terms-of-service)
      Navbar · Terms of Service header · Terms of Service · Footer
   2. Legal > Privacy Policy (/legal/privacy-policy)
      Navbar · Privacy Policy header · Privacy Policy · Footer
   3. Legal > Cookie Policy (/legal/cookie-policy)
      Navbar · Cookie Policy header · Cookie Policy · Footer
   4. Legal > Returns Policy (/legal/returns-policy)
      Navbar · Returns Policy header · Returns policy · Footer

Page count in Sitemap: 23

## Global: Navbar

- Component: Navbar • Inline • Full-width • Logo Left
- Used on: all 23 pages, with identical content on every page.
- Logo: image placeholder, alt text empty. Wireframe source is `.../6a867bf8f2c6aa13446fad58_company-logo.svg`. In Design mode the logo shows the uploaded "MISSION" light logo.
- Nav items, in order:
  - About
  - Services (dropdown, icon: keyboard_arrow_down). The dropdown items are collapsed in the wireframe; their text was read from the hidden menu:
    - Bookkeeping & Accounting
    - QuickBooks Cleanup
    - QuickBooks Setup & Integration
    - Advisory
    - Fractional CFO
    - Custom Reporting
    - Point-of-Sale Support
  - Products
  - Partner Program
  - Blog
  - Contact
- CTA button: Schedule a free consultation
- Link targets: [NOT REACHED]. Relume doesn't put link targets in the wireframe markup; no href is set on any nav link.
- Hidden layers: none at the top level of the Navbar.

## Global: Footer

- Component: Footer • Grouped Menu • Horizontal
- Used on: all 23 pages, with identical content on every page.
- Logo: image placeholder, alt text empty, same company-logo.svg as the navbar.
- Contact details:
  - Address: 36 Cross Highway, Westport, CT 06880
  - Phone: (203) 227-9475
- Column "Services": Bookkeeping & Accounting · QuickBooks Cleanup · QuickBooks Setup & Integration · Advisory · Fractional CFO · Custom Reporting · Point-of-Sale Support
- Column "Company": About · QuickBooks Products · Partner Program · Blog · Contact
- Newsletter block:
  - Heading: QuickBooks tips, once a month
  - Text: Plain-English answers to the questions owners ask us most. No sales emails.
  - Field: input type=email, placeholder "Your email address", name=email
  - Button: Subscribe
  - Error message (hidden state): Something went wrong. Please try again.
  - Success message (hidden state): Thanks — check your inbox to confirm.
- Copyright line: MISSION Accounting. All rights reserved.
  - No "©" or year appears in the text.
- Legal links: Terms of Service · Privacy Policy · Cookie Policy · Returns Policy
- Social links: [NOT REACHED]. The "Social Link List" layer (5 Social Link items) is toggled hidden, so it isn't rendered.
- Other hidden layers, not rendered: "Image List" (3 Credential items) · "Company Name Image"
- Link targets: [NOT REACHED], same reason as the navbar.

## Page: Home

- URL path: / (home)
- SEO title: Bookkeeping & Accounting in Westport, CT | MISSION Accounting
- SEO description: A Westport, CT bookkeeping and accounting firm for established businesses: monthly books, QuickBooks cleanup, setup and advisory. Schedule a free consultation.

### Section 1: Navbar • Inline • Full-width • Logo Left
- Sitemap section name: Navbar
- Uses the Global Navbar.

### Section 2: Hero Header • Media • Horizontal
- Sitemap section name: Hero — Schedule a free consultation
- Tagline: Bookkeeping & Accounting for established businesses
- Heading (H1): Your bookkeeper left and the books are months behind. We take it from here.
- Body: MISSION Accounting is a Westport, Connecticut bookkeeping, accounting and QuickBooks team for established businesses — $1M to $10M a year, with the inventory, multi-entity and nonprofit complexity most bookkeepers turn away. We get your books current, then keep them that way.
- List items:
  - [icon: event_available] Reconciled, current books every month
  - [icon: build] QuickBooks cleaned up, set up and integrated properly
  - [icon: groups] A team of ProAdvisors behind you, not one person
- Buttons: Schedule a free consultation · Call (203) 227-9475
- Image placeholder: alt text empty

### Section 3: Credibility List Section • Caption • Center • Vertical
- Sitemap section name: Credibility / Logo List
- Heading (H2): Intuit-certified QuickBooks expertise
- Logo images (alt text empty for all three): logoipsum-1.svg · logoipsum-2.svg · logoipsum-3.svg

### Section 4: Feature List Section • Center • Vertical
- Sitemap section name: Does this sound like you?
- Tagline: The moment clients call us
- Heading (H2): Does this sound like you?
- Body: If one of these is where you are right now, you're in the right place. It's how most of our clients arrived.
- Cards:
  1. [icon: person_off] Our bookkeeper just left: Retired, moved on, or turned out to be someone you couldn't rely on. We pick up the history, find what's missing and take over the month-end.
  2. [icon: warning] We've lost confidence in our accountant: Work that arrives late, wrong, or after three unanswered emails. We'll tell you honestly what state the books are in before anything else.
  3. [icon: history] We're months — or years — behind: Accounts unreconciled to the point where nobody wants to open QuickBooks. Cleanup comes first, then the monthly work resumes.
  4. [icon: receipt_long] Our taxes are unfiled: The books aren't clean enough to file from. We get them fileable, then hand your CPA exactly what they need.
  5. [icon: account_balance] The bank wants clean financials: A lender, an investor or a buyer is asking for numbers you'd stand behind. We produce financials you can hand over.
  6. [icon: inventory_2] Our operation outgrew our help: Inventory, several entities or nonprofit reporting rules are past what one bookkeeper can carry. That's the work we prefer.

### Section 5: Feature List Section • Left • Vertical
- Sitemap section name: Services in tier order
- Tagline: What we do
- Heading (H2): Where most clients start, and where it can go
- Body: Bookkeeping and accounting is the work for nearly everyone. QuickBooks cleanup gets you out of a hole; setup and advisory come next. Fractional CFO sits at the top, and we take on a limited number of clients for it.
- Cards (carousel):
  1. [icon: calculate] Bookkeeping & Accounting: Current, reconciled books every month, from a team that knows QuickBooks deeply. Button: What's included
  2. [icon: build] QuickBooks Cleanup: Behind by months or years? We get your books current, accurate and ready to file from again. Button: How cleanup works
  3. [icon: integration_instructions] QuickBooks Setup & Integration: Configured and integrated correctly the first time, with your team trained to use it. Button: How setup works
  4. [icon: lightbulb] Advisory: The step beyond clean books: using your numbers to make better decisions. Button: What advisory adds
  5. [icon: strategy] Fractional CFO: Senior financial leadership without a full-time hire, led by our managing partner. Button: What a CFO does
  6. [icon: bar_chart] Custom Reporting: Reports built around the questions you actually need answered. Button: See custom reports
  7. [icon: point_of_sale] Point-of-Sale Support: Point-of-sale systems that feed your books properly, without the reconciliation mess. Button: POS and your books
- Carousel controls: arrow_back / arrow_forward. One pair is visible; a second pair is hidden.

### Section 6: Stat Highlight Section • List • Center • Vertical
- Sitemap section name: Tenure in numbers
- Heading (H2): The proof is how long clients stay
- Stats:
  - 10+ years: Working with several clients for more than a decade
  - Since 2007: Our longest-running client relationship, still on the books today
  - 29 reviews: Google reviews from clients, and climbing

### Section 7: Feature List Section • Left • Vertical
- Sitemap section name: A bench, not just a bookkeeper
- Tagline: Why MISSION
- Heading (H2): A bench, not just a bookkeeper
- Body: You don't need a bigger firm. You need the right people on your books — which is a different thing entirely.
- Items:
  1. A specialist network, staffed to your work: CPAs, controllers and accounting specialists are brought in when the problem calls for them — accounting system design, data integration, financial modeling. You get the right expertise for the job, not whoever happens to be free.
  2. Deep QuickBooks expertise, and the software itself: Multiple Level 2 Advanced ProAdvisors, a ProAdvisor Elite-certified managing partner, and an Intuit reseller relationship. Setup, integration, point-of-sale, reporting and the books themselves, all in one place.
  3. Relationships measured in years: Several clients have worked with us for more than a decade, one since 2007. We're built to be the last bookkeeper change a business has to make.

### Section 8: Feature List Section • Left • Vertical
- Sitemap section name: Industries we're comfortable in
- Heading (H2): The complicated operations are the ones we prefer
- Body: Construction, restaurants, nonprofits, property management and manufacturing carry the messiest books: inventory, several entities, restricted funds, point-of-sale data that never reconciles. If your operation is simple, a good solo bookkeeper will serve you well. If it isn't, this is the work we want.
- Cards (carousel; each card has an image placeholder with empty alt text):
  1. Construction: Job costing, work in progress and change orders, kept straight in QuickBooks.
  2. Restaurants: Food and labour costs, daily sales and point-of-sale data that actually ties back to the bank.
  3. Nonprofits: Fund accounting, restricted and unrestricted revenue, reported the way your board and your auditor expect.
  4. Property management: Rent rolls, owner statements and tenant receipts, reconciled to the bank every month.
  5. Manufacturing: Inventory, landed cost and work-in-progress reporting that holds up at year end.
- Carousel controls: arrow_back / arrow_forward. One pair is visible; a second pair is hidden.

### Section 9: Testimonial Section • List • Left • Vertical
- Sitemap section name: Client testimonials
- Heading (H2): What long-term clients say
- Testimonials:
  1. "We have been working with Bernard for over 10 years. He has been terrific." — Jacquie Herz, Jornik Manufacturing, Stamford CT
  2. "I have been working with Bernard at MISSION since 2007." — Richard Cipolla, Richard Cipolla Designs, Stamford CT
  3. "Great customer service from Bernard and his team – very friendly and helpful." — Mary Iaffaldano, Milford, CT

### Section 10: Team Section • List • Left • Vertical
- Sitemap section name: The team behind your books
- Heading (H2): Who you'll work with
- Team members (each has an image placeholder with empty alt text):
  1. Bernard P. Roesch, Co-founder and Managing Partner: Harvard MBA in finance and operations, more than 20 years of consulting, and QuickBooks ProAdvisor Elite certification. He leads our fractional CFO work.
  2. Carol A. Onorato, Director of Operations: Level 2 Advanced QuickBooks ProAdvisor with a background in tax preparation, cash management and operations. Carol runs the day-to-day work behind every client's books.
  3. Robert (Rob) James, Onboarding and Client Pipeline: Level 2 Advanced QuickBooks ProAdvisor. Rob onboards new clients and is usually the first person a new client speaks to.
- Heading (H3): There's a wider bench behind them
- Body: MISSION is a small core team on purpose. When a job calls for a specialist, we staff one onto it — so you're never handed off to a stranger.
- Button: Meet the whole team

### Section 11: Content Feed Section • List • Left • Vertical
- Sitemap section name: Latest articles
- Heading (H2): Plain-English answers to the questions we get asked
- Body: More than 300 articles on QuickBooks, bookkeeping and cash flow, most of them written by Bernard.
- Button: Read all articles
- Article cards (each has an image placeholder with empty alt text):
  1. QuickBooks Desktop to Online: what actually changes: Moving from Desktop to Online changes how you work day to day. Here's what carries across, what has to be rebuilt, and how to plan the switch.
  2. QuickBooks Online vs Enterprise: going beyond the basics: Inventory, sales orders and location tracking are where Online runs out of road. Two client examples show where Enterprise earns its cost.
  3. Is automated accounting software the future of financial accounting?: Automation handles the routine and leaves the judgment. We look at what it genuinely replaces, and what still needs a person who knows your books.

### Section 12: CTA Section • Single Path Verbal • Center
- Sitemap section name: Schedule a free consultation
- Heading (H2): Let's look at your books
- Body: A free consultation with Bernard or Rob. Bring your situation as it is — we'll tell you what we'd do first, and what it would take.
- Buttons: Schedule a free consultation · Call (203) 227-9475

### Section 13: Footer • Grouped Menu • Horizontal
- Sitemap section name: Footer
- Uses the Global Footer.

## Page: About

- URL path: /about
- SEO title: About MISSION Accounting | Our Team & QuickBooks Experts
- SEO description: Meet the team behind MISSION: advanced-certified QuickBooks ProAdvisors, a ProAdvisor Elite managing partner and a network of CPAs and controllers.

### Section 1: Navbar • Inline • Full-width • Logo Left
- Sitemap section name: Navbar
- Uses the Global Navbar.

### Section 2: Hero Header • Media • Horizontal
- Sitemap section name: About MISSION hero
- Tagline: About MISSION
- Heading (H1): A Westport firm that has been closing books since 2007
- Body: MISSION is three principals and a specialist bench in Westport, Connecticut. We keep the books, the QuickBooks and the financial decisions of established local businesses, mostly between $1M and $10M a year, and you deal with the person doing the work.
- List items:
  - [icon: check_circle] ProAdvisor Elite and Advanced Certified
  - [icon: check_circle] Working with Connecticut businesses since 2007
  - [icon: check_circle] CPAs, controllers and CFOs on the bench behind us
- Buttons: Schedule a free consultation · Call (203) 227-9475
- Image placeholder: alt text empty

### Section 3: Feature List Section • Left • Vertical
- Sitemap section name: What we are, and what we're not
- Tagline: Fit
- Heading (H2): What we are, and what we're not
- Body: Four things decide whether we are right for you. Read them before you call us.
- Items (H3 headings):
  1. [icon: storefront] Built for established businesses: Most clients are trading past $1M with real complexity: inventory, several entities, payroll, or more than one revenue stream.
  2. [icon: groups] Small on purpose: Three principals and a named bench of specialists. Your file is worked on by people you can call by name.
  3. [icon: receipt_long] Not your tax preparer: We keep the books and build the schedules; your CPA files. If you do not have one, we work with whoever you appoint.
  4. [icon: verified_user] Straight about fit: If you need a cheaper first bookkeeper, or a full-time CFO, we say so rather than take the fee.

### Section 4: Stat Highlight Section • List • Center • Vertical
- Sitemap section name: Where we've been
- Tagline: Our record
- Heading (H2): Where we've been
- Body: Longevity is the point. A bookkeeper who might disappear next quarter is a risk to your file and your deadlines.
- Stats:
  - 2007 / In practice since: Founded in Westport, Connecticut, and still working out of the same town.
  - 3 / Principals on client files: Every file is owned by one of the three of us, not passed down to a junior.
  - 300+ / Articles published: A free library on QuickBooks and bookkeeping, answering the questions owners actually ask.

### Section 5: Team Section • List • Left • Vertical
- Sitemap section name: The people you'll work with
- Heading (H2): The people you'll work with
- Body: Three principals, all QuickBooks certified, all of them working on client files. You will know which one owns yours.
- Team members (each has an image placeholder with empty alt text):
  1. Bernard P. Roesch, Co-founder and Managing Partner: Harvard MBA in finance and operations, more than 20 years of consulting, and QuickBooks ProAdvisor Elite certification. He leads our fractional CFO work.
  2. Carol A. Onorato, Director of Operations: Level 2 Advanced QuickBooks ProAdvisor with a background in tax preparation, cash management and operations. Carol runs the day-to-day work behind every client's books.
  3. Robert (Rob) James, Onboarding and Client Pipeline: Level 2 Advanced QuickBooks ProAdvisor. Rob onboards new clients and is usually the first person a new client speaks to.
- Heading (H3): A wider bench behind them
- Body: Around fifteen CPAs, controllers and accounting-firm owners sit behind this core team. When a job calls for a specialist, one is staffed onto it rather than hired in a hurry.

### Section 6: Feature List Section • Left • Vertical
- Sitemap section name: How we work with your CPA and your team
- Tagline: Working together
- Heading (H2): How we work with your CPA and your team
- Body: A bookkeeper who does not know where their job ends creates work for everyone else.
- Items:
  1. [icon: sync_alt] A clear division of labour: We keep the books current and the schedules tidy. Your CPA handles the return and the tax positions, and we do not pretend otherwise.
  2. [icon: event_available] Year end without a scramble: We close your year and hand over a clean trial balance and supporting schedules, so nothing has to be reconstructed in March.
  3. [icon: person] Your staff stay where they are useful: If someone on your team enters bills or runs payroll, we work around it rather than replacing it.

### Section 7: Credibility List Section • Caption • Center • Vertical
- Sitemap section name: Certifications and partner status
- Heading (H2): Certifications and partner status
- Body: Bernard holds QuickBooks ProAdvisor Elite status, Carol is an Advanced Certified ProAdvisor, and MISSION is an authorised Intuit reseller. The badges below are the ones Intuit issues us.
- Logo images (alt text empty for all three): logoipsum-1.svg · logoipsum-2.svg · logoipsum-3.svg

### Section 8: Testimonial Section • List • Left • Vertical
- Sitemap section name: What clients say
- Tagline: Clients
- Heading (H2): What clients say
- Body: Three of the Connecticut businesses we look after, in their own words.
- Testimonials:
  1. "We have been working with Bernard for over 10 years. He has been terrific." — Jacquie Herz, Jornik Manufacturing, Stamford CT
  2. "I have been working with Bernard at MISSION since 2007." — Richard Cipolla, Richard Cipolla Designs, Stamford CT
  3. "Great customer service from Bernard and his team – very friendly and helpful." — Mary Iaffaldano, Milford, CT

### Section 9: CTA Section • Single Path Verbal • Center
- Sitemap section name: Schedule a free consultation
- Tagline: Free consultation
- Heading (H2): Let's look at your books, as they are
- Body: A free consultation with Bernard or Rob. Bring the situation as it stands, however untidy, and we will tell you what we would do first and what it would take.
- Buttons: Schedule a free consultation · Call (203) 227-9475

### Section 10: Footer • Grouped Menu • Horizontal
- Sitemap section name: Footer
- Uses the Global Footer.
