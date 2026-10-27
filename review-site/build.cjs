// Build the client review site: one standalone page per lane, version and device,
// generated from the canvas boards, with images copied next to them.
const fs = require('fs');
const path = require('path');
const S = '/tmp/claude-0/-home-user-mission-website-design/88308b14-4326-5d33-9419-62732a99c4fd/scratchpad';
const A = '/home/user/mission-website-design/assets';
const SRC = S + '/canvas/project';
const OUT = S + '/review';

const blobs = {
  b70d1fd6eb5a9839c3acd3ccea5d44a1: A + '/photos/ecommerce-packing-orders.webp',
  '2066a54da13614d9c2246994e32d1902': A + '/photos/restaurant-chef-plating.webp',
  b29865f8838e8d694583c88108f0c2aa: S + '/artifact-files/17b46128-259c-40d5-b7d3-374c526f9a58/b29865f8838e8d694583c88108f0c2aa.svg',
  c81310e520e144cd622a899707febdc7: S + '/artifact-files/17b46128-259c-40d5-b7d3-374c526f9a58/c81310e520e144cd622a899707febdc7.svg',
  '5a6f8298d29fe5b417692e04bb5cefb5': S + '/badges/proadvisor-elite.png',
  '1f90e7cd2b6fe11043a8aed199ff3bea': S + '/badges/certified-advanced-qbo.png',
  '8a6858620a6c323d48dea6c25360ff27': S + '/badges/certified-advanced-desktop.png',
  bdd1481bd009109078c5f28e16b35880: S + '/badges/certified-qbo.png',
  cd885cfb7d6c05d7b71c90e8441a681f: S + '/badges/certified-level-2.png',
  '34b1807ca27f04b30ace3c235cf23ea4': S + '/badges/certified-level-1.png',
  '9eef1fc8b132f5488cb3871c7327a754': S + '/badges/certified-enterprise.png',
  '39493efadd289f62e0315fad774e3ce0': S + '/badges/certified-pos.png',
  c76296e63f1cbdfd3cc1859696beddca: A + '/photos/hero-thinking-at-desk.webp',
  '37cbc555ab9573d99c3c204f11469679': A + '/photos/lounge-laptop-portrait.webp',
  '959f667ae9fbf3a0eb90cf0ce15668ff': A + '/photos/reviewing-papers-window.webp',
  '3b6448ffe67d241e50c579a0950384e9': A + '/photos/team-around-laptop.webp',
  '16a347e2aaf4894dd3d60cbfb48a31af': A + '/photos/consultation-desk-wide.webp',
  c7127cc17cfd8909184853095227a34d: A + '/photos/thinking-at-laptop.webp',
  '3554cab00abc02f5b19956702ff92a9f': A + '/photos/construction-plans-review.webp',
  b0f8fafa98dcbe0082a836a30303b5e5: A + '/headshots/headshot-1.png',
  '8dcd87561fad4fb41686cffb42d245b4': A + '/headshots/headshot-2.png',
  '4a8aee7bf8f13bc1315ec9fa3aa9642d': A + '/headshots/headshot-3-starred.png',
  '74637ef8512b80f58ebfb040dd9bddc1': A + '/photos/mockup-monitor-dashboard.webp',
  '18c3a9b86077ecbe9ef147e19def1ec8': A + '/backgrounds/01_hero_bg.jpg',
  c623887169b726fd9a88e8f7ca06bb17: A + '/backgrounds/03_value_proposition_bg.jpg',
  '88aad9f94b46f07630f64f20dcc012ab': A + '/backgrounds/08_how_it_works_bg.jpg',
  fedd3d2ceb5420934109b0ae6cbefe7a: A + '/backgrounds/09_faq_bg.jpg',
  '8be5233d6f752c62fe0c170b175cee61': A + '/backgrounds/12_footer_bg.jpg',
};

const lanes = ['d', 'g', 'c'];
const used = new Set();
const missing = new Set();
fs.mkdirSync(OUT + '/pages', { recursive: true });
fs.mkdirSync(OUT + '/img', { recursive: true });

function page(file, width, title) {
  const t = fs.readFileSync(path.join(SRC, file), 'utf8');
  const helmet = t.match(/<helmet>([\s\S]*?)<\/helmet>/)[1];
  const body = t.match(/<\/helmet>\s*([\s\S]*?)<\/x-dc>/)[1];
  const script = t.match(/<script type="text\/x-dc"[^>]*>([\s\S]*?)<\/script>/);
  const props = (t.match(/data-props='([^']*)'/) || [, '{}'])[1];
  const fix = (s) => s.replace(/\/_blob\/([0-9a-f]{32})/g, (m, id) => {
    if (!blobs[id]) { missing.add(id + ' in ' + file); return m; }
    used.add(id);
    return '../img/' + id + path.extname(blobs[id]);
  });
  return '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n' +
    '<meta name="viewport" content="width=' + width + '">\n<title>' + title + '</title>\n' +
    fix(helmet) + '\n<style>html,body{margin:0;overflow-x:hidden}#dc-root{overflow-x:clip}</style>\n</head>\n<body>\n' +
    '<div id="dc-root"></div>\n<template id="dc-tpl">' + fix(body) + '</template>\n' +
    '<script type="application/json" id="dc-props">' + props + '</script>\n' +
    '<script src="../rt.js"></script>\n' +
    (script ? '<script>\n' + script[1].trim() + '\nDC.boot(Component);\n</script>\n' : '<script>DC.boot(function(){});</script>\n') +
    '</body>\n</html>\n';
}

for (const l of lanes) {
  for (const v of ['3']) {
    const base = 'lane-' + l + v;
    const L = l.toUpperCase() + v;
    fs.writeFileSync(OUT + '/pages/' + l + v + '-desktop.html', page(base + '-home.dc.html', 1440, 'MISSION homepage · Lane ' + L + ' · Desktop'));
    fs.writeFileSync(OUT + '/pages/' + l + v + '-mobile.html', page(base + '-home-mobile.dc.html', 390, 'MISSION homepage · Lane ' + L + ' · Mobile'));
  }
}
for (const id of used) fs.copyFileSync(blobs[id], OUT + '/img/' + id + path.extname(blobs[id]));
fs.copyFileSync(blobs.b29865f8838e8d694583c88108f0c2aa, OUT + '/img/mission-logo.svg');
console.log('pages', fs.readdirSync(OUT + '/pages').length, 'images', used.size, 'missing', [...missing]);
