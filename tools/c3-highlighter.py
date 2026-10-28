# Lane C3 (28 Oct, by request): lime wipe on the "When people usually call us" cards, a highlighter on text links and
# blog titles, and a highlighter press with a burst of confetti on click. Runs after hover-pack.py; skips boards already done.
# Usage: python3 tools/c3-highlighter.py <canvas>/project
import re, sys

MARK = '/* Highlighter (28 Oct) */'
P = sys.argv[1]
E = 'cubic-bezier(.22,.61,.36,1)'

CSS = MARK + '''
/* "When people usually call us" cards: the same lime wipe as the case study rows; nothing moves */
.hv-cells{border-radius:18px;overflow:hidden}
.hv-cell{background:linear-gradient(#C1F432,#C1F432) no-repeat 0 0/0%% 100%% !important;transition:background-size .5s %(E)s}
.hv-cell:hover{background-size:100%% 100%% !important}
.hv-cell:hover h3{color:#0A2240 !important}
/* Highlighter (revised 28 Oct): a messy lime marker stroke, taller than the letters and running a little past both ends, drawn left to right;
   the letters turn navy only as the stroke reaches them (.hl-ink), so they never vanish on the dark sections */
.hl{position:relative;background-image:url("data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 40' preserveAspectRatio='none'><path fill='%%23C1F432' fill-opacity='.55' d='M1 15C40 11 95 13 140 10S190 9 199 12L198 31C150 33 90 30 45 32S8 33 2 30C0 25 0 20 1 15Z'/><path fill='%%23C1F432' fill-opacity='.95' d='M5 8C28 5 62 9 98 6S168 4 195 7C199 13 197 21 199 27S196 33 194 34C160 36 118 33 80 35S30 36 6 34C2 28 4 22 2 17S3 11 5 8Z'/></svg>");background-repeat:no-repeat;background-position:0 55%%;background-size:0%% 112%%;-webkit-box-decoration-break:clone;box-decoration-break:clone;padding:0 .42em;margin:0 -.42em;text-decoration-color:currentColor;transition:background-size .55s cubic-bezier(.65,0,.35,1),text-decoration-color .3s ease}
a.hl:hover,a.hl:focus-visible,.hv-post:hover .hl{background-size:100%% 112%%;text-decoration-color:transparent !important}
.hl-ink{background-image:linear-gradient(90deg,#0A2240 50%%,currentColor 50%%);background-size:200%% 100%%;background-position:100%% 0;background-repeat:no-repeat;-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent;-webkit-box-decoration-break:clone;box-decoration-break:clone;transition:background-position .55s cubic-bezier(.65,0,.35,1) .04s}
a.hl:hover .hl-ink,a.hl:focus-visible .hl-ink,.hv-post:hover .hl-ink{background-position:0 0}
a.hl:hover svg,a.hl:focus-visible svg{color:#0A2240 !important;transition:transform .25s ease,color .2s ease .4s}
.hv-post{cursor:pointer}
.hv-post:hover h3{color:#0A2240 !important}
@media (prefers-reduced-motion: reduce){.hl,.hl-ink,.hv-cell{transition:none !important}}
''' % {'E': E}

MOBILE_CSS = '.hv-cells{border-radius:16px}\n'

# on click: the stroke presses down to full height and back, and a burst of lime and blue confetti flies out of the click
JS = '''  popHighlight(e) {
    const path = e.composedPath ? e.composedPath() : [];
    const hit = path.find((n) => n && n.classList && (n.classList.contains('hl') || n.classList.contains('hv-post')));
    if (!hit) return;
    const mark = hit.classList.contains('hl') ? hit : hit.querySelector('.hl');
    if (!mark || !mark.animate) return;
    mark.animate([{ backgroundSize: '100% 112%' }, { backgroundSize: '100% 150%', offset: 0.35 }, { backgroundSize: '100% 112%' }], { duration: 520, easing: 'ease-out' });
    mark.animate([{ transform: 'scale(1)' }, { transform: 'scale(0.96)', offset: 0.3 }, { transform: 'scale(1)' }], { duration: 420, easing: 'ease-out' });
    const doc = mark.ownerDocument;
    const colors = ['#C1F432', '#C1F432', '#0A7FD0', '#7CC4F8'];
    for (let i = 0; i < 12; i++) {
      const bit = doc.createElement('span');
      const size = 5 + Math.random() * 5;
      bit.style.cssText = 'position:fixed;left:' + e.clientX + 'px;top:' + e.clientY + 'px;width:' + size + 'px;height:' + size + 'px;margin:' + (-size / 2) + 'px 0 0 ' + (-size / 2) + 'px;border-radius:' + (i % 3 ? '50%' : '2px') + ';background:' + colors[i % 4] + ';pointer-events:none;z-index:2147483647';
      doc.body.appendChild(bit);
      const a = (Math.PI * 2 * i) / 12 + Math.random() * 0.5;
      const d = 34 + Math.random() * 30;
      const fly = bit.animate([
        { transform: 'translate(0,0) scale(1) rotate(0deg)', opacity: 1 },
        { transform: 'translate(' + Math.cos(a) * d + 'px,' + (Math.sin(a) * d + 12) + 'px) scale(0.4) rotate(' + (Math.random() * 240 - 120) + 'deg)', opacity: 0 }
      ], { duration: 650 + Math.random() * 250, easing: 'cubic-bezier(.22,.61,.36,1)' });
      fly.onfinish = () => bit.remove();
    }
  }
'''
MOUNT_OLD = '  componentDidMount() {\n    this.listenBtn();\n'
MOUNT_NEW = ('  componentDidMount() {\n    this.listenBtn();\n'
             '    // highlighter press and confetti on click (skipped for reduced motion)\n'
             "    this.onHlClick = (e) => { if (!(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches)) this.popHighlight(e); };\n"
             "    document.addEventListener('click', this.onHlClick, true);\n")
UNMOUNT_OLD = '  componentWillUnmount() {\n'
UNMOUNT_NEW = "  componentWillUnmount() {\n    document.removeEventListener('click', this.onHlClick, true);\n"


def addcls(tag, cls):
    if 'class="' in tag:
        return tag.replace('class="', 'class="%s ' % cls, 1)
    return re.sub(r'^<(\w+)', r'<\1 class="%s"' % cls, tag)


def body(b, mobile):
    n = {}
    def sub(pat, fn, key):
        nonlocal b
        b, k = re.subn(pat, fn, b)
        n[key] = k
    ink = lambda t: '<span class="hl-ink">' + t + '</span>'
    sub(r'(<a href="#\w+" style="color: #0A2240; font-size: 1\dpx; font-weight: 700; text-underline-offset: 3px">)([^<]*)', lambda m: addcls(m.group(1), 'hl') + ink(m.group(2)), 'service links')
    sub(r'(<a href="#products" style="font-weight: 700; color: #7CC4F8; text-underline-offset: 3px">)([^<]*)', lambda m: addcls(m.group(1), 'hl') + ink(m.group(2)), 'software link')
    sub(r'(<a class="hv-arrow"[^>]*>)([^<]*)', lambda m: m.group(1).replace('class="hv-arrow"', 'class="hv-arrow hl"') + ink(m.group(2)), 'arrow links')
    sub(r'(<article class="hv-post"[^>]*>.*?<h3 [^>]*>)([^<]*)(</h3>)', lambda m: m.group(1) + '<span class="hl">' + ink(m.group(2)) + '</span>' + m.group(3), 'blog titles')
    # the cards' container: on desktop the grid inside the padded card, on mobile the card itself
    i = b.index('class="hv-cell"')
    j = b.rfind('<div', 0, i)
    k = b.index('>', j) + 1
    b = b[:j] + addcls(b[j:k], 'hv-cells') + b[k:]
    # the cards fill their white panel edge to edge, so the wipe reaches its rounded corners (like the case study rows)
    if mobile:
        old = 'class="hv-cells" style="background: #FFFFFF; border-radius: 16px; padding: 4px 8px;'
        assert b.count(old) == 1
        b = b.replace(old, 'class="hv-cells" style="background: #FFFFFF; border-radius: 16px; padding: 0;')
        b, k = re.subn(r'(<article class="hv-cell" style="padding: )18px 12px;', r'\g<1>18px 20px;', b)
        n['mobile cells widened'] = k
    else:
        old = '<div style="background: #FFFFFF; border-radius: 18px; padding: 8px; box-shadow: 0 20px 50px rgba(10, 34, 64, 0.08)">\n<div class="hv-cells"'
        assert b.count(old) == 1
        b = b.replace(old, '<div style="background: #FFFFFF; border-radius: 18px; padding: 0; box-shadow: 0 20px 50px rgba(10, 34, 64, 0.08)">\n<div class="hv-cells"')
    return b, n


def run(f, mobile):
    s = open(f).read()
    if MARK in s:
        return 'already'
    head, rest = s.split('</helmet>', 1)
    b, tail = rest.split('<script type="text/x-dc"', 1)
    b, n = body(b, mobile)
    css = CSS + (MOBILE_CSS if mobile else '')
    i = head.index('</style>')
    head = head[:i] + css + head[i:]
    # the hover pack's cell tint, and blog titles turning blue, give way to the wipe and the highlighter
    for old in ['.hv-cell{transition:background-color .25s ease}\n.hv-cell:hover{background:#F2F8FE}\n.hv-cell:hover h3{color:#0A7FD0 !important}\n',
                '.hv-post:hover h3{color:#0A7FD0 !important}\n']:
        assert head.count(old) == 1, old
        head = head.replace(old, '')
    for a, c in [(MOUNT_OLD, JS + MOUNT_NEW), (UNMOUNT_OLD, UNMOUNT_NEW)]:
        assert tail.count(a) == 1, a
        tail = tail.replace(a, c)
    open(f, 'w').write(head + '</helmet>' + b + '<script type="text/x-dc"' + tail)
    return n


for suf, mob in [('-home', False), ('-home-mobile', True)]:
    f = '%s/lane-c3%s.dc.html' % (P, suf)
    print(f.split('/')[-1], run(f, mob))
