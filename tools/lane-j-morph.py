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
# 5. no lime in the case studies (8 Nov, by request): the story rows get a light ice-blue hover instead of the lime wipe,
#    and the section's links lose the highlighter (they underline, and the arrow moves)
j = j.replace('</style>', """/* the review switches stay at the top while the page scrolls (8 Nov, by request) */
.lj .tg-bar{position:sticky;top:0;z-index:100}
/* case studies without lime (8 Nov) */
.lj #case-studies .hv-row{background:transparent !important;transition:background-color .3s ease}
.lj #case-studies .hv-row:hover,.lj #case-studies .hv-row:focus-visible{background:#F2F8FE !important}
.lj #case-studies .hv-row:hover [style*="var(--eb)"],.lj #case-studies .hv-row:focus-visible [style*="var(--eb)"]{color:var(--eb) !important}
.lj #case-studies .hl{background-image:none !important}
.lj #case-studies .hl-ink{background:none !important;-webkit-text-fill-color:currentColor !important}
.lj #case-studies a.hl svg{color:inherit !important}
/* Font review switch (8 Nov): H2 (Space Grotesk headings + Open Sans; the default) or C3 (Plus Jakarta Sans throughout) */
.lj[data-font="h2"]{font-family:'Open Sans','Helvetica Neue',Arial,sans-serif}
.lj[data-font="c3"] *:not(.tg-bar):not(.tg-bar *){font-family:'Plus Jakarta Sans','Helvetica Neue',Arial,sans-serif !important}
.lj[data-font="c3"] h1,.lj[data-font="c3"] h2,.lj[data-font="c3"] h3{font-weight:800 !important;letter-spacing:-.03em}
</style>""", 1)
j = j.replace('&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800', '&amp;family=Plus+Jakarta+Sans:wght@400;500;600;700;800&amp;family=Open+Sans:wght@400;600', 1)
j = j.replace('data-geo="off" class="lh lj"', 'data-geo="off" data-font="{{ fontMode }}" class="lh lj"', 1)
bar = j.index('class="tg-bar"'); k = j.index('<span></span>\n</div>', bar)
j = j[:k] + ('<span style="display: inline-flex; align-items: center; gap: 8px"><span class="tg-label">Font</span><span class="tg-group" role="group" aria-label="Font">'
             '<button type="button" class="tg-opt" aria-pressed="{{ isFontH2 }}" onClick="{{ setFontH2 }}">H2</button>'
             '<button type="button" class="tg-opt" aria-pressed="{{ isFontC3 }}" onClick="{{ setFontC3 }}">C3</button></span></span>\n') + j[k:]
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
      fontMode: (this.state && this.state.font) || 'h2',
      isFontH2: ((this.state && this.state.font) || 'h2') === 'h2' ? 'true' : 'false',
      isFontC3: ((this.state && this.state.font) || 'h2') === 'c3' ? 'true' : 'false',
      setFontH2: this.setFontH2 || (this.setFontH2 = () => this.setFont('h2')),
      setFontC3: this.setFontC3 || (this.setFontC3 = () => this.setFont('c3')),
""", 1)
assert 'setFontC3' in j and 'data-font=' in j and 'aria-label="Font"' in j
open(out, 'w').write(j)
print('morphed', out)
