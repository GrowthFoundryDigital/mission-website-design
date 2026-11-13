# Lane K generator (13 Nov 2026, by request): a new lane built from the reference design Growth Foundry supplied
# (assets/photos/lane-k/k-reference-design.webp) and the background images that go with it (assets/photos/lane-k/).
# Layout and look follow the reference: dark navy and light blue-white sections, slanted condensed headlines, bright blue
# accents, lime buttons, photo and texture backgrounds. Content follows MISSION's real facts (Business DNA, the 8 Nov meeting,
# Lane J's copy), by request, where the reference text was not sourced: 5.0 from 32 Google reviews, a verbatim testimonial, the
# real case studies and FAQ; team headshots are labelled placeholders until MISSION supplies photos.
# Usage: python3 tools/lane-k-gen.py <out dir>   -> lane-k-home.dc.html (1440) and lane-k-home-mobile.dc.html (390)
import os, sys

OUT = sys.argv[1]

# Image slots. STAND-IN marks a slot waiting for its image from the reference set (re-send pending): swap the id when it arrives.
B = '/_blob/'
IMG = {
    'hero':     B + 'c7b34dc9f98b5531b52c5bc1cb27ff06',   # STAND-IN for the climber on the overhang: hiker on the summit
    'services': B + 'c83f8b0698ce7879ae30780c584bcc65',   # STAND-IN for the hiker on the summit (used by the hero for now): sky
    'mission':  B + 'fffa2c71ba1ad1c02f0d03a0cc647d85',   # team around a laptop (library photo)
    'cases':    B + 'a0baf662031ad30aadb27f1de3969ea1',   # contour lines
    'quote':    B + 'a0baf662031ad30aadb27f1de3969ea1',   # STAND-IN for the blurred office with diagonal bands: contour lines
    'team':     None,                                     # STAND-IN slot for the glass towers (plain light background for now)
    'partner':  B + '9e1790fb97143f88b3da5af39894de49',   # globe network (stands in for the target rings too)
    'trusted':  B + 'c83f8b0698ce7879ae30780c584bcc65',   # sky with sunburst
    'cta':      B + 'c7b34dc9f98b5531b52c5bc1cb27ff06',   # STAND-IN for the mountain range: hiker on the summit
    'footer':   B + 'a0baf662031ad30aadb27f1de3969ea1',   # contour lines
    'logo':     B + 'b29865f8838e8d694583c88108f0c2aa',   # MISSION logo, blue
    'elite':    B + '5a6f8298d29fe5b417692e04bb5cefb5',   # QuickBooks ProAdvisor Elite badge
    'cs_construction': B + 'b0f169f77a9c9c69b7b62fef8e9ec86b',
    'cs_jewelry':      B + '2a1cf94d53635b523c60effebc3a5529',
    'cs_interiors':    B + '959f667ae9fbf3a0eb90cf0ce15668ff',
}

NAVY, NAVY2, BLUE, LIME, INK, MUTED, ICE = '#061428', '#0A2240', '#1FA2FF', '#C1F432', '#0A1B2E', '#4A5A70', '#EDF3F9'

def ic(name, size=22, stroke='currentColor', sw=1.8):
    P = {
        'target': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/><path d="M12 1v4M12 19v4M1 12h4M19 12h4"/>',
        'users': '<path d="M16 20v-1.5a3.5 3.5 0 0 0-3.5-3.5h-5A3.5 3.5 0 0 0 4 18.5V20"/><circle cx="10" cy="8" r="3.5"/><path d="M20 20v-1.5a3.5 3.5 0 0 0-2.5-3.35M15.5 4.65a3.5 3.5 0 0 1 0 6.7"/>',
        'bars': '<path d="M4 20V14M9 20V10M14 20V6M19 20V3"/>',
        'refresh': '<path d="M20 11a8 8 0 0 0-14.5-4.5L4 8"/><path d="M4 3v5h5"/><path d="M4 13a8 8 0 0 0 14.5 4.5L20 16"/><path d="M20 21v-5h-5"/>',
        'star': '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
        'calc': '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 11h2M12 11h2M16 11v6M8 15h2M12 15h2"/>',
        'laptop': '<rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/>',
        'chart': '<path d="M4 20h16"/><path d="M6 16v-4M10 16V9M14 16v-6M18 16V5"/>',
        'layers': '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
        'building': '<path d="M4 21V5l7-2v18M11 9h8v12M7 8h1M7 12h1M7 16h1M14 13h2M14 17h2"/><path d="M2 21h20"/>',
        'growth': '<path d="M3 17l6-6 4 4 8-8"/><path d="M15 7h6v6"/>',
        'shield': '<path d="M12 3l8 3v6c0 4.5-3.4 8.4-8 9-4.6-.6-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
        'compass': '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
        'process': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v3M21 12h-3M12 21v-3M3 12h3"/>',
        'team': '<circle cx="8" cy="8" r="3"/><circle cx="16" cy="8" r="3"/><path d="M2.5 19a5.5 5.5 0 0 1 11 0M10.5 19a5.5 5.5 0 0 1 11 0"/>',
        'arrow': '<path d="M5 12h14M13 6l6 6-6 6"/>',
        'cal': '<rect x="3" y="4.5" width="18" height="16.5" rx="2"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/>',
        'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
        'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
        'plus': '<path d="M12 5v14M5 12h14"/>',
        'minus': '<path d="M5 12h14"/>',
        'chev': '<path d="M6 9l6 6 6-6"/>',
        'quote': '<path d="M7 7h4v4c0 3-1.5 5-4 6M15 7h4v4c0 3-1.5 5-4 6"/>',
        'person': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
        'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    }
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">%s</svg>' % (size, size, stroke, sw, P[name]))

CSS = '''
.lk{font-family:'Inter','Helvetica Neue',Arial,sans-serif;color:#C9D6E8;-webkit-font-smoothing:antialiased;font-size:16px;line-height:1.6}
.lk *{box-sizing:border-box}
.lk a{color:inherit}
.lk h1,.lk h2,.lk h3,.lk .cond{margin:0;font-family:'Barlow Condensed','Arial Narrow',sans-serif;font-style:italic;font-weight:800;text-transform:uppercase;letter-spacing:-.005em;line-height:.94}
.lk p{margin:0}
.lk .eb{display:flex;align-items:center;gap:14px;font:700 12px/1.3 'Inter',sans-serif;letter-spacing:.2em;text-transform:uppercase;color:%(BLUE)s}
.lk .eb::after{content:'';width:44px;height:2px;background:currentColor;opacity:.8}
.lk .eb.c::after{display:none}
.lk .dk{color:#C9D6E8}
.lk .dk h1,.lk .dk h2,.lk .dk h3{color:#FFFFFF}
.lk .lt{color:%(MUTED)s}
.lk .lt h2,.lk .lt h3{color:%(INK)s}
.lk .blue{color:%(BLUE)s !important}
/* buttons: lime, crisp corners; outlined buttons fill with lime on hover (as on Lane J) */
.lk .btn{display:inline-flex;align-items:center;justify-content:center;gap:10px;height:50px;padding:0 24px;border-radius:4px;border:1px solid %(LIME)s;background:%(LIME)s;color:%(NAVY)s;font:700 15px/1 'Inter',sans-serif;text-decoration:none;white-space:nowrap;cursor:pointer;transition:transform .4s cubic-bezier(.22,.61,.36,1),background-color .4s ease,color .4s ease,border-color .4s ease,box-shadow .4s ease}
.lk .btn:hover,.lk .btn:focus-visible{transform:translateY(-2px);box-shadow:0 10px 24px rgba(193,244,50,.28)}
.lk .btn .ar{transition:transform .4s cubic-bezier(.22,.61,.36,1)}
.lk .btn:hover .ar{transform:translateX(3px)}
.lk .btn-o{background:transparent;color:#FFFFFF;border-color:rgba(255,255,255,.55)}
.lk .btn-o:hover,.lk .btn-o:focus-visible{background:%(LIME)s;color:%(NAVY)s;border-color:%(LIME)s}
/* text links: the lime square wipe, left to right, the words inking dark as it reaches them */
.lk .lw{position:relative;isolation:isolate;display:inline-flex;align-items:center;gap:8px;text-decoration:none;font-weight:600;cursor:pointer}
.lk .lw::before{content:'';position:absolute;top:-5px;bottom:-5px;left:-8px;right:-8px;z-index:-1;background:%(LIME)s;transform:scaleX(0);transform-origin:left center;transition:transform .45s cubic-bezier(.22,.61,.36,1)}
.lk .lw:hover::before,.lk .lw:focus-visible::before{transform:scaleX(1)}
.lk .lw{transition:color .2s ease .15s}
.lk .lw:hover,.lk .lw:focus-visible{color:#101419 !important}
/* cards */
.lk .card{background:#FFFFFF;border-radius:6px;box-shadow:0 18px 40px rgba(4,16,34,.22);transition:transform .3s ease,box-shadow .3s ease;cursor:pointer;text-decoration:none;color:%(MUTED)s}
.lk .card:hover{transform:translateY(-5px);box-shadow:0 26px 54px rgba(4,16,34,.3)}
.lk .card h3{color:%(INK)s}
.lk .card .go{color:%(INK)s;transition:transform .3s ease,color .3s ease}
.lk .card:hover .go{transform:translateX(4px);color:%(BLUE)s}
.lk .card img{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
.lk .card:hover img{transform:scale(1.05)}
.lk .nav a{color:#FFFFFF;text-decoration:none;font:500 14px/1 'Inter',sans-serif;display:inline-flex;align-items:center;gap:4px;transition:color .2s ease}
.lk .nav a:hover{color:%(LIME)s}
.lk .foot a:not(.btn){color:#AEBCCD;text-decoration:none;transition:color .2s ease}
.lk .foot a:not(.btn):hover{color:%(LIME)s}
.lk .faq{display:flex;align-items:center;gap:14px;padding:16px 4px;border-top:1px solid #D9E2EC;font-weight:600;color:%(INK)s;cursor:pointer}
.lk .faq svg{color:%(BLUE)s;flex:none;transition:transform .25s ease}
.lk .faq:hover svg{transform:rotate(90deg)}
.lk .ph{position:relative;overflow:hidden}
.lk .ph > img{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover}
.lk .slash{position:absolute;background:%(BLUE)s;transform:skewX(-18deg)}
.lk .cursor{cursor:pointer}
@media (prefers-reduced-motion: reduce){.lk *{transition:none !important}}
''' % dict(BLUE=BLUE, LIME=LIME, NAVY=NAVY, INK=INK, MUTED=MUTED)

def build(m):
    W = 390 if m else 1440
    pad = '0 20px' if m else '0 40px'
    wrap = lambda inner, extra='': ('<div style="position: relative; z-index: 2; %smargin: 0 auto; padding: %s%s">%s</div>'
                                    % ('' if m else 'max-width: 1280px; ', pad, extra, inner))
    cal, arr = ic('cal', 17), '<span class="ar" style="display: inline-flex">%s</span>' % ic('arrow', 16)
    btn = lambda label, href='#schedule', icon=True, extra='': ('<a class="btn" href="%s"%s>%s%s%s</a>' % (href, (' style="%s"' % extra) if extra else '', cal if icon else '', label, '' if icon else arr))
    A = []
    a = A.append

    # ---------- 01 Hero ----------
    hero_h = 820 if m else 760
    a('<!-- 01 Hero: the photo behind, the headline on the left, the five facts along the bottom -->')
    a('<section class="dk" aria-label="Hero" style="position: relative; overflow: hidden; background: %s">' % NAVY)
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0"><img src="%s" alt="" style="object-position: %s"></div>' % (IMG['hero'], '70% 30%' if m else 'center 35%'))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: %s"></div>' % (
        'linear-gradient(180deg, rgba(6,20,40,.82) 0%, rgba(6,20,40,.70) 55%, rgba(6,20,40,.95) 100%)' if m else
        'linear-gradient(90deg, rgba(6,20,40,.96) 0%, rgba(6,20,40,.82) 38%, rgba(6,20,40,.25) 70%, rgba(6,20,40,.1) 100%), linear-gradient(0deg, rgba(6,20,40,.9) 0%, rgba(6,20,40,0) 30%)'))
    # header
    if m:
        hdr = ('<header style="display: flex; align-items: center; justify-content: space-between; height: 72px">'
               '<a href="#top" aria-label="MISSION home" style="display: flex"><img src="%s" alt="MISSION" style="height: 22px; width: auto; display: block"></a>'
               '<div style="display: flex; gap: 8px"><a class="btn" href="#schedule" style="height: 40px; padding: 0 14px; font-size: 13.5px">%sSchedule</a>'
               '<button type="button" aria-label="Open menu" class="cursor" style="all: unset; cursor: pointer; width: 40px; height: 40px; display: inline-flex; align-items: center; justify-content: center; border: 1px solid rgba(255,255,255,.5); border-radius: 4px; color: #FFFFFF">'
               '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button></div></header>'
               % (IMG['logo'], ic('cal', 15)))
    else:
        chev = ic('chev', 13, sw=2.2)
        nav = ''.join('<a href="%s">%s%s</a>' % (h, t, chev if c else '') for t, h, c in [('Services', '#services', 1), ('Who we serve', '#who', 1), ('Case studies', '#case-studies', 0), ('About', '#team', 1), ('Resources', '#faq', 1)])
        hdr = ('<header style="display: flex; align-items: center; justify-content: space-between; height: 92px; gap: 24px">'
               '<a href="#top" aria-label="MISSION home" style="display: flex"><img src="%s" alt="MISSION" style="height: 30px; width: auto; display: block"></a>'
               '<nav class="nav" aria-label="Main" style="display: flex; gap: 30px; white-space: nowrap">%s</nav>'
               '<div style="display: flex; gap: 12px"><a class="btn btn-o" href="tel:+12032279475" style="height: 44px; padding: 0 18px; font-size: 14px">%s(203) 227-9475</a>'
               '<a class="btn" href="#schedule" style="height: 44px; padding: 0 18px; font-size: 14px">%sSchedule a free consultation</a></div></header>'
               % (IMG['logo'], nav, ic('phone', 15), ic('cal', 15)))
    hero = (hdr +
        '<div id="top" style="display: flex; flex-direction: column; gap: %s; max-width: %s; padding: %s">' % ('20px' if m else '24px', '100%' if m else '720px', '44px 0 0' if m else '96px 0 0') +
        '<p class="eb c" style="color: #FFFFFF; letter-spacing: %s; font-size: %s">Bookkeeping / Accounting / QuickBooks / Fractional CFO</p>' % ('.12em' if m else '.2em', '10.5px' if m else '12px') +
        '<h1 style="font-size: %s; color: #FFFFFF">Complex books.<br><span class="blue">Clear answers.</span></h1>' % ('62px' if m else '112px') +
        '<p style="font-size: %s; line-height: 1.6; color: #DCE6F2; max-width: 560px">We fix messy books, keep them right every month, and show you your numbers in plain words. You get to focus on running your business.</p>' % ('16px' if m else '18px') +
        '<div style="display: flex; %s gap: 12px; padding-top: 6px">%s<a class="btn btn-o" href="#case-studies"%s>Read client stories%s</a></div>' % (
            'flex-direction: column;' if m else 'flex-wrap: wrap;', btn('Schedule a free consultation', extra='width: 100%' if m else ''), ' style="width: 100%"' if m else '', arr) +
        '</div>')
    stats = [('target', '25+', 'Years in business'), ('users', '850', 'Clients served'), ('bars', '100–140', 'Clients a year'), ('refresh', '50', 'Recurring clients'), ('star', '80%', 'Come by referral')]
    cells = ''.join(
        '<div style="display: flex; align-items: center; gap: 14px; padding: %s; %s"><span style="color: %s; flex: none">%s</span>'
        '<span style="display: flex; flex-direction: column; gap: 2px"><span class="cond" style="font-size: %s; color: #FFFFFF">%s</span><span style="font-size: %s; color: #AFC0D4">%s</span></span></div>'
        % ('14px 0' if m else '26px 0', ('border-top: 1px solid rgba(255,255,255,.12)' if m and i else '') if m else ('border-left: 1px solid rgba(255,255,255,.14); padding-left: 28px' if i else ''),
           BLUE, ic(n, 30 if not m else 26, sw=1.6), '28px' if m else '34px', v, '13px' if m else '13.5px', l)
        for i, (n, v, l) in enumerate(stats))
    statbar = ('<div style="margin-top: %s; border-top: 1px solid rgba(255,255,255,.16); display: %s">%s</div>'
               % ('48px' if m else '92px', 'flex; flex-direction: column' if m else 'grid; grid-template-columns: repeat(5, minmax(0, 1fr))', cells))
    a(wrap(hero + statbar, '; padding-bottom: %s' % ('8px' if m else '0')))
    a('</section>')

    # ---------- 02 The mission (who we are) ----------
    a('\n<!-- 02 The mission: a specialist team, with the team photo in a slanted frame -->')
    a('<section id="who-we-are" class="lt" aria-label="The mission" style="position: relative; overflow: hidden; background: linear-gradient(180deg, #F4F8FC 0%%, %s 100%%); padding: %s">' % (ICE, '64px 0' if m else '110px 0'))
    txt = ('<div style="display: flex; flex-direction: column; gap: 22px">'
           '<p class="eb">The mission</p><h2 style="font-size: %s">A specialist team that knows your business.</h2>'
           '<p style="font-size: 17px; max-width: 470px">You started a business, not a bookkeeping job. We keep your books clean and correct. You don\'t have to hire a full finance team or get lost at a big firm.</p>'
           '<div style="padding-top: 6px">%s</div></div>' % ('46px' if m else '72px', btn("Let's talk about your needs", icon=False, extra='width: 100%' if m else '')))
    photo = ('<div style="position: relative; height: %s">'
             '<div class="ph" style="position: absolute; inset: 0; clip-path: polygon(%s)"><img src="%s" alt="Specialists reviewing a client\'s numbers together" style="object-position: center 30%%"></div>'
             '<div class="slash" aria-hidden="true" style="left: %s; top: 0; bottom: 0; width: %s"></div></div>'
             % ('300px' if m else '470px', '10% 0, 100% 0, 100% 100%, 0 100%' if m else '16% 0, 100% 0, 100% 100%, 0 100%', IMG['mission'], '0' if m else '2%', '10px' if m else '16px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s%s</div>' % ('flex; flex-direction: column' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr)', '36px' if m else '56px', txt, photo)))
    a('</section>')

    # ---------- 03 Services ----------
    a('\n<!-- 03 Services: four cards on navy, the photo fading in from the right -->')
    a('<section id="services" class="dk" aria-label="Services" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '64px 0' if m else '100px 0 110px'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; %s"><img src="%s" alt="" style="object-position: center 40%%"></div>' % ('inset: 0; opacity: .35' if m else 'top: 0; right: 0; bottom: 0; width: 62%', IMG['services']))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: %s"></div>' % (
        'linear-gradient(180deg, rgba(6,20,40,.7), rgba(6,20,40,.95))' if m else 'linear-gradient(90deg, %s 38%%, rgba(6,20,40,.55) 70%%, rgba(6,20,40,.35) 100%%), linear-gradient(0deg, %s 0%%, rgba(6,20,40,0) 55%%)' % (NAVY, NAVY)))
    svcs = [('calc', 'Bookkeeping & Accounting', 'Books that match your bank and that you can trust, kept by a team that knows QuickBooks inside out.', '#bookkeeping'),
            ('laptop', 'QuickBooks Setup & Advisory', 'Set up right, then put to good use. Once your books are clean, we help you use the numbers to make better choices.', '#setup'),
            ('chart', 'Fractional CFO', 'A part-time finance chief for your business, without hiring one full-time. Our managing partner leads this.', '#cfo'),
            ('layers', 'Additional support', 'QuickBooks Cleanup, Custom Reporting and POS Integration, for when your books need more.', '#cleanup')]
    cards = ''.join(
        '<a class="card" href="%s" style="display: flex; flex-direction: column; gap: 12px; padding: %s; min-height: %s"><span style="color: %s">%s</span>'
        '<h3 style="font-family: \'Inter\', sans-serif; font-style: normal; text-transform: none; font-size: 19px; font-weight: 700; letter-spacing: -.01em; line-height: 1.2">%s</h3>'
        '<p style="font-size: 14.5px; line-height: 1.55">%s</p><span class="go" style="margin-top: auto; display: inline-flex">%s</span></a>'
        % (h, '22px' if m else '28px 26px', 'auto' if m else '268px', BLUE, ic(n, 34, sw=1.6), t, d, ic('arrow', 20)) for n, t, d, h in svcs)
    head = ('<div style="display: %s; gap: %s; align-items: end; margin-bottom: %s">'
            '<div style="display: flex; flex-direction: column; gap: 20px"><p class="eb">Our services</p><h2 style="font-size: %s">Mission-critical<br>financial support.</h2></div>'
            '<p style="font-size: 17px; max-width: 420px; color: #DCE6F2">A complete financial team for businesses that need more than basic bookkeeping.</p></div>'
            % ('flex; flex-direction: column; align-items: flex-start' if m else 'grid; grid-template-columns: 1fr 1fr', '18px' if m else '40px', '34px' if m else '56px', '46px' if m else '72px'))
    a(wrap(head + '<div style="display: grid; grid-template-columns: %s; gap: %s">%s</div>' % ('1fr' if m else 'repeat(4, minmax(0, 1fr))', '14px' if m else '22px', cards)))
    a('</section>')

    # ---------- 04 Who we serve ----------
    a('\n<!-- 04 Who we serve: who MISSION works with, from the Business DNA -->')
    a('<section id="who" class="lt" aria-label="Who we serve" style="position: relative; overflow: hidden; background: linear-gradient(180deg, %s 0%%, #F6F9FC 100%%); padding: %s">' % (ICE, '60px 0' if m else '96px 0'))
    pts = [('building', 'Established businesses', 'Typically $1M–$10M a year'), ('layers', 'Running QuickBooks', 'Most already use it'), ('growth', 'Real complexity', 'Inventory, ecommerce, more than one company')]
    pcells = ''.join(
        '<div style="display: flex; %s gap: %s; padding: %s; %s"><span style="color: %s; flex: none">%s</span><span style="display: flex; flex-direction: column; gap: 4px">'
        '<span style="font: 700 16px/1.3 \'Inter\', sans-serif; color: %s">%s</span><span style="font-size: 14px; color: %s">%s</span></span></div>'
        % ('align-items: center;' if m else 'flex-direction: column; align-items: center; text-align: center;', '16px' if m else '14px', '16px 0' if m else '0 24px',
           ('border-top: 1px solid #D5DFEA' if i else '') if m else ('border-left: 1px solid #D5DFEA' if i else ''), BLUE, ic(n, 40, sw=1.5), INK, t, MUTED, d)
        for i, (n, t, d) in enumerate(pts))
    txt = ('<div style="display: flex; flex-direction: column; gap: 22px"><p class="eb">Who we serve</p><h2 style="font-size: %s">Built for established<br>businesses.</h2>'
           '<p style="font-size: 17px; max-width: 500px">We work with established small and mid-sized businesses across the US, typically $1M–$10M in annual revenue, that need more than basic bookkeeping. Fully remote, nationwide.</p></div>' % ('46px' if m else '72px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: %s">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 6fr) minmax(0, 6fr)', '30px' if m else '56px', txt,
              'flex; flex-direction: column' if m else 'grid; grid-template-columns: repeat(3, minmax(0, 1fr))', pcells)))
    a('</section>')

    # ---------- 05 Case studies ----------
    a('\n<!-- 05 Case studies: the real stories, on the contour-line texture -->')
    a('<section id="case-studies" class="dk" aria-label="Case studies" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY2, '64px 0' if m else '100px 0'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0; opacity: .9"><img src="%s" alt=""></div>' % IMG['cases'])
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(6,20,40,.85) 0%, rgba(6,20,40,.45) 60%, rgba(6,20,40,.3) 100%)"></div>')
    cs = [('cs_construction', 'Construction', 'A construction company had useful QuickBooks tools it wasn’t using.', 'We found the tools already built into their QuickBooks Enterprise that nobody was using.', 'https://missionaccountinghelp.com/customers/quickbooks-enterprise-support', 'center 35%'),
          ('cs_jewelry', 'Jewelry', 'Custom orders, and knowing where each piece is.', 'How a jewelry business tracks custom orders, and where each item is kept, in QuickBooks Enterprise.', 'https://missionaccountinghelp.com/customers/quickbooks-online-vs-enterprise', '60% 50%'),
          ('cs_interiors', 'Interiors', 'Bills approved and spending tracked, automatically.', 'How Wren’s Nest Interiors made bill approvals and expense tracking automatic.', 'https://missionaccountinghelp.com/technology/accounting-software/automated-accounting-software', '58% 38%')]
    ccards = ''.join(
        '<a class="card" href="%s" target="_blank" rel="noopener" style="display: flex; flex-direction: column; overflow: hidden">'
        '<div class="ph" style="height: %s"><img src="%s" alt="" style="object-position: %s"></div>'
        '<div style="display: flex; flex-direction: column; gap: 10px; padding: 18px 20px 20px; flex: 1">'
        '<span style="align-self: flex-start; font: 700 11px/1 \'Inter\', sans-serif; letter-spacing: .06em; padding: 6px 9px; border-radius: 3px; background: #E3F1FF; color: #0B5FA8">%s</span>'
        '<h3 style="font-size: 25px; line-height: 1">%s</h3><p style="font-size: 14px; line-height: 1.55">%s</p>'
        '<span class="go" style="margin-top: auto; align-self: flex-end; display: inline-flex">%s</span></div></a>'
        % (u, '180px' if m else '170px', IMG[k], pos, tag, t, d, ic('arrow', 20)) for k, tag, t, d, u, pos in cs)
    txt = ('<div style="display: flex; flex-direction: column; gap: 22px"><p class="eb">Case studies</p><h2 style="font-size: %s">Real problems.<br>Real progress.</h2>'
           '<p style="font-size: 17px; color: #DCE6F2; max-width: 380px">Messy books, fixed. These are real MISSION clients and what changed for them.</p>'
           '<div style="padding-top: 6px">%s</div></div>' % ('46px' if m else '68px', btn('See all case studies', href='#case-studies', icon=False, extra='width: 100%' if m else '')))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: grid; grid-template-columns: %s; gap: %s">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 4fr) minmax(0, 8fr)', '34px' if m else '48px', txt, '1fr' if m else 'repeat(3, minmax(0, 1fr))', '16px' if m else '20px', ccards)))
    a('</section>')

    # ---------- 06 Testimonial and facts ----------
    a('\n<!-- 06 One client in their own words (verbatim), with three facts -->')
    a('<section class="dk" aria-label="What clients say" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '56px 0' if m else '72px 0'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0; opacity: .55"><img src="%s" alt="" style="object-position: center 60%%"></div>' % IMG['quote'])
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(6,20,40,.92) 0%, rgba(6,20,40,.75) 100%)"></div>')
    q = ('<figure style="margin: 0; display: flex; gap: 18px; align-items: flex-start"><span class="blue" style="flex: none; font: 800 italic 90px/0.8 \'Barlow Condensed\', sans-serif">“</span>'
         '<div style="display: flex; flex-direction: column; gap: 14px"><blockquote style="margin: 0; font: 500 %s/1.45 \'Inter\', sans-serif; color: #FFFFFF">“We have been working with Bernard for over 10 years. He has been terrific.”</blockquote>'
         '<figcaption style="font-size: 14px; color: #AFC0D4">— Jacquie Herz, Jornik Manufacturing, Stamford, CT</figcaption></div></figure>' % ('19px' if m else '23px'))
    facts = [('25+', 'Years of experience'), ('850', 'Clients served'), ('50', 'Recurring clients')]
    fc = ''.join('<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 6px; padding: %s; %s"><span class="cond" style="font-size: %s; color: #FFFFFF">%s</span><span style="font-size: 13.5px; color: #AFC0D4; text-align: center">%s</span></div>'
                 % ('8px 4px' if m else '0 18px', 'border-left: 1px solid rgba(255,255,255,.18)' if (i or not m) else '', '40px' if m else '56px', v, l) for i, (v, l) in enumerate(facts))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr))">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 6fr) minmax(0, 6fr)', '34px' if m else '48px', q, fc)))
    a('</section>')

    # ---------- 07 Team ----------
    a('\n<!-- 07 The team: real names and roles; headshots are placeholders until MISSION supplies photos -->')
    a('<section id="team" class="lt" aria-label="The team" style="position: relative; overflow: hidden; background: linear-gradient(180deg, #F6F9FC 0%%, %s 100%%); padding: %s">' % (ICE, '64px 0' if m else '100px 0'))
    people = [('Bernard P. Roesch', 'Co-founder & Managing Partner'), ('Carol A. Onorato', 'Director of Operations'), ('Robert (Rob) James', 'New-client onboarding & marketing')]
    pc = ''.join(
        '<div style="display: flex; flex-direction: column; gap: 12px"><div style="position: relative; height: %s; border-radius: 6px; overflow: hidden; background: linear-gradient(160deg, #13345C 0%%, %s 100%%); display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 10px; color: rgba(255,255,255,.55)">'
        '<div class="slash" aria-hidden="true" style="right: -20px; top: -10px; width: 46px; height: 130%%; opacity: .9"></div>%s'
        '<span style="position: relative; font: 600 12px/1 \'Inter\', sans-serif; letter-spacing: .14em; text-transform: uppercase">Headshot to come</span></div>'
        '<div><p style="font: 700 16px/1.3 \'Inter\', sans-serif; color: %s">%s</p><p style="font-size: 13.5px; color: %s">%s</p></div></div>'
        % ('210px' if m else '290px', NAVY, ic('person', 64, sw=1.2), INK, n, MUTED, r) for n, r in people)
    txt = ('<div style="display: flex; flex-direction: column; gap: 22px"><p class="eb">Our team</p><h2 style="font-size: %s">Experience. Expertise.<br>A team on your side.</h2>'
           '<p style="font-size: 17px; max-width: 470px">You get more than one bookkeeper. Our core team holds advanced QuickBooks certifications, and we bring in trusted accountants and specialists from our wider network when your work needs them.</p>'
           '<div style="padding-top: 6px">%s</div></div>' % ('44px' if m else '64px', btn('Meet our team', href='#team', icon=False, extra='width: 100%' if m else '')))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: grid; grid-template-columns: %s; gap: %s">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr)', '34px' if m else '56px', txt, 'repeat(2, minmax(0, 1fr))' if m else 'repeat(3, minmax(0, 1fr))', '14px' if m else '20px', pc)))
    a('</section>')

    # ---------- 08 Strategic partner ----------
    a('\n<!-- 08 More than a bookkeeper: four strengths from the Business DNA, on the globe image -->')
    a('<section class="dk" aria-label="A strategic partner" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '64px 0' if m else '88px 0'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; %s"><img src="%s" alt="" style="object-position: %s"></div>' % ('inset: 0; opacity: .5' if m else 'top: 0; right: 0; bottom: 0; width: 70%', IMG['partner'], '70% 50%' if m else 'center 50%'))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: %s"></div>' % ('linear-gradient(180deg, rgba(6,20,40,.8), rgba(6,20,40,.95))' if m else 'linear-gradient(90deg, %s 30%%, rgba(6,20,40,.75) 60%%, rgba(6,20,40,.55) 100%%)' % NAVY))
    st = [('shield', 'QuickBooks experts', 'Advanced-certified QuickBooks ProAdvisors'), ('compass', 'Strategic guidance', 'Advisory and fractional CFO support'),
          ('process', 'A clear process', 'Consultation, onboarding, then monthly work'), ('team', 'Dedicated team', 'Account managers who know your system')]
    sc = ''.join('<div style="display: flex; %s gap: 12px; padding: %s; %s"><span style="color: %s">%s</span><span style="display: flex; flex-direction: column; gap: 4px"><span style="font: 700 16px/1.3 \'Inter\', sans-serif; color: #FFFFFF">%s</span><span style="font-size: 13.5px; color: #AFC0D4">%s</span></span></div>'
                 % ('align-items: center;' if m else 'flex-direction: column; align-items: center; text-align: center;', '14px 0' if m else '0 18px', ('border-top: 1px solid rgba(255,255,255,.14)' if i else '') if m else ('border-left: 1px solid rgba(255,255,255,.16)' if i else ''), BLUE, ic(n, 40, sw=1.5), t, d) for i, (n, t, d) in enumerate(st))
    txt = ('<div style="display: flex; flex-direction: column; gap: 20px"><p class="eb">More than a bookkeeper</p><h2 class="blue" style="font-size: %s">A strategic partner.</h2>'
           '<p style="font-size: 16.5px; color: #DCE6F2; max-width: 470px">We get the books current and accurate, then take over the recurring bookkeeping and accounting, with QuickBooks set up properly. From there the work can grow into custom reporting, advisory and fractional CFO support.</p></div>' % ('46px' if m else '68px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: %s">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr)', '30px' if m else '48px', txt, 'flex; flex-direction: column' if m else 'grid; grid-template-columns: repeat(4, minmax(0, 1fr))', sc)))
    a('</section>')

    # ---------- 09 Trusted, certified, proven ----------
    a('\n<!-- 09 Trusted. Certified. Proven.: the Elite badge and three real numbers, over the sky -->')
    a('<section class="lt" aria-label="Certified by Intuit" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (ICE, '52px 0' if m else '64px 0'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0; opacity: .28"><img src="%s" alt="" style="object-position: center 30%%"></div>' % IMG['trusted'])
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(237,243,249,.97) 0%, rgba(237,243,249,.8) 100%)"></div>')
    boxes = [('25+', 'Years in business'), ('850', 'Clients served'), ('5.0★', 'Google reviews (32)')]
    bx = ''.join('<div style="display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 4px; padding: %s; border-radius: 6px; background: %s; box-shadow: 0 14px 30px rgba(6,20,40,.18)"><span class="cond" style="font-size: %s; color: #FFFFFF">%s</span><span style="font-size: 12.5px; color: #AFC0D4; text-align: center">%s</span></div>'
                 % ('16px 8px' if m else '18px 26px', NAVY2, '30px' if m else '40px', v, l) for v, l in boxes)
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">'
           '<h2 class="blue" style="font-size: %s">Trusted.<br>Certified.<br>Proven.</h2>'
           '<img src="%s" alt="QuickBooks ProAdvisor Elite badge" style="height: %s; width: auto; align-self: flex-start; %s">'
           '<div style="display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: %s; %s">%s</div></div>'
           % ('flex; flex-direction: column; align-items: flex-start' if m else 'grid; grid-template-columns: auto auto 1fr', '24px' if m else '48px', '44px' if m else '52px', IMG['elite'], '90px' if m else '110px', '' if m else 'justify-self: center', '10px' if m else '16px', 'width: 100%' if m else '', bx)))
    a('</section>')

    # ---------- 10 FAQ ----------
    a('\n<!-- 10 Questions people ask before the first call (Lane J\'s; the first answer is open) -->')
    a('<section id="faq" class="lt" aria-label="Frequently asked questions" style="position: relative; background: #FFFFFF; padding: %s">' % ('60px 0' if m else '96px 0'))
    qs = ['What happens in the free consultation?', 'Do I need to prepare anything?', 'Is my business too small for you?', 'We already have a tax accountant. Does that change anything?', 'How quickly can you start?']
    fq = ''.join('<div><div class="faq" role="button" tabindex="0" aria-expanded="%s">%s<span>%s</span></div>%s</div>'
                 % ('true' if i == 0 else 'false', ic('minus' if i == 0 else 'plus', 18, sw=2.2), qq,
                    '<p style="font-size: 15px; padding: 0 0 18px 32px">It\'s a chat, not a sales pitch. Bernard or Rob will ask how your books are going, look at anything you can share, and tell you what they would fix first.</p>' if i == 0 else '')
                 for i, qq in enumerate(qs))
    txt = ('<div style="display: flex; flex-direction: column; gap: 20px"><p class="eb">Frequently asked questions</p><h2 style="font-size: %s">Got questions?<br>We\'ve got answers.</h2>'
           '<p style="font-size: 17px; max-width: 420px">Questions people ask before the first call.</p></div>' % ('44px' if m else '64px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: start">%s<div style="border-bottom: 1px solid #D9E2EC">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr)', '28px' if m else '64px', txt, fq)))
    a('</section>')

    # ---------- 11 Call to action ----------
    a('\n<!-- 11 Your next step: the closing call to action -->')
    a('<section id="schedule" class="dk" aria-label="Your next step" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '72px 0' if m else '96px 0'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0"><img src="%s" alt="" style="object-position: %s"></div>' % (IMG['cta'], '75% 40%' if m else 'center 45%'))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: %s"></div>' % ('linear-gradient(180deg, rgba(6,20,40,.85), rgba(6,20,40,.75))' if m else 'linear-gradient(90deg, rgba(6,20,40,.95) 0%, rgba(6,20,40,.8) 45%, rgba(6,20,40,.35) 100%)'))
    txt = ('<div style="display: flex; flex-direction: column; gap: 18px"><p class="eb c" style="color: #FFFFFF">Ready to take control of your books?</p>'
           '<h2 style="font-size: %s">Your next chapter starts<br>with a conversation.</h2>'
           '<p style="font-size: 17px; color: #DCE6F2; max-width: 540px">Book a free call with Bernard or Rob. Come as you are, mess and all. We\'ll tell you what we\'d fix first and what it would take.</p></div>' % ('42px' if m else '64px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: flex; flex-direction: column; gap: 12px; %s">%s<a class="btn btn-o" href="tel:+12032279475"%s>%sCall (203) 227-9475</a></div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 7fr) auto', '28px' if m else '48px', txt, '' if m else 'align-items: stretch',
              btn('Schedule a free consultation', extra='width: 100%' if m else ''), ' style="width: 100%"' if m else '', ic('phone', 16))))
    a('</section>')

    # ---------- 12 Footer ----------
    a('\n<!-- 12 Footer: logo, four link columns, contact and the button -->')
    a('<footer id="contact" class="dk foot" style="position: relative; overflow: hidden; background: #040E1D; padding: %s">' % ('52px 0 28px' if m else '72px 0 32px'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0; opacity: .35"><img src="%s" alt=""></div>' % IMG['footer'])
    cols = [('Services', [('Bookkeeping & Accounting', '#bookkeeping'), ('QuickBooks Setup & Advisory', '#setup'), ('Fractional CFO', '#cfo'), ('QuickBooks Cleanup', '#cleanup'), ('Custom Reporting', '#reporting'), ('POS Integration', '#pos')]),
            ('Who we serve', [('Established businesses', '#who'), ('Industries', '#who'), ('Case studies', '#case-studies')]),
            ('About', [('Our team', '#team'), ('Partner Program', '#partners'), ('Contact', '#contact')]),
            ('Resources', [('Blog', '#blog'), ('Podcast', 'http://missionaccountinghelp.com/feed/podcast'), ('FAQs', '#faq')])]
    cl = ''.join('<nav aria-label="%s" style="display: flex; flex-direction: column; gap: 9px; font-size: 13.5px"><p style="margin: 0 0 4px; font: 700 12px/1.3 \'Inter\', sans-serif; color: #FFFFFF">%s</p>%s</nav>'
                 % (t, t, ''.join('<a href="%s">%s</a>' % (h, x) for x, h in links)) for t, links in cols)
    contact = ('<div style="display: flex; flex-direction: column; gap: 14px">'
               '<a href="tel:+12032279475" style="display: inline-flex; align-items: center; gap: 10px; font-size: 14px; color: #FFFFFF"><span class="blue" style="display: inline-flex">%s</span>(203) 227-9475</a>'
               '<a href="mailto:info@missionaccountinghelp.com" style="display: inline-flex; align-items: center; gap: 10px; font-size: 14px; color: #FFFFFF"><span class="blue" style="display: inline-flex">%s</span>info@missionaccountinghelp.com</a>'
               '<div style="padding-top: 6px">%s</div></div>' % (ic('phone', 16), ic('mail', 16), btn('Schedule a free consultation', extra='width: 100%' if m else '')))
    brand = ('<div style="display: flex; flex-direction: column; gap: 14px"><img src="%s" alt="MISSION" style="height: %s; width: auto; align-self: flex-start">'
             '<p style="font-size: 13.5px; color: #AEBCCD; max-width: 260px">Bookkeeping, accounting and QuickBooks for established businesses. Nationwide, fully remote.</p></div>' % (IMG['logo'], '26px' if m else '30px'))
    grid = ('<div style="display: %s; gap: %s">%s%s%s</div>'
            % ('flex; flex-direction: column' if m else 'grid; grid-template-columns: minmax(0, 1.8fr) repeat(4, minmax(0, 1.15fr)) minmax(0, 2.6fr)', '34px' if m else '28px', brand,
               ('<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 28px 20px">%s</div>' % cl) if m else cl, contact))
    bottom = ('<div style="margin-top: %s; border-top: 1px solid rgba(255,255,255,.12); padding-top: 20px; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 10px; font-size: 12.5px; color: #8496AD">'
              '<span>© 2026 MISSION. All rights reserved.</span><span style="display: flex; gap: 22px"><a href="#privacy">Privacy Policy</a><a href="#terms">Terms of Service</a></span></div>' % ('40px' if m else '56px'))
    a(wrap(grid + bottom))
    a('</footer>')

    # stacked layouts stretch their children on mobile (centred, they shrank to their content and the mission photo vanished)
    body = '\n'.join(A).replace('align-items: AIX', 'align-items: stretch' if m else 'align-items: center')
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@1,700;1,800&amp;family=Inter:wght@400;500;600;700&amp;display=swap">')
    title = 'Lane K homepage, %s' % ('mobile' if m else 'desktop')
    return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n%s\n<style>%s</style>\n</helmet>\n'
            '<div class="lk" style="width: %dpx; background: %s">\n%s\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":8000}}\'>\n'
            'class Component extends DCLogic {\n  // Lane K is a static design board (no review switches yet)\n  renderVals() {\n    return {};\n  }\n}\n</script>\n</body>\n</html>\n'
            % (title, fonts, CSS, W, NAVY, body, W))

os.makedirs(OUT, exist_ok=True)
for m, name in [(False, 'lane-k-home.dc.html'), (True, 'lane-k-home-mobile.dc.html')]:
    open(os.path.join(OUT, name), 'w').write(build(m))
    print('wrote', os.path.join(OUT, name))
