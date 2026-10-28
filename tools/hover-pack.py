# Hover pack for Lanes D3, G3 and C3 (28 Oct; Lane H2 gets its hovers from lane-h2-gen.py): adds hover classes where a board styles inline, and one CSS block per board.
# Idempotent: skips a board that already carries the marker.
import re, sys

MARK = '/* Hover pack (28 Oct) */'
P = sys.argv[1]  # the canvas project folder, e.g. python3 tools/hover-pack.py <canvas>/project

D3 = MARK + r"""
.tg-btn,a.ld-cut,button.ld-cut{transition:transform .25s ease,box-shadow .25s ease,filter .25s ease}
.tg-btn:hover,.tg-btn:focus-visible{transform:translateY(-2px);box-shadow:0 12px 26px rgba(14,58,102,.22)}
li.ld-cut-lg{transition:transform .3s ease,box-shadow .3s ease}
li.ld-cut-lg:hover,li.ld-cut-lg:focus-within{transform:translateY(-4px);box-shadow:0 20px 44px rgba(14,58,102,.14)}
li.ld-cut-lg:hover h3,li.ld-cut-lg:focus-within h3{color:#1E73BE !important}
li.ld-cut-lg img{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
li.ld-cut-lg:hover img{transform:scale(1.04)}
figure{transition:transform .3s ease,box-shadow .3s ease}
figure:hover{transform:translateY(-4px)}
.ld-post img{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
.ld-post:hover img{transform:scale(1.05)}
.ld-cut-sm img,.ld-cut img{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
"""

G3 = MARK + r"""
.lg .btn,.lg .lnk{transition:background-color .35s cubic-bezier(.4,0,.2,1),border-color .35s cubic-bezier(.4,0,.2,1),color .35s cubic-bezier(.4,0,.2,1),transform .25s ease,box-shadow .25s ease}
.lg .row{transition:transform .25s ease}
.lg .row:hover{transform:translateX(8px)}
.lg .row h3{transition:color .25s ease}
.lg .row .ti{transition:transform .25s ease}
.lg .row:hover h3{color:#1E73BE}
.lg .row:hover .ti{transform:scale(1.15)}
.lg figure{transition:transform .3s ease,box-shadow .3s ease,background-color .3s ease}
.lg figure:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(14,58,102,.14)}
.lg .card .ph{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
.lg .card:not(.cs-card):hover .ph{transform:scale(1.05)}
.lg .card:not(.cs-card):hover{box-shadow:0 20px 44px rgba(7,13,23,.25)}
/* Case study cards (28 Oct, toned down by request): no lift, no zoom; the blue edge and arrow nudge stay */
.lg .cs-card:hover,.lg .cs-card:focus-visible{transform:none}
.lg article img{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
.lg article:hover img{transform:scale(1.05)}
.lg .foot a[target="_blank"]:hover{text-decoration:underline;text-underline-offset:3px}
"""

C3 = MARK + r"""
/* Buttons (28 Oct, revised by request): a 2px lift only, with no invert and no shadow */
.tg-btn{transition:transform .25s ease,filter .25s ease,opacity .2s ease}
.tg-btn:hover,.tg-btn:focus-visible{transform:translateY(-2px)}
[data-btn="blue"] .tg-btn:hover,[data-btn="blue"] .tg-btn:focus-visible{filter:brightness(1.12)}
.hv-nav{transition:color .2s ease}
.hv-nav:hover,.hv-nav:focus-visible{color:#FFFFFF !important;text-decoration:underline !important;text-decoration-thickness:2px;text-underline-offset:6px}
.hv-foot{transition:color .2s ease}
.hv-foot:hover,.hv-foot:focus-visible{color:#7CC4F8 !important}
.hv-arrow svg{transition:transform .25s ease}
.hv-arrow:hover,.hv-arrow:focus-visible{text-decoration:underline !important;text-underline-offset:4px}
.hv-arrow:hover svg,.hv-arrow:focus-visible svg{transform:translateX(4px)}
.hv-row{transition:background-color .25s ease,transform .25s ease}
.hv-row:hover,.hv-row:focus-visible{background:#EEF6FD !important;transform:translateX(4px)}
.hv-row:hover h3,.hv-row:focus-visible h3{color:#0A7FD0 !important}
.hv-feat{transition:transform .3s ease,box-shadow .3s ease}
.hv-feat img{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
.hv-feat:hover{transform:translateY(-4px)}
.hv-feat:hover img{transform:scale(1.04)}
.hv-cell{transition:background-color .25s ease}
.hv-cell:hover{background:#F2F8FE}
.hv-cell:hover h3{color:#0A7FD0 !important}
.hv-card{transition:transform .3s ease,box-shadow .3s ease}
.hv-card:hover{transform:translateY(-6px);box-shadow:0 22px 44px rgba(10,34,64,.22)}
.hv-post img{transition:transform .6s cubic-bezier(.22,.61,.36,1)}
.hv-post h3{transition:color .25s ease}
.hv-post:hover img{transform:scale(1.05)}
.hv-post:hover h3{color:#0A7FD0 !important}
.hv-faq{transition:color .2s ease}
.hv-faq svg{transition:transform .25s ease}
.hv-faq:hover,.hv-faq:focus-visible{color:#0A7FD0 !important}
.hv-faq:hover svg{transform:rotate(90deg)}
.hv-circ{transition:transform .25s ease}
.hv-circ:hover,.hv-circ:focus-visible{transform:translateY(-2px)}
.hv-ghost{transition:transform .25s ease}
.hv-ghost:hover,.hv-ghost:focus-visible{transform:translateY(-2px)}
.hv-soc{transition:transform .25s ease,background-color .25s ease}
.hv-soc:hover,.hv-soc:focus-visible{transform:translateY(-3px) scale(1.06);background:#7CC4F8 !important}
.hv-fig{transition:transform .3s ease,box-shadow .3s ease}
.hv-fig:hover{transform:translateY(-4px);box-shadow:0 18px 40px rgba(10,34,64,.3)}
"""


def add_class(s, pattern, cls, tag_re=r'<(a|button|article|figure)\b'):
    # add cls to every opening tag whose style matches pattern (and which has no class yet)
    n = 0
    def fix(m):
        nonlocal n
        tag = m.group(0)
        if 'class="' in tag:
            return tag
        n += 1
        return re.sub(r'^<(\w+)', r'<\1 class="%s"' % cls, tag)
    s = re.sub(tag_re + r'[^>]*?style="' + pattern + r'[^>]*>', fix, s)
    return s, n


def c3(s, mobile):
    counts = {}
    rules = [
        (r'color: #D6E2F2; text-decoration: none', 'hv-nav', r'<a\b'),
        (r'color: #E3EAF3; text-decoration: none', 'hv-foot', r'<a\b'),
        (r'color: #FFFFFF; text-decoration: none"', 'hv-foot', r'<a\b'),
        (r'(?:align-self: [a-z-]+; )?display: inline-flex; align-items: center; gap: 8px; (?:padding-top: \d+px; )?font-size: 1\d(?:\.\d)?px; font-weight: 700', 'hv-arrow', r'<a\b'),
        (r'display: flex; align-items: center; gap: 1[468]px; padding: \d+px \d+px;', 'hv-row', r'<a\b'),
        (r'background: #FFFFFF; border-radius: 16px; overflow: hidden; box-shadow', 'hv-feat', r'<article\b'),
        (r'padding: 2\dpx 2\dpx 30px; display: flex; flex-direction: column; gap: 12px', 'hv-cell', r'<article\b'),
        (r'flex: 0 0 2\d\dpx; box-sizing: border-box; background:', 'hv-card', r'<article\b'),
        (r'display: flex; flex-direction: column; gap: 10px"', 'hv-post', r'<article\b'),
        (r'width: 100%; display: flex; align-items: center; justify-content: space-between; gap: 14px', 'hv-faq', r'<button\b'),
        (r'width: 4\dpx; height: 4\dpx; border-radius: 50%', 'hv-circ', r'<button\b'),
        (r'display: inline-flex; align-items: center; height: 5\dpx; padding: 0 2\dpx; border-radius: 12px; background: rgba\(255, 255, 255, 0.06\)', 'hv-ghost', r'<a\b'),
        (r'display: inline-flex; align-items: center; justify-content: center; width: 4\dpx; height: 4\dpx', 'hv-soc', r'<a\b'),
        (r'display: inline-flex; align-items: center; gap: 8px; height: 42px', 'hv-soc', r'<a\b'),
        (r'position: absolute; left: \d+px; bottom: \d+px; max-width: \d+px; margin: 0; background: #7CC4F8', 'hv-fig', r'<figure\b'),
        # mobile-only shapes
        (r'padding: 18px 12px; display: flex; gap: 14px; align-items: flex-start', 'hv-cell', r'<article\b'),
        (r'position: absolute; left: 12px; right: 12px; bottom: 12px; margin: 0; background: #7CC4F8', 'hv-fig', r'<figure\b'),
        (r'width: 44px; height: 44px; border-radius: 50%', 'hv-circ', r'<a\b'),
        (r'display: flex; justify-content: center; align-items: center; height: 50px', 'hv-ghost', r'<a\b'),
    ]
    for pat, cls, tag in rules:
        s, n = add_class(s, pat, cls, tag)
        counts[cls] = counts.get(cls, 0) + n
    return s, counts


def inject(f, css, fn=None, mobile=False):
    s = open(f).read()
    if MARK in s:
        return 'already'
    counts = {}
    if fn:
        head, rest = s.split('</helmet>', 1)
        body, tail = rest.split('<script type="text/x-dc"', 1)
        body, counts = fn(body, mobile)
        s = head + '</helmet>' + body + '<script type="text/x-dc"' + tail
    i = s.index('</style>\n</helmet>')
    s = s[:i] + css + s[i:]
    open(f, 'w').write(s)
    return counts


for name, css, fn in [('lane-d3', D3, None), ('lane-g3', G3, None), ('lane-c3', C3, c3)]:
    for suf, mob in [('-home', False), ('-home-mobile', True)]:
        f = '%s/%s%s.dc.html' % (P, name, suf)
        print(f.split('/')[-1], inject(f, css, fn, mob))
