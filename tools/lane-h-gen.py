# Lane H generator: one content source, rendered as the desktop (1440) and mobile (390) boards.
# Style: the "Decisive Clarity" style board (Space Grotesk + Open Sans, Electric Blue, near-black, chalk),
# with the project lime #C1F432 on buttons and the Mission blue logo. Copy: ELI15, as on C3, D3 and G3.
import sys

OUT = sys.argv[1]

LOGO = '/_blob/b29865f8838e8d694583c88108f0c2aa'
LOGO_W = '/_blob/c81310e520e144cd622a899707febdc7'  # white logo, for the Electric Blue hero only (allowed there by request)
PH = {
    'office': '/_blob/c76296e63f1cbdfd3cc1859696beddca',
    'construction': '/_blob/3554cab00abc02f5b19956702ff92a9f',
    'ecommerce': '/_blob/b70d1fd6eb5a9839c3acd3ccea5d44a1',
    'kitchen': '/_blob/2066a54da13614d9c2246994e32d1902',
    'laptop': '/_blob/c7127cc17cfd8909184853095227a34d',
    'team': '/_blob/3b6448ffe67d241e50c579a0950384e9',
    'lounge': '/_blob/37cbc555ab9573d99c3c204f11469679',
    'papers': '/_blob/959f667ae9fbf3a0eb90cf0ce15668ff',
}
HERO_BG = {  # the Lane C3 hero variants: (desktop, mobile) focal points
    'kitchen': ('A chef plating dishes in a restaurant kitchen', ('62% 40%', '80% 28%')),
    'office': ('A business owner thinking at a desk', ('62% 30%', '74% 30%')),
    'ecommerce': ('A business owner packing an online order', ('66% 38%', '82% 30%')),
}
HEADS = ['/_blob/b0f8fafa98dcbe0082a836a30303b5e5', '/_blob/8dcd87561fad4fb41686cffb42d245b4', '/_blob/4a8aee7bf8f13bc1315ec9fa3aa9642d']
BADGES = [
    ('5a6f8298d29fe5b417692e04bb5cefb5', 'QuickBooks ProAdvisor Elite badge'),
    ('cd885cfb7d6c05d7b71c90e8441a681f', 'Certified QuickBooks Level 2 ProAdvisor badge'),
    ('34b1807ca27f04b30ace3c235cf23ea4', 'Certified QuickBooks Level 1 ProAdvisor badge'),
    ('1f90e7cd2b6fe11043a8aed199ff3bea', 'Certified Advanced QuickBooks Online ProAdvisor badge'),
    ('8a6858620a6c323d48dea6c25360ff27', 'Certified ProAdvisor, Advanced QuickBooks Desktop badge'),
    ('bdd1481bd009109078c5f28e16b35880', 'Certified QuickBooks Online ProAdvisor badge'),
    ('9eef1fc8b132f5488cb3871c7327a754', 'Certified ProAdvisor, QuickBooks Enterprise badge'),
]
PROADVISOR = 'https://proadvisor.intuit.com/app/accountant/search?searchId=bernard-roesch'

I = {  # line icons, 24px grid, drawn with currentColor
    'doc': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5"/><path d="M9 14l2 2 4-4"/>',
    'gear': '<circle cx="12" cy="12" r="3"/><path d="M12 2.5v3M12 18.5v3M4.6 4.6l2.1 2.1M17.3 17.3l2.1 2.1M2.5 12h3M18.5 12h3M4.6 19.4l2.1-2.1M17.3 6.7l2.1-2.1"/>',
    'people': '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><circle cx="17" cy="9" r="2.5"/><path d="M16 14.2a5 5 0 0 1 5.5 5.8"/>',
    'spark': '<path d="M12 3l1.8 4.7 4.7 1.8-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M18 15l.8 2.2L21 18l-2.2.8L18 21l-.8-2.2L15 18l2.2-.8z"/>',
    'receipt': '<path d="M6 2.5h12v19l-3-2-3 2-3-2-3 2z"/><path d="M9 7h6M9 11h6M9 15h4"/>',
    'pos': '<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6.5 15h4"/>',
    'bars': '<path d="M3 21h18"/><path d="M6 17v-5M11 17V7M16 17v-8M21 17V4" transform="translate(-1.5 0)"/>',
    'cap': '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
    'box': '<path d="M21 8l-9-5-9 5v8l9 5 9-5z"/><path d="M3 8l9 5 9-5M12 13v8"/>',
    'pminus': '<circle cx="9" cy="8" r="4"/><path d="M2 21a7 7 0 0 1 14 0M16 11h6"/>',
    'shield': '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M12 8v5M12 16h.01"/>',
    'clock': '<path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5M12 7v5l3 2"/>',
    'filex': '<path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M10 12l4 4M14 12l-4 4"/>',
    'bank': '<path d="M3 10l9-6 9 6M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 21h18"/>',
    'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
    'heart': '<path d="M12 20s-7-4.5-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.5-9 9-9 9z"/>',
    'hat': '<path d="M3 18h18M5 18v-3a7 7 0 0 1 14 0v3M10 8V5h4v3"/>',
    'fork': '<path d="M7 3v8M5 3v5a2 2 0 0 0 4 0V3M7 11v10M17 3c-2 2-3 5-3 8h3v10"/>',
    'bldg': '<rect x="4" y="3" width="10" height="18"/><path d="M14 9h6v12h-6M8 7h2M8 11h2M8 15h2"/>',
    'factory': '<path d="M3 21V10l6 4V10l6 4V6h6v15z"/><path d="M7 17h2M12 17h2M17 17h2"/>',
    'cart': '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.5 12h11.5l2-8H6.2"/>',
}
CAL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4.5" width="18" height="16.5" rx="2"></rect><path d="M16 2.5v4"></path><path d="M8 2.5v4"></path><path d="M3 10h18"></path></svg>'
ARR = '<svg class="ar" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
PLUS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M12 5v14M5 12h14"></path></svg>'
QUOTE = '<svg width="30" height="24" viewBox="0 0 30 24" fill="#2459F5" aria-hidden="true"><path d="M0 24V14C0 6 4 1.5 12 0l1.5 3C9 4.5 7 7.5 7 11h5v13zm17 0V14c0-8 4-12.5 12-14l1 3c-4.5 1.5-6.5 4.5-6.5 8H29v13z"></path></svg>'


def ic(name, size=26, color=None):
    st = ' style="color: %s"' % color if color else ''
    return '<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"%s>%s</svg>' % (size, size, st, I[name])


def esc(s):
    return s.replace('&', '&amp;') if '&amp;' not in s else s


# ---- content (ELI15, from the C3/D3/G3 wording; brand lines from the style board) ----
NAV = [('#services', 'Services'), ('#case-studies', 'Case studies'), ('#about', 'About'), ('#products', 'Products'), ('#blog', 'Blog'), ('#contact', 'Contact')]
HERO_P = 'We fix messy books, keep them right every month, and show you your numbers in plain words. You get to focus on running your business.'
TIERS = [
    ('doc', 'Bookkeeping &amp; Accounting', 'Almost every client needs this'),
    ('gear', 'QuickBooks Setup &amp; Advisory', 'Set up right, then put to good use'),
    ('people', 'Fractional CFO', 'Big decisions, for a few clients'),
]
CASES = [
    ('Food production', 'A bakery tracking food that spoils fast', 'How a bakery keeps count of fresh goods in QuickBooks Enterprise.', 'https://missionaccountinghelp.com/customers/quickbooks-online-vs-enterprise'),
    ('Jewelry', 'A jewelry business keeping track of custom orders', 'How a jewelry business tracks custom orders, and where each piece is kept, in QuickBooks Enterprise.', 'https://missionaccountinghelp.com/customers/quickbooks-online-vs-enterprise'),
    ('Bills and expenses', 'Bills to approve and spending to track', "How Wren's Nest Interiors made bill approvals and expense tracking automatic.", 'https://missionaccountinghelp.com/technology/accounting-software/automated-accounting-software'),
]
SOFTWARE = ['QuickBooks Online', 'QuickBooks Desktop', 'QuickBooks Enterprise', 'Intuit Enterprise Suite', 'QuickBooks Workforce', 'QuickBooks Payments']
SPECIAL = [('box', 'Keeping track of stock'), ('hat', 'What each job really costs'), ('cart', 'Selling in more than one place online'), ('layers', 'More than one company')]
TOP = [
    ('doc', 'Bookkeeping &amp; Accounting', 'Almost every client ends up here', 'Up to date, every month', 'Books that match your bank and that you can trust, every month, kept by a team that knows QuickBooks inside out.'),
    ('gear', 'QuickBooks Setup &amp; Advisory', 'Moving off spreadsheets, or outgrowing your setup', 'A system built around how you work', 'QuickBooks set up and connected the right way, then we help you use your numbers to make better choices about prices, cash and growth.'),
    ('people', 'Fractional CFO', 'Only for a few clients', 'Big decisions', 'A part-time finance chief, Bernard, without hiring one full-time. Our managing partner leads this.'),
]
SUPPORT = [
    ('spark', 'QuickBooks Cleanup', 'Months of bank statements nobody has matched to the books, brought up to date.'),
    ('receipt', 'Tax Readiness', 'We fix the books, help you find a tax accountant (a CPA), and talk with them before they start.'),
    ('pos', 'POS Integration', 'We connect your checkout system, like Square or Shopify, to QuickBooks so your sales show up on their own.'),
    ('bars', 'Custom Reporting', "Normal reports answer your accountant's questions. Custom reports answer yours."),
    ('cap', 'QuickBooks Training', 'We teach your team how to use your own setup.'),
]
TRIGGERS = [
    ('pminus', 'Our bookkeeper just left', 'Maybe they retired, moved on, or you couldn\'t count on them. We go through what they left, fill in the gaps, and take over the monthly work.'),
    ('shield', "We don't trust our accountant anymore", 'The work comes late, has mistakes, or your emails go unanswered. First, we tell you honestly how your books look.'),
    ('clock', "We're months, or years, behind", 'Nobody has matched the bank statements to the books in so long that no one wants to open QuickBooks. We clean it up first, then keep it up every month.'),
    ('filex', "Our taxes haven't been filed", 'Your books are too messy to do taxes from. We fix the books, help you find a tax accountant (a CPA), and talk with them before they start.'),
    ('bank', 'The bank wants clear, correct numbers', 'A bank, investor or buyer wants numbers you can trust. We get you reports you can hand over with confidence.'),
    ('layers', 'Our business got too big for our bookkeeper', 'Lots of stock, more than one company, or nonprofit rules can be too much for one bookkeeper. That\'s the kind of work we like best.'),
]
INDUSTRIES = [
    ('heart', 'Nonprofits', "Money set aside for certain uses tracked apart from money that isn't, and reported the way your board and your auditor expect."),
    ('hat', 'Construction', 'What each job really costs, unfinished work and changes to the job, all kept straight in QuickBooks.'),
    ('fork', 'Restaurants', 'Food and staff costs, daily sales and checkout numbers that actually match the bank.'),
    ('bldg', 'Property management', 'Rent lists, owner statements and tenant payments, matched to the bank every month.'),
    ('factory', 'Manufacturing', 'Stock, its full cost including shipping, and unfinished work, in reports that still add up at year end.'),
    ('cart', 'Ecommerce', 'Shopify and Amazon sales matched to QuickBooks, for businesses that sell in more than one place.'),
]
SPEC_P = "We're best at three things: showing what each job really costs for businesses that sell their time, keeping track of stock, and making sure Shopify and Amazon sales match QuickBooks. We're also happy to handle nonprofit rules and businesses with more than one company. If your business is simple, one good bookkeeper is enough. If it isn't, this is the work we want."
QUOTES = [  # word for word from the Business DNA
    ('We have been working with Bernard for over 10 years. He has been terrific.', 'Jacquie Herz', 'Jornik Manufacturing, Stamford, CT'),
    ('I have been working with Bernard at MISSION since 2007.', 'Richard Cipolla', 'Richard Cipolla Designs, Stamford, CT'),
    ('I have worked with Bernard for 10 years.', 'Kristin Fine', 'Fine Concepts, Darien, CT'),
    ('Great customer service from Bernard and his team – very friendly and helpful.', 'Mary Iaffaldano', 'Milford, CT'),
    ('Bernard and Gina have been a great team.', 'Jane Didona', 'Didona Associates, Danbury, CT'),
]
STATS = [('10+', 'years several of our clients have stayed'), ('~50', 'client reviews on our ProAdvisor profile'), ('5.0', 'our average star rating on Google')]
TEAM = [
    ('Bernard P. Roesch', 'Co-founder and Managing Partner · Harvard Business School MBA, Elite-tier QuickBooks ProAdvisor'),
    ('Carol A. Onorato', 'Director of Operations · Level 2 Advanced QuickBooks ProAdvisor'),
    ('Rob James', 'Prospect pipeline and new-client onboarding · Level 2 Advanced QuickBooks ProAdvisor'),
]
TEAM_P = "We're business advisors who know accounting software really well. Our core team holds advanced QuickBooks certifications, and we bring in trusted accountants and specialists from our wider network when your work needs them."
FAQ = [
    ('What happens in the free consultation?', "It's a chat, not a sales pitch. Bernard or Rob will ask how your books are going, look at anything you can share, and tell you what they would fix first."),
    ('Do I need to prepare anything?', None),
    ('Is my business too small for you?', None),
    ('We already have a tax accountant. Does that change anything?', None),
    ('How quickly can you start?', None),
]
BLOG = [
    ('QuickBooks', 'QuickBooks Desktop to Online: what actually changes', 'Switching from the desktop version to the online one changes your daily routine. Here\'s what to expect.', 'lounge', '78% 60%'),
    ('Customers', 'QuickBooks Online vs Enterprise: going beyond the basics', 'The big differences show up when you track stock, orders and where things are kept.', 'papers', 'center 40%'),
    ('Technology', 'Is automated accounting software the future of financial accounting?', 'Software can do the boring, repeat work. People still make the judgment calls. Here\'s what that means for you.', 'laptop', 'center 40%'),
]
FOOT_SERVICES = [('#bookkeeping', 'Bookkeeping &amp; Accounting'), ('#setup', 'QuickBooks Setup &amp; Advisory'), ('#cfo', 'Fractional CFO'), ('#cleanup', 'QuickBooks Cleanup'), ('#tax', 'Tax Readiness'), ('#reporting', 'Custom Reporting'), ('#pos', 'POS Integration'), ('#training', 'QuickBooks Training')]
FOOT_CO = [('#about', 'About'), ('#products', 'QuickBooks Products'), ('#partners', 'Partner Program'), ('#blog', 'Blog'), ('http://missionaccountinghelp.com/feed/podcast', 'Podcast'), ('#contact', 'Contact')]
FOOT_LEGAL = [('#terms', 'Terms of Service'), ('#privacy', 'Privacy Policy'), ('#cookies', 'Cookie Policy'), ('#returns', 'Returns Policy')]


CSS = r"""
body{margin:0;background:#101419}
.lh{font-family:'Open Sans','Helvetica Neue',Arial,sans-serif;color:#3A424D;-webkit-font-smoothing:antialiased;font-size:15px;line-height:1.6}
.lh *{box-sizing:border-box}
.lh h1,.lh h2,.lh h3{margin:0;font-family:'Space Grotesk','Open Sans',sans-serif;font-weight:600;color:#101419;letter-spacing:-.025em;text-wrap:balance}
.lh p{margin:0}
.lh .dk{background:#101419;color:#B9C0CA}
.lh .dk h1,.lh .dk h2,.lh .dk h3{color:#FFFFFF}
.lh .bl{background:#2459F5;color:#DCE5FF}
.lh .bl h1,.lh .bl h2,.lh .bl h3{color:#FFFFFF}
.lh .ch{background:#F5F6F7}
.lh .wh{background:#FFFFFF}
.lh .eb{margin:0;display:flex;align-items:center;gap:14px;font:600 12px/1.3 'Space Grotesk',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#2459F5}
.lh .eb b{font-weight:600;color:#101419}
.lh .dk .eb{color:#8FAEFF}
.lh .dk .eb b{color:#FFFFFF}
.lh .bl .eb,.lh .bl .eb b{color:#FFFFFF}
.lh .bl .btn-o{color:#FFFFFF;border-color:rgba(255,255,255,.55)}
.lh .bl .btn-o:hover,.lh .bl .btn-o:focus-visible{border-color:#FFFFFF}
.lh .bl .btn-p{background:#101419}
.lh .bl .btn-p:hover,.lh .bl .btn-p:focus-visible{background:#000000}
.lh .bl .nav a{color:#E3EAFF}
.lh .bl .nav a:hover,.lh .bl .nav a:focus-visible{color:#FFFFFF}
.hero-bg-kitchen,.hero-bg-office,.hero-bg-ecommerce{display:none}
[data-hero="kitchen"] .hero-bg-kitchen,[data-hero="office"] .hero-bg-office,[data-hero="ecommerce"] .hero-bg-ecommerce{display:block}
.lh .mu{color:#5E6670}
.lh .dk .mu{color:#9AA3AE}
.lh .bl .mu{color:#DCE5FF}
.lh .btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:52px;padding:0 24px;border-radius:4px;border:1px solid transparent;font:600 15px/1 'Space Grotesk',sans-serif;text-decoration:none;white-space:nowrap;cursor:pointer;transition:background-color .25s ease,color .25s ease,border-color .25s ease}
.lh .btn-p{background:#2459F5;color:#FFFFFF}
.lh .btn-p:hover,.lh .btn-p:focus-visible{background:#1B47CC}
.lh .btn-o{background:transparent;color:#101419;border-color:#C9CED6}
.lh .btn-o:hover,.lh .btn-o:focus-visible{border-color:#101419}
.lh .dk .btn-o{color:#FFFFFF;border-color:rgba(255,255,255,.3)}
.lh .dk .btn-o:hover,.lh .dk .btn-o:focus-visible{border-color:#FFFFFF}
.lh .btn-w{background:#FFFFFF;color:#101419}
.lh .btn-w:hover,.lh .btn-w:focus-visible{background:#E8EEFF}
.lh .lk{display:inline-flex;align-items:center;gap:8px;font:600 14.5px/1.3 'Space Grotesk',sans-serif;color:#2459F5;text-decoration:none}
.lh .dk .lk{color:#FFFFFF}
.lh .lk .ar,.lh .btn .ar{transition:transform .25s ease}
.lh .lk:hover .ar,.lh .btn:hover .ar,.lh a:hover .lk .ar{transform:translateX(3px)}
.lh .nav a{color:#C3C9D2;text-decoration:none;font-size:14px;font-weight:600;transition:color .2s ease}
.lh .nav a:hover,.lh .nav a:focus-visible{color:#FFFFFF}
.lh .ph{position:relative;overflow:hidden;background:#1B2029}
.lh .ph img{display:block;width:100%;height:100%;object-fit:cover;filter:saturate(.35) contrast(1.1) brightness(.84)}
.lh .ph::after{content:"";position:absolute;inset:0;background:#2459F5;mix-blend-mode:color;opacity:.22;pointer-events:none}
.lh .dots{background-image:radial-gradient(#8FA3C8 1.3px,transparent 1.4px);background-size:16px 16px}
.lh .dk .dots,.lh .dots.on-dk{background-image:radial-gradient(rgba(255,255,255,.28) 1.3px,transparent 1.4px)}
.lh .wedge{clip-path:polygon(0 0,100% 0,62% 100%,0 100%)}
.lh .ic{display:inline-flex;align-items:center;justify-content:center;flex:none;color:#2459F5}
.lh .dk .ic{color:#8FAEFF}
.lh .card{background:#FFFFFF;border:1px solid #E2E5EA;border-radius:6px;transition:border-color .25s ease,transform .25s ease}
.lh a.card{text-decoration:none;color:inherit;display:flex}
.lh a.card:hover,.lh a.card:focus-visible{border-color:#2459F5;transform:translateY(-3px)}
.lh .tag{font:600 11.5px/1.3 'Space Grotesk',sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#2459F5}
.lh .dk .tag{color:#8FAEFF}
.lh .faq{all:unset;box-sizing:border-box;width:100%;display:flex;align-items:center;justify-content:space-between;gap:20px;padding:22px 0;border-top:1px solid #DDE1E6;cursor:pointer;font:600 17px/1.35 'Space Grotesk',sans-serif;color:#101419}
.lh .faq svg{color:#2459F5;flex:none;transition:transform .25s ease}
.lh .faq[aria-expanded="true"] svg{transform:rotate(45deg)}
.lh .foot a{color:#AEB5BF;text-decoration:none;font-size:13.5px;transition:color .2s ease}
.lh .foot a:hover,.lh .foot a:focus-visible{color:#FFFFFF}
.lh .foot .fh{margin:0 0 6px;font:600 11.5px/1.3 'Space Grotesk',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8FAEFF}
.lh .foot input{flex:1;min-width:0;height:48px;padding:0 14px;border:1px solid rgba(255,255,255,.2);border-radius:4px;background:rgba(255,255,255,.05);font:400 14px/1 'Open Sans',sans-serif;color:#FFFFFF}
.lh .foot input::placeholder{color:#7D8692}
.lh .foot input:focus{outline:none;border-color:#8FAEFF}
.lh .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.lh .script{font-family:'Caveat',cursive;font-weight:600;color:#FFFFFF;line-height:.95}
@media (prefers-reduced-motion: reduce){.lh *{transition:none !important}}
/* Review toggle: blue (#2459F5) or green (#C1F432) solid buttons */
.tg-bar{min-height:40px;box-sizing:border-box;background:#141414;color:#FFFFFF;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:12px;padding:6px 8px;font:500 12.5px/1 system-ui,-apple-system,'Segoe UI',sans-serif}
.tg-bar .tg-label{color:#BDBDBD}
.tg-bar .tg-group{display:inline-flex;background:#2B2B2B;border-radius:999px;padding:3px;gap:2px}
.tg-bar .tg-opt{all:unset;cursor:pointer;display:inline-flex;align-items:center;gap:7px;height:26px;padding:0 12px;border-radius:999px;color:#D0D0D0;font:600 12px/1 system-ui,-apple-system,'Segoe UI',sans-serif;transition:background-color .2s ease,color .2s ease}
.tg-bar .tg-opt:hover{color:#FFFFFF}
.tg-bar .tg-opt:focus-visible{outline:2px solid #8FAEFF;outline-offset:2px}
.tg-bar .tg-opt[aria-pressed="true"]{background:#FFFFFF;color:#141414}
.tg-bar .tg-dot{width:10px;height:10px;border-radius:50%;display:inline-block}
[data-btn="green"] .tg-btn{background:#C1F432 !important;color:#101419 !important;border-color:#C1F432 !important}
[data-btn="green"] .tg-btn:hover,[data-btn="green"] .tg-btn:focus-visible{opacity:.9}
[data-btn="green"] .tg-btn *{color:#101419 !important}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600&amp;family=Open+Sans:wght@400;600&amp;family=Caveat:wght@600&amp;display=swap">'


def sched(label='Schedule a free consultation', extra=''):
    return '<a class="btn btn-p tg-btn" href="#schedule"%s>%s%s</a>' % (extra, CAL, label)


def eyebrow(num, text):
    return '<p class="eb"><b>%s</b><span>%s</span></p>' % (num, text)


def stars():
    return '<span aria-hidden="true" style="display: inline-flex; align-items: center">' + ''.join(
        '<img src="%s" alt="" style="position: relative; z-index: %d; width: 34px; height: 34px; border-radius: 50%%; object-fit: cover; border: 2px solid #2459F5; margin-left: %dpx">' % (h, 3 - i, 0 if i == 0 else -10)
        for i, h in enumerate(HEADS)) + '</span>'


def page(m):
    # m: True for the 390 mobile board
    W = 390 if m else 1440
    G = 20 if m else 40          # side gutter
    wrap = 'max-width: 1160px; margin: 0 auto; padding: 0 %dpx' % G if not m else 'padding: 0 20px'
    sec = (52 if m else 100)     # section padding
    h2 = 34 if m else 54
    o = []
    A = o.append
    A('<div data-btn="{{ btnMode }}" data-hero="{{ heroMode }}" class="lh" style="width: %dpx; background: #101419">' % W)
    A('<div class="tg-bar" aria-label="Review control, not part of the design">')
    A('<span class="tg-label">Review · %s</span>' % ('buttons' if m else 'button color'))
    A('<div class="tg-group" role="group" aria-label="Button color">')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isBlue }}" onClick="{{ setBlue }}"><span class="tg-dot" style="background: #2459F5"></span>Blue</button>')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isGreen }}" onClick="{{ setGreen }}"><span class="tg-dot" style="background: #C1F432"></span>%s</button>' % ('Green' if m else 'Green #C1F432'))
    A('</div>')
    A('<span style="display: inline-flex; align-items: center; gap: 8px"><span class="tg-label">Hero</span><span class="tg-group" role="group" aria-label="Hero background">')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isKitchen }}" onClick="{{ setKitchen }}">Kitchen</button>')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isOffice }}" onClick="{{ setOffice }}">Office</button>')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isEcommerce }}" onClick="{{ setEcommerce }}">Ecommerce</button>')
    A('</span></span>\n</div>\n')

    # ---------- 01 Hero ----------
    A('<!-- 01 Hero: Electric Blue on the left, a photo on the right (kitchen, office or ecommerce, chosen in the review bar), three core services along the bottom -->')
    A('<section class="bl" style="position: relative; overflow: hidden">')
    if m:
        A('<header style="position: relative; z-index: 3; height: 68px; padding: 0 20px; display: flex; align-items: center; justify-content: space-between">')
        A('<a href="#top" aria-label="MISSION home" style="display: flex"><img src="%s" alt="MISSION" style="height: 24px; width: auto; display: block"></a>' % LOGO_W)
        A('<div style="display: flex; gap: 8px"><a class="btn btn-p tg-btn" href="#schedule" style="height: 40px; padding: 0 14px; font-size: 13.5px">%sSchedule</a>' % CAL)
        A('<button type="button" aria-label="Open menu" style="all: unset; cursor: pointer; width: 40px; height: 40px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,.5); border-radius: 4px; color: #FFFFFF"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"></path></svg></button></div>')
        A('</header>')
        A('<div id="top" style="position: relative; z-index: 2; padding: 36px 20px 0; display: flex; flex-direction: column; gap: 20px">')
        A('<p class="eb" style="letter-spacing: .16em">Practical. Reassuring. Experienced.</p>')
        A('<h1 style="font-size: 44px; line-height: 1; letter-spacing: -.035em">Complex books.<br>Clear answers.</h1>')
        A('<p style="font-size: 16.5px; line-height: 1.6; color: #EEF2FF">%s</p>' % HERO_P)
        A('<div style="display: flex; flex-direction: column; gap: 12px; padding-top: 6px">%s<a class="btn btn-o" href="#case-studies">Read client stories%s</a></div>' % (sched(extra=' style="width: 100%"'), ARR))
        A('<div style="display: flex; align-items: center; gap: 12px; font-size: 13.5px; color: #EEF2FF">%s<span><strong style="color: #FFFFFF">5.0 average</strong> on Google reviews</span></div>' % stars())
        A('</div>')
        A('<div style="position: relative; margin-top: 32px; height: 250px; overflow: hidden">')
        for k, (alt, pos) in HERO_BG.items():
            A('<img class="hero-bg-%s" src="%s" alt="" style="position: absolute; inset: 0; width: 100%%; height: 100%%; object-fit: cover; object-position: %s">' % (k, PH[k], pos[1]))
        A('<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(180deg, #2459F5 0%, rgba(36, 89, 245, 0) 30%)"></div>')
        A('<div aria-hidden="true" class="wedge" style="position: absolute; left: 0; bottom: 0; width: 46%; height: 56px; background: #101419"></div>')
        A('<p class="script" aria-hidden="true" style="position: absolute; right: 18px; top: 26px; font-size: 30px; transform: rotate(-7deg); text-align: right; text-shadow: 0 1px 12px rgba(0, 0, 0, .35)">Numbers create<br>possibility.</p>')
        A('</div>')
        A('<div class="dk" style="padding: 8px 20px 28px; display: flex; flex-direction: column">')
        for k, (icn, t, s) in enumerate(TIERS):
            A('<div style="display: flex; align-items: center; gap: 14px; padding: 16px 0;%s"><span class="ic">%s</span><span style="display: flex; flex-direction: column; gap: 2px"><strong style="font: 600 15.5px/1.3 \'Space Grotesk\', sans-serif; color: #FFFFFF">%s</strong><span style="font-size: 13px; color: #9AA3AE">%s</span></span></div>' % ('' if k == 0 else ' border-top: 1px solid rgba(255,255,255,.12);', ic(icn, 26), t, s))
        A('</div>')
    else:
        A('<div aria-hidden="true" style="position: absolute; top: 0; right: 0; bottom: 101px; width: 46%">')
        for k, (alt, pos) in HERO_BG.items():
            A('<img class="hero-bg-%s" src="%s" alt="" style="position: absolute; inset: 0; width: 100%%; height: 100%%; object-fit: cover; object-position: %s">' % (k, PH[k], pos[0]))
        A('<div style="position: absolute; inset: 0; background: linear-gradient(90deg, #2459F5 0%, rgba(36, 89, 245, .55) 16%, rgba(36, 89, 245, 0) 42%)"></div>')
        A('</div>')
        A('<div aria-hidden="true" class="wedge" style="position: absolute; left: 54%; bottom: 101px; width: 260px; height: 88px; background: #101419; z-index: 1"></div>')
        A('<p class="script" aria-hidden="true" style="position: absolute; right: 64px; top: 150px; z-index: 2; font-size: 46px; transform: rotate(-7deg); text-align: right; text-shadow: 0 1px 14px rgba(0, 0, 0, .35)">Numbers create<br>possibility.</p>')
        A('<header style="position: relative; z-index: 3">')
        A('<nav aria-label="Main" class="nav" style="max-width: 1160px; margin: 0 auto; padding: 0 40px; height: 88px; display: flex; align-items: center; justify-content: space-between; gap: 24px">')
        A('<a href="#top" aria-label="MISSION home" style="display: flex"><img src="%s" alt="MISSION" style="height: 28px; width: auto; display: block"></a>' % LOGO_W)
        A('<div style="display: flex; align-items: center; gap: 30px">' + ''.join('<a href="%s">%s</a>' % x for x in NAV) + '</div>')
        A('<div style="display: flex; align-items: center; gap: 20px"><a href="tel:+12032279475" style="color: #FFFFFF">(203) 227-9475</a><a class="btn btn-p tg-btn" href="#schedule" style="height: 44px; padding: 0 18px; font-size: 14px; color: #FFFFFF">%sSchedule a consultation</a></div>' % CAL)
        A('</nav>\n</header>')
        A('<div id="top" style="position: relative; z-index: 2; max-width: 1160px; margin: 0 auto; padding: 96px 40px 120px">')
        A('<div style="max-width: 640px; display: flex; flex-direction: column; gap: 26px">')
        A('<p class="eb" style="letter-spacing: .18em">Practical. Reassuring. Experienced.</p>')
        A('<h1 style="font-size: 84px; line-height: .96; letter-spacing: -.04em">Complex books.<br>Clear answers.</h1>')
        A('<p style="font-size: 18px; line-height: 1.6; color: #EEF2FF; max-width: 520px">%s</p>' % HERO_P)
        A('<div style="display: flex; align-items: center; gap: 14px; padding-top: 6px">%s<a class="btn btn-o" href="#case-studies">Read client stories%s</a></div>' % (sched(), ARR))
        A('<div style="display: flex; align-items: center; gap: 12px; font-size: 14px; color: #EEF2FF">%s<span><strong style="color: #FFFFFF">5.0 average</strong> on Google reviews</span></div>' % stars())
        A('</div>\n</div>')
        A('<div class="dk" style="position: relative; z-index: 2">')
        A('<div style="max-width: 1160px; margin: 0 auto; padding: 0 40px; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr))">')
        for k, (icn, t, s) in enumerate(TIERS):
            A('<a href="#services" style="display: flex; align-items: center; gap: 16px; padding: 28px %s; text-decoration: none;%s"><span class="ic">%s</span><span style="display: flex; flex-direction: column; gap: 3px"><strong style="font: 600 16px/1.3 \'Space Grotesk\', sans-serif; color: #FFFFFF">%s</strong><span style="font-size: 13.5px; color: #9AA3AE">%s</span></span></a>' % ('0' if k == 0 else '0 0 0 32px', '' if k == 0 else ' border-left: 1px solid rgba(255,255,255,.12);', ic(icn, 30), t, s))
        A('</div>\n</div>')
    A('</section>\n')

    # ---------- 02 Case studies ----------
    A('<!-- 02 Case studies lead the page: featured construction story, three story cards, a closing call -->')
    A('<section id="case-studies" aria-label="Case studies" class="ch" style="position: relative; padding: %dpx 0">' % sec)
    A('<div style="%s; display: flex; flex-direction: column; gap: %dpx">' % (wrap, 28 if m else 48))
    if m:
        A('<div style="display: flex; flex-direction: column; gap: 16px">%s<h2 style="font-size: %dpx; line-height: 1.04">Real problems clients had, and how we fixed them.</h2><p class="mu" style="font-size: 15.5px">Real stories from our blog. Each one shows the problem a business had and how we set up QuickBooks to fix it.</p></div>' % (eyebrow('01', 'Case studies'), h2))
    else:
        A('<div style="display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: 40px; align-items: end"><div style="display: flex; flex-direction: column; gap: 18px">%s<h2 style="font-size: %dpx; line-height: 1.02">Real problems clients had, and how we fixed them.</h2></div><p class="mu" style="font-size: 16.5px; max-width: 440px">Real stories from our blog. Each one shows the problem a business had and how we set up QuickBooks to fix it.</p></div>' % (eyebrow('01', 'Case studies'), h2))
    feat_url = 'https://missionaccountinghelp.com/customers/quickbooks-enterprise-support'
    if m:
        A('<a href="%s" target="_blank" rel="noopener" style="display: flex; flex-direction: column; text-decoration: none; border-radius: 6px; overflow: hidden; background: #101419">' % feat_url)
        A('<div class="ph" style="height: 230px"><img src="%s" alt="A construction crew reviewing plans on a job site" style="object-position: center 40%%"></div>' % PH['construction'])
        A('<div style="padding: 24px 22px 26px; display: flex; flex-direction: column; gap: 12px"><span class="tag" style="color: #8FAEFF">Construction · Featured story</span><h3 style="font-size: 25px; line-height: 1.15; color: #FFFFFF">A construction company had useful QuickBooks tools it wasn\'t using</h3><p style="font-size: 15px; color: #B9C0CA">We found the tools already built into their QuickBooks Enterprise that nobody was using, and set them up for the way they work.</p><span class="lk" style="color: #FFFFFF; padding-top: 4px">Read the story%s</span></div>' % ARR)
        A('</a>')
    else:
        A('<a href="%s" target="_blank" rel="noopener" style="display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); text-decoration: none; border-radius: 6px; overflow: hidden; background: #101419; min-height: 460px">' % feat_url)
        A('<div class="ph" style="position: relative"><img src="%s" alt="A construction crew reviewing plans on a job site" style="position: absolute; inset: 0; object-position: center 40%%"><span aria-hidden="true" class="wedge" style="position: absolute; left: 0; bottom: 0; width: 220px; height: 84px; background: #2459F5; z-index: 1"></span></div>' % PH['construction'])
        A('<div style="position: relative; padding: 48px 44px; display: flex; flex-direction: column; justify-content: space-between; gap: 28px"><div aria-hidden="true" class="dots on-dk" style="position: absolute; top: 28px; right: 28px; width: 120px; height: 72px"></div><span class="tag" style="color: #8FAEFF">Construction · Featured story</span><div style="display: flex; flex-direction: column; gap: 16px"><h3 style="font-size: 34px; line-height: 1.1; color: #FFFFFF">A construction company had useful QuickBooks tools it wasn\'t using</h3><p style="font-size: 16px; color: #B9C0CA">We found the tools already built into their QuickBooks Enterprise that nobody was using, and set them up for the way they work.</p></div><span class="lk" style="color: #FFFFFF">Read the story%s</span></div>' % ARR)
        A('</a>')
    A('<div style="display: grid; grid-template-columns: %s; gap: %dpx">' % ('minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', 14 if m else 20))
    for lab, t, p, u in CASES:
        A('<a class="card" href="%s" target="_blank" rel="noopener" style="flex-direction: column; justify-content: space-between; gap: 18px; padding: %s; min-height: %s"><span style="display: flex; flex-direction: column; gap: 12px"><span class="tag">%s</span><h3 style="font-size: %dpx; line-height: 1.2">%s</h3><span class="mu" style="font-size: 14.5px">%s</span></span><span class="lk">Read the story%s</span></a>' % (u, '22px' if m else '28px', 'auto' if m else '250px', lab, 20 if m else 22, t, p, ARR))
    A('</div>')
    if m:
        A('<div style="display: flex; flex-direction: column; gap: 16px; padding: 24px 22px; border-radius: 6px; background: #2459F5"><h3 style="font-size: 22px; color: #FFFFFF">Do your books look like this?</h3><p style="font-size: 15px; color: #DCE5FF">Come as you are, mess and all. We\'ll tell you what we\'d fix first.</p>%s</div>' % sched(extra=' style="width: 100%; background: #FFFFFF; color: #101419"'))
    else:
        A('<div style="display: flex; align-items: center; justify-content: space-between; gap: 24px; padding: 30px 36px; border-radius: 6px; background: #2459F5"><div style="display: flex; flex-direction: column; gap: 6px"><h3 style="font-size: 26px; color: #FFFFFF">Do your books look like this?</h3><p style="font-size: 15.5px; color: #DCE5FF">Come as you are, mess and all. We\'ll tell you what we\'d fix first.</p></div>%s</div>' % sched(extra=' style="background: #FFFFFF; color: #101419"'))
    A('</div>\n</section>\n')

    # ---------- 03 Software strip ----------
    A('<!-- 03 Software strip -->')
    A('<section aria-label="Software we know" class="wh" style="border-top: 1px solid #E2E5EA; border-bottom: 1px solid #E2E5EA">')
    if m:
        A('<div style="padding: 28px 20px; display: flex; flex-direction: column; gap: 14px"><p class="tag" style="margin: 0; color: #5E6670">The software we know really well</p><div style="display: flex; flex-wrap: wrap; gap: 8px 18px; font: 600 15px/1.4 \'Space Grotesk\', sans-serif; color: #101419">' + ''.join('<span>%s</span>' % s for s in SOFTWARE) + '</div></div>')
    else:
        A('<div style="max-width: 1160px; margin: 0 auto; padding: 30px 40px; display: flex; align-items: center; justify-content: space-between; gap: 24px"><p class="tag" style="margin: 0; color: #5E6670; flex: none">The software we know really well</p><div style="display: flex; flex-wrap: wrap; justify-content: flex-end; gap: 10px 34px; font: 600 16px/1.4 \'Space Grotesk\', sans-serif; color: #101419">' + ''.join('<span>%s</span>' % s for s in SOFTWARE) + '</div></div>')
    A('</section>\n')

    # ---------- 04 Positioning ----------
    A('<!-- 04 Positioning, after the style board: a specialist team, with the photography grid -->')
    A('<section id="about" aria-label="Who we are" class="dk" style="position: relative; overflow: hidden; padding: %dpx 0">' % sec)
    if m:
        A('<div style="padding: 0 20px; display: flex; flex-direction: column; gap: 20px">%s<h2 style="font-size: %dpx; line-height: 1.04">A specialist team that knows your business.</h2><p style="font-size: 15.5px">You started a business, not a bookkeeping job. We keep your books clean and correct. You don\'t have to hire a full finance team or get lost at a big firm.</p>' % (eyebrow('02', 'Who we are'), h2))
    else:
        A('<div style="max-width: 1160px; margin: 0 auto; padding: 0 40px; display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 6fr); gap: 64px; align-items: center"><div style="display: flex; flex-direction: column; gap: 24px">%s<h2 style="font-size: %dpx; line-height: 1.02">A specialist team that knows your business.</h2><p style="font-size: 16.5px; max-width: 460px">You started a business, not a bookkeeping job. We keep your books clean and correct. You don\'t have to hire a full finance team or get lost at a big firm.</p>' % (eyebrow('02', 'Who we are'), h2))
    A('<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: %s; padding-top: 8px">' % ('12px 14px' if m else '16px 24px'))
    for icn, t in SPECIAL:
        A('<div style="display: flex; align-items: center; gap: 12px; padding-top: 14px; border-top: 1px solid rgba(255,255,255,.14)"><span class="ic">%s</span><span style="font: 600 %spx/1.3 \'Space Grotesk\', sans-serif; color: #FFFFFF">%s</span></div>' % (ic(icn, 22), '14' if m else '15', t))
    A('</div>')
    A('<a class="lk" href="#services" style="padding-top: 8px">What we do%s</a>' % ARR)
    if not m:
        A('</div>')
    grid = [('ecommerce', 'A business owner packing an online order', '60% 35%'), ('construction', 'A construction crew reviewing plans', 'center 40%'), ('kitchen', 'A chef plating dishes in a restaurant kitchen', '72% 40%'), ('laptop', 'A business owner thinking at a laptop', 'center 40%')]
    A('<div style="position: relative; display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: %dpx">' % (8 if m else 12))
    for i, (k, alt, pos) in enumerate(grid):
        A('<div class="ph" style="height: %dpx; border-radius: 4px"><img src="%s" alt="%s" style="object-position: %s"></div>' % (150 if m else 250, PH[k], alt, pos))
    A('<div aria-hidden="true" class="dots on-dk" style="position: absolute; %s; width: 120px; height: 80px; z-index: -1"></div>' % ('right: -10px; bottom: -24px' if m else 'right: -36px; top: -36px'))
    A('</div>')
    A('</div>\n</section>\n')

    # ---------- 05 Services ----------
    A('<!-- 05 Services, in tier order: Bookkeeping, then QuickBooks Setup & Advisory, then Fractional CFO (limited) -->')
    A('<section id="services" aria-label="Services" class="wh" style="padding: %dpx 0">' % sec)
    A('<div style="%s; display: flex; flex-direction: column; gap: %dpx">' % (wrap, 28 if m else 48))
    intro = 'Almost every client needs bookkeeping and accounting. QuickBooks setup and advice build on that. A part-time finance chief (Fractional CFO) sits at the top, for a small number of clients.'
    if m:
        A('<div style="display: flex; flex-direction: column; gap: 16px">%s<h2 style="font-size: %dpx; line-height: 1.04">Where most clients start, and what comes next.</h2><p class="mu" style="font-size: 15.5px">%s</p></div>' % (eyebrow('03', 'What we do'), h2, intro))
    else:
        A('<div style="display: grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr); gap: 40px; align-items: end"><div style="display: flex; flex-direction: column; gap: 18px">%s<h2 style="font-size: %dpx; line-height: 1.02">Where most clients start, and what comes next.</h2></div><p class="mu" style="font-size: 16.5px">%s</p></div>' % (eyebrow('03', 'What we do'), h2, intro))
    A('<div style="display: grid; grid-template-columns: %s; gap: %dpx">' % ('minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', 14 if m else 20))
    ids = ['bookkeeping', 'setup', 'cfo']
    for k, (icn, name, tag, t, p) in enumerate(TOP):
        dark = k == 0
        bg = 'background: #101419; border-color: #101419;' if dark else ''
        A('<div id="%s" class="card%s" style="%s display: flex; flex-direction: column; gap: 18px; padding: %s; min-height: %s"><span class="ic" style="width: 52px; height: 52px; border-radius: 6px; background: %s; color: %s">%s</span><div style="display: flex; flex-direction: column; gap: 8px"><span class="tag" style="color: %s">%s</span><p style="font: 600 13.5px/1.3 \'Space Grotesk\', sans-serif; color: %s">%s</p><h3 style="font-size: %dpx; line-height: 1.15;%s">%s</h3><p style="font-size: 14.5px; color: %s">%s</p></div></div>' % (
            ids[k], '', bg, '24px 22px' if m else '32px 30px', 'auto' if m else '330px',
            '#2459F5' if dark else '#EEF2FE', '#FFFFFF' if dark else '#2459F5', ic(icn, 26),
            '#8FAEFF' if dark else '#2459F5', tag, '#8FAEFF' if dark else '#2459F5', name, 24 if m else 28, ' color: #FFFFFF;' if dark else '', t, '#B9C0CA' if dark else '#5E6670', p))
    A('</div>')
    A('<div style="display: grid; grid-template-columns: %s; gap: %dpx">' % ('minmax(0, 1fr)' if m else 'repeat(5, minmax(0, 1fr))', 10 if m else 16))
    sid = ['cleanup', 'tax', 'pos', 'reporting', 'training']
    for k, (icn, name, p) in enumerate(SUPPORT):
        A('<div id="%s" style="display: flex; %s gap: 12px; padding: %s; border-top: 2px solid #101419"><span class="ic">%s</span><span style="display: flex; flex-direction: column; gap: 6px"><strong style="font: 600 15.5px/1.3 \'Space Grotesk\', sans-serif; color: #101419">%s</strong><span class="mu" style="font-size: 13.5px; line-height: 1.55">%s</span></span></div>' % (sid[k], 'flex-direction: row; align-items: flex-start;' if m else 'flex-direction: column;', '16px 0 6px' if m else '20px 0 0', ic(icn, 24), name, p))
    A('</div>')
    A('<div id="products" style="display: flex; %s gap: 16px; padding: 20px 24px; border-radius: 6px; background: #F5F6F7"><p style="font-size: 15px; color: #3A424D">We also sell <strong style="color: #101419">QuickBooks products</strong>, because we\'re an Intuit reseller. Call us for prices.</p><a class="lk" href="#services">All services%s</a></div>' % ('flex-direction: column; align-items: flex-start;' if m else 'align-items: center; justify-content: space-between;', ARR))
    A('</div>\n</section>\n')

    # ---------- 06 Triggers ----------
    A('<!-- 06 The six moments clients call us -->')
    A('<section aria-label="Does this sound like you?" class="ch" style="padding: %dpx 0">' % sec)
    A('<div style="%s; display: flex; flex-direction: column; gap: %dpx">' % (wrap, 28 if m else 48))
    tp = "If one of these sounds like you, you're in the right place. Most of our clients came to us this way."
    if m:
        A('<div style="display: flex; flex-direction: column; gap: 16px">%s<h2 style="font-size: %dpx; line-height: 1.04">Does this sound like you?</h2><p class="mu" style="font-size: 15.5px">%s</p></div>' % (eyebrow('04', 'When people usually call us'), h2, tp))
    else:
        A('<div style="display: flex; align-items: flex-end; justify-content: space-between; gap: 40px"><div style="display: flex; flex-direction: column; gap: 18px; max-width: 640px">%s<h2 style="font-size: %dpx; line-height: 1.02">Does this sound like you?</h2><p class="mu" style="font-size: 16.5px">%s</p></div>%s</div>' % (eyebrow('04', 'When people usually call us'), h2, tp, sched()))
    A('<div style="display: grid; grid-template-columns: %s; gap: %dpx">' % ('minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', 0 if m else 20))
    for k, (icn, t, p) in enumerate(TRIGGERS):
        if m:
            A('<div style="display: flex; gap: 14px; padding: 18px 0; border-top: 1px solid #DDE1E6;%s"><span class="ic" style="padding-top: 2px">%s</span><span style="display: flex; flex-direction: column; gap: 6px"><h3 style="font-size: 18px; line-height: 1.25">%s</h3><span class="mu" style="font-size: 14px">%s</span></span></div>' % (' border-bottom: 1px solid #DDE1E6;' if k == 5 else '', ic(icn, 24), t, p))
            continue
        A('<div class="card" style="display: flex; flex-direction: column; gap: 14px; padding: %s"><div style="display: flex; align-items: center; justify-content: space-between"><span class="ic">%s</span><span style="font: 600 13px/1 \'Space Grotesk\', sans-serif; color: #A3AAB4">0%d</span></div><h3 style="font-size: %dpx; line-height: 1.25">%s</h3><p class="mu" style="font-size: 14.5px">%s</p></div>' % ('22px' if m else '28px', ic(icn, 28), k + 1, 19 if m else 21, t, p))
    A('</div>')
    if m:
        A(sched(extra=' style="width: 100%"'))
    A('</div>\n</section>\n')

    # ---------- 07 Specialties ----------
    A('<!-- 07 Specialties and industries -->')
    A('<section aria-label="How we work" class="wh" style="padding: %dpx 0">' % sec)
    if m:
        A('<div style="padding: 0 20px; display: flex; flex-direction: column; gap: 22px"><div style="display: flex; flex-direction: column; gap: 16px">%s<h2 style="font-size: %dpx; line-height: 1.04">We like the tricky businesses best.</h2><p class="mu" style="font-size: 15.5px">%s</p></div>' % (eyebrow('05', 'How we work'), h2, SPEC_P))
    else:
        A('<div style="max-width: 1160px; margin: 0 auto; padding: 0 40px; display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 72px; align-items: start"><div style="position: sticky; top: 0; display: flex; flex-direction: column; gap: 22px">%s<h2 style="font-size: %dpx; line-height: 1.02">We like the tricky businesses best.</h2><p class="mu" style="font-size: 16px">%s</p><a class="lk" href="#schedule">Not on the list? Schedule a free consultation%s</a></div>' % (eyebrow('05', 'How we work'), h2, SPEC_P, ARR))
    A('<div style="display: flex; flex-direction: column">')
    for k, (icn, t, p) in enumerate(INDUSTRIES):
        A('<div style="display: flex; align-items: flex-start; gap: %dpx; padding: %s; border-top: 1px solid #E2E5EA;%s"><span class="ic" style="width: %dpx; height: %dpx; border-radius: 6px; background: #EEF2FE">%s</span><span style="display: flex; flex-direction: column; gap: 4px"><h3 style="font-size: %dpx">%s</h3><span class="mu" style="font-size: 14.5px">%s</span></span></div>' % (14 if m else 22, '18px 0' if m else '24px 0', ' border-bottom: 1px solid #E2E5EA;' if k == len(INDUSTRIES) - 1 else '', 44 if m else 52, 44 if m else 52, ic(icn, 22 if m else 26), 18 if m else 20, t, p))
    A('</div>')
    if m:
        A('<a class="lk" href="#schedule">Not on the list? Schedule a free consultation%s</a>' % ARR)
    A('</div>\n</section>\n')

    # ---------- 08 Proof ----------
    A('<!-- 08 Certified by Intuit, on the Electric Blue band -->')
    A('<section aria-label="Certified by Intuit" class="bl" style="position: relative; overflow: hidden; padding: %dpx 0">' % sec)
    A('<div aria-hidden="true" class="dots on-dk" style="position: absolute; %s; width: 220px; height: 140px"></div>' % ('right: 0; top: 24px' if m else 'left: 40px; bottom: 40px'))
    A('<div style="position: relative; %s; display: %s; gap: %dpx; align-items: center">' % (wrap if m else 'max-width: 1160px; margin: 0 auto; padding: 0 40px', 'flex; flex-direction: column' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 6fr)', 32 if m else 72))
    A('<div style="display: flex; flex-direction: column; gap: 20px">%s<h2 style="font-size: %dpx; line-height: 1.02">Proof you can look up yourself.</h2><p style="font-size: %spx">Intuit, the company that makes QuickBooks, has tested and certified our team on QuickBooks Online, Desktop and Enterprise. You can see our certificates and client reviews on Intuit\'s website.</p><p style="font: 600 15px/1.4 \'Space Grotesk\', sans-serif; color: #FFFFFF">Certified at Intuit\'s Elite and Level 2 Advanced levels.</p><a class="btn btn-w" href="%s" target="_blank" rel="noopener" style="align-self: flex-start">See certifications and reviews%s</a></div>' % (eyebrow('06', 'Certified by Intuit'), h2, '15.5' if m else '16.5', PROADVISOR, ARR))
    A('<div style="background: #FFFFFF; border-radius: 6px; padding: %s; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: %s; align-items: center; justify-items: center; width: 100%%">' % ('18px' if m else '32px', '12px 8px' if m else '22px 18px'))
    for b, alt in BADGES:
        A('<img src="/_blob/%s" alt="%s" style="width: 100%%; max-width: %dpx; height: auto; display: block">' % (b, alt, 70 if m else 116))
    A('<div style="width: 100%%; aspect-ratio: 1; max-width: %dpx; border-radius: 4px; background: #101419; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 6px; gap: 2px"><strong style="font: 600 %dpx/1 \'Space Grotesk\', sans-serif; color: #FFFFFF">~50</strong><span style="font-size: %spx; line-height: 1.3; color: #B9C0CA">client reviews on our ProAdvisor profile</span></div>' % (70 if m else 116, 18 if m else 30, '8' if m else '11'))
    A('</div>')
    A('</div>\n</section>\n')

    # ---------- 09 Testimonials ----------
    A('<!-- 09 What clients say: loyalty stats and the testimonials, word for word -->')
    A('<section aria-label="What clients say" class="dk" style="padding: %dpx 0">' % sec)
    A('<div style="%s; display: flex; flex-direction: column; gap: %dpx">' % (wrap, 28 if m else 48))
    if m:
        A('<div style="display: flex; flex-direction: column; gap: 16px">%s<h2 style="font-size: %dpx; line-height: 1.04">Clients stay for years.</h2><p style="font-size: 15.5px">Several clients have been with us for 10+ years.</p></div>' % (eyebrow('07', 'What clients say'), h2))
    else:
        A('<div style="display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); gap: 40px; align-items: end"><div style="display: flex; flex-direction: column; gap: 18px">%s<h2 style="font-size: %dpx; line-height: 1.02">Clients stay for years.</h2><p style="font-size: 16.5px">Several clients have been with us for 10+ years.</p></div>' % (eyebrow('07', 'What clients say'), h2))
    A('<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: %dpx">' % (8 if m else 20))
    for v, l in STATS:
        A('<div style="display: flex; flex-direction: column; gap: 8px; padding-top: %dpx; border-top: 2px solid #2459F5"><strong style="font: 600 %dpx/1 \'Space Grotesk\', sans-serif; letter-spacing: -.03em; color: #FFFFFF">%s</strong><span style="font-size: %spx; line-height: 1.4; color: #9AA3AE">%s</span></div>' % (12 if m else 16, 34 if m else 56, v, '12' if m else '14', l))
    A('</div>')
    if not m:
        A('</div>')
    A('<div style="display: grid; grid-template-columns: %s; gap: %dpx">' % ('minmax(0, 1fr)' if m else 'repeat(6, minmax(0, 1fr))', 12 if m else 20))
    spans = [3, 3, 2, 2, 2]
    for k, (q, n, c) in enumerate(QUOTES):
        big = k < 2
        A('<figure style="margin: 0; %s display: flex; flex-direction: column; justify-content: space-between; gap: 22px; padding: %s; border-radius: 6px; background: %s">' % ('' if m else 'grid-column: span %d;' % spans[k], '24px 22px' if m else ('34px 32px' if big else '28px'), '#2459F5' if k == 0 else '#1B2029'))
        A('<div style="display: flex; flex-direction: column; gap: 16px">%s<blockquote style="margin: 0; font: 500 %dpx/1.35 \'Space Grotesk\', sans-serif; letter-spacing: -.01em; color: #FFFFFF">"%s"</blockquote></div>' % (QUOTE.replace('#2459F5', '#FFFFFF') if k == 0 else QUOTE, (20 if m else (26 if big else 20)), q))
        A('<figcaption style="display: flex; flex-direction: column; gap: 2px; padding-top: 14px; border-top: 1px solid rgba(255,255,255,.16)"><strong style="font: 600 14.5px/1.3 \'Space Grotesk\', sans-serif; color: #FFFFFF">%s</strong><span style="font-size: 13px; color: %s">%s</span></figcaption>' % (n, '#DCE5FF' if k == 0 else '#9AA3AE', c))
        A('</figure>')
    A('</div>')
    A('<a class="lk" href="%s" target="_blank" rel="noopener">See client reviews%s</a>' % (PROADVISOR, ARR))
    A('</div>\n</section>\n')

    # ---------- 10 Team ----------
    A('<!-- 10 The team -->')
    A('<section aria-label="The team" class="wh" style="padding: %dpx 0">' % sec)
    A('<div style="%s; display: %s; gap: %dpx; align-items: stretch">' % (wrap if m else 'max-width: 1160px; margin: 0 auto; padding: 0 40px', 'flex; flex-direction: column' if m else 'grid; grid-template-columns: minmax(0, 6fr) minmax(0, 5fr)', 28 if m else 64))
    A('<div class="ph" style="position: relative; border-radius: 6px; min-height: %dpx"><img src="%s" alt="Specialists reviewing a client\'s numbers together" style="position: absolute; inset: 0; object-position: 55%% 34%%"><span aria-hidden="true" class="wedge" style="position: absolute; left: 0; bottom: 0; width: %dpx; height: %dpx; background: #2459F5; z-index: 1"></span></div>' % (260 if m else 520, PH['team'], 150 if m else 240, 52 if m else 84))
    A('<div style="display: flex; flex-direction: column; justify-content: center; gap: 22px">%s<h2 style="font-size: %dpx; line-height: 1.02">A whole team, not just one bookkeeper.</h2><p class="mu" style="font-size: %spx">%s</p>' % (eyebrow('08', 'The team'), h2, '15.5' if m else '16', TEAM_P))
    A('<div style="display: flex; flex-direction: column">')
    for k, (n, r) in enumerate(TEAM):
        A('<div style="display: flex; flex-direction: column; gap: 3px; padding: 14px 0; border-top: 1px solid #E2E5EA;%s"><strong style="font: 600 16px/1.3 \'Space Grotesk\', sans-serif; color: #101419">%s</strong><span class="mu" style="font-size: 13.5px">%s</span></div>' % (' border-bottom: 1px solid #E2E5EA;' if k == 2 else '', n, r))
    A('</div>')
    A('<a class="btn btn-o" href="#about" style="align-self: flex-start">Meet the team%s</a>' % ARR)
    A('</div>\n</div>\n</section>\n')

    # ---------- 11 FAQ ----------
    A('<!-- 11 Questions before the first call -->')
    A('<section aria-label="Before you call" class="ch" style="padding: %dpx 0">' % sec)
    A('<div style="%s; display: %s; gap: %dpx">' % (wrap if m else 'max-width: 1160px; margin: 0 auto; padding: 0 40px', 'flex; flex-direction: column' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr); align-items: start', 24 if m else 72))
    A('<div style="display: flex; flex-direction: column; gap: 18px">%s<h2 style="font-size: %dpx; line-height: 1.04">Questions people ask before the first call.</h2></div>' % (eyebrow('09', 'Before you call'), h2))
    A('<div style="display: flex; flex-direction: column; border-bottom: 1px solid #DDE1E6">')
    for k, (q, a) in enumerate(FAQ):
        A('<div><button type="button" class="faq" aria-expanded="%s"%s>%s%s</button>%s</div>' % ('true' if a else 'false', ' style="font-size: 16px"' if m else '', q, PLUS, '<p class="mu" style="font-size: 15px; padding: 0 40px 22px 0">%s</p>' % a if a else ''))
    A('</div>')
    A('</div>\n</section>\n')

    # ---------- 12 Blog ----------
    A('<!-- 12 From the blog -->')
    A('<section id="blog" aria-label="From the blog" class="wh" style="padding: %dpx 0">' % sec)
    A('<div style="%s; display: flex; flex-direction: column; gap: %dpx">' % (wrap, 28 if m else 44))
    A('<div style="display: flex; %s gap: 20px"><div style="display: flex; flex-direction: column; gap: 16px">%s<h2 style="font-size: %dpx; line-height: 1.04">Simple answers to the questions we hear most.</h2><p class="mu" style="font-size: 15px">300+ articles on QuickBooks, bookkeeping, accounting and financial planning.</p></div><a class="btn btn-o" href="#blog" style="flex: none">Read all articles%s</a></div>' % ('flex-direction: column; align-items: flex-start;' if m else 'align-items: flex-end; justify-content: space-between;', eyebrow('10', 'From the blog'), h2, ARR))
    A('<div style="display: grid; grid-template-columns: %s; gap: %dpx">' % ('minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', 24 if m else 24))
    for tag, t, p, ph, pos in BLOG:
        if m:
            A('<article style="display: grid; grid-template-columns: 112px minmax(0, 1fr); gap: 14px; align-items: start"><div class="ph" style="height: 112px; border-radius: 6px"><img src="%s" alt="" style="object-position: %s"></div><div style="display: flex; flex-direction: column; gap: 6px"><span class="tag">%s</span><h3 style="font-size: 16.5px; line-height: 1.25">%s</h3><p class="mu" style="font-size: 13.5px; line-height: 1.5">%s</p></div></article>' % (PH[ph], pos, tag, t, p))
            continue
        A('<article style="display: flex; flex-direction: column; gap: 12px"><div class="ph" style="height: %dpx; border-radius: 6px"><img src="%s" alt="" style="object-position: %s"></div><span class="tag" style="padding-top: 6px">%s</span><h3 style="font-size: %dpx; line-height: 1.25">%s</h3><p class="mu" style="font-size: 14.5px">%s</p></article>' % (150 if m else 230, PH[ph], pos, tag, 19 if m else 20, t, p))
    A('</div>')
    A('</div>\n</section>\n')

    # ---------- 13 CTA + footer ----------
    A('<!-- 13 Footer, with the call to action and the style board\'s graphic elements -->')
    A('<footer id="contact" class="dk foot" style="position: relative; overflow: hidden">')
    A('<div id="schedule" style="position: relative; %s; padding-top: %dpx; padding-bottom: %dpx; display: %s; gap: %dpx; align-items: center">' % (wrap if m else 'max-width: 1160px; margin: 0 auto; padding-left: 40px; padding-right: 40px', 72 if m else 120, 64 if m else 104, 'flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr)', 32 if m else 64))
    A('<div style="display: flex; flex-direction: column; gap: 22px">%s<h2 style="font-size: %dpx; line-height: .98; letter-spacing: -.035em">Your books.<br>In order.</h2><p style="font-size: %spx; max-width: 520px">Book a free call with Bernard or Rob. Come as you are, mess and all. We\'ll tell you what we\'d fix first and what it would take.</p><div style="display: flex; %s gap: 12px; padding-top: 4px">%s<a class="btn btn-o" href="tel:+12032279475">Call (203) 227-9475</a></div></div>' % (eyebrow('11', 'Your next step'), 48 if m else 84, '15.5' if m else '17', 'flex-direction: column;' if m else 'align-items: center;', sched(extra=' style="width: 100%"' if m else '')))
    A('<div aria-hidden="true" style="position: relative; width: 100%%; height: %dpx">' % (130 if m else 300))
    A('<div style="position: absolute; left: 0; top: 0; width: 62%; height: 62%; background: #2459F5; clip-path: polygon(0 0, 100% 0, 58% 100%, 0 100%)"></div>')
    A('<div style="position: absolute; right: 0; bottom: 0; width: 70%; height: 46%; background: #1B2029; clip-path: polygon(22% 0, 100% 0, 100% 100%, 0 100%)"></div>')
    A('<div class="dots on-dk" style="position: absolute; right: 0; top: 0; width: 34%; height: 40%"></div>')
    if not m:
        A('<p style="position: absolute; left: 0; bottom: 0; margin: 0; font: 600 12px/1.5 \'Space Grotesk\', sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #9AA3AE">Simple structure<br>for a more<br>confident business.</p>')
    A('</div>')
    A('</div>')
    A('<div style="border-top: 1px solid rgba(255,255,255,.1)">')
    A('<div style="%s; padding-top: %dpx; padding-bottom: 32px; display: flex; flex-direction: column; gap: %dpx">' % (wrap if m else 'max-width: 1160px; margin: 0 auto; padding-left: 40px; padding-right: 40px', 48 if m else 64, 36 if m else 56))
    A('<div style="display: grid; grid-template-columns: %s; gap: %s">' % ('repeat(2, minmax(0, 1fr))' if m else 'minmax(0, 2fr) repeat(3, minmax(0, 1fr))', '32px 20px' if m else '36px 40px'))
    A('<div style="display: flex; flex-direction: column; gap: 16px; min-width: 0;%s">' % (' grid-column: span 2;' if m else ''))
    A('<img src="%s" alt="MISSION" style="height: 26px; width: auto; align-self: flex-start">' % LOGO)
    A('<p style="font-size: 14px; max-width: 360px">Business advisors who know accounting software really well. Bookkeeping, accounting and QuickBooks for grown-up businesses with tricky books.</p>')
    A('<address style="font-style: normal; font-size: 14px; line-height: 1.75">Nationwide, fully remote<br><a href="mailto:info@missionaccountinghelp.com" style="color: #FFFFFF">info@missionaccountinghelp.com</a><br><a href="tel:+12032279475" style="color: #FFFFFF">(203) 227-9475</a></address>')
    A('<div style="display: flex; flex-wrap: wrap; gap: 8px 18px"><a href="https://www.facebook.com/MissionAccounting/" target="_blank" rel="noopener">Facebook</a><a href="https://www.linkedin.com/company/mission-quickbooks/" target="_blank" rel="noopener">MISSION on LinkedIn</a><a href="https://www.linkedin.com/in/bernard-roesch/" target="_blank" rel="noopener">Bernard on LinkedIn</a></div>')
    A('<form style="display: flex; flex-direction: column; gap: 8px; max-width: 400px; padding-top: 6px"><p style="margin: 0; font: 600 15px/1.3 \'Space Grotesk\', sans-serif; color: #FFFFFF">QuickBooks tips by email</p><p style="font-size: 13.5px">Simple answers to the questions business owners ask us most. No sales emails.</p><label for="nl-email-h%s" class="sr">Email address</label><div style="display: flex; gap: 8px; padding-top: 4px"><input id="nl-email-h%s" type="email" placeholder="Your email address"><button class="btn btn-w tg-btn" type="submit" style="height: 48px; padding: 0 18px; font-size: 14px; border: 0">Subscribe</button></div></form>' % ('m' if m else '', 'm' if m else ''))
    A('</div>')
    for title, links in [('Services', FOOT_SERVICES), ('Company', FOOT_CO), ('Legal', FOOT_LEGAL)]:
        A('<nav aria-label="%s" style="display: flex; flex-direction: column; gap: 10px"><p class="fh">%s</p>%s</nav>' % (title, title, ''.join('<a href="%s"%s>%s</a>' % (u, ' target="_blank" rel="noopener"' if u.startswith('http') else '', t) for u, t in links)))
    A('</div>')
    A('<div style="display: flex; flex-wrap: wrap; justify-content: space-between; gap: 10px; padding-top: 22px; border-top: 1px solid rgba(255,255,255,.1); font-size: 12.5px; color: #7D8692"><span>© 2026 MISSION. All rights reserved.</span><span>Intuit, QuickBooks and ProAdvisor are trademarks of Intuit Inc.</span></div>')
    A('</div>\n</div>')
    A('</footer>\n')
    A('</div>')
    return '\n'.join(o)


SCRIPT = """class Component extends DCLogic {
  setBtn(v) {
    // the review toggle; boards of the same lane stay in step through a broadcast channel
    this.setState({ btn: v });
    try { if (this.btnChannel) this.btnChannel.postMessage({ btn: v }); } catch (e) {}
  }
  setHero(v) {
    // the hero background toggle (kitchen, office or ecommerce photo), shared with the other Lane H board
    this.setState({ hero: v });
    try { if (this.btnChannel) this.btnChannel.postMessage({ hero: v }); } catch (e) {}
  }
  listenBtn() {
    try {
      this.btnChannel = new BroadcastChannel('mission-buttons-lane-h');
      this.btnChannel.onmessage = (e) => {
        if (e.data && e.data.btn) this.setState({ btn: e.data.btn });
        if (e.data && e.data.hero) this.setState({ hero: e.data.hero });
      };
    } catch (e) {}
  }
  renderVals() {
    return {
      btnMode: (this.state && this.state.btn) || 'green',
      isBlue: ((this.state && this.state.btn) || 'green') === 'blue' ? 'true' : 'false',
      isGreen: ((this.state && this.state.btn) || 'green') === 'green' ? 'true' : 'false',
      setBlue: this.setBlue || (this.setBlue = () => this.setBtn('blue')),
      setGreen: this.setGreen || (this.setGreen = () => this.setBtn('green')),
      heroMode: (this.state && this.state.hero) || 'kitchen',
      isKitchen: ((this.state && this.state.hero) || 'kitchen') === 'kitchen' ? 'true' : 'false',
      isOffice: ((this.state && this.state.hero) || 'kitchen') === 'office' ? 'true' : 'false',
      isEcommerce: ((this.state && this.state.hero) || 'kitchen') === 'ecommerce' ? 'true' : 'false',
      setKitchen: this.setKitchen || (this.setKitchen = () => this.setHero('kitchen')),
      setOffice: this.setOffice || (this.setOffice = () => this.setHero('office')),
      setEcommerce: this.setEcommerce || (this.setEcommerce = () => this.setHero('ecommerce')),
    };
  }
  componentDidMount() {
    this.listenBtn();
  }
  componentWillUnmount() {
    try { if (this.btnChannel) this.btnChannel.close(); } catch (e) {}
  }
}"""


def doc(m):
    w = 390 if m else 1440
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>Lane H homepage, %s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n%s\n<style>%s</style>\n</helmet>\n%s\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":8000}}\'>\n%s\n</script>\n</body>\n</html>\n') % ('mobile' if m else 'desktop', FONTS, CSS, page(m), w, SCRIPT)


open(OUT + '/lane-h-home.dc.html', 'w').write(doc(False))
open(OUT + '/lane-h-home-mobile.dc.html', 'w').write(doc(True))
print('ok')
