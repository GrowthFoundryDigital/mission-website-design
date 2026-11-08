# Usage: python3 tools/lane-j-make-gen.py tools/lane-h2-gen.py tools/lane-j-gen.py, then python3 tools/lane-j-gen.py <canvas project folder>
# Lane J (Round 2, 8 Nov): the blend of H2 and C3 agreed in the client meeting. Built as a patched copy of the H2 generator:
# H2's structure and type, no hero divider and no shapes, Electric Blue on fewer and smaller areas (hero, proof band gone),
# C3's softer ice-blue sections, the ecommerce hero photo (office as the second option, kitchen dropped), a still headline,
# 32 Google reviews (meeting notes), Jewelry in place of Restaurants, and Industries in the menu.
import sys
src = open(sys.argv[1]).read()
def rep(a, b, n=1):
    global src
    c = src.count(a)
    assert c == n, (a[:90], c)
    src = src.replace(a, b)

rep('Lane H2 generator: Lane H with the geometry sprinkled through the page', 'Lane J generator (Round 2, 8 Nov): the H2 and C3 blend, made from the Lane H2 generator; H2 was Lane H with the geometry sprinkled through the page')
# files, titles, channel
rep("open(OUT + '/lane-h2-home.dc.html', 'w')", "open(OUT + '/lane-j-home.dc.html', 'w')")
rep("open(OUT + '/lane-h2-home-mobile.dc.html', 'w')", "open(OUT + '/lane-j-home-mobile.dc.html', 'w')")
rep('<title>Lane H2 homepage, %s</title>', '<title>Lane J homepage, %s</title>')
rep('Lane H2 board', 'Lane J board', 4)
rep("mission-buttons-lane-h2", "mission-buttons-lane-j")
# no divider and no shapes: the page is always in H2's "divider off, shapes off" state, and no shape is drawn at all
rep('data-div="{{ divMode }}" data-blue="{{ blueMode }}" data-geo="{{ geoMode }}" class="lh"', 'data-div="off" data-blue="{{ blueMode }}" data-geo="off" class="lh lj"')
for fn in ['def poly(', 'def sq(', 'def dotp(', 'def frame(', 'def corners(']:
    i = src.index(fn); j = src.index('\n', i)
    src = src[:j + 1] + "    return ''  # Lane J: no shapes\n" + src[j + 1:]
rep("def scatter(items):\n", "def scatter(items):\n    return ''  # Lane J: no shapes\n")
# review bar: buttons, photos (ecommerce first, office; kitchen dropped) and blue; divider and shapes switches removed
rep("""    A('<button type="button" class="tg-opt" aria-pressed="{{ isKitchen }}" onClick="{{ setKitchen }}">Kitchen</button>')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isOffice }}" onClick="{{ setOffice }}">Office</button>')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isEcommerce }}" onClick="{{ setEcommerce }}">Ecommerce</button>')""",
"""    A('<button type="button" class="tg-opt" aria-pressed="{{ isEcommerce }}" onClick="{{ setEcommerce }}">Ecommerce</button>')
    A('<button type="button" class="tg-opt" aria-pressed="{{ isOffice }}" onClick="{{ setOffice }}">Office</button>')""")
i = src.index("    # hero divider on or off (28 Oct)"); j = src.index("    # Electric Blue or Mission Blue (29 Oct)")
src = src[:i] + src[j:]
i = src.index("    # geometric shapes on or off (29 Oct)"); j = src.index("A('</span></span>\\n</div>\\n')", i)
src = src[:i] + "    A('<span></span>\\n</div>\\n')" + src[j + len("A('</span></span>\\n</div>\\n')"):]
rep("""    'kitchen': ('A chef plating dishes in a restaurant kitchen', ('62% 40%', '80% 28%')),\n""", "")
rep("|| 'kitchen'", "|| 'ecommerce'", 4)
# the photo grid beside "A specialist team": the kitchen photo (restaurant imagery, dropped in the meeting) becomes the office photo
rep("('kitchen', 'A chef plating dishes in a restaurant kitchen', '72% 40%')", "('office', 'A business owner thinking at a desk', '62% 30%')")
# 32 Google reviews (meeting notes, 8 Nov)
rep('<strong style="color: #FFFFFF">5.0 average</strong> on Google reviews', '<strong style="color: #FFFFFF">5.0 average</strong> from 32 Google reviews', 2)
rep("('5.0', 'our average star rating on Google')", "('5.0', 'our average star rating from 32 Google reviews')")
# industries: Jewelry in, Restaurants out (meeting notes); Industries in the menu
rep("    ('fork', 'Restaurants', 'Food and staff costs, daily sales and checkout numbers that actually match the bank.'),",
    "    ('gem', 'Jewelry', 'Custom orders, and where each piece is kept, tracked in QuickBooks Enterprise.'),")
rep("I = {  # line icons, 24px grid, drawn with currentColor\n", "I = {  # line icons, 24px grid, drawn with currentColor\n    'gem': '<path d=\"M6 3h12l4 6-10 12L2 9z\"/><path d=\"M2 9h20M12 21 8 9l4-6 4 6-4 12\"/>',\n")
rep("NAV = [('#services', 'Services'), ('#case-studies', 'Case studies')", "NAV = [('#services', 'Services'), ('#industries', 'Industries'), ('#case-studies', 'Case studies')")
rep("""<section aria-label="How we work" class="wh\"""", """<section id="industries" aria-label="How we work" class="wh\"""")
# fewer, smaller blue areas: the full-width Electric Blue proof band becomes C3's ice blue, with dark type and an outline button
rep("""    A('<!-- 08 Certified by Intuit, on the Electric Blue band -->')
    A('<section aria-label="Certified by Intuit" class="bl" """, """    A('<!-- 08 Certified by Intuit, on the C3 ice blue (Lane J: fewer blue areas) -->')
    A('<section aria-label="Certified by Intuit" class="ice" """)
rep("""<p style="font: 600 15px/1.4 \\'Space Grotesk\\', sans-serif; color: #FFFFFF">Certified at Intuit\\'s Elite and Level 2 Advanced levels.</p><a class="btn btn-w\"""",
    """<p style="font: 600 15px/1.4 \\'Space Grotesk\\', sans-serif; color: #101419">Certified at Intuit\\'s Elite and Level 2 Advanced levels.</p><a class="btn btn-o\"""")
rep(".lh .ch{background:#F5F6F7}", ".lh .ch{background:#F5F6F7}\n/* Lane J: C3's softer ice blue for the light sections */\n.lj .ch,.lj .ice{background:#E8F3FD}")
# footer call to action: the angled graphic goes (no shapes), and the call to action runs the full width
i = src.index("    A('<div aria-hidden=\"true\" class=\"foot-geo%s\""); j = src.index("    A('</div>')\n    A('</div>')\n    A('<div style=\"border-top: 1px solid rgba(255,255,255,.1)\">')", i)
src = src[:i] + src[j + len("    A('</div>')\n"):]
rep("'grid; grid-template-columns: minmax(0, 7fr) minmax(0, 5fr)', 32 if m else 64))", "'block', 32 if m else 64))")
open(sys.argv[2], 'w').write(src)
print('genj written')
