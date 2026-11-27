"""Build check-menu-sitewide.html from home-guest-check.html so both menus match.
Run: python3 mksitewide.py   (from anywhere). Reuses the homepage's left-side CSS, LAYOUT, SPOTS and svgArt."""
import re, os
D = os.path.dirname(os.path.abspath(__file__)) + '/../'
h = open(D + 'home-guest-check.html').read()

def between(s, a, b, incl_b=False):
    i = s.index(a); j = s.index(b, i)
    return s[i:j + (len(b) if incl_b else 0)]

css_left = between(h, '/* ---------- left side', '/* ---------- right two thirds')
css_left = css_left.replace('#ben-home{--ben-u', '#ben-menu{--ben-u')
cfg = between(h, '    /* 1. Upload these two images', '    /* 5. Where the prints')
links = between(h, '    links: {', '    },', True)
layout = between(h, '  var LAYOUT = {', '  $(\'ben-left\').innerHTML')
# the napkin links home (on the homepage it just clears the picked line)
layout = layout.replace("'<a class=\"ben-napkin\" href=\"#\"", "'<a class=\"ben-napkin\" href=\"'+esc(CONFIG.homePath)+'\"")
assert 'CONFIG.homePath' in layout and "'</g></a>' + spots" in layout
cats = re.findall(r'cat:"(\w+)", code:"\w+", url:"/work-new/([\w-]+)"', h)
catmap = ', '.join('"%s":"%s"' % (s, c) for c, s in cats)

out = '''<!-- ============================================================
  BETH ERIN NEWMAN · "BEN'S" MENU ON EVERY PAGE  (v3, 2026-11-19, matches the homepage)
  Paste ALL of this into: Pages panel > Custom Code (at the bottom) > Code Injection > FOOTER.
  The napkin and guest check stay fixed on the left; the page content sits in the right two thirds
  and scrolls under the napkin, so moving between pages only changes the right side.
  It hides the site header and footer on those pages. On phones it becomes a Menu button.
  The homepage has its own copy of the menu, so this skips it.
  While you build, it only shows on your hidden pages (showOn), so the live site is untouched.
  Built from home-guest-check.html by tools/mksitewide.py, so the two menus always match.
  NOTE: no blank lines on purpose.
============================================================ -->
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Rock+Salt&family=Permanent+Marker&display=swap" rel="stylesheet">
<style>
#ben-menu{
  --ben-accent:#2E3BFF; --ben-line-blue:#0001AD; --ben-hand-ink:#1C1C1C; --ben-shadow:rgba(20,20,22,.28);
  --ben-h:100vh;
  position:fixed; left:0; top:0; width:100vw; height:var(--ben-h); z-index:2147483000; pointer-events:none; text-align:left;
}
@supports (height:100dvh){#ben-menu{--ben-h:100dvh}}
#ben-menu *{box-sizing:border-box}
#ben-menu a{text-decoration:none}
''' + css_left + '''/* the page content: right two thirds, starting just under the napkin, scrolling beneath it */
html.ben-menu-on #header, html.ben-menu-on #footer-sections, html.ben-menu-on .header-announcement-bar-wrapper{display:none!important}
html.ben-menu-on .section-background, html.ben-menu-on .section-border{display:none!important}
html.ben-menu-on #siteWrapper{margin-left:calc(max(300px, 33.333vw) + 8px); padding-top:calc(min(100vw / 1440, 100vh / 1024) * 300); background:transparent!important}
.benm-btn{display:none}
/* phones: content full width, the menu opens from a button */
@media (max-width:860px){
  html.ben-menu-on #siteWrapper{margin-left:0; padding-top:0}
  #ben-menu{pointer-events:auto; overflow-y:auto; background:rgba(163,171,114,.96); opacity:0; visibility:hidden; transition:opacity .25s, visibility .25s}
  #ben-menu.open{opacity:1; visibility:visible}
  #ben-menu .ben-left{height:auto; pointer-events:auto}
  #ben-menu .ben-art-d{display:none}
  #ben-menu .ben-art-m{display:block; position:relative; width:min(100%, 520px); height:auto; aspect-ratio:402/735; margin:0 auto}
  .benm-btn{display:block; position:fixed; left:16px; bottom:16px; z-index:2147483001; font:500 12px/1 "IBM Plex Mono",ui-monospace,Menlo,monospace; letter-spacing:.08em; text-transform:uppercase; background:#FFFDF6; color:#0001AD; border:1px solid #0001AD; padding:10px 12px; cursor:pointer; box-shadow:0 8px 16px -8px rgba(0,0,0,.35)}
}
@media (prefers-reduced-motion:reduce){#ben-menu *{transition:none!important}}
</style>
<script>
(function(){
  /* ======================= CONFIG: edit me ======================= */
  var CONFIG = {
    /* Pages that get the menu. While building: your hidden pages only. On launch day: ["*"] */
    showOn: ["/work-new", "/about-new"],
    homePath: "/home-new",          /* launch day: "/" */
    workPath: "/work-new",          /* launch day: "/work" */
    /* Each project page's check line (its URL slug: the line it belongs to). Current page's line shows blue and underlined. */
    cats: {''' + catmap + '''},
''' + cfg + links + '''
  };
  /* ===================== end of CONFIG ===================== */
  if (window.BEN_MENU_DONE) return; window.BEN_MENU_DONE = 1;
  var path = (window.BEN_PATH || location.pathname).replace(/\\/+$/, '') || '/';
  var show = CONFIG.showOn.some(function(p){ return p === '*' || path === p || path.indexOf(p + '/') === 0; });
  if (!show || path === CONFIG.homePath || document.getElementById('ben-home')) return;
  var inEditor = false;
  try { inEditor = window.top !== window.self; } catch (e) { inEditor = true; }
  if (inEditor && !window.BEN_PREVIEW) return; /* keep the editor usable */
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }
''' + layout + '''  var menu = document.createElement('nav');
  menu.id = 'ben-menu'; menu.setAttribute('aria-label', 'Menu');
  menu.innerHTML = '<div class="ben-left">' + svgArt('d') + svgArt('m') + '</div>';
  document.body.appendChild(menu);
  document.documentElement.classList.add('ben-menu-on');
  /* check lines jump to the homepage with that line picked; this page's line stays lit */
  var slug = path.indexOf(CONFIG.workPath + '/') === 0 ? path.slice(CONFIG.workPath.length + 1).split('/')[0] : '';
  var mine = CONFIG.cats[slug];
  [].forEach.call(menu.querySelectorAll('a[data-cat]'), function(a){
    a.setAttribute('href', CONFIG.homePath + '#' + a.dataset.cat.toLowerCase());
    a.removeAttribute('role');
    a.removeAttribute('aria-pressed');
    if (a.dataset.cat === mine) { a.classList.add('hov'); a.setAttribute('aria-current', 'true'); }
  });
  var btn = document.createElement('button');
  btn.className = 'benm-btn'; btn.type = 'button'; btn.textContent = 'Menu'; btn.setAttribute('aria-expanded', 'false');
  document.body.appendChild(btn);
  btn.addEventListener('click', function(){ var o = menu.classList.toggle('open'); btn.textContent = o ? 'Close' : 'Menu'; btn.setAttribute('aria-expanded', o); });
  menu.addEventListener('click', function(e){ if (e.target === menu) { menu.classList.remove('open'); btn.textContent = 'Menu'; btn.setAttribute('aria-expanded', 'false'); } });
})();
</script>
'''
out = re.sub(r'\n\s*\n', '\n', out)
open(D + 'check-menu-sitewide.html', 'w').write(out)
print('wrote', len(out), 'bytes;', len(cats), 'project lines')
