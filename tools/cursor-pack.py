# Pointer cursor pack (9 Nov, by request: "the blog posts on all lanes don't have a cursor when hovering"): in the mockups, blog
# posts, cards, rows and photos react on hover but are not links, so the browser showed the plain arrow. This adds one CSS line per
# lane giving every element with a hover effect the pointer cursor. Found by reading each page's :hover rules in a browser and
# keeping the elements that are not inside a link or button. Lane J gets the same line from tools/lane-j-morph.py.
# Idempotent: skips a file that already carries the marker.
# Usage: python3 tools/cursor-pack.py <file> [<file> ...]   (canvas boards lane-<x>-home*.dc.html or review pages <x>-*.html)
import os, re, sys

MARK = '/* Pointer cursor pack (9 Nov) */'
SEL = {
    'd3': '.ld-post,li.ld-cut-lg,figure',
    'g3': '.lg .row,.lg figure',
    'c3': '.hv-feat,.hv-card,.hv-fig,.hv-cell',
    'h2': '.lh .card,.lh .qcard,.lh .post,.lh .hv-row,.lh .hv-ind,.lh .hv-sup,.lh .hv-li',
}
for f in sys.argv[1:]:
    m = re.match(r'(?:lane-)?(d3|g3|c3|h2)[-]', os.path.basename(f))
    if not m:
        print('skip (not D3, G3, C3 or H2):', f); continue
    s = open(f).read()
    if MARK in s:
        print('already has it:', f); continue
    i = s.index('</style>')
    s = s[:i] + MARK + '\n' + SEL[m.group(1)] + '{cursor:pointer}\n' + s[i:]
    open(f, 'w').write(s)
    print('added:', f)
