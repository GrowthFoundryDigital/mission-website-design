# Usage: python3 tools/review-no-forms.py review-site/public/pages/*.html
# Review copy only (18 Nov): the published review pages get no <form>, <input> or <textarea>, so nothing on the shared
# review site looks like it collects details (Google Safe Browsing flagged the workers.dev copy as phishing). Each field
# becomes a look-alike, non-typeable box (span.rv-field) with the field's own styles; forms become divs and submit
# buttons plain buttons. The canvas boards keep their real fields. Safe to run again on a page already done.
import re, sys

def css_dupes(css):
    out_base, out_ph = [], []
    for m in re.finditer(r'([^{}]+)\{([^{}]*)\}', css):
        sel, body = m.group(1).strip(), m.group(2)
        if not re.search(r'\b(input|textarea)\b', sel) or sel.startswith('@') or ':focus' in sel:
            continue
        parts = [p.strip() for p in sel.split(',') if re.search(r'\b(input|textarea)\b', p) and ':focus' not in p]
        if not parts:
            continue
        ph = [p for p in parts if '::placeholder' in p]
        base = [p for p in parts if '::placeholder' not in p]
        if base:
            out_base.append(','.join(re.sub(r'\b(input|textarea)\b', '.rv-field', p) for p in base) + '{' + body + '}')
        if ph:
            body_imp = re.sub(r'(color:[^;}]+?)(\s*;|\s*$)', r'\1 !important\2', body)
            out_ph.append(','.join(re.sub(r'\b(input|textarea)\b::placeholder', '.rv-field.rv-ph', p) for p in ph) + '{' + body_imp + '}')
    return out_base + out_ph

def field(tag, attrs, text=''):
    st = re.search(r'\sstyle="([^"]*)"', attrs)
    st = st.group(1).rstrip('; ') + '; ' if st else ''
    ph = re.search(r'\splaceholder="([^"]*)"', attrs)
    label = ph.group(1) if ph else ''
    shape = ('display: block; height: 61px; ' if tag == 'textarea' else 'display: flex; align-items: center; white-space: nowrap; overflow: hidden; ')
    return '<span class="rv-field%s" aria-hidden="true" style="%s%scursor: default">%s</span>' % (' rv-ph' if label else '', st, shape, label)

for path in sys.argv[1:]:
    s = open(path).read()
    if '.rv-field' not in s:
        # style rules for the stand-in boxes, added once to the first <style> block
        extra = []
        for m in re.finditer(r'<style[^>]*>(.*?)</style>', s, re.S):
            extra += css_dupes(m.group(1))
        add = '\n/* review copy: stand-in boxes for the form fields (no real inputs on the shared review site) */\n' + \
              '.rv-field{box-sizing:border-box;font:inherit;color:inherit;background:transparent}\n.rv-field.rv-ph{color:#757575 !important}\n' + '\n'.join(extra) + '\n'
        i = s.index('</style>'); s = s[:i] + add + s[i:]
    s = re.sub(r'<input\b([^>]*)>', lambda m: field('input', m.group(1)), s)
    s = re.sub(r'<textarea\b([^>]*)>.*?</textarea>', lambda m: field('textarea', m.group(1)), s, flags=re.S)
    s = re.sub(r'<form\b([^>]*)>', lambda m: '<div' + re.sub(r'\sonsubmit="[^"]*"', '', m.group(1)) + '>', s)
    s = s.replace('</form>', '</div>')
    s = s.replace('type="submit"', 'type="button"')
    s = re.sub(r'(<label\b[^>]*?)\sfor="[^"]*"', r'\1', s)
    open(path, 'w').write(s)
    print(path, 'forms', s.count('<form'), 'inputs', s.count('<input'), 'textareas', s.count('<textarea'))
