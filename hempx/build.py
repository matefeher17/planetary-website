#!/usr/bin/env python3
"""A három oldal (index, projekt, kapcsolat) generálása közös fejlécből/láblécből.
Futtatás: python3 build.py   (a kimenet ugyanebbe a mappába kerül)"""
import html, pathlib

OUT = pathlib.Path(__file__).parent
LINKEDIN = 'https://www.linkedin.com/company/hempx-innovation-ltd/'
EMAIL = 'hempx2025@gmail.com'
PID = 'NKFIH-2025-1.1.2.-Gyorsítósáv-2025-00019'


def T(hu, en, tag='span', cls='', extra=''):
    """Kétnyelvű elem: a magyar szöveg az alap, az angol data-en attribútumban van."""
    c = f' class="{cls}"' if cls else ''
    return f'<{tag}{c} {extra} data-en="{html.escape(en, quote=True)}">{hu}</{tag}>'


def head(title, desc, meta_en, page_css=''):
    return f'''<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{html.escape(desc, quote=True)}">
<meta name="robots" content="index, follow">
<meta property="og:title" content="{html.escape(title, quote=True)}">
<meta property="og:description" content="{html.escape(desc, quote=True)}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/hempx-logo.png">
<link rel="icon" type="image/png" href="assets/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script>window.HEMPX_META={{hu:{{title:{title!r},desc:{desc!r}}},en:{{title:{meta_en[0]!r},desc:{meta_en[1]!r}}}}};</script>
</head>
<body>
'''


def nav(active):
    def a(href, hu, en, key, ext=False):
        cur = ' aria-current="page"' if key == active else ''
        tgt = ' target="_blank" rel="noopener" class="ext"' if ext else ''
        return f'<li><a href="{href}"{cur}{tgt} data-en="{en}">{hu}</a></li>'
    items = (a('index.html', 'Főoldal', 'Home', 'home') +
             a('projekt.html', 'Gyorsítósáv projekt', 'Accelerator Project', 'projekt') +
             a('kapcsolat.html', 'Kapcsolat', 'Contact', 'kapcsolat') +
             a(LINKEDIN, 'LinkedIn', 'LinkedIn', 'li', ext=True))
    mob = items.replace('<li>', '').replace('</li>', '')
    return f'''<nav>
  <a href="index.html" class="brand" aria-label="HempX – kezdőlap" data-en-aria="HempX – home">
    <img src="assets/hempx-mark.png" alt="" width="73" height="56"><span>Hemp<b>X</b></span>
  </a>
  <ul class="nav-links">{items}</ul>
  <button class="lang" type="button" aria-label="Switch to English">EN</button>
  <button class="burger" id="burger" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
</nav>
<div class="mobile-menu" id="mobileMenu">{mob}<button class="lang" type="button">EN</button></div>
'''


def newsletter():
    return f'''<section class="band" style="padding-top:0">
  <div class="wrap">
    <div class="news reveal">
      <div>
        {T('Kövesd nyomon a fejlesztéseinket', 'Follow our developments', 'h2')}
        {T('Iratkozz fel hírlevelünkre, és elsőként értesülsz a HempX eredményeiről.', 'Subscribe to our newsletter and be the first to hear about HempX results.', 'p')}
      </div>
      <a class="btn btn-leaf js-news" href="#">{T('Feliratkozom a hírlevélre →', 'Subscribe to the newsletter →')}</a>
    </div>
  </div>
</section>
'''


def footer():
    return f'''<footer>
  <div class="foot">
    <a href="index.html" class="brand"><img src="assets/hempx-mark.png" alt="" width="73" height="56"><span>Hemp<b>X</b> Innovációs Kft.</span></a>
    <ul>
      <li><a href="index.html" data-en="Home">Főoldal</a></li>
      <li><a href="projekt.html" data-en="Accelerator Project">Gyorsítósáv projekt</a></li>
      <li><a href="kapcsolat.html" data-en="Contact">Kapcsolat</a></li>
      <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn ↗</a></li>
      <li><a class="js-news" href="#" data-en="Newsletter">Hírlevél</a></li>
    </ul>
  </div>
  <div class="foot-bottom">
    {T('© 2026 HempX Innovációs Kft. Minden jog fenntartva.', '© 2026 HempX Innovation Ltd. All rights reserved.')}
    <a href="mailto:{EMAIL}">{EMAIL}</a>
  </div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
'''


# ═══════════════════════════ FŐOLDAL ═══════════════════════════
def index():
    h = head('HempX Innovációs Kft. | Kender-mész Kompozit Építőanyag Fejlesztés',
             'A HempX Innovációs Kft. új generációs, kenderalapú kompozit építőanyagokat fejleszt: ipari rostkenderből, speciális mészkeverékekből és természetes adhezív rendszerekből.',
             ('HempX Innovation Ltd. | Hemp-Lime Composite Building Materials',
              'HempX Innovation Ltd. develops next-generation hemp-based composite building materials from industrial fibre hemp, special lime mixtures and natural adhesive systems.'))
    h += nav('home')
    h += f'''
<header class="hero">
  <div>
    <div class="badge"><i></i>{T('Kenderalapú építőanyag-innováció', 'Hemp-based building material innovation')}</div>
    {T('Kender kompozit alapú <em>építőanyagok</em> fejlesztése', 'Development of hemp composite <em>building materials</em>', 'h1')}
    {T('Fenntartható építőipari innováció ipari rostkenderből és természetes adhezív rendszerekből.', 'Sustainable construction innovation from industrial fibre hemp and natural adhesive systems.', 'p', 'lede')}
    {T('A HempX Innovációs Kft. új generációs, kenderalapú kompozit építőanyagokat fejleszt – a laboratóriumi prototípustól az üzemi környezetben validált megoldásokig.', 'HempX Innovation Ltd. develops next-generation hemp-based composite building materials – from laboratory prototype to industrially validated solutions.', 'p', 'lede', 'style="margin-top:1rem"')}
    <div class="actions">
      <a class="btn btn-solid" href="projekt.html">{T('A projekt megismerése →', 'Discover the project →')}</a>
      <a class="btn btn-line js-news" href="#">{T('Kövesd nyomon a fejlesztéseinket', 'Follow our developments')}</a>
    </div>
  </div>
  <div class="hero-photos">
    <div class="frame"><img src="assets/gyartosor.webp" alt="Kenderkompozit blokkgyártó sor üzem közben" width="1050" height="1400"></div>
    <div class="frame"><img src="assets/pozdorja.webp" alt="Ipari kender pozdorja a tenyérben" width="900" height="1200"></div>
    <div class="frame"><img src="assets/tegla-raklap.webp" alt="Kenderkompozit blokkok raklapon" width="562" height="1000"></div>
  </div>
</header>

<section class="band" id="miert">
  <div class="wrap">
    <div class="grid g2" style="margin-bottom:3.5rem">
      <div class="reveal">
        {T('Miért a kender', 'Why hemp', 'span', 'eyebrow')}
        {T('A kender mint <em>építőipari</em> lehetőség', 'Hemp as a <em>construction industry</em> opportunity', 'h2')}
        {T('Az ipari kender gyorsan növő, évente megújuló, regionálisan is termeszthető alapanyag. Pozdorjája – a szár fás része – kiváló alapot kínál könnyű, páraáteresztő, jó hőtechnikai tulajdonságú építőipari kompozitokhoz.', 'Industrial hemp is a fast-growing, annually renewable raw material that can be grown regionally. Its hurd – the woody core of the stem – provides an excellent base for lightweight, vapour-permeable construction composites with good thermal properties.', 'p', 'lede')}
        {T('A HempX célja, hogy kender, speciális mészkeverékek és természetes adhezív komponensek kombinációjával olyan új építőanyag-család jöjjön létre, amely egyszerre szolgálja a fenntartható építést, a karbonlábnyom csökkentését és a korszerű műszaki teljesítményt.', 'HempX aims to create a new family of building materials by combining hemp, special lime mixtures and natural adhesive components – serving sustainable construction, lower carbon footprint and modern technical performance at once.', 'p', 'lede', 'style="margin-top:1rem"')}
      </div>
      <div class="frame reveal" style="aspect-ratio:4/3"><img src="assets/rost.webp" alt="Kenderrost közelről" width="900" height="1200" loading="lazy"></div>
    </div>
    <div class="grid g3">
      <div class="card reveal">
        <span class="no">{T('01 / Alapanyag', '01 / Raw material')}</span>
        {T('Természetes és megújuló', 'Natural and renewable', 'h3')}
        {T('Alacsony vízigényű, gyors növekedésű növény, amely évente megújuló biomasszát ad, miközben növekedése során szén-dioxidot köt meg.', 'A low-water, fast-growing crop that provides renewable biomass every year while binding carbon dioxide as it grows.', 'p')}
        {T('8–15 t/ha szárazanyag', '8–15 t/ha dry matter', 'span', 'data')}
      </div>
      <div class="card reveal">
        <span class="no">{T('02 / Épületfizika', '02 / Building physics')}</span>
        {T('Kedvező hő- és páratechnika', 'Favourable thermal and moisture behaviour', 'h3')}
        {T('A kenderalapú rendszerek alacsony testsűrűsége jó komfortérzetet és kedvező hőtárolási viselkedést biztosíthat.', 'The low density of hemp-based systems can provide good comfort and favourable heat-storage behaviour.', 'p')}
        <span class="data">λ ≈ 0,06–0,08 W/mK</span>
      </div>
      <div class="card reveal">
        <span class="no">{T('03 / Validáció', '03 / Validation')}</span>
        {T('Tudományosan igazolt', 'Scientifically validated', 'h3')}
        {T('Nem csupán anyagkísérletezés: laboratóriumi és üzemi környezetben mért, dokumentált fejlesztési folyamat.', 'Not just material experimentation – a documented development process measured in laboratory and industrial environments.', 'p')}
        {T('SZTE + Mélyépítő Labor', 'University of Szeged + Mélyépítő Labor', 'span', 'data')}
      </div>
    </div>
  </div>
</section>

<section class="band dark quote on-dark">
  <div class="wrap reveal">
    {T('„A kender nem csupán mezőgazdasági alapanyag, hanem építőipari lehetőség: természetes, megújuló és képes új irányt adni a fenntartható anyagfejlesztésnek.”', '“Hemp is not just an agricultural raw material but a construction industry opportunity: natural, renewable, and capable of giving new direction to sustainable material development.”', 'blockquote')}
    {T('— HempX Innovációs Kft. · K+F csapat', '— HempX Innovation Ltd. · R&amp;D Team', 'cite')}
  </div>
</section>

<section class="band alt">
  <div class="wrap">
    <div class="grid g2">
      <div class="reveal">
        {T('Gyorsítósáv projekt', 'Accelerator Project', 'span', 'eyebrow')}
        {T('A laboratóriumtól az <em>üzemi validációig</em>', 'From the laboratory to <em>industrial validation</em>', 'h2')}
        {T('Projektünk kiindulópontja egy laboratóriumban tesztelt alfa prototípus; a cél az üzemi környezetben validált, műszakilag dokumentált, TRL7 szintű kenderkompozit építőanyag-család.', 'Our project starts from a laboratory-tested alpha prototype; the goal is a TRL7-level hemp composite building material family – validated in an industrial environment and technically documented.', 'p', 'lede')}
        <div class="chips">
          {T('Homlokzati és burkolati panelek', 'Facade and cladding panels', 'span', 'chip plain')}
          {T('Hibrid fa–kenderkompozit elemek', 'Hybrid timber–hemp elements', 'span', 'chip plain')}
          {T('Önthető kenderkompozit', 'Castable hemp composite', 'span', 'chip plain')}
        </div>
        <div class="actions"><a class="btn btn-solid" href="projekt.html">{T('Részletek a projektről →', 'Project details →')}</a></div>
      </div>
      <div class="frame reveal" style="aspect-ratio:4/3"><img src="assets/termekek.webp" alt="Kenderkompozit panelek és blokkok a telephelyen" width="1600" height="1200" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="band">
  <div class="wrap">
    <div class="reveal" style="margin-bottom:2.5rem">
      {T('Laborban és üzemben', 'In the lab and on the line', 'span', 'eyebrow')}
      {T('Mérhető, <em>dokumentált</em> fejlesztés', 'Measurable, <em>documented</em> development', 'h2')}
    </div>
    <div class="grid g3">
      <div class="frame reveal" style="aspect-ratio:3/4"><img src="assets/labor.webp" alt="Szegedi Tudományegyetem műszeres laboratóriuma" width="900" height="1200" loading="lazy"></div>
      <div class="frame reveal" style="aspect-ratio:3/4"><img src="assets/keveres.webp" alt="Kenderkeverék kitöltése a formába" width="784" height="1100" loading="lazy"></div>
      <div class="frame reveal" style="aspect-ratio:3/4"><img src="assets/gyartosor.webp" alt="Blokkgyártó sor" width="1050" height="1400" loading="lazy"></div>
    </div>
    <div class="actions" style="justify-content:center">
      <a class="btn btn-line" href="{LINKEDIN}" target="_blank" rel="noopener">{T('Kövess minket LinkedIn-en ↗', 'Follow us on LinkedIn ↗')}</a>
    </div>
  </div>
</section>
'''
    h += newsletter() + footer()
    return h


# ═══════════════════════════ PROJEKT ═══════════════════════════
def partner(logo, name_hu, name_en, role_hu, role_en, txt_hu, txt_en, alt):
    return f'''<div class="card partner reveal">
  <div class="top"><div class="logo"><img src="assets/{logo}" alt="{alt}"></div>
  <div>{T(name_hu, name_en, 'h3') if name_en else f'<h3>{name_hu}</h3>'}{T(role_hu, role_en, 'div', 'role')}</div></div>
  {T(txt_hu, txt_en, 'p')}
</div>'''


def prod(no, h_hu, h_en, items):
    lis = ''.join(f'<li data-en="{html.escape(e, quote=True)}">{hu}</li>' for hu, e in items)
    return f'<div class="card reveal"><span class="no">{no}</span>{T(h_hu, h_en, "h3")}<ul>{lis}</ul></div>'


def faq(q_hu, q_en, a_hu, a_en):
    return f'''<div class="faq-item"><button class="faq-q" aria-expanded="false">{T(q_hu, q_en)}<span class="plus">+</span></button>
<div class="faq-a">{T(a_hu, a_en, 'p')}</div></div>'''


def projekt():
    h = head('Gyorsítósáv projekt | Kender kompozit építőanyag fejlesztés | HempX',
             'A HempX Innovációs Kft. NKFI Gyorsítósáv projektje: kender–mész–adhezív alapú, fenntartható építőipari kompozitok fejlesztése TRL7 technológiai szintig.',
             ('Accelerator Project | Hemp Composite Building Material Development | HempX',
              'The HempX Innovation Ltd. NRDI Accelerator project: developing hemp–lime–adhesive based sustainable construction composites up to TRL7.'))
    h += nav('projekt')
    h += f'''
<header class="page-hero">
  <div>
    {T('NKFI Gyorsítósáv · 2025–2027', 'NRDI Accelerator Programme · 2025–2027', 'span', 'eyebrow')}
    {T('Kender kompozit alapú <em>építőanyagok</em> fejlesztése', 'Development of hemp composite <em>building materials</em>', 'h1')}
    {T('A HempX a Nemzeti Kutatási, Fejlesztési és Innovációs Alap Gyorsítósáv programjának támogatásával kender–mész–adhezív alapú kompozit építőanyag-családot fejleszt. A kiindulópont egy laboratóriumban tesztelt alfa prototípus; a cél az üzemi környezetben validált, műszakilag dokumentált TRL7 szint elérése.', 'With the support of the Accelerator Programme of the National Research, Development and Innovation Fund, HempX is developing a family of hemp–lime–adhesive based composite building materials. The starting point is a laboratory-tested alpha prototype; the goal is to reach TRL7 – an industrially validated, technically documented level.', 'p', 'lede')}
    <div class="chips">
      <a class="chip" href="#tamogatas" data-en="Funding">Támogatás</a>
      <a class="chip" href="#adatok" data-en="Project data">Projektadatok</a>
      <a class="chip" href="#tudomany" data-en="Science">Tudomány</a>
      <a class="chip" href="#partnerek" data-en="Partners">Partnerek</a>
      <a class="chip" href="#termekek" data-en="Products">Termékek</a>
      <a class="chip" href="#piac" data-en="Market">Piac</a>
      <a class="chip" href="#gyik" data-en="FAQ">GYIK</a>
    </div>
    <div class="actions"><a class="btn btn-solid js-news" href="#">{T('Kövesd nyomon a fejlesztéseinket', 'Follow our developments')}</a></div>
  </div>
  <div class="hero-photos" style="height:min(70vh,720px)">
    <div class="frame"><img src="assets/keveres.webp" alt="Kenderkeverék kitöltése a formába" width="784" height="1100"></div>
    <div class="frame"><img src="assets/tegla-raklap.webp" alt="Kenderkompozit blokkok raklapon" width="562" height="1000"></div>
    <div class="frame"><img src="assets/termekek.webp" alt="Kenderkompozit panelek és blokkok" width="1600" height="1200"></div>
  </div>
</header>

<!-- ───── Támogatás: kép + HempX logó + összeg (csak ezen az oldalon jelenik meg) ───── -->
<section class="band" id="tamogatas" style="padding-bottom:0">
  <div class="wrap">
    <div class="fund reveal">
      <!-- TODO: tedd a hivatalos támogatási arculati elemet (pl. NKFI / Gyorsítósáv kép) assets/tamogatas.png néven az assets mappába; a szaggatott keret ekkor automatikusan lecserélődik. -->
      <div class="fund-img">
        <img src="assets/tamogatas.png" alt="Nemzeti Kutatási, Fejlesztési és Innovációs Alap – támogatási arculati elem" onerror="this.parentNode.innerHTML='<div class=&quot;fund-ph&quot;>A támogatási arculati elem helye<br>(assets/tamogatas.png)</div>'">
      </div>
      <div class="fund-body">
        {T('Elnyert támogatás', 'Grant awarded', 'div', 'lbl')}
        {T('279 907 170 Ft', '279,907,170 HUF', 'div', 'fund-amount')}
        {T('Vissza nem térítendő támogatás az NKFI Alap Gyorsítósáv programjából. A projekt a Nemzeti Kutatási, Fejlesztési és Innovációs Alap Gyorsítósáv programjának támogatásával valósul meg.', 'Non-repayable grant from the Accelerator Programme of the NRDI Fund. The project is implemented with the support of the Accelerator Programme of the National Research, Development and Innovation Fund.', 'p')}
      </div>
      <div class="fund-logo"><img src="assets/hempx-logo.png" alt="HempX Research &amp; Development logó"></div>
    </div>
  </div>
</section>

<section class="band" id="adatok">
  <div class="wrap">
    <div class="reveal" style="margin-bottom:2.5rem">
      {T('Projektadatok', 'Project data', 'span', 'eyebrow')}
      {T('Az <em>NKFI Gyorsítósáv</em> projekt', 'The <em>NRDI Accelerator</em> project', 'h2')}
    </div>
    <div class="spec reveal">
      <div>{T('Projektazonosító', 'Project ID', 'div', 'k')}<div class="v" style="font-size:1rem">NKFIH-2025-1.1.2.-<br>Gyorsítósáv-2025-00019</div></div>
      <div>{T('Projektidőszak', 'Project period', 'div', 'k')}<div class="v big">2025–2027</div>{T('24 hónap', '24 months', 'div', 'v')}</div>
      <div>{T('Technológiai szint', 'Technology readiness', 'div', 'k')}<div class="v big">TRL4 → TRL7</div></div>
      <div>{T('Kedvezményezett', 'Beneficiary', 'div', 'k')}<div class="v big" style="font-size:1.5rem">HempX<br>Innovációs Kft.</div></div>
    </div>
  </div>
</section>

<section class="band alt" id="celok">
  <div class="wrap">
    <div class="reveal" style="margin-bottom:2.5rem">
      {T('Célkitűzések', 'Objectives', 'span', 'eyebrow')}
      {T('Öt lépés az <em>üzemi validációig</em>', 'Five steps to <em>industrial validation</em>', 'h2')}
    </div>
    <div class="grid g3">
      <div class="card reveal"><span class="no">01</span>{T('Anyagtudományi alapok', 'Materials science foundations', 'h3')}{T('A kender pozdorja, a mészbázisú kötőanyagok és a természetes adhezív komponensek kölcsönhatásainak feltárása: sűrűség, porozitás, szilárdság, nedvességállóság, tartósság.', 'Exploring the interaction of hemp hurd, lime-based binders and natural adhesives: density, porosity, strength, moisture resistance, durability.', 'p')}</div>
      <div class="card reveal"><span class="no">02</span>{T('Gyártástechnológiai fejlesztés', 'Production technology', 'h3')}{T('Professzionális keverőberendezés, egyedi blokkgyártó sor és prototípusgyártási környezet a reprodukálható, állandó minőségű előállításhoz.', 'Professional mixing equipment, a custom block production line and a prototype production environment for reproducible, consistent quality.', 'p')}</div>
      <div class="card reveal"><span class="no">03</span>{T('Prototípusok és validáció', 'Prototypes and validation', 'h3')}{T('Több termékirány prototípus-fejlesztése, vizsgálata laboratóriumi, szimulált és valós üzemi környezetben.', 'Prototype development of several product lines, tested in laboratory, simulated and real industrial environments.', 'p')}</div>
      <div class="card reveal"><span class="no">04</span>{T('Szabványosítás, minősítés', 'Standardisation and certification', 'h3')}{T('Mechanikai, fagyállósági, vízfelvételi, hőtechnikai és akusztikai vizsgálatok, tűzvédelmi besorolás előkészítése, MSZ EN szabványok szerinti akkreditált mérések.', 'Mechanical, frost-resistance, water-absorption, thermal and acoustic tests, preparation of fire classification, accredited measurements under MSZ EN standards.', 'p')}</div>
      <div class="card reveal"><span class="no">05</span>{T('Piacra jutási stratégia', 'Market-entry strategy', 'h3')}{T('Célpiacok és versenytársak elemzése, árképzés, értékesítési csatornák, kiállítások, pilot projektek és zöld közbeszerzési lehetőségek.', 'Target-market and competitor analysis, pricing, sales channels, trade fairs, pilot projects and green procurement opportunities.', 'p')}</div>
      <div class="frame reveal"><img src="assets/pozdorja.webp" alt="Ipari kender pozdorja" width="900" height="1200" loading="lazy" style="min-height:260px"></div>
    </div>
  </div>
</section>

<section class="band" id="tudomany">
  <div class="wrap">
    <div class="grid g2" style="margin-bottom:4rem">
      <div class="reveal">
        {T('Technológiai érettség', 'Technology readiness', 'span', 'eyebrow')}
        {T('A laboratóriumtól az <em>üzemi validációig</em>', 'From laboratory to <em>industrial validation</em>', 'h2')}
        <div class="trl" role="img" aria-label="TRL4 → TRL7"><div><b></b><span>TRL4</span></div><div><b></b><span>TRL5</span></div><div><b></b><span>TRL6</span></div><div><b></b><span>TRL7</span></div></div>
        <div class="trl-cap">{T('Kiindulás: laboratóriumban tesztelt alfa prototípus.', 'Starting point: laboratory-tested alpha prototype.')}{T('Cél: üzemi környezetben validált, dokumentált prototípus.', 'Goal: industrially validated, documented prototype.')}</div>
      </div>
      <div class="frame reveal" style="aspect-ratio:4/5;max-height:70vh"><img src="assets/labor.webp" alt="Szegedi Tudományegyetem műszeres laboratóriuma" width="900" height="1200" loading="lazy"></div>
    </div>
    <div class="grid g2" style="align-items:start">
      <div class="reveal">
        {T('Vizsgált anyagjellemzők', 'Material properties tested', 'h3')}
        <div class="chips">
          {''.join(f'<span class="chip plain" data-en="{e}">{hu}</span>' for hu, e in [('nyomószilárdság','compressive strength'),('hajlítószilárdság','flexural strength'),('húzószilárdság','tensile strength'),('kopásállóság','abrasion resistance'),('csúszásellenállás','slip resistance'),('vízfelvétel','water absorption'),('fagyállóság','frost resistance'),('páradiffúzió','vapour diffusion'),('hővezetés (λ)','thermal conductivity (λ)'),('akusztika','acoustics'),('tűzvédelem','fire protection'),('UV- / öregedésállóság','UV / ageing resistance')])}
        </div>
        {T('Az akkreditált, MSZ EN szabványok szerinti minősítő vizsgálatokat a Mélyépítő Labor Kft. végzi.', 'Accredited certification tests according to MSZ EN standards are carried out by Mélyépítő Labor Kft.', 'p', 'cap', 'style="font-size:1rem;margin-top:1.2rem"')}
      </div>
      <div class="reveal">
        {T('Nagyműszeres vizsgálatok · SZTE', 'Advanced instrumental analysis · University of Szeged', 'h3')}
        <div class="chips">
          <span class="chip plain">IR / Raman</span><span class="chip plain">XRD</span>
          {T('termoanalitika', 'thermal analysis', 'span', 'chip plain')}<span class="chip plain">Mikro-CT</span><span class="chip plain">SEM–EDS</span>
          {T('N₂-adszorpció', 'N₂ adsorption', 'span', 'chip plain')}{T('nedvesítési vizsgálat', 'wetting test', 'span', 'chip plain')}
        </div>
        {T('A Szegedi Tudományegyetem műszeres platformja a kötési folyamat, a pórusszerkezet és a szerkezet–tulajdonság összefüggések mélyebb megértését támogatja.', 'The instrumental platform of the University of Szeged supports a deeper understanding of the binding process, pore structure and structure–property relationships.', 'p', 'cap', 'style="font-size:1rem;margin-top:1.2rem"')}
      </div>
    </div>
  </div>
</section>

<section class="band alt" id="partnerek">
  <div class="wrap">
    <div class="reveal" style="margin-bottom:2.5rem">
      {T('Konzorcium', 'Consortium', 'span', 'eyebrow')}
      {T('Projektpartnerek és <em>szerepek</em>', 'Project partners and <em>roles</em>', 'h2')}
    </div>
    <div class="grid g4" style="grid-template-columns:repeat(auto-fit,minmax(min(620px,100%),1fr))">
      {partner('hempx-mark.png','HempX Innovációs Kft.',None,'Konzorciumvezető','Consortium leader','Receptúrák kidolgozása, a titkos know-how kezelése, prototípus- és mintagyártás, valamint a projekt szakmai és pénzügyi menedzsmentje.','Development of formulations, management of confidential know-how, prototype and sample production, and the project’s professional and financial management.','HempX')}
      {partner('szte.png','Szegedi Tudományegyetem','University of Szeged','Ipari kutatás','Industrial research','Nagyműszeres anyagvizsgálatok, mikrostruktúra-elemzés, valamint a kötési és száradási folyamatok, illetve a szerkezet–tulajdonság összefüggések feltárása.','Advanced instrumental material testing, microstructure analysis, and exploration of binding and drying processes and structure–property relationships.','SZTE')}
      {partner('melyepito.jpg','Mélyépítő Labor Kft.',None,'Akkreditált minősítés','Accredited certification','Akkreditált, MSZ EN szabványok szerinti vizsgálatok: fagyállóság, sűrűség, szilárdság és vízzárósági mérések.','Accredited testing according to MSZ EN standards: frost resistance, density, strength and water-tightness measurements.','Mélyépítő Labor')}
      {partner('macline.jpg','Macline Hungary Kft.',None,'Piacra jutás','Market entry','A piacra jutási stratégia kidolgozása, piaci igényfelmérés, üzleti partnerek azonosítása és szakmai kiállításokon való részvétel.','Development of the market-entry strategy, market needs assessment, identification of business partners, and participation in trade exhibitions.','Macline')}
    </div>
    {T('↳ Alapanyag-biztosítás: <b>Green Pol Kft.</b>', '↳ Raw material supply: <b>Green Pol Kft.</b>', 'p', '', 'style="margin-top:2rem;font-weight:600;color:var(--muted)"')}
  </div>
</section>

<section class="band dark on-dark" id="termekek">
  <div class="wrap">
    <div class="grid g2" style="margin-bottom:3.5rem">
      <div class="reveal">
        {T('Termékfejlesztések', 'Product developments', 'span', 'eyebrow')}
        {T('Kenderkompozit <em>építőanyag-család</em>', 'Hemp composite <em>building material family</em>', 'h2')}
        {T('A fejlesztés alatt álló termékek prototípus- és validációs fázisban vannak. A cél a laboratóriumi alfa prototípusoktól az üzemi környezetben validált, TRL7 szintű megoldásokig eljutni.', 'The products under development are in the prototype and validation phase. The goal is to progress from laboratory alpha prototypes to industrially validated, TRL7-level solutions.', 'p', 'lede')}
      </div>
      <div class="frame reveal" style="aspect-ratio:4/3"><img src="assets/termekek.webp" alt="Kenderkompozit panelek és blokkok a telephelyen" width="1600" height="1200" loading="lazy"></div>
    </div>
    <div class="grid g3">
      {prod('01','Homlokzati és belső burkolati panelek','Facade and interior cladding panels',[('belső falburkolatok','interior wall claddings'),('akusztikai panelek','acoustic panels'),('homlokzati panelek','facade panels'),('padlóburkolati elemek','floor covering elements'),('látszó, természetes textúrák','exposed, natural textures')])}
      {prod('02','Hibrid fa–kenderkompozit szerkezetek','Hybrid timber–hemp composite structures',[('vázkitöltő elemek','frame infill elements'),('födémszerkezeti komponensek','floor structure components'),('előregyártott moduláris rendszerek','prefabricated modular systems'),('hőszigetelő falazati elemek','thermal insulating wall elements')])}
      {prod('03','Önthető kenderkompozit rendszerek','Castable hemp composite systems',[('zsaluzott kivitelezés','formwork construction'),('moduláris építés','modular construction'),('ipari kivitelezhetőség','industrial feasibility'),('természetes anyaghasználat','use of natural materials')])}
    </div>
  </div>
</section>

<section class="band" id="piac">
  <div class="wrap">
    <div class="reveal" style="margin-bottom:2.5rem">
      {T('Piaci hasznosulás', 'Market application', 'span', 'eyebrow')}
      {T('Célcsoportok és <em>versenyelőnyök</em>', 'Target groups and <em>competitive advantages</em>', 'h2')}
      {T('Elsődleges célcsoportjaink azok az építőipari szereplők, akik fenntartható, alacsony karbonlábnyomú és innovatív anyagmegoldásokat keresnek.', 'Our primary target groups are construction industry players seeking sustainable, low-carbon and innovative material solutions.', 'p', 'lede')}
    </div>
    <div class="grid g3">
      <div class="card reveal"><span class="no">01</span>{T('Önkormányzatok és közintézmények', 'Municipalities and public institutions', 'h3')}{T('Zöld közbeszerzési szempontok mentén: közterületi és klímatudatos városfejlesztési, valamint fenntartható burkolati pilot projektekhez.', 'Along green public procurement criteria: for public space and climate-conscious urban development, and sustainable paving pilot projects.', 'p')}</div>
      <div class="card reveal"><span class="no">02</span>{T('Kivitelezők és beruházók', 'Contractors and investors', 'h3')}{T('LEED, BREEAM vagy DGNB szempontrendszer szerint megvalósuló, zöld minősítésű építkezésekhez kínálnak validált, dokumentált alternatívát.', 'A validated, documented alternative for green-certified construction under LEED, BREEAM or DGNB rating systems.', 'p')}</div>
      <div class="card reveal"><span class="no">03</span>{T('Építőanyag-kereskedelmi hálózatok', 'Building material retail networks', 'h3')}{T('Hosszabb távon a szabványosított, tanúsított és üzemi környezetben validált termékek nagyobb kereskedelmi hálózatok számára is értékesíthetővé válhatnak.', 'In the longer term, standardised, certified products validated in an industrial environment may become marketable through larger retail networks.', 'p')}</div>
    </div>
    <div class="reveal" style="margin-top:4rem;padding-top:3rem;border-top:2px solid var(--line)">
      {T('Versenyelőnyök', 'Competitive advantages', 'span', 'eyebrow')}
      <div class="adv">
        {''.join(f'<div data-en="{e}">{hu}</div>' for hu, e in [('Hiánypótló termékkategória Magyarországon','A gap-filling product category in Hungary'),('TRL7 szintű validációs cél','TRL7-level validation target'),('Hazai fejlesztés és gyártási know-how','Domestic development and manufacturing know-how'),('Rövidebb ellátási lánc','Shorter supply chain'),('Alacsony karbonlábnyomú alapanyaghasználat','Low-carbon raw material use'),('Egyetemi és akkreditált laboratóriumi háttér','University and accredited laboratory background')])}
      </div>
    </div>
  </div>
</section>

<section class="band alt" id="gyik">
  <div class="wrap">
    <div class="reveal">
      {T('GYIK', 'FAQ', 'span', 'eyebrow')}
      {T('Gyakran ismételt <em>kérdések</em>', 'Frequently asked <em>questions</em>', 'h2')}
    </div>
    <div class="faq reveal" style="margin-top:2rem">
      {faq('Mi az a kenderkompozit építőanyag?','What is a hemp composite building material?','Olyan építőipari anyag, amely ipari kenderből származó komponenseket – például pozdorját – kötőanyagokkal és adalékokkal kombinál. A HempX projektben a fejlesztés kender–mész–adhezív rendszerekre épül.','A construction material that combines components derived from industrial hemp – such as hurd – with binders and additives. In the HempX project, development is based on hemp–lime–adhesive systems.')}
      {faq('Ugyanaz, mint a hagyományos kenderbeton?','Is it the same as traditional hempcrete?','Nem teljesen. A hagyományos hempcrete főként hőszigetelő és vázkitöltő anyagként ismert. A HempX projekt ennél szélesebb alkalmazási kört vizsgál, többek között burkolati és szerkezeti elemek irányába, javított mechanikai és tartóssági jellemzőkkel.','Not entirely. Traditional hempcrete is mainly known as a thermal insulation and frame-infill material. The HempX project investigates a broader range of applications, including cladding and structural elements, with improved mechanical and durability properties.')}
      {faq('Kereskedelmi forgalomban vannak már a termékek?','Are the products already commercially available?','A projekt jelenleg kutatás-fejlesztési és prototípus-validációs szakaszban van. A cél a TRL7 technológiai érettségi szint elérése, amely üzemi környezetben validált prototípusokat jelent.','The project is currently in the research, development and prototype-validation phase. The goal is to reach TRL7, meaning prototypes validated in an industrial environment.')}
      {faq('Miért fenntartható a kenderalapú építőanyag?','Why is hemp-based building material sustainable?','Az ipari kender gyorsan növő, évente megújuló növény, amely növekedése során szén-dioxidot köt meg. Regionális termesztése csökkentheti a szállítási igényt, építőipari felhasználása pedig hozzájárulhat az alacsony karbonlábnyomú építéshez.','Industrial hemp is a fast-growing, annually renewable plant that binds carbon dioxide as it grows. Its regional cultivation can reduce transport needs, and its use in construction can contribute to low-carbon building.')}
      {faq('Milyen vizsgálatok igazolják a termékek teljesítményét?','What tests verify the performance of the products?','Mechanikai, hőtechnikai, akusztikai, nedvességállósági, fagyállósági, kopásállósági és nagyműszeres anyagszerkezeti vizsgálatok. Az akkreditált méréseket a Mélyépítő Labor Kft., a nagyműszeres vizsgálatokat a Szegedi Tudományegyetem végzi.','Mechanical, thermal, acoustic, moisture-resistance, frost-resistance, abrasion-resistance and advanced instrumental material-structure tests. Accredited measurements are carried out by Mélyépítő Labor Kft., instrumental analyses by the University of Szeged.')}
    </div>
  </div>
</section>
'''
    h += newsletter()
    h = h.replace('<footer>', '<footer>', 1)
    f = footer().replace('<div class="foot-bottom">', f'<div class="foot-bottom"><span style="font-size:.85rem">{PID}</span>', 1)
    return h + f


# ═══════════════════════════ KAPCSOLAT ═══════════════════════════
def kapcsolat():
    h = head('Kapcsolat | HempX Innovációs Kft.',
             'Vegye fel a kapcsolatot a HempX Innovációs Kft.-vel kutatási együttműködés, beruházás, partnerség vagy zöld közbeszerzési lehetőség ügyében.',
             ('Contact | HempX Innovation Ltd.',
              'Get in touch with HempX Innovation Ltd. about research collaboration, investment, partnership or green procurement opportunities.'))
    h += nav('kapcsolat')
    h += f'''
<header class="page-hero" style="min-height:100vh;align-items:center">
  <div>
    {T('Kapcsolat', 'Contact', 'span', 'eyebrow')}
    {T('Építsük együtt a <em>kenderalapú</em> építőipart', 'Let’s build the <em>hemp-based</em> construction industry together', 'h1')}
    {T('Legyen szó kutatási együttműködésről, beruházásról, partnerségről vagy zöld közbeszerzési lehetőségről – örömmel beszélünk Önnel a HempX fejlesztéseiről.', 'Whether it’s research collaboration, investment, partnership or green procurement opportunities – we’d be happy to talk to you about HempX’s developments.', 'p', 'lede')}
    <div style="margin-top:2.5rem">
      <div class="detail">{T('Cég', 'Company', 'span', 'l')}<span>HempX Innovációs Kft.</span></div>
      <div class="detail">{T('Ország', 'Country', 'span', 'l')}{T('Magyarország', 'Hungary')}</div>
      <div class="detail">{T('Közösségi', 'Social', 'span', 'l')}<a href="{LINKEDIN}" target="_blank" rel="noopener" style="font-weight:700;color:var(--green)">LinkedIn ↗</a></div>
    </div>
  </div>
  <div class="contact-card reveal">
    {T('Írjon nekünk', 'Write to us', 'span', 'eyebrow')}<br>
    <a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
    {T('Kérdéseivel, együttműködési vagy partnerségi javaslataival forduljon hozzánk közvetlenül e-mailben.', 'Please contact us directly by email with any questions, collaboration ideas or partnership proposals.', 'p', '', 'style="margin:1.5rem 0 2rem;font-size:1.1rem;color:var(--muted)"')}
    <div class="actions" style="margin-top:0">
      <a class="btn btn-solid" href="mailto:{EMAIL}">{T('E-mail küldése', 'Send email')}</a>
      <a class="btn btn-line js-news" href="#">{T('Kövesd nyomon a fejlesztéseinket', 'Follow our developments')}</a>
    </div>
  </div>
</header>
'''
    return h + footer()


for name, fn in [('index.html', index), ('projekt.html', projekt), ('kapcsolat.html', kapcsolat)]:
    (OUT / name).write_text(fn(), encoding='utf-8')
    print('written', name)
