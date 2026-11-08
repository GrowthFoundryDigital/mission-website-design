# Usage: python3 tools/board-to-page.py <board.dc.html> <reference page.html> <out page.html> "<title>" <reference board.dc.html> (run from the repo root)
# turn a canvas board (.dc.html) into a review-site page, using an existing review page of the same kind as the wrapper
import re, sys, glob, os
board, ref, out, title = sys.argv[1:5]
c = open(board).read(); p = open(ref).read()
def helmet(s): return s[s.index('<helmet>') + 8:s.index('</helmet>')]
def body(s): return s[s.index('</helmet>') + 9:s.index('</x-dc>')]
def script(s):
    i = s.index('data-dc-script'); i = s.index('>', i) + 1; return s[i:s.index('</script>', i)]
def props(s): return re.search(r"data-props='([^']*)'", s).group(1)
rc = open(sys.argv[5]).read()  # the reference board the reference page was made from
# image ids -> files in review-site/public/img
ext = {os.path.basename(f).split('.')[0]: os.path.basename(f) for f in glob.glob('review-site/public/img/*')}
def fwd(t):
    def f(m):
        k = m.group(1); assert k in ext, 'no image for ' + k; return '../img/' + ext[k]
    return re.sub(r'/_blob/([0-9a-f]{32})', f, t)
# check the reference pair round-trips through the same steps
def make(src, page):
    q = page
    q = q.replace(helmet(rc).strip(), fwd(helmet(src)).strip(), 1) if helmet(rc).strip() in q else q
    i = q.index('<template id="dc-tpl">') + len('<template id="dc-tpl">'); j = q.index('</template>', i)
    q = q[:i] + fwd(body(src)) + q[j:]
    q = q.replace(script(rc).strip(), script(src).strip(), 1)
    q = q.replace('<script type="application/json" id="dc-props">' + props(rc) + '</script>', '<script type="application/json" id="dc-props">' + props(src) + '</script>', 1)
    q = re.sub(r'<title>[^<]*</title>', '<title>' + title + '</title>', q, 1)
    return q
assert helmet(rc).strip() in p or fwd(helmet(rc)).strip() in p, 'helmet not found in reference page'
if fwd(helmet(rc)).strip() in p and helmet(rc).strip() not in p:
    p2 = p.replace(fwd(helmet(rc)).strip(), helmet(rc).strip(), 1); p = p2
assert script(rc).strip() in p
open(out, 'w').write(make(c, p))
print('written', out)
