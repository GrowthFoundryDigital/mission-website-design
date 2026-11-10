# Usage: python3 tools/lane-j-morph.py <lane-j board> <lane-c3 board, same device> <out board>  (after tools/lane-j-gen.py)
# Lane J, morph pass (8 Nov, by request: "morph the design and style of H2 and C3", not H2 re-skinned).
# Runs on the boards written by lane-j-gen.py and takes from the C3 boards:
#   type     H2's Space Grotesk headings, C3's Plus Jakarta Sans for body text
#   corners  10px on cards and photos with C3's soft shadows; buttons stay crisp (4px)
#   dark     C3's navy with its blue glow for the dark content sections; near-black only for the footer and the hero strip
#   layouts  C3's case-study section (featured story, story list, navy call-out card, more stories) and C3's
#            "When people usually call us" cells with the lime wipe; everything else keeps H2's layout
import re, sys
jf, cf, out = sys.argv[1:4]
j = open(jf).read(); c = open(cf).read()

def section(s, start):
    i = s.index(start); k = s.index('</section>', i) + len('</section>')
    return i, k
def port(block):
    block = block.replace('{{ primary }}', 'var(--eb)').replace('#0A7FD0', 'var(--eb)')
    block = re.sub(r'(<h[23] style="[^"]*?)font-weight: 800', r'\1font-weight: 600', block)
    block = re.sub(r'(class="tg-btn[^"]*" [^>]*?)border-radius: 12px', r'\1border-radius: 4px', block)
    return block

# H2's "Do your books look like this?" band, kept from J's own case-study section before C3's replaces it (10 Nov, by request)
_b = j.index('<div class="bl-band"'); _e = j.index('</a>', _b) + len('</a>')
_e = j.index('</div>', _e) + len('</div>')
band = j[_b:_e]
assert band.count('<div') == band.count('</div>') and 'Do your books look like this?' in band, band[:200]
# 1. layouts from C3
for jstart, cstart in [('<!-- 02 Case studies', '<!-- 01b Case studies'), ('<!-- 06 The six moments', '<!-- 04b Triggers'),
                       ('<!-- 05 Services', '<!-- 05 Services carousel')]:  # services from C3 too (8 Nov, by request)
    a, b = section(j, jstart); x, y = section(c, cstart)
    j = j[:a] + '<!-- from Lane C3 (Lane J morph) -->\n' + port(c[x:y]) + j[b:]

# case studies (10 Nov, by request): C3's navy "Do your books look like this?" card leaves the story column, H2's blue band closes the
# section instead (after the placeholder tiles, as on H2), and the featured story's photo may shrink so the featured card ends level
# with the three stories beside it (the two columns start and end together)
a = j.index('<!-- from Lane C3 (Lane J morph) -->\n<!-- 01b Case studies'); b = j.index('</section>', a)
sec = j[a:b]
k = sec.index('<div style="background: radial-gradient(55% 70% at 88% 18%, rgba(10, 127, 208, 0.30)')
ke = sec.index('</div>', k) + len('</div>')
assert 'Do your books look like this?' in sec[k:ke] and sec[k:ke].count('<div') == 1, sec[k:ke][:300]
sec = sec[:k].rstrip('\n') + '\n' + sec[ke:].lstrip('\n')
if 'min-height: 400px' in sec:
    assert sec.count('class="hv-feat-ph" style="position: relative; flex: 1; min-height: 400px"') == 1
    sec = sec.replace('class="hv-feat-ph" style="position: relative; flex: 1; min-height: 400px"', 'class="hv-feat-ph" style="position: relative; flex: 1; min-height: 240px"')
end = sec.rindex('</div>')
sec = sec[:end] + band + '\n' + sec[end:]
j = j[:a] + sec + j[b:]

# C3's order: the triggers (ice blue) sit between "who we are" and the services carousel, so the two navy sections never touch
m1 = '<!-- from Lane C3 (Lane J morph) -->\n<!-- 05 Services carousel'; m2 = '<!-- from Lane C3 (Lane J morph) -->\n<!-- 04b Triggers'
a = j.index(m1); b = j.index('</section>', a) + len('</section>'); svc = j[a:b]; j = j[:a] + j[b:]
a = j.index(m2); b = j.index('</section>', a) + len('</section>'); j = j[:b] + '\n\n' + svc + j[b:]

# 2. the C3 hover styles those sections use (case-study rows, featured photo zoom, the lime wipe cells, the highlighter links)
ccss = c[c.index('<style>') + 7:c.index('</style>')].split('\n')
keep = [l for l in ccss if re.search(r'hv-feat|hv-row|hv-cell|\.hl\b|hl-ink|hv-arrow|hv-card|hv-circ', l) and not l.lstrip().startswith(('/*', 'the letters'))]
keep = [l.replace('[style*="#0A7FD0"]', '[style*="var(--eb)"]') for l in keep]
morph_css = '''
/* ---------- Lane J morph (8 Nov): H2 x C3 ---------- */
/* type: H2 headings, C3 body */
.lj{font-family:'Plus Jakarta Sans','Helvetica Neue',Arial,sans-serif}
/* corners: 10px cards and photos with soft shadows; buttons stay crisp */
.lj .card{border-radius:10px;box-shadow:0 10px 28px rgba(10,34,64,.06)}
.lj .ph{border-radius:10px}
/* dark sections: C3 navy with its blue glow; the footer and the hero strip stay near-black */
.lj .dk{background:radial-gradient(55% 70% at 88% 18%,rgba(10,127,208,.30) 0%,rgba(10,127,208,0) 70%),radial-gradient(45% 60% at 0% 100%,rgba(124,196,248,.10) 0%,rgba(124,196,248,0) 70%),#0A2240}
.lj .foot,.lj .bl .dk{background:#101419}
/* hovers from C3 for the ported sections */
''' + '\n'.join(keep) + '\n'
i = j.index('</style>'); j = j[:i] + morph_css + j[i:]

# the services carousel's arrows (desktop): the same scroll helper C3 uses
if '{{ prev }}' in j:
    j = j.replace('class Component extends DCLogic {\n', "class Component extends DCLogic {\n  scrollCards(dir) {\n    // one card plus its gap per click (C3's services carousel)\n    if (this.track) this.track.scrollBy({ left: dir * 300, behavior: 'smooth' });\n  }\n", 1)
    j = j.replace('  renderVals() {\n    return {\n', "  renderVals() {\n    return {\n      setTrack: this.setTrack || (this.setTrack = (el) => { this.track = el; }),\n      prev: this.prev || (this.prev = () => this.scrollCards(-1)),\n      next: this.next || (this.next = () => this.scrollCards(1)),\n", 1)
    assert 'scrollCards(dir)' in j and 'setTrack:' in j

# 3. fonts and corners across the page
j = j.replace('family=Open+Sans:wght@400;600', 'family=Plus+Jakarta+Sans:wght@400;500;600;700;800')
j = j.replace("'Open Sans'", "'Plus Jakarta Sans'")
j = j.replace('border-radius: 6px', 'border-radius: 10px')
j = re.sub(r'(class="ph" style="[^"]*?)border-radius: 4px', r'\1border-radius: 10px', j)
# 4. details: the hero menu stays on one line in the wider body font; testimonial and service cards suit the navy;
#    the case-study intro line stays removed, as on the other lanes (review comments, 29 Oct)
j = j.replace('<div style="display: flex; align-items: center; gap: 30px"><a href="#services">', '<div style="display: flex; align-items: center; gap: 26px; white-space: nowrap"><a href="#services">')
j = j.replace('border-radius: 10px; background: #1B2029"', 'border-radius: 10px; background: rgba(255, 255, 255, 0.06); border: 1px solid rgba(255, 255, 255, 0.10)"')
j = j.replace('class="card" style="background: #101419; border-color: #101419;', 'class="card" style="background: #0A2240; border-color: #0A2240;')
j, n = re.subn(r'<p [^>]*>(?:Real stories from our blog\. )?Each one shows the problem a business had and how we set up QuickBooks to fix it\.</p>', '', j)
assert n == 1, n
# 5. hovers (8 Nov, by request): no fill on the case-study rows; one lime text-link wipe everywhere (C3's highlighter links,
#    the rows' "Read the story", blog titles); no lime on non-text hovers (cells, industry rows, the who-we-are list)
j = j.replace('</style>', """/* the review switches stay at the top while the page scrolls (8 Nov, by request) */
.lj .tg-bar{position:sticky;top:0;z-index:100}
/* case studies (8 Nov, by request): no fill on the story rows at all (lime, then light blue, then navy were tried); the row does not
   slide (an H2 hover rule shares the hv-row class) and only the caret nudges; its "Read the story" takes the text-link wipe below */
.lj #case-studies .hv-row{background:none !important;transform:none !important}
.lj #case-studies .hv-row:hover [style*="var(--eb)"],.lj #case-studies .hv-row:focus-visible [style*="var(--eb)"]{color:var(--eb) !important}
.lj #case-studies .hv-row:hover h3,.lj #case-studies .hv-row:focus-visible h3{color:#0A2240}
/* one text-link hover across the page (8 Nov, by request): every text link gets the lime square wipe of "Not on the list? Schedule a
   free consultation": left to right, 8px past each end, the words inking near-black as it reaches them. C3's hand-drawn highlighter
   links take it, as do the "Read the story" lines in the case-study rows and the blog titles (when the card is hovered) */
.lj .hl{background-image:none !important;padding:0;margin:0;position:relative;isolation:isolate;text-decoration-color:currentColor;transition:text-decoration-color .3s ease}
.lj .hl::before,.lj #case-studies .hv-row > span > span:last-child::before{content:'';position:absolute;top:-5px;bottom:-5px;left:-8px;right:-8px;z-index:-1;background:#C1F432;transform:scaleX(0);transform-origin:left center;transition:transform .45s cubic-bezier(.22,.61,.36,1);pointer-events:none}
.lj a.hl:hover::before,.lj a.hl:focus-visible::before,.lj #case-studies .hv-row:hover > span > span:last-child::before,.lj #case-studies .hv-row:focus-visible > span > span:last-child::before{transform:scaleX(1)}
.lj a.hl:hover,.lj a.hl:focus-visible{text-decoration-color:transparent !important}
/* a link inside a sentence keeps the block tight, so it does not cover the next word */
.lj p > .hl::before{left:-3px;right:-3px;top:-2px;bottom:-2px}
.lj .hl-ink{background-image:linear-gradient(90deg,#101419 50%,currentColor 50%);transition:background-position .45s cubic-bezier(.22,.61,.36,1) .03s}
.lj a.hl:hover svg,.lj a.hl:focus-visible svg{color:#101419 !important;transition:transform .4s cubic-bezier(.22,.61,.36,1),color .15s ease .3s}
.lj #case-studies .hv-arrow:hover,.lj #case-studies .hv-arrow:focus-visible{text-decoration:none !important}
.lj #case-studies .hv-row > span > span:last-child{align-self:flex-start;position:relative;isolation:isolate;transition:color .2s ease .15s,text-decoration-color .3s ease}
.lj #case-studies .hv-row:hover > span > span:last-child,.lj #case-studies .hv-row:focus-visible > span > span:last-child{color:#101419 !important;text-decoration-color:transparent !important}
/* blog titles: the same wipe, as one continuous pass across wrapped lines */
.lj .post .tw{background:linear-gradient(#C1F432,#C1F432) no-repeat 0 0/0% 100%;padding:1px 8px;margin:0 -8px;-webkit-box-decoration-break:slice;box-decoration-break:slice;transition:background-size .6s cubic-bezier(.22,.61,.36,1)}
.lj .post:hover .tw{background-size:100% 100%}
.lj .post:hover h3{color:#101419}
/* no lime on hover except text links and buttons (8 Nov, by request): the "When people usually call us" cells, the industry rows
   and the "who we are" list keep their other hovers but lose the lime */
.lj .hv-cell{background:none !important}
.lj .hv-cell:hover h3{color:inherit !important}
.lj .hv-ind::before{display:none}
.lj .hv-li:hover{border-top-color:rgba(255,255,255,.14) !important}
.lj .hv-li:hover .ic{color:var(--eb)}
.lj .dk .hv-li:hover .ic{color:var(--eb-lt)}
@media (prefers-reduced-motion: reduce){.lj .hl::before,.lj .post .tw,.lj #case-studies .hv-row > span > span:last-child::before{transition:none}}
/* footer call to action centred in the band (8 Nov, by request: too much empty space on the right; Mobbin references:
   Figma, Coda, Podia, Homerun) */
.lj #schedule > div{align-items:center;text-align:center}
.lj #schedule > div > p:not(.eb){margin-left:auto;margin-right:auto}
.lj #schedule > div > div{justify-content:center}
/* mobile: the buttons stay full width */
.lj #schedule > div > div[style*="flex-direction: column"]{align-self:stretch}
/* pointer cursor on everything with a hover effect that is not a link (9 Nov, by request; the other lanes get it from tools/cursor-pack.py) */
.lh .qcard,.lh .post,.lh .hv-ind,.lh .hv-li,.hv-feat,.hv-card,.hv-cell{cursor:pointer}
/* the Office hero photo (10 Nov) has its subject on the left, behind the headline: mirrored so she sits in the open side */
.lj .hero-bg-office{transform:scaleX(-1)}
/* Font review switch (8 Nov): C3 (Plus Jakarta Sans throughout; the default) or H2 (Space Grotesk headings + Open Sans) */
.lj[data-font="h2"]{font-family:'Open Sans','Helvetica Neue',Arial,sans-serif}
.lj[data-font="c3"] *:not(.tg-bar):not(.tg-bar *){font-family:'Plus Jakarta Sans','Helvetica Neue',Arial,sans-serif !important}
.lj[data-font="c3"] h1,.lj[data-font="c3"] h2,.lj[data-font="c3"] h3{font-weight:800 !important;letter-spacing:-.03em}
</style>""", 1)
j = j.replace('&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800', '&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Open+Sans:wght@400;600', 1)
j = j.replace('data-geo="off" class="lh lj"', 'data-geo="off" data-font="{{ fontMode }}" class="lh lj"', 1)
bar = j.index('class="tg-bar"'); k = j.index('<span></span>\n</div>', bar)
j = j[:k] + ('<span style="display: inline-flex; align-items: center; gap: 8px"><span class="tg-label">Font</span><span class="tg-group" role="group" aria-label="Font">'
             '<button type="button" class="tg-opt" aria-pressed="{{ isFontC3 }}" onClick="{{ setFontC3 }}">C3</button>'
             '<button type="button" class="tg-opt" aria-pressed="{{ isFontH2 }}" onClick="{{ setFontH2 }}">H2</button></span></span>\n') + j[k:]
j = j.replace('class Component extends DCLogic {\n', """class Component extends DCLogic {
  setFont(v) {
    // the font switch (h2 or c3), shared with the other Lane J board
    this.setState({ font: v });
    try { if (this.btnChannel) this.btnChannel.postMessage({ font: v }); } catch (e) {}
  }
""", 1)
j = j.replace("        if (e.data && e.data.blue) this.setState({ blue: e.data.blue });\n", "        if (e.data && e.data.blue) this.setState({ blue: e.data.blue });\n        if (e.data && e.data.font) this.setState({ font: e.data.font });\n", 1)
j = j.replace("  renderVals() {\n    return {\n", """  renderVals() {
    return {
      fontMode: (this.state && this.state.font) || 'c3',
      isFontH2: ((this.state && this.state.font) || 'c3') === 'h2' ? 'true' : 'false',
      isFontC3: ((this.state && this.state.font) || 'c3') === 'c3' ? 'true' : 'false',
      setFontH2: this.setFontH2 || (this.setFontH2 = () => this.setFont('h2')),
      setFontC3: this.setFontC3 || (this.setFontC3 = () => this.setFont('c3')),
""", 1)
assert 'setFontC3' in j and 'data-font=' in j and 'aria-label="Font"' in j
# 6. lime buttons are final (8 Nov, client decision): the button colour switch goes and the page is always in green mode
j = j.replace('data-btn="{{ btnMode }}"', 'data-btn="green"', 1)
k = j.index('<span class="tg-label">Review · '); e = j.index('</div>', k) + len('</div>')
assert 'aria-label="Button color"' in j[k:e]
j = j[:k] + '<span class="tg-label">Review ·</span>' + j[e:]
# "What we do": its 8px gap above is a margin, not padding, so the lime wipe hugs the words (8 Nov, by request)
j = j.replace('<a class="lk" href="#services" style="padding-top: 8px">', '<a class="lk" href="#services" style="margin-top: 8px">', 1)
assert '<a class="lk" href="#services" style="margin-top: 8px">' in j
# mobile hero (8 Nov, by request: too much space at the bottom): the photo strip under the hero copy goes (with the divider off it
# was an empty 270px window onto the background photo); the copy ends 44px above the services list, and the shade over the
# photo stays dark to the bottom so the reviews line keeps its contrast
if '<div class="hero-band" style=' in j:
    j = j.replace('</style>', """/* mobile hero without the empty photo strip (8 Nov) */
.lj .hero-band{display:none}
.lj #top{padding-bottom:44px !important}
.lj .hero-full > div{background:linear-gradient(180deg,rgba(16,20,25,.82) 0%,rgba(16,20,25,.74) 60%,rgba(16,20,25,.62) 100%) !important}
</style>""", 1)
# the hero eyebrow stays white (it was Electric Blue briefly on 10 Nov, then changed back by request)
# no "Who we are" section on J (10 Nov, by request); its "About" links (header, footer, "Meet the team") now go to the team section
a = j.index('<!-- 04 Positioning'); b = j.index('</section>', a) + len('</section>')
assert 'id="about"' in j[a:b] and j[a:b].count('<section') == 1
j = j[:a].rstrip('\n') + '\n\n' + j[b:].lstrip('\n')
assert j.count('<section aria-label="The team" ') == 1
j = j.replace('<section aria-label="The team" ', '<section id="team" aria-label="The team" ', 1)
j = j.replace('href="#about"', 'href="#team"')
# greys instead of the light blue (10 Nov, by request: "copy H2 using greys"): H2's chalk grey #F5F6F7 and white replace C3's ice
# blue, in H2's rhythm: case studies grey, "When people usually call us" white (as on H2), certified and the questions grey; the
# ice-blue service card becomes grey and the blue-grey dividers become H2's grey. The sky-blue cards and text on navy stay
j = j.replace('aria-label="Case studies" style="position: relative; overflow: hidden; background: #E8F3FD"', 'aria-label="Case studies" style="position: relative; overflow: hidden; background: #F5F6F7"', 1)
j = j.replace('<!-- 04b Triggers -->\n<section style="position: relative; overflow: hidden; background: #E8F3FD">', '<!-- 04b Triggers -->\n<section style="position: relative; overflow: hidden; background: #FFFFFF">', 1)
j = j.replace('.lj .ch,.lj .ice{background:#E8F3FD}', '.lj .ch,.lj .ice{background:#F5F6F7}', 1)
j = j.replace('background: #E8F3FD', 'background: #F5F6F7')
j = j.replace('#DCE7F3', '#E2E5EA')
assert '#E8F3FD' not in j, [m.start() for m in re.finditer('#E8F3FD', j)][:5]
# blog titles: an inline wrapper for the text-link wipe (8 Nov, by request)
j, n = re.subn(r'(<article class="post"[^\n]*?<h3 [^>]*>)([^<]+)(</h3>)', r'\1<span class="tw">\2</span>\3', j)
assert n == 3, n
open(out, 'w').write(j)
print('morphed', out)
