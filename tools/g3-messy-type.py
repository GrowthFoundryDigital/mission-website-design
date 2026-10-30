# Usage: python3 tools/g3-messy-type.py <lane-g3-home.dc.html> <lane-g3-home-mobile.dc.html>  (after wrapping the word in <span class="messy" data-text="messy">)
# G3 (30 Oct, by request): "MESSY" in the hero headline treated as digital decay. The letters fill with white that breaks
# into square pixels towards the end of the word, one horizontal slice is cut out and nudged sideways, and a few loose
# pixels drift off the Y. All sizes are in em, so the same CSS fits the 88 px desktop and the 50 px mobile headline.
import random, sys
from urllib.parse import quote

W, H, C = 308, 114, 6         # the word's box in hundredths of an em (3.08em wide, 0.90em line + .16em/.08em padding), pixel cell 0.06em
rnd = random.Random(7)
cells = []
for x in range(0, W, C):
    for y in range(0, H, C):
        t = x / W
        if t < 0.40:
            keep = True
        elif t < 0.68:
            keep = rnd.random() > 0.05          # a few early drop-outs
        else:
            k = (t - 0.68) / 0.32               # 0 at the start of the Y, 1 at its end
            keep = rnd.random() > 0.06 + 0.58 * k ** 1.3
        if not keep:
            cells.append((x, y))
holes = ''.join('<rect x="%g" y="%g" width="%g" height="%g"/>' % (x - .3, y - .3, C + .6, C + .6) for x, y in cells)
svg = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" preserveAspectRatio="none" shape-rendering="crispEdges">'
       '<defs><mask id="m"><rect width="%d" height="%d" fill="#fff"/><g fill="#000">%s</g></mask></defs>'
       '<rect width="%d" height="%d" fill="#fff" mask="url(#m)"/></svg>') % (W, H, W, H, holes, W, H)
url = 'url("data:image/svg+xml,%s")' % quote(svg, safe='/:= ')

CSS = '''/* "MESSY" treated as digital decay (30 Oct, by request): pixels drop out towards the end of the word,
   one slice is cut and shifted, and a few loose pixels drift off; static for reduced motion */
.lg .messy{position:relative;display:inline-block;color:transparent;-webkit-text-fill-color:transparent;background:%(url)s 0 0/100%% 100%% no-repeat;-webkit-background-clip:text;background-clip:text;
  padding:.16em 0 .08em;margin:-.16em 0 -.08em;
  -webkit-mask-image:linear-gradient(#000 0 52%%,transparent 52%% 61%%,#000 61%%);mask-image:linear-gradient(#000 0 52%%,transparent 52%% 61%%,#000 61%%)}
.lg .messy::before{content:attr(data-text);position:absolute;left:0;top:0;padding:inherit;color:transparent;-webkit-text-fill-color:transparent;background:inherit;-webkit-background-clip:text;background-clip:text;
  -webkit-mask-image:none;mask-image:none;clip-path:inset(52%% 0 39%% 0);transform:translateX(.07em);animation:messySlice 6s steps(1) infinite}
.lg .messy::after{content:'';position:absolute;left:100%%;top:.3em;width:.06em;height:.06em;margin-left:.04em;background:#FFFFFF;
  box-shadow:.12em .1em 0 #FFFFFF,.05em .3em 0 #1E73BE,.22em .2em 0 rgba(255,255,255,.55),.16em .5em 0 #FFFFFF,.3em .38em 0 #1E73BE,.08em .62em 0 rgba(255,255,255,.4)}
@keyframes messySlice{0%%,88%%{transform:translateX(.07em)}90%%{transform:translateX(-.05em)}92%%{transform:translateX(.13em)}94%%,100%%{transform:translateX(.07em)}}
@media (prefers-reduced-motion: reduce){.lg .messy::before{animation:none}}
''' % {'url': url}

for f in sys.argv[1:]:
    s = open(f).read()
    if '.lg .messy{' in s:
        print(f, 'already'); continue
    i = s.index('</style>')
    open(f, 'w').write(s[:i] + CSS + s[i:])
    print(f, 'ok', len(cells), 'pixels out')
