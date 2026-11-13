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
    'hero':     B + '8dcb3de219da9fe675e8e0f20be57256',   # climber on the overhang at sunset, with target rings and lines (13 Nov; replaces the first climber photo)
    'services': B + 'c7b34dc9f98b5531b52c5bc1cb27ff06',   # hiker on the summit, as in the reference
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
    'team_photo': B + '3d6b714436163c0b81700732407cd2ff',  # busy office, an advisor at her laptop (library photo; 13 Nov, by request, replaces the client-meeting photo)
    'cs_construction': B + 'dfd86de5e4c6c2aa6ee6ec5df6d9d9d0',   # crane over a steel frame at sunset (13 Nov, supplied for this card)
    'cs_jewelry':      B + '856fca6512e92dce3beccc32c801534c',   # diamond ring on dark fabric (13 Nov, supplied for this card)
    'cs_interiors':    B + '03953d5f25e1452b9fc441dfa089cdda',   # armchair and table by a sunlit window (13 Nov, supplied for this card)
}

NAVY, NAVY2, BLUE, LIME, INK, MUTED, ICE = '#061428', '#0A2240', '#1FA2FF', '#C1F432', '#0A1B2E', '#4A5A70', '#EDF3F9'

def svpos(m):
    # services carousel stops: desktop shows 4 of the 7 cards (4 stops), mobile 1 (7 stops)
    return 7 if m else 4


def svcss(m):
    vis, gap = (1, 14) if m else (4, 22)
    w = '86%' if m else 'calc((100%% - %dpx) / 4)' % (3 * gap)
    step = 'calc(86%% + %dpx)' % gap if m else 'calc((100%% - %dpx) / 4 + %dpx)' % (3 * gap, gap)
    # no clipping box (13 Nov, by request: cards were cut off while sliding): the row starts in line with the heading and the
    # cards run out to both edges of the page, which the section's overflow: hidden trims
    out = [
           '.lk .k-sv-track{display:flex;align-items:stretch;gap:%dpx;transition:transform .6s cubic-bezier(.22,.61,.36,1)}' % gap,
           '.lk .k-sv-track>.card{flex:none;width:%s}' % w]
    out += ['.lk .k-sv-track[data-pos="%d"]{transform:translateX(calc(%s * -%d))}' % (i, step, i) for i in range(1, svpos(m))]
    return '\n'.join(out) + '\n'


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
        'pos': '<rect x="2.5" y="5" width="19" height="14" rx="2"/><path d="M2.5 10h19M6.5 15h4"/>',
        'box': '<path d="M12 3l8 4.5v9L12 21l-8-4.5v-9z"/><path d="M4 7.5l8 4.5 8-4.5M12 12v9"/>',
        'minus': '<path d="M5 12h14"/>',
        'chev': '<path d="M6 9l6 6 6-6"/>',
        'quote': '<path d="M7 7h4v4c0 3-1.5 5-4 6M15 7h4v4c0 3-1.5 5-4 6"/>',
        'person': '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
        'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
    }
    return ('<svg width="%d" height="%d" viewBox="0 0 24 24" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" '
            'stroke-linejoin="round" aria-hidden="true">%s</svg>' % (size, size, stroke, sw, P[name]))

CSS = '''
body{margin:0;background:%(NAVY)s}
.lk{font-family:'Inter','Helvetica Neue',Arial,sans-serif;color:#C9D6E8;-webkit-font-smoothing:antialiased;font-size:16px;line-height:1.6}
.lk *{box-sizing:border-box}
.lk a{color:inherit}
.lk h1,.lk h2,.lk h3,.lk .cond{margin:0;font-family:'Barlow Condensed','Arial Narrow',sans-serif;font-style:italic;font-weight:800;text-transform:uppercase;letter-spacing:-.005em;line-height:.94}
.lk p{margin:0}
.lk .eb{display:flex;align-items:center;gap:14px;font:700 12px/1.3 'Inter',sans-serif;letter-spacing:.2em;text-transform:uppercase;color:%(BLUE)s}
.lk .eb::after{content:'';flex:none;width:56px;height:12px;
  background:radial-gradient(circle,#FFFFFF 0 1.2px,#FFD98A 2px,rgba(255,150,40,.55) 3.4px,rgba(255,150,40,0) 6px) no-repeat,
             linear-gradient(90deg,rgba(255,170,70,.0),rgba(255,170,70,.9)) no-repeat,
             linear-gradient(currentColor,currentColor) no-repeat;
  background-size:12px 12px,10px 2px,89%% 2px;background-position:100%% 50%%,87%% 50%%,0 50%%;
  animation:kFuse 5.2s linear infinite,kSpark .18s steps(2) infinite alternate}
/* the eyebrow line is a lit fuse (13 Nov, by request, kept subtle): a small spark burns along the line toward the words, the cord
   shortening behind it with a warm glow at the tip, then the line comes back and it starts again */
@keyframes kFuse{
  0%%{background-size:12px 12px,10px 2px,89%% 2px;background-position:100%% 50%%,87%% 50%%,0 50%%;opacity:.85}
  60%%{background-size:12px 12px,10px 2px,11%% 2px;background-position:0 50%%,-9%% 50%%,0 50%%;opacity:.85}
  66%%{background-size:0 0,0 2px,0 2px;background-position:0 50%%,-9%% 50%%,0 50%%;opacity:0}
  78%%{background-size:0 0,0 2px,89%% 2px;background-position:100%% 50%%,87%% 50%%,0 50%%;opacity:0}
  88%%,100%%{background-size:12px 12px,10px 2px,89%% 2px;background-position:100%% 50%%,87%% 50%%,0 50%%;opacity:.85}}
@keyframes kSpark{from{filter:brightness(1)}to{filter:brightness(1.35)}}
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
.lk .lt .btn-o{color:%(INK)s;border-color:#9FB0C4}
.lk .lt .btn-o:hover,.lk .lt .btn-o:focus-visible{color:%(NAVY)s;border-color:%(LIME)s}
.lk .nl-field:focus-within{border-color:rgba(255,255,255,.6) !important;background:rgba(255,255,255,.1) !important}
.lk .nl-field input::placeholder{color:#8496AD}
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
.lk .slash{position:absolute;background:%(BLUE)s;transform:skewX(-5deg)}
.lk .cursor{cursor:pointer}
/* case studies (13 Nov): slanted cards with a glowing edge; the highlighted one (arrows and dots) glows brighter and lifts */
/* the slant was reduced twice on 13 Nov, by request (14 to 7 to 4 degrees on desktop, 8 to 4 to 2 on mobile) */
.lk .k-cs-row{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:26px;padding:12px 24px}
.lk .k-cs{display:block;text-decoration:none;transform:skewX(-4deg);border:1.5px solid rgba(31,162,255,.55);border-radius:4px;background:#0A2240;overflow:hidden;
  box-shadow:0 0 0 rgba(31,162,255,0);transition:transform .45s cubic-bezier(.22,.61,.36,1),box-shadow .45s ease,border-color .45s ease}
.lk .k-cs-in{transform:skewX(4deg);margin:0 -13px;position:relative}
.lk .k-cs-ph{position:relative;height:230px;overflow:hidden}
.lk .k-cs-ph img{position:absolute;inset:0;width:100%%;height:100%%;object-fit:cover;transition:transform .7s cubic-bezier(.22,.61,.36,1)}
.lk .k-cs-ph::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,34,64,0) 30%%,#0A2240 100%%)}
.lk .k-cs-body{position:relative;margin-top:-56px;padding:0 54px 28px 42px;display:flex;flex-direction:column;gap:10px}
.lk .k-cs-t{font-family:'Inter',sans-serif !important;font-style:italic !important;text-transform:none !important;font-weight:800 !important;font-size:23px !important;line-height:1.15 !important;letter-spacing:-.02em !important;color:#FFFFFF}
.lk .k-cs-go{display:inline-flex;align-items:center;gap:8px;margin-top:6px;font:700 14.5px/1 'Inter',sans-serif;color:%(LIME)s}
.lk .k-cs-go svg{transition:transform .3s ease}
.lk .k-cs:hover,.lk .k-cs:focus-visible{border-color:#4FC3FF;box-shadow:0 0 0 1px rgba(79,195,255,.6),0 0 26px rgba(31,162,255,.55),0 0 60px rgba(31,162,255,.25)}
.lk .k-cs:hover,.lk .k-cs:focus-visible{transform:skewX(-4deg) translateY(-10px)}
/* desktop shows all three cards, so the arrows and dots are for mobile only (13 Nov: no card looks hovered until it is) */
.lk .k-cs-navbar{display:none !important}
.lk .k-cs:hover .k-cs-ph img{transform:scale(1.06)}
.lk .k-cs:hover .k-cs-go svg{transform:translateX(4px)}
.lk .k-cs-nav{all:unset;cursor:pointer;width:46px;height:46px;border-radius:50%%;border:2px solid #FFFFFF;color:#FFFFFF;display:inline-flex;align-items:center;justify-content:center;transition:background-color .25s ease,color .25s ease,border-color .25s ease}
.lk .k-cs-nav:hover,.lk .k-cs-nav:focus-visible{background:%(LIME)s;border-color:%(LIME)s;color:%(NAVY)s}
.lk .k-cs-dot{all:unset;cursor:pointer;width:11px;height:11px;border-radius:50%%;background:rgba(255,255,255,.35);transition:background-color .25s ease,transform .25s ease}
.lk .k-cs-dot[aria-pressed="true"]{background:%(BLUE)s;transform:scale(1.15)}
@media (max-width: 600px){
  .lk .k-cs-row{grid-template-columns:1fr;padding:12px 22px}
  .lk .k-cs{transform:skewX(-2deg)}
  .lk .k-cs-in{transform:skewX(2deg);margin:0 -8px}
  .lk .k-cs-body{padding:0 28px 24px}
  .lk .k-cs[data-on="false"]{display:none}
  .lk .k-cs:hover,.lk .k-cs:focus-visible{transform:skewX(-2deg)}
  .lk[data-angles="off"] .k-cs:hover,.lk[data-angles="off"] .k-cs:focus-visible{transform:none !important}
  .lk .k-cs-navbar{display:flex !important}
  .lk .k-cs-ph{height:200px}
}
.lk .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
/* the badge marquee: two copies of the row, the track slides left by one copy and loops */
@keyframes kMarquee{from{transform:translateX(0)}to{transform:translateX(-50%%)}}
.lk .k-track{animation:kMarquee 34s linear infinite}
.lk .k-marquee:hover .k-track{animation-play-state:paused}
@media (prefers-reduced-motion: reduce){.lk *{transition:none !important}}
/* review bar (not part of the design) and its two switches (13 Nov, by request) */
.lk .tg-bar{position:sticky;top:0;z-index:100;min-height:40px;box-sizing:border-box;background:#141414;color:#FFFFFF;display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:12px;padding:6px 8px;font:500 12.5px/1 system-ui,-apple-system,'Segoe UI',sans-serif}
.lk .tg-bar .tg-label{color:#BDBDBD}
.lk .tg-bar .tg-group{display:inline-flex;background:#2B2B2B;border-radius:999px;padding:3px;gap:2px}
.lk .tg-bar .tg-opt{all:unset;cursor:pointer;display:inline-flex;align-items:center;gap:7px;height:26px;padding:0 12px;border-radius:999px;color:#D0D0D0;font:600 12px/1 system-ui,-apple-system,'Segoe UI',sans-serif;transition:background-color .2s ease,color .2s ease}
.lk .tg-bar .tg-opt:hover{color:#FFFFFF}
.lk .tg-bar .tg-opt:focus-visible{outline:2px solid %(BLUE)s;outline-offset:2px}
.lk .tg-bar .tg-opt[aria-pressed="true"]{background:#FFFFFF;color:#141414}
/* Angles off: straight case-study cards, a square mission photo and upright bars on the headshot frames (the italic headings stay) */
.lk[data-angles="off"] .k-cs,.lk[data-angles="off"] .k-cs-in{transform:none !important}
.lk[data-angles="off"] .k-cs-in{margin:0 !important}
.lk[data-angles="off"] .k-cs-body{padding:0 28px 28px !important}
.lk[data-angles="off"] .k-cs:hover,.lk[data-angles="off"] .k-cs:focus-visible{transform:translateY(-10px) !important}
.lk[data-angles="off"] .k-ang-clip{clip-path:none !important}
.lk[data-angles="off"] .slash{transform:none}
/* Eyebrow lines None: no line or fuse after the eyebrows */
.lk[data-eb="none"] .eb::after{display:none}
/* Copy: Standard is the sourced copy; Mission puts headings, eyebrows and short lines in a spy-mission voice (same facts) */
.lk[data-copy="mission"] .cp-s,.lk[data-copy="standard"] .cp-m{display:none}
@media (prefers-reduced-motion: reduce){.lk .k-track{animation:none}.lk .eb::after{animation:none;background:linear-gradient(currentColor,currentColor) no-repeat 0 50%%/100%% 2px}}
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
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0"><img src="%s" alt="" style="object-position: %s"></div>' % (IMG['hero'], '68% 40%' if m else 'center 40%'))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: %s"></div>' % (
        'linear-gradient(180deg, rgba(6,20,40,.82) 0%, rgba(6,20,40,.70) 55%, rgba(6,20,40,.95) 100%)' if m else
        'linear-gradient(90deg, rgba(6,20,40,.96) 0%, rgba(6,20,40,.82) 38%, rgba(6,20,40,.25) 70%, rgba(6,20,40,.1) 100%), linear-gradient(0deg, rgba(6,20,40,.9) 0%, rgba(6,20,40,0) 30%)'))
    # a dark band behind the header (13 Nov, by request) so the phone button and menu stay legible over the rock in the photo
    a('<div aria-hidden="true" style="position: absolute; left: 0; right: 0; top: 0; height: %spx; background: linear-gradient(180deg, rgba(6,20,40,.92) 0%%, rgba(6,20,40,.78) 45%%, rgba(6,20,40,0) 100%%)"></div>' % (150 if m else 190))
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
    # the hero headline is 88 px on desktop and 52 px on mobile (13 Nov, by request; it was 112 / 62)
    hero = (hdr +
        '<div id="top" style="display: flex; flex-direction: column; gap: %s; max-width: %s; padding: %s">' % ('20px' if m else '24px', '100%' if m else '720px', '44px 0 0' if m else '96px 0 0') +
        '<p class="eb c" style="color: #FFFFFF; letter-spacing: %s; font-size: %s">Bookkeeping / Accounting / QuickBooks / Fractional CFO</p>' % ('.12em' if m else '.2em', '10.5px' if m else '12px') +
        '<h1 style="font-size: %s; color: #FFFFFF"><span class="cp-s">Complex books.<br><span class="blue">Clear answers.</span></span><span class="cp-m">Messy books?<br><span class="blue">Mission accepted.</span></span></h1>' % ('52px' if m else '88px') +
        '<p style="font-size: %s; line-height: 1.6; color: #DCE6F2; max-width: 560px">We fix messy books, keep them right every month, and show you your numbers in plain words. You get to focus on running your business.</p>' % ('16px' if m else '18px') +
        '<div style="display: flex; %s gap: 12px; padding-top: 6px">%s<a class="btn btn-o" href="#case-studies"%s>Read client stories%s</a></div>' % (
            'flex-direction: column;' if m else 'flex-wrap: wrap;', btn('Schedule a free consultation', extra='width: 100%' if m else ''), ' style="width: 100%"' if m else '', arr) +
        '</div>')
    # the five facts along the bottom of the hero were removed (13 Nov, by request); the hero ends below the buttons
    a(wrap(hero, '; padding-bottom: %s' % ('64px' if m else '120px')))
    a('</section>')

    # ---------- 02 The mission (who we are) ----------
    a('\n<!-- 02 The mission: a specialist team, with the team photo in a slanted frame -->')
    a('<section id="who-we-are" class="lt" aria-label="The mission" style="position: relative; overflow: hidden; background: linear-gradient(180deg, #F4F8FC 0%%, %s 100%%); padding: %s">' % (ICE, '64px 0' if m else '110px 0'))
    txt = ('<div style="display: flex; flex-direction: column; gap: 22px">'
           '<p class="eb"><span class="cp-s">The mission</span><span class="cp-m">Your briefing</span></p><h2 style="font-size: %s"><span class="cp-s">A specialist team that knows your business.</span><span class="cp-m">A specialist team, briefed on your business.</span></h2>'
           '<p style="font-size: 17px; max-width: 470px">You started a business, not a bookkeeping job. We keep your books clean and correct. You don\'t have to hire a full finance team or get lost at a big firm.</p>'
           '<div style="padding-top: 6px">%s</div></div>' % ('46px' if m else '72px', btn("Let's talk about your needs", icon=False, extra='width: 100%' if m else '')))
    photo = ('<div style="position: relative; height: %s">'
             '<div class="ph k-ang-clip" style="position: absolute; inset: 0; clip-path: polygon(%s)"><img src="%s" alt="Specialists reviewing a client\'s numbers together" style="object-position: center 30%%"></div>'
             '</div>'
             % ('300px' if m else '470px', '2.5% 0, 100% 0, 100% 100%, 0 100%' if m else '4% 0, 100% 0, 100% 100%, 0 100%', IMG['mission']))
    # the blue slanted bar beside the photo was removed (13 Nov, by request); the photo keeps its slanted left edge.
    # (An ice-blue overlay version was tried on 13 Nov and reverted by request.)
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s%s</div>' % ('flex; flex-direction: column' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr)', '36px' if m else '56px', txt, photo)))
    a('</section>')

    # ---------- 03 Services ----------
    a('\n<!-- 03 Services: four cards on navy, the photo fading in from the right -->')
    a('<section id="services" class="dk" aria-label="Services" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '64px 0' if m else '100px 0 110px'))
    # the hiker photo is blurred behind a frosted overlay (13 Nov, by request), so the cards stand out; scaled up a little so the soft edges stay out of view
    a('<div class="ph" aria-hidden="true" style="position: absolute; %s"><img src="%s" alt="" style="object-position: center 40%%; filter: blur(%s); transform: scale(1.08)"></div>' % ('inset: 0; opacity: .35' if m else 'top: 0; right: 0; bottom: 0; width: 62%', IMG['services'], '8px' if m else '12px'))
    a('<div aria-hidden="true" style="position: absolute; %s; background: rgba(6,20,40,.22)"></div>' % ('inset: 0' if m else 'top: 0; right: 0; bottom: 0; width: 62%'))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: %s"></div>' % (
        'linear-gradient(180deg, rgba(6,20,40,.7), rgba(6,20,40,.95))' if m else 'linear-gradient(90deg, %s 38%%, rgba(6,20,40,.55) 70%%, rgba(6,20,40,.35) 100%%), linear-gradient(0deg, %s 0%%, rgba(6,20,40,0) 55%%)' % (NAVY, NAVY)))
    # all seven services (13 Nov, by request), in Lane G3's order and wording where Lane K had none; four at a time on desktop, one on mobile, in a carousel
    svcs = [('calc', 'Bookkeeping & Accounting', 'Books that match your bank and that you can trust, kept by a team that knows QuickBooks inside out.', '#bookkeeping'),
            ('laptop', 'QuickBooks Setup & Advisory', 'Set up right, then put to good use. Once your books are clean, we help you use the numbers to make better choices.', '#setup'),
            ('chart', 'Fractional CFO', 'A part-time finance chief for your business, without hiring one full-time. Our managing partner leads this.', '#cfo'),
            ('refresh', 'QuickBooks Cleanup', 'Months of bank statements nobody has matched to the books, or books left behind when a bookkeeper moved on. We bring them up to date and make them right.', '#cleanup'),
            ('pos', 'POS Integration', 'We connect your checkout system, like Square or Shopify, to QuickBooks so your sales show up in your books on their own.', '#pos'),
            ('bars', 'Custom Reporting', "Normal reports answer your accountant's questions. Custom reports answer yours.", '#reporting'),
            ('box', 'QuickBooks Products', "QuickBooks Online, Desktop, Enterprise and Intuit Enterprise Suite. You can buy them from us, because we're an Intuit reseller.", '#products')]
    cards = ''.join(
        '<a class="card" href="%s" style="display: flex; flex-direction: column; gap: 12px; padding: %s; min-height: %s"><span style="color: %s">%s</span>'
        '<h3 style="font-family: \'Inter\', sans-serif; font-style: normal; text-transform: none; font-size: 19px; font-weight: 700; letter-spacing: -.01em; line-height: 1.2">%s</h3>'
        '<p style="font-size: 14.5px; line-height: 1.55">%s</p><span class="go" style="margin-top: auto; display: inline-flex">%s</span></a>'
        % (h, '22px' if m else '28px 26px', 'auto' if m else '268px', BLUE, ic(n, 34, sw=1.6), t, d, ic('arrow', 20)) for n, t, d, h in svcs)
    nsv = svpos(m)
    svbtn = lambda lab, dirn, fn: ('<button type="button" class="k-cs-nav" aria-label="%s" onClick="{{ %s }}"><span style="display: inline-flex; transform: rotate(%ddeg)">%s</span></button>'
                                   % (lab, fn, 180 if dirn < 0 else 0, ic('arrow', 20, sw=2)))
    svdots = ''.join('<button type="button" class="k-cs-dot" aria-label="Services, view %d of %d" aria-pressed="{{ svOn%d }}" onClick="{{ svGo%d }}"></button>' % (i + 1, nsv, i, i) for i in range(nsv))
    svnav = ('<div style="display: flex; align-items: center; justify-content: %s; gap: 22px; margin-top: %s">%s<div style="display: flex; gap: 10px">%s</div>%s</div>'
             % ('space-between' if m else 'flex-end', '26px' if m else '40px', svbtn('Previous services', -1, 'svPrev'), svdots, svbtn('Next services', 1, 'svNext')))
    # a button to the main services page under the line (13 Nov, by request), as in the case studies; '#services' until the page URL is confirmed
    head = (('<div style="display: %s; gap: %s; align-items: ' + ('stretch' if m else 'end') + '; margin-bottom: %s">'
             '<div style="display: flex; flex-direction: column; gap: 20px"><p class="eb"><span class="cp-s">Our services</span><span class="cp-m">Capabilities</span></p><h2 style="font-size: %s">Mission-critical<br>financial support.</h2></div>'
             '<div style="display: flex; flex-direction: column; gap: 20px; %s"><p style="font-size: 17px; max-width: 420px; color: #DCE6F2"><span class="cp-s">A complete financial team for businesses that need more than basic bookkeeping.</span><span class="cp-m">A complete financial team, ready to deploy when basic bookkeeping is not enough.</span></p>'
             '<div>%s</div></div></div>')
            % ('flex; flex-direction: column' if m else 'grid; grid-template-columns: 1fr 1fr', '18px' if m else '40px', '34px' if m else '56px', '46px' if m else '72px',
               '' if m else 'align-items: flex-start; padding-bottom: 8px', btn('See all services', href='#services', icon=False, extra='width: 100%' if m else '')))
    a(wrap(head + '<div class="k-sv-vp"><div class="k-sv-track" data-pos="{{ svPos }}">%s</div></div>' % cards + svnav))
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
    txt = ('<div style="display: flex; flex-direction: column; gap: 22px"><p class="eb"><span class="cp-s">Who we serve</span><span class="cp-m">Client profile</span></p><h2 style="font-size: %s"><span class="cp-s">Built for established<br>businesses.</span><span class="cp-m">Built for established<br>businesses with real complexity.</span></h2>'
           '<p style="font-size: 17px; max-width: 500px">We work with established small and mid-sized businesses across the US, typically $1M–$10M in annual revenue, that need more than basic bookkeeping. Fully remote, nationwide.</p></div>' % ('46px' if m else '72px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: %s">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 6fr) minmax(0, 6fr)', '30px' if m else '56px', txt,
              'flex; flex-direction: column' if m else 'grid; grid-template-columns: repeat(3, minmax(0, 1fr))', pcells)))
    a('</section>')

    # ---------- 05 Case studies ----------
    a('\n<!-- 05 Case studies: the real stories, on the contour-line texture -->')
    a('<section id="case-studies" class="dk" aria-label="Case studies" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY2, '64px 0' if m else '100px 0'))
    # no background image on the case studies (13 Nov, by request): plain navy
    # case studies (13 Nov, by request, from Growth Foundry's inspiration image): a stacked heading with "Real progress." in blue, then
    # slanted (parallelogram) cards with a glowing blue edge, the photo fading into navy, an icon and industry, the title, one line and
    # "View case study"; arrows and dots move the highlighted card (on mobile they page through one card at a time). Wording stays
    # sourced (the inspiration's own titles and lines are not used); the photos are stand-ins until the case-study images arrive.
    CASES = [('cs_construction', '55% 28%', 'crane', 'Construction', '<span class="cp-s">Useful QuickBooks tools, finally in use.</span><span class="cp-m">Objective: put unused QuickBooks tools to work.</span>',
              'We found the tools already built into their QuickBooks Enterprise that nobody was using.', 'https://missionaccountinghelp.com/customers/quickbooks-enterprise-support'),
             ('cs_jewelry', '58% 42%', 'gem', 'Jewelry', '<span class="cp-s">Custom orders, and knowing where each piece is.</span><span class="cp-m">Objective: track every custom order and every piece.</span>',
              'How a jewelry business tracks custom orders, and where each item is kept, in QuickBooks Enterprise.', 'https://missionaccountinghelp.com/customers/quickbooks-online-vs-enterprise'),
             ('cs_interiors', '62% 55%', 'sofa', 'Interiors', '<span class="cp-s">Bills approved and spending tracked, automatically.</span><span class="cp-m">Objective: bill approvals and spending on autopilot.</span>',
              'How Wren’s Nest Interiors made bill approvals and expense tracking automatic.', 'https://missionaccountinghelp.com/technology/accounting-software/automated-accounting-software')]
    ICX = {'crane': '<path d="M4 21V5M4 5h16M4 5l5 5M14 5v4M12 9h4v3h-4zM2 21h6M8 5V3"/>',
           'gem': '<path d="M6 3h12l4 6-10 12L2 9z"/><path d="M2 9h20M9 3l3 6 3-6M12 9v12"/>',
           'sofa': '<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><path d="M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v4H2zM5 17v2M19 17v2"/>'}
    def kcard(i, k, pos, icon, ind, t, d, url):
        return ('<a class="k-cs" data-on="{{ csOn%d }}" href="%s" target="_blank" rel="noopener">'
                '<div class="k-cs-in">'
                '<div class="k-cs-ph"><img src="%s" alt="" style="object-position: %s"></div>'
                '<div class="k-cs-body">'
                '<span style="display: inline-flex; align-items: center; gap: 10px; font: 700 12px/1 \'Inter\', sans-serif; letter-spacing: .18em; text-transform: uppercase; color: #FFFFFF">'
                '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">%s</svg>%s</span>'
                '<h3 class="k-cs-t">%s</h3><p style="font-size: 14px; line-height: 1.5; color: #D5E3F2">%s</p>'
                '<span class="k-cs-go">View case study%s</span></div></div></a>'
                % (i, url, IMG[k], pos, ICX[icon], ind, t, d, ic('arrow', 16, sw=2.2)))
    cards = ''.join(kcard(i, *c) for i, c in enumerate(CASES))
    navbtn = lambda lab, dirn, fn: ('<button type="button" class="k-cs-nav" aria-label="%s" onClick="{{ %s }}">%s</button>'
                                   % (lab, fn, '<span style="display: inline-flex; transform: rotate(%s)">%s</span>' % ('180deg' if dirn < 0 else '0deg', ic('arrow', 20, sw=2))))
    dots = ''.join('<button type="button" class="k-cs-dot" aria-label="Case study %d" aria-pressed="{{ csOn%d }}" onClick="{{ csGo%d }}"></button>' % (i + 1, i, i) for i in range(3))
    nav = ('<div class="k-cs-navbar" style="display: flex; align-items: center; justify-content: space-between; margin-top: %s; padding: 0 %s">%s<div style="display: flex; gap: 10px">%s</div>%s</div>'
           % ('22px' if m else '36px', '4px' if m else '70px', navbtn('Previous case study', -1, 'csPrev'), dots, navbtn('Next case study', 1, 'csNext')))
    # the line and the button sit to the right of the heading on desktop (13 Nov, by request); stacked on mobile
    head = (('<div style="display: %s; gap: %s; align-items: ' + ('stretch' if m else 'end') + '; margin-bottom: %s">'
             '<div style="display: flex; flex-direction: column; gap: 20px"><p class="eb"><span class="cp-s">Case studies</span><span class="cp-m">Case files</span></p><h2 style="font-size: %s"><span class="cp-s">Real problems.<br><span class="blue">Real progress.</span></span><span class="cp-m">Real cases.<br><span class="blue">Real results.</span></span></h2></div>'
             '<div style="display: flex; flex-direction: column; gap: 20px; %s"><p style="font-size: 17px; color: #DCE6F2; max-width: 420px"><span class="cp-s">Messy books, fixed. These are real MISSION clients and what changed for them.</span><span class="cp-m">Messy books, cleared. These are real MISSION clients and what changed for them.</span></p>'
             '<div>%s</div></div></div>')
            % ('flex; flex-direction: column' if m else 'grid; grid-template-columns: minmax(0, 1fr) auto', '22px' if m else '56px', '36px' if m else '56px', '50px' if m else '84px',
               '' if m else 'align-items: flex-start; padding-bottom: 8px', btn('See all case studies', href='#case-studies', icon=False, extra='width: 100%' if m else '')))
    a(wrap(head + '<div class="k-cs-row">%s</div>' % cards + nav))
    a('</section>')

    # ---------- 06 Testimonial and facts ----------
    a('\n<!-- 06 One client in their own words (verbatim), with three facts -->')
    a('<section class="dk" aria-label="What clients say" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '56px 0' if m else '72px 0'))
    # no background image (13 Nov, by request): plain navy
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
    # 07 The team, rebuilt 13 Nov by request in the other lanes' pattern (a photo beside the roster of the core team, with each person's
    # role and certification as in Lane G3), in Lane K's mission look: a slanted photo frame, faint target rings, a certification tag and a roster
    a('\n<!-- 07 The team: a photo beside the core-team roster (names, roles and certifications from the Business DNA) -->')
    a('<section id="team" class="lt" aria-label="The team" style="position: relative; overflow: hidden; background: linear-gradient(180deg, #F6F9FC 0%%, %s 100%%); padding: %s">' % (ICE, '64px 0' if m else '100px 0'))
    people = [('Bernard P. Roesch', 'Co-founder &amp; Managing Partner', 'Harvard Business School MBA · Elite-tier QuickBooks ProAdvisor'),
              ('Carol A. Onorato', 'Director of Operations', 'Level 2 Advanced QuickBooks ProAdvisor'),
              ('Robert (Rob) James', 'Prospect pipeline, onboarding &amp; marketing', 'Level 2 Advanced QuickBooks ProAdvisor')]
    roster = ('<div style="display: flex; flex-direction: column"><p style="font: 700 11.5px/1 \'Inter\', sans-serif; letter-spacing: .18em; text-transform: uppercase; color: %s; padding-bottom: 14px">'
              '<span class="cp-s">The core team</span><span class="cp-m">Team roster</span></p>' % MUTED
              + ''.join('<div style="display: grid; grid-template-columns: 34px minmax(0, 1fr); gap: 14px; align-items: start; padding: %s; border-top: 1px solid #D5DFEA">'
                        '<span style="color: %s; padding-top: 2px">%s</span><div style="display: flex; flex-direction: column; gap: 3px">'
                        '<p style="font: 700 17px/1.3 \'Inter\', sans-serif; color: %s">%s</p><p style="font-size: 14px; color: %s">%s</p>'
                        '<p style="font-size: 13px; color: %s">%s</p></div></div>'
                        % ('14px 0' if m else '16px 0', BLUE, ic('target', 26, sw=1.6), INK, n, INK, r, MUTED, c) for n, r, c in people)
              + '<div style="border-top: 1px solid #D5DFEA"></div></div>')
    rings = ('<svg aria-hidden="true" viewBox="0 0 200 200" style="position: absolute; right: %s; bottom: %s; width: %s; height: %s; opacity: .55" fill="none" stroke="#7FD0FF" stroke-width=".8">'
             '<circle cx="100" cy="100" r="96"/><circle cx="100" cy="100" r="62"/><circle cx="100" cy="100" r="28" stroke-dasharray="3 4"/>'
             '<path d="M100 0v40M100 160v40M0 100h40M160 100h40"/></svg>' % (('-80px', '-80px', '240px', '240px') if m else ('-120px', '-120px', '380px', '380px')))
    photo = ('<div style="position: relative; height: %s">'
             '<div class="ph k-ang-clip" style="position: absolute; inset: 0; clip-path: polygon(%s)"><img src="%s" alt="A MISSION advisor at work in the office" style="object-position: 30%% 50%%">'
             '<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(200deg, rgba(6,20,40,0) 40%%, rgba(6,20,40,.55) 100%%)"></div>%s</div>'
             '<div style="position: absolute; left: %s; bottom: %s; background: %s; color: #FFFFFF; padding: 12px 16px; font: 700 11px/1.45 \'Inter\', sans-serif; letter-spacing: .14em; text-transform: uppercase">Advanced-certified<br>QuickBooks ProAdvisors</div></div>'
             % ('300px' if m else '600px', '0 0, 100% 0, 97.5% 100%, 0 100%' if m else '0 0, 100% 0, 96% 100%, 0 100%', IMG['team_photo'], rings, '0' if m else '-1px', '18px' if m else '36px', BLUE))
    txt = ('<div style="display: flex; flex-direction: column; gap: 22px"><p class="eb"><span class="cp-s">Our team</span><span class="cp-m">Your field team</span></p>'
           '<h2 style="font-size: %s"><span class="cp-s">A whole team, not just<br>one bookkeeper.</span><span class="cp-m">A whole team behind<br>every assignment.</span></h2>'
           '<p style="font-size: 17px; max-width: 520px">You get more than one bookkeeper. Our core team holds advanced QuickBooks certifications, and we bring in trusted accountants and specialists from our wider network when your work needs them.</p>'
           '%s<div style="padding-top: 6px">%s</div></div>' % ('44px' if m else '64px', roster, btn('Meet our team', href='#team', icon=False, extra='width: 100%' if m else '')))
    if m:
        a(wrap('<div style="display: flex; flex-direction: column; gap: 30px">%s%s</div>' % (photo, txt)))
    else:
        a(wrap('<div style="display: grid; grid-template-columns: minmax(0, 5fr) minmax(0, 6fr); gap: 72px; align-items: center">%s%s</div>' % (photo, txt)))
    a('</section>')

    # ---------- 08 Strategic partner ----------
    a('\n<!-- 08 More than a bookkeeper: four strengths from the Business DNA, on the globe image -->')
    a('<section class="dk" aria-label="A strategic partner" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '64px 0' if m else '88px 0'))
    # the globe background and its shading were removed (13 Nov, by request); the section is plain deep navy
    st = [('shield', 'QuickBooks experts', 'Advanced-certified QuickBooks ProAdvisors'), ('compass', 'Strategic guidance', 'Advisory and fractional CFO support'),
          ('process', 'A clear process', 'Consultation, onboarding, then monthly work'), ('team', 'Dedicated team', 'Account managers who know your system')]
    sc = ''.join('<div style="display: flex; %s gap: 12px; padding: %s; %s"><span style="color: %s">%s</span><span style="display: flex; flex-direction: column; gap: 4px"><span style="font: 700 16px/1.3 \'Inter\', sans-serif; color: #FFFFFF">%s</span><span style="font-size: 13.5px; color: #AFC0D4">%s</span></span></div>'
                 % ('align-items: center;' if m else 'flex-direction: column; align-items: center; text-align: center;', '14px 0' if m else '0 18px', ('border-top: 1px solid rgba(255,255,255,.14)' if i else '') if m else ('border-left: 1px solid rgba(255,255,255,.16)' if i else ''), BLUE, ic(n, 40, sw=1.5), t, d) for i, (n, t, d) in enumerate(st))
    txt = ('<div style="display: flex; flex-direction: column; gap: 20px"><p class="eb"><span class="cp-s">More than a bookkeeper</span><span class="cp-m">Beyond the books</span></p><h2 class="blue" style="font-size: %s"><span class="cp-s">A strategic partner.</span><span class="cp-m">Your partner in the field.</span></h2>'
           '<p style="font-size: 16.5px; color: #DCE6F2; max-width: 470px">We get the books current and accurate, then take over the recurring bookkeeping and accounting, with QuickBooks set up properly. From there the work can grow into custom reporting, advisory and fractional CFO support.</p></div>' % ('46px' if m else '68px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: %s">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr)', '30px' if m else '48px', txt, 'flex; flex-direction: column' if m else 'grid; grid-template-columns: repeat(4, minmax(0, 1fr))', sc)))
    a('</section>')

    # ---------- 09 Trusted, certified, proven ----------
    # 13 Nov, by request: the three number boxes and the single Elite badge give way to all eight ProAdvisor badges in an endless
    # marquee that runs from the right edge to the left and fades out before it reaches the heading
    a('\n<!-- 09 Trusted. Certified. Proven.: the heading, and all eight ProAdvisor badges in an endless marquee, over the sky -->')
    a('<section class="lt" aria-label="Certified by Intuit" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (ICE, '52px 0' if m else '64px 0'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0; opacity: .28"><img src="%s" alt="" style="object-position: center 30%%"></div>' % IMG['trusted'])
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: linear-gradient(90deg, rgba(237,243,249,.97) 0%, rgba(237,243,249,.8) 100%)"></div>')
    badges = [('5a6f8298d29fe5b417692e04bb5cefb5', 'QuickBooks ProAdvisor Elite badge'), ('1f90e7cd2b6fe11043a8aed199ff3bea', 'Certified Advanced QuickBooks Online ProAdvisor badge'),
              ('8a6858620a6c323d48dea6c25360ff27', 'Certified ProAdvisor, Advanced QuickBooks Desktop badge'), ('bdd1481bd009109078c5f28e16b35880', 'Certified QuickBooks Online ProAdvisor badge'),
              ('cd885cfb7d6c05d7b71c90e8441a681f', 'Certified QuickBooks Level 2 ProAdvisor badge'), ('34b1807ca27f04b30ace3c235cf23ea4', 'Certified QuickBooks Level 1 ProAdvisor badge'),
              ('9eef1fc8b132f5488cb3871c7327a754', 'Certified ProAdvisor, QuickBooks Enterprise badge'), ('39493efadd289f62e0315fad774e3ce0', 'Certified ProAdvisor, Point of Sale badge')]
    bh = 74 if m else 100
    one = lambda hidden: ''.join('<img src="%s%s" alt="%s" style="flex: none; height: %dpx; width: auto; margin-right: %dpx">'
                                 % (B, bid, '' if hidden else alt, bh, 40 if m else 56) for bid, alt in badges)
    track = ('<div class="k-marquee" style="overflow: hidden; -webkit-mask-image: linear-gradient(90deg, transparent 0, #000 %dpx); mask-image: linear-gradient(90deg, transparent 0, #000 %dpx); %s">'
             '<div class="k-track" style="display: flex; align-items: center; width: max-content; padding: 10px 0">%s<span aria-hidden="true" style="display: contents">%s</span></div></div>'
             % (70 if m else 160, 70 if m else 160, 'margin: 0 -20px' if m else 'margin-right: -120px', one(False), one(True)))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">'
           '<h2 class="blue" style="font-size: %s; position: relative; z-index: 1"><span class="cp-s">Trusted.<br>Certified.<br>Proven.</span><span class="cp-m">Trusted.<br>Certified.<br>Cleared.</span></h2>%s</div>'
           % ('flex; flex-direction: column' if m else 'grid; grid-template-columns: auto minmax(0, 1fr)', '22px' if m else '24px', '44px' if m else '52px', track)))
    a('</section>')

    # ---------- 10 FAQ ----------
    a('\n<!-- 10 Questions people ask before the first call (Lane J\'s; the first answer is open) -->')
    a('<section id="faq" class="lt" aria-label="Frequently asked questions" style="position: relative; background: #FFFFFF; padding: %s">' % ('60px 0' if m else '96px 0'))
    qs = ['<span class="cp-s">What happens in the free consultation?</span><span class="cp-m">What happens at the first briefing, the free consultation?</span>', '<span class="cp-s">Do I need to prepare anything?</span><span class="cp-m">Do I need to prepare anything for the briefing?</span>', '<span class="cp-s">Is my business too small for you?</span><span class="cp-m">Is my business too small for you?</span>', '<span class="cp-s">We already have a tax accountant. Does that change anything?</span><span class="cp-m">We already have a tax accountant. Does that change the plan?</span>', '<span class="cp-s">How quickly can you start?</span><span class="cp-m">How quickly can the work start?</span>']
    fq = ''.join('<div><div class="faq" role="button" tabindex="0" aria-expanded="%s">%s<span>%s</span></div>%s</div>'
                 % ('true' if i == 0 else 'false', ic('minus' if i == 0 else 'plus', 18, sw=2.2), qq,
                    '<p style="font-size: 15px; padding: 0 0 18px 32px">It\'s a chat, not a sales pitch. Bernard or Rob will ask how your books are going, look at anything you can share, and tell you what they would fix first.</p>' if i == 0 else '')
                 for i, qq in enumerate(qs))
    txt = ('<div style="display: flex; flex-direction: column; gap: 20px"><p class="eb"><span class="cp-s">Frequently asked questions</span><span class="cp-m">Debriefing</span></p><h2 style="font-size: %s"><span class="cp-s">Got questions?<br>We\'ve got answers.</span><span class="cp-m">Questions before<br>the briefing? Answers.</span></h2>'
           '<p style="font-size: 17px; max-width: 420px"><span class="cp-s">Questions people ask before the first call.</span><span class="cp-m">What people ask before the first briefing.</span></p></div>' % ('44px' if m else '64px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: start">%s<div style="border-bottom: 1px solid #D9E2EC">%s</div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 5fr) minmax(0, 7fr)', '28px' if m else '64px', txt, fq)))
    a('</section>')

    # ---------- 11 Call to action ----------
    a('\n<!-- 11 Your next step: the closing call to action -->')
    a('<section id="schedule" class="dk" aria-label="Your next step" style="position: relative; overflow: hidden; background: %s; padding: %s">' % (NAVY, '72px 0' if m else '96px 0'))
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0"><img src="%s" alt="" style="object-position: %s"></div>' % (IMG['cta'], '75% 40%' if m else 'center 45%'))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: %s"></div>' % ('linear-gradient(180deg, rgba(6,20,40,.85), rgba(6,20,40,.75))' if m else 'linear-gradient(90deg, rgba(6,20,40,.95) 0%, rgba(6,20,40,.8) 45%, rgba(6,20,40,.35) 100%)'))
    txt = ('<div style="display: flex; flex-direction: column; gap: 18px"><p class="eb c" style="color: #FFFFFF"><span class="cp-s">Ready to take control of your books?</span><span class="cp-m">Ready for your briefing?</span></p>'
           '<h2 style="font-size: %s"><span class="cp-s">Your next chapter starts<br>with a conversation.</span><span class="cp-m">Every assignment starts<br>with a briefing.</span></h2>'
           '<p style="font-size: 17px; color: #DCE6F2; max-width: 540px">Book a free call with Bernard or Rob. Come as you are, mess and all. We\'ll tell you what we\'d fix first and what it would take.</p></div>' % ('42px' if m else '64px'))
    a(wrap('<div style="display: %s; gap: %s; align-items: AIX">%s<div style="display: flex; flex-direction: column; gap: 12px; %s">%s<a class="btn btn-o" href="tel:+12032279475"%s>%sCall (203) 227-9475</a></div></div>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 7fr) auto', '28px' if m else '48px', txt, '' if m else 'align-items: stretch',
              btn('Schedule a free consultation', extra='width: 100%' if m else ''), ' style="width: 100%"' if m else '', ic('phone', 16))))
    a('</section>')

    # ---------- 11b From the blog (13 Nov, by request): the three posts Lane J shows, between the call to action and the footer ----------
    a('\n<!-- 11b From the blog: three recent posts -->')
    a('<section id="blog" class="lt" aria-label="From the blog" style="position: relative; overflow: hidden; background: linear-gradient(180deg, #F6F9FC 0%%, %s 100%%); padding: %s">' % (ICE, '60px 0' if m else '96px 0'))
    posts = [('37cbc555ab9573d99c3c204f11469679', '78% 60%', 'QuickBooks', 'QuickBooks Desktop to Online: what actually changes', 'Switching from the desktop version to the online one changes your daily routine. Here\'s what to expect.'),
             ('959f667ae9fbf3a0eb90cf0ce15668ff', 'center 40%', 'Customers', 'QuickBooks Online vs Enterprise: going beyond the basics', 'The big differences show up when you track stock, orders and where things are kept.'),
             ('c7127cc17cfd8909184853095227a34d', 'center 40%', 'Technology', 'Is automated accounting software the future of financial accounting?', 'Software can do the boring, repeat work. People still make the judgment calls. Here\'s what that means for you.')]
    pc = ''.join(
        '<a class="card" href="#blog" style="display: flex; flex-direction: column; overflow: hidden">'
        '<div class="ph" style="height: %s"><img src="%s%s" alt="" style="object-position: %s"></div>'
        '<div style="display: flex; flex-direction: column; gap: 10px; padding: 18px 22px 22px; flex: 1">'
        '<span style="align-self: flex-start; font: 700 11px/1 \'Inter\', sans-serif; letter-spacing: .06em; padding: 6px 9px; border-radius: 3px; background: #E3F1FF; color: #0B5FA8">%s</span>'
        # titles in sentence case, in the case-study title style (13 Nov, by request), instead of the condensed capitals
        '<h3 class="k-cs-t">%s</h3><p style="font-size: 14px; line-height: 1.55">%s</p>'
        '<span class="go" style="margin-top: auto; align-self: flex-end; display: inline-flex">%s</span></div></a>'
        % ('190px' if m else '210px', B, bid, pos, tag, t, d, ic('arrow', 20)) for bid, pos, tag, t, d in posts)
    head = ('<div style="display: flex; %s gap: 20px; margin-bottom: %s">'
            '<div style="display: flex; flex-direction: column; gap: 18px"><p class="eb"><span class="cp-s">From the blog</span><span class="cp-m">Field notes</span></p><h2 style="font-size: %s"><span class="cp-s">Simple answers to the%squestions we hear most.</span><span class="cp-m">Field intel on the questions we hear most.</span></h2>'
            '<p style="font-size: 16px">300+ articles on QuickBooks, bookkeeping, accounting and financial planning.</p></div>'
            '<a class="btn btn-o" href="#blog" style="flex: none%s">Read all articles%s</a></div>'
            % ('flex-direction: column; align-items: stretch;' if m else 'align-items: flex-end; justify-content: space-between;', '30px' if m else '44px', '42px' if m else '60px', ' ' if m else '<br>', '' if m else '', '<span class="ar" style="display: inline-flex">%s</span>' % ic('arrow', 16)))
    a(wrap(head + '<div style="display: grid; grid-template-columns: %s; gap: %s">%s</div>' % ('1fr' if m else 'repeat(3, minmax(0, 1fr))', '16px' if m else '22px', pc)))
    a('</section>')

    # ---------- 12 Footer ----------
    a('\n<!-- 12 Footer: logo, four link columns, contact and the button -->')
    a('<footer id="contact" class="dk foot" style="position: relative; overflow: hidden; background: #040E1D; padding: %s">' % ('52px 0 28px' if m else '72px 0 32px'))
    # blurred like the services photo, under the same light navy overlay (13 Nov, by request)
    a('<div class="ph" aria-hidden="true" style="position: absolute; inset: 0; opacity: .35"><img src="%s" alt="" style="filter: blur(%s); transform: scale(1.08)"></div>' % (IMG['footer'], '8px' if m else '12px'))
    a('<div aria-hidden="true" style="position: absolute; inset: 0; background: rgba(6,20,40,.22)"></div>')
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
    # the email sign-up at the top of the footer (13 Nov, by request: it was missing), as on Lane J, with the real copy
    eid = 'nl-email-km' if m else 'nl-email-k'
    sub = ('<form class="nl-card" style="display: %s; gap: %s; align-items: AIX; padding: %s; margin-bottom: %s; border-radius: 8px; background: rgba(255,255,255,.05); border: 1px solid rgba(255,255,255,.12)">'
           '<div style="display: flex; flex-direction: column; gap: 8px"><p class="eb c"><span class="cp-s">Stay in the know</span><span class="cp-m">Stay briefed</span></p><h2 style="font-size: %s"><span class="cp-s">QuickBooks tips by email</span><span class="cp-m">QuickBooks intel by email</span></h2>'
           '<p style="font-size: 15px; color: #C9D6E8">Simple answers to the questions business owners ask us most. No sales emails.</p></div>'
           '<div><label for="%s" class="sr">Email address</label>'
           '<div class="nl-field" style="display: flex; align-items: center; gap: 6px; padding: 6px; border-radius: 6px; background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.2)">'
           '<input id="%s" type="email" placeholder="%s" style="flex: 1; min-width: 0; height: 46px; box-sizing: border-box; background: transparent; border: 0; outline: 0; color: #FFFFFF; font-family: inherit; font-size: 15px; padding: 0 12px">'
           '<button class="btn" type="submit" style="flex: none; height: 46px; padding: 0 %s">Subscribe<span class="ar" style="display: inline-flex">%s</span></button></div></div></form>'
           % ('flex; flex-direction: column; align-items: stretch' if m else 'grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr)', '20px' if m else '48px', '24px 20px' if m else '34px 40px', '40px' if m else '56px',
              '34px' if m else '44px', eid, eid, 'Email address' if m else 'Your email address', '16px' if m else '22px', ic('arrow', 16)))
    a(wrap(sub + grid + bottom))
    a('</footer>')

    # stacked layouts stretch their children on mobile (centred, they shrank to their content and the mission photo vanished)
    body = '\n'.join(A).replace('align-items: AIX', 'align-items: stretch' if m else 'align-items: center')
    # case studies and services swap places (13 Nov, by request): case studies now follow The mission, services follow Who we serve
    def _cut(b, mark):
        i = b.index(mark); k = b.index('</section>', i) + len('</section>'); return b[i:k]
    cs, sv = _cut(body, '<!-- 05 Case studies'), _cut(body, '<!-- 03 Services')
    body = body.replace(sv, '@@SV@@').replace(cs, sv).replace('@@SV@@', cs)
    fonts = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:ital,wght@1,700;1,800&amp;family=Inter:wght@400;500;600;700&amp;display=swap">')
    title = 'Lane K homepage, %s' % ('mobile' if m else 'desktop')
    # review bar (13 Nov, by request): Angles on/off and eyebrow lines Fuse/None, kept in step across the Lane K boards
    bar = ('<div class="tg-bar" aria-label="Review control, not part of the design">'
           '<span class="tg-label">Review ·</span>'
           '<span style="display: inline-flex; align-items: center; gap: 8px"><span class="tg-label">Angles</span><span class="tg-group" role="group" aria-label="Angles">'
           '<button type="button" class="tg-opt" aria-pressed="{{ isAngOn }}" onClick="{{ setAngOn }}">On</button>'
           '<button type="button" class="tg-opt" aria-pressed="{{ isAngOff }}" onClick="{{ setAngOff }}">Off</button></span></span>'
           '<span style="display: inline-flex; align-items: center; gap: 8px"><span class="tg-label">Eyebrow lines</span><span class="tg-group" role="group" aria-label="Eyebrow lines">'
           '<button type="button" class="tg-opt" aria-pressed="{{ isEbFuse }}" onClick="{{ setEbFuse }}">Fuse</button>'
           '<button type="button" class="tg-opt" aria-pressed="{{ isEbNone }}" onClick="{{ setEbNone }}">None</button></span></span>'
           '<span style="display: inline-flex; align-items: center; gap: 8px"><span class="tg-label">Copy</span><span class="tg-group" role="group" aria-label="Copy">'
           '<button type="button" class="tg-opt" aria-pressed="{{ isCopyStd }}" onClick="{{ setCopyStd }}">Standard</button>'
           '<button type="button" class="tg-opt" aria-pressed="{{ isCopyMis }}" onClick="{{ setCopyMis }}">Mission</button></span></span>'
           '</div>')
    head = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<title>%s</title>\n<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n%s\n<style>%s</style>\n</helmet>\n'
            '<div class="lk" data-angles="{{ angMode }}" data-eb="{{ ebMode }}" data-copy="{{ copyMode }}" style="width: %dpx; background: %s">\n%s\n%s\n</div>\n</x-dc>\n'
            '<script type="text/x-dc" data-dc-script data-props=\'{"$preview":{"width":%d,"height":8000}}\'>\n'
            % (title, fonts, CSS + svcss(m), W, NAVY, bar, body, W))
    return head + SCRIPT.replace('SVN', str(svpos(m))) + '</script>\n</body>\n</html>\n'


SCRIPT = r"""class Component extends DCLogic {
  // the case-study carousel: which card is highlighted (desktop) or shown (mobile)
  go(i) { this.setState({ cs: (i + 3) % 3 }); }
  // the services carousel: SVN stops (4 cards in view on desktop, 1 on mobile)
  sgo(i) { this.setState({ sv: (i + SVN) % SVN }); }
  // the review switches (angles on/off, eyebrow lines fuse/none), shared with the other Lane K boards
  setAng(v) {
    this.setState({ ang: v });
    try { if (this.ch) this.ch.postMessage({ ang: v }); } catch (e) {}
  }
  setEb(v) {
    this.setState({ eb: v });
    try { if (this.ch) this.ch.postMessage({ eb: v }); } catch (e) {}
  }
  setCopy(v) {
    this.setState({ copy: v });
    try { if (this.ch) this.ch.postMessage({ copy: v }); } catch (e) {}
  }
  componentDidMount() {
    try {
      this.ch = new BroadcastChannel('mission-buttons-lane-k');
      this.ch.onmessage = (e) => {
        if (e.data && e.data.ang) this.setState({ ang: e.data.ang });
        if (e.data && e.data.eb) this.setState({ eb: e.data.eb });
        if (e.data && e.data.copy) this.setState({ copy: e.data.copy });
      };
    } catch (e) {}
  }
  componentWillUnmount() {
    try { if (this.ch) this.ch.close(); } catch (e) {}
  }
  renderVals() {
    const c = (this.state && this.state.cs) || 0;
    const v = (this.state && this.state.sv) || 0;
    const ang = (this.state && this.state.ang) || 'on';
    const eb = (this.state && this.state.eb) || 'fuse';
    const cp = (this.state && this.state.copy) || 'mission';
    this.sg = this.sg || [];
    const sv = { svPos: String(v), svPrev: this.sp || (this.sp = () => this.sgo(((this.state && this.state.sv) || 0) - 1)), svNext: this.sn || (this.sn = () => this.sgo(((this.state && this.state.sv) || 0) + 1)) };
    for (let i = 0; i < SVN; i++) { sv['svOn' + i] = v === i ? 'true' : 'false'; sv['svGo' + i] = this.sg[i] || (this.sg[i] = () => this.sgo(i)); }
    return {
      ...sv,
      angMode: ang, isAngOn: ang === 'on' ? 'true' : 'false', isAngOff: ang === 'off' ? 'true' : 'false',
      setAngOn: this.a1 || (this.a1 = () => this.setAng('on')), setAngOff: this.a0 || (this.a0 = () => this.setAng('off')),
      ebMode: eb, isEbFuse: eb === 'fuse' ? 'true' : 'false', isEbNone: eb === 'none' ? 'true' : 'false',
      setEbFuse: this.e1 || (this.e1 = () => this.setEb('fuse')), setEbNone: this.e0 || (this.e0 = () => this.setEb('none')),
      copyMode: cp, isCopyStd: cp === 'standard' ? 'true' : 'false', isCopyMis: cp === 'mission' ? 'true' : 'false',
      setCopyStd: this.c0 || (this.c0 = () => this.setCopy('standard')), setCopyMis: this.c1 || (this.c1 = () => this.setCopy('mission')),
      csOn0: c === 0 ? 'true' : 'false', csOn1: c === 1 ? 'true' : 'false', csOn2: c === 2 ? 'true' : 'false',
      csGo0: this.g0 || (this.g0 = () => this.go(0)), csGo1: this.g1 || (this.g1 = () => this.go(1)), csGo2: this.g2 || (this.g2 = () => this.go(2)),
      csPrev: this.gp || (this.gp = () => this.go(((this.state && this.state.cs) || 0) - 1)),
      csNext: this.gn || (this.gn = () => this.go(((this.state && this.state.cs) || 0) + 1)),
    };
  }
}
"""

os.makedirs(OUT, exist_ok=True)
for m, name in [(False, 'lane-k-home.dc.html'), (True, 'lane-k-home-mobile.dc.html')]:
    open(os.path.join(OUT, name), 'w').write(build(m))
    print('wrote', os.path.join(OUT, name))
