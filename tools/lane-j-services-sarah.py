# Usage: python3 tools/lane-j-services-sarah.py <board or review page> ...  (16 Nov: Sarah's revisions to Lane J's services cards; run once on files that still have the numbered circles and arrows)
import re, sys
def transform(s, mobile):
    i = s.index('From behind to ahead'); st = s.rindex('<section', 0, i); en = s.index('</section>', i)
    sec = s[st:en]
    n0 = sec.count('<article class="hv-card"')
    # 1. arrows between the cards
    sec, na = re.subn(r'<span aria-hidden="true" style="flex: 0 0 2[48]px; display: flex; align-items: center; justify-content: center; color: #7CC4F8"><svg[^>]*><path d="M5 12h14M13 6l6 6-6 6"></path></svg></span>\n', '', sec)
    # 2. numbered circles (card 06 keeps its "Limited availability" pill)
    sec, nb = re.subn(r'<div style="display: flex; justify-content: space-between; align-items: center; gap: 8px"><span style="width: 30px; height: 30px; border-radius: 50%;[^"]*">0\d</span>(<span style="background: #C1F432;[^"]*">Limited availability</span>)</div>',
                      lambda m: m.group(1).replace('<span style="background: #C1F432;', '<span style="align-self: flex-start; background: #C1F432;'), sec)
    sec, nc = re.subn(r'<span style="align-self: flex-start; width: 30px; height: 30px; border-radius: 50%;[^"]*">0\d</span>', '', sec)
    # 3. the service link(s) move to the top of each card, larger, still underlined
    def card(m):
        a = m.group(0)
        lk = re.search(r'<div style="margin-top: auto; display: flex; flex-wrap: wrap; gap: 6px">(.*?)</div></article>$', a)
        links = lk.group(1).replace('font-size: 13px; font-weight: 700', 'font-size: %s; font-weight: 700; line-height: 1.25' % ('18px' if mobile else '19px')).replace('font-size: 12.5px">·', 'font-size: 17px">·')
        a = a[:lk.start()] + '</article>'
        top = '<div style="display: flex; flex-wrap: wrap; align-items: baseline; gap: 2px 8px">%s</div>' % links
        # after the opening tag and the optional pill
        k = a.index('>') + 1
        if a[k:].startswith('<span style="align-self: flex-start; background: #C1F432;'):
            k = a.index('</span>', k) + len('</span>')
        a = a[:k] + top + a[k:]
        # the situation title steps down a little so the service name leads
        a = re.sub(r'(<h3 style="margin: 0; font-weight: 600; font-size: )2[12]px(; line-height: 1.15)', r'\g<1>%s\2' % ('17px' if mobile else '18px'), a)
        a = a.replace('min-height: 260px; ', '')
        return a
    sec, nd = re.subn(r'<article class="hv-card".*?</article>', card, sec, flags=re.S)
    # the track gets a plain gap instead of the arrows
    old = 'display: flex; align-items: stretch; overflow-x: auto;'
    assert sec.count(old) == 1; sec = sec.replace(old, 'display: flex; align-items: stretch; gap: %s; overflow-x: auto;' % ('14px' if mobile else '20px'))
    print('cards', n0, 'arrows', na, 'pill', nb, 'circles', nc, 'cards moved', nd, file=sys.stderr)
    assert na == 5 and nb == 1 and nc == 5 and nd == 6
    return s[:st] + sec + s[en:]
for path, mobile in [(a, a.endswith(('-mobile.dc.html', 'j-mobile.html'))) for a in sys.argv[1:]]:
    s = open(path).read(); open(path, 'w').write(transform(s, mobile)); print('done', path)
