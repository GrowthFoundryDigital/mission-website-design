# All lanes (2 Nov, review comment): more client stories in less space. Under the three story cards, a compact grid of six
# more stories, one line of tags and a title each. MISSION has published four stories so far (Business DNA, Case Studies),
# so these six are marked placeholders until real ones arrive; the tag line follows the agreed template: industry · software.
N = 6
C = '<!-- more client stories, compact (2 Nov, review comment): placeholders until MISSION supplies more stories -->\n'
def items(fn):
    return ''.join(fn(i + 5) for i in range(N))
NOTE = 'Placeholders: six more client stories to come.'

def d3(m):
    arr = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none"><path d="M5 12h14M13 6l6 6-6 6"></path></svg>'
    it = lambda k: ('<a href="#case-studies" style="display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: %s; border-top: 1px solid #E6E4DE; color: #0E3A66; text-decoration: none">'
                    '<span style="display: flex; flex-direction: column; gap: 6px"><span style="font-size: %dpx; letter-spacing: 0.12em; text-transform: uppercase; color: #1E73BE">Industry · Software</span>'
                    '<span style="font-size: %dpx; font-weight: 500; line-height: 1.3">Client story %d: problem-first title</span></span>%s</a>') % ('14px 0' if m else '16px 0', 12 if m else 13, 16 if m else 17, k, arr)
    return (C + '<div style="display: flex; flex-direction: column; gap: 10px"><div style="display: grid; grid-template-columns: %s; gap: 0 32px">%s</div>'
            '<p style="margin: 0; font-size: 12.5px; color: #777777">%s</p></div>\n') % ('minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', items(it), NOTE)

def g3(m):
    arr = '<svg class="ar" width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none"><path d="M7 17L17 7"></path><path d="M8 7h9v9"></path></svg>'
    it = lambda k: ('<a href="#case-studies" style="display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: %s; border-top: 1px solid #DCE1E8; color: #0E3A66; text-decoration: none">'
                    '<span style="display: flex; flex-direction: column; gap: 6px"><span class="eb">Industry · Software</span>'
                    '<span style="font-family: \'Inter Tight\', sans-serif; font-size: %dpx; letter-spacing: -.015em; line-height: 1.25">Client story %d: problem-first title</span></span>%s</a>') % ('14px 0' if m else '18px 0', 17 if m else 19, k, arr)
    return (C + '<div style="display: flex; flex-direction: column; gap: 10px; margin-top: %dpx"><div style="display: grid; grid-template-columns: %s; gap: 0 28px">%s</div>'
            '<p class="sm" style="font-size: 12.5px">%s</p></div>\n') % (10 if m else 12, 'minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', items(it), NOTE)

def c3(m):
    arr = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" style="flex: none; color: #0A7FD0"><path d="M9 6l6 6-6 6"></path></svg>'
    it = lambda k: ('<a href="#case-studies" style="display: flex; align-items: center; justify-content: space-between; gap: 14px; padding: %s; background: #FFFFFF; border-radius: 12px; box-shadow: 0 8px 22px rgba(10, 34, 64, 0.06); color: #0A2240; text-decoration: none">'
                    '<span style="display: flex; flex-direction: column; gap: 5px"><span style="font-size: 11px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #0A7FD0">Industry · Software</span>'
                    '<span style="font-size: %dpx; font-weight: 800; line-height: 1.25; letter-spacing: -0.01em">Client story %d: problem-first title</span></span>%s</a>') % ('14px 16px' if m else '16px 18px', 15 if m else 16, k, arr)
    return (C + '<div style="display: flex; flex-direction: column; gap: 10px"><div style="display: grid; grid-template-columns: %s; gap: %s">%s</div>'
            '<p style="margin: 0; font-size: 12.5px; color: #5B6B80">%s</p></div>\n') % ('minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', '10px' if m else '12px', items(it), NOTE)

def h2(m, ARR):
    it = lambda k: ('<a href="#case-studies" style="display: flex; align-items: center; justify-content: space-between; gap: 16px; padding: %s; border-top: 1px solid #DCE1E8; color: #101419; text-decoration: none">'
                    '<span style="display: flex; flex-direction: column; gap: 6px"><span class="tag">Industry · Software</span>'
                    '<span style="font: 600 %dpx/1.3 \\\'Space Grotesk\\\', sans-serif">Client story %d: problem-first title</span></span><span style="flex: none; color: var(--eb)">%s</span></a>') % ('14px 0' if m else '16px 0', 15 if m else 16, k, ARR)
    return ('<div style="display: flex; flex-direction: column; gap: 10px"><div style="display: grid; grid-template-columns: %s; gap: 0 28px">%s</div>'
            '<p class="mu" style="font-size: 12.5px">%s</p></div>') % ('minmax(0, 1fr)' if m else 'repeat(3, minmax(0, 1fr))', items(it), NOTE)
