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

# 1. layouts from C3
for jstart, cstart in [('<!-- 02 Case studies', '<!-- 01b Case studies'), ('<!-- 06 The six moments', '<!-- 04b Triggers'),
                       ('<!-- 05 Services', '<!-- 05 Services carousel')]:  # services from C3 too (8 Nov, by request)
    a, b = section(j, jstart); x, y = section(c, cstart)
    j = j[:a] + '<!-- from Lane C3 (Lane J morph) -->\n' + port(c[x:y]) + j[b:]

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
# 5. no lime in the case studies (8 Nov, by request): the story rows keep C3's left-to-right wipe, in navy instead of lime,
#    and do not slide sideways (an H2 hover rule shares the hv-row class);
#    one text-link hover everywhere (8 Nov, by request): C3's highlighter links take H2's square wipe
j = j.replace('</style>', """/* the review switches stay at the top while the page scrolls (8 Nov, by request) */
.lj .tg-bar{position:sticky;top:0;z-index:100}
/* case studies without lime (8 Nov): the story rows fill navy from left to right (light blue blended into the section, 8 Nov),
   and the words turn light as the navy passes them */
.lj #case-studies .hv-row{background:linear-gradient(#0A2240,#0A2240) no-repeat 0 0/0% 100% !important;transition:background-size .5s cubic-bezier(.22,.61,.36,1)}
.lj #case-studies .hv-row:hover,.lj #case-studies .hv-row:focus-visible{background-size:100% 100% !important;transform:none}
.lj #case-studies .hv-row [style*="color"]{transition:color .3s ease .12s}
.lj #case-studies .hv-row:hover [style*="color: #0A2240"],.lj #case-studies .hv-row:focus-visible [style*="color: #0A2240"],.lj #case-studies .hv-row:hover h3,.lj #case-studies .hv-row:focus-visible h3{color:#FFFFFF !important}
.lj #case-studies .hv-row:hover [style*="color: #3B4A63"],.lj #case-studies .hv-row:focus-visible [style*="color: #3B4A63"]{color:#C9D6E8 !important}
.lj #case-studies .hv-row:hover [style*="var(--eb)"],.lj #case-studies .hv-row:focus-visible [style*="var(--eb)"]{color:#7CC4F8 !important}
/* one text-link hover across the page (8 Nov, by request): the square wipe the "What we do" links use, left to right, 8px past each end,
   in place of C3's hand-drawn highlighter; lime on the page, navy in the case studies */
.lj .hl{background-image:none !important;padding:0;margin:0;position:relative;isolation:isolate;text-decoration-color:currentColor;transition:text-decoration-color .3s ease}
.lj .hl::before{content:'';position:absolute;top:-5px;bottom:-5px;left:-8px;right:-8px;z-index:-1;background:#C1F432;transform:scaleX(0);transform-origin:left center;transition:transform .45s cubic-bezier(.22,.61,.36,1);pointer-events:none}
.lj a.hl:hover::before,.lj a.hl:focus-visible::before{transform:scaleX(1)}
/* a link inside a sentence keeps the block tight, so it does not cover the next word */
.lj p > .hl::before{left:-3px;right:-3px;top:-2px;bottom:-2px}
.lj a.hl:hover,.lj a.hl:focus-visible{text-decoration-color:transparent !important}
.lj .hl-ink{background-image:linear-gradient(90deg,#101419 50%,currentColor 50%);transition:background-position .45s cubic-bezier(.22,.61,.36,1) .03s}
.lj a.hl:hover svg,.lj a.hl:focus-visible svg{color:#101419 !important;transition:transform .4s cubic-bezier(.22,.61,.36,1),color .15s ease .3s}
.lj #case-studies .hl::before{background:#0A2240}
.lj #case-studies .hl-ink{background-image:linear-gradient(90deg,#FFFFFF 50%,currentColor 50%)}
.lj #case-studies a.hl:hover svg,.lj #case-studies a.hl:focus-visible svg{color:#FFFFFF !important}
.lj #case-studies .hv-arrow:hover,.lj #case-studies .hv-arrow:focus-visible{text-decoration:none !important}
@media (prefers-reduced-motion: reduce){.lj .hl::before,.lj #case-studies .hv-row [style*="color"]{transition:none}}
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
open(out, 'w').write(j)
print('morphed', out)
