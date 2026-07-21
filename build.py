import os
import json

with open("content/data.json", encoding="utf-8") as f:
    DATA = json.load(f)

with open("content/photos-info.json", encoding="utf-8") as f:
    PHOTOS = json.load(f)

PAGES = [
    ("index", "Accueil"),
    ("services", "Nos Services"),
    ("pourquoi-nous-choisir", "Pourquoi nous choisir"),
    ("contact", "Contact"),
]

WHATSAPP_SVG = '<svg viewBox="0 0 24 24" fill="white"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.32 4.95L2 22l5.29-1.39a9.9 9.9 0 0 0 4.75 1.21h.01c5.46 0 9.9-4.45 9.9-9.91C21.96 6.45 17.5 2 12.04 2zm5.79 14.11c-.24.68-1.4 1.3-1.93 1.35-.5.05-1.12.07-1.81-.11-.42-.11-.95-.29-1.64-.57-2.9-1.25-4.79-4.17-4.94-4.36-.14-.2-1.19-1.58-1.19-3.02 0-1.43.75-2.14 1.02-2.43.27-.29.58-.37.78-.37.19 0 .39 0 .56.01.18.01.42-.07.65.5.24.58.82 2 .89 2.14.07.14.12.31.02.5-.09.19-.14.31-.28.48-.14.17-.29.37-.42.5-.14.14-.28.29-.12.57.16.28.71 1.17 1.53 1.89 1.05.94 1.94 1.23 2.22 1.37.28.14.44.12.61-.07.16-.19.7-.82.89-1.1.19-.28.37-.23.63-.14.26.09 1.65.78 1.93.92.28.14.47.21.54.33.07.12.07.68-.17 1.36z"/></svg>'
FACEBOOK_SVG = '<svg viewBox="0 0 24 24" fill="white"><path d="M13.5 21v-7.5h2.5l.4-3H13.5V8.5c0-.87.24-1.46 1.49-1.46H16.5V4.36C16.24 4.32 15.36 4.25 14.33 4.25c-2.15 0-3.63 1.31-3.63 3.72v2.53H8.2v3h2.5V21h2.8z"/></svg>'
TIKTOK_SVG = '<svg viewBox="0 0 24 24" fill="white"><path d="M16.6 5.82c-.9-.6-1.55-1.55-1.75-2.65h-2.85v12.6c0 1.35-1.1 2.45-2.45 2.45a2.45 2.45 0 0 1 0-4.9c.25 0 .5.04.73.1V10.4a5.3 5.3 0 0 0-.73-.05A5.3 5.3 0 1 0 15 15.65V9.35a7.3 7.3 0 0 0 4.2 1.33V7.83c-.9 0-1.85-.3-2.6-.85z"/></svg>'
PHONE_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
PLAY_SVG = '<svg viewBox="0 0 24 24" fill="white"><path d="M8 5v14l11-7z"/></svg>'
PAUSE_SVG = '<svg viewBox="0 0 24 24" fill="white"><path d="M6 5h4v14H6zM14 5h4v14h-4z"/></svg>'

def svg_filters():
    return """
<svg width="0" height="0" style="position:absolute">
  <defs>
    <filter id="roughen" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.03 0.09" numOctaves="2" seed="3" result="noise">
        <animate attributeName="seed" values="3;7;3" dur="2.2s" repeatCount="indefinite"/>
      </feTurbulence>
      <feDisplacementMap in="SourceGraphic" in2="noise" scale="4"/>
    </filter>
    <filter id="roughen2" x="-20%" y="-20%" width="140%" height="140%">
      <feTurbulence type="fractalNoise" baseFrequency="0.025 0.08" numOctaves="2" seed="9" result="noise2">
        <animate attributeName="seed" values="9;14;9" dur="2.6s" repeatCount="indefinite"/>
      </feTurbulence>
      <feDisplacementMap in="SourceGraphic" in2="noise2" scale="5"/>
    </filter>
  </defs>
</svg>
"""

def sketch_border():
    return """
<svg class="sketch-border" preserveAspectRatio="none">
  <rect class="mag" x="1" y="1" width="calc(100% - 2px)" height="calc(100% - 2px)"/>
  <rect x="1" y="1" width="calc(100% - 2px)" height="calc(100% - 2px)"/>
</svg>
"""

def social_bar():
    return f"""
<div class="social-bar">
  <a class="social whatsapp" href="https://wa.me/{DATA['whatsapp_number']}" target="_blank" aria-label="WhatsApp">{WHATSAPP_SVG}</a>
  <a class="social facebook" href="#" target="_blank" aria-label="Facebook">{FACEBOOK_SVG}</a>
  <a class="social tiktok" href="{DATA['tiktok_url']}" target="_blank" aria-label="TikTok">{TIKTOK_SVG}</a>
</div>
"""

def float_whatsapp():
    return f'<a class="float-wa" href="https://wa.me/{DATA["whatsapp_number"]}" target="_blank" aria-label="Ecrire sur WhatsApp">{WHATSAPP_SVG}</a>'

def triangle(size_class="tri-stage", spin_duration=None):
    dur_style = f' style="animation-duration:{spin_duration}"' if spin_duration else ""
    return f"""
<div class="{size_class}">
  <div class="tri-glow"></div>
  <div class="tri-float">
    <div class="tri-spin"{dur_style}>
      <img src="assets/triangle-mark.png" alt="">
    </div>
  </div>
</div>
"""

def nav(active):
    items = ""
    for slug, label in PAGES:
        href = "index.html" if slug == "index" else f"{slug}.html"
        cls = "active" if slug == active else ""
        items += f'<a class="{cls}" href="{href}">{label}</a>\n'
    return f"""
<header>
  <div class="nav">
    <a class="logo" href="index.html"><img src="assets/logo-white.png" alt="Averon Technologies"></a>
    <nav class="menu" id="menu">
      {items}
      <a class="cta" href="contact.html">Demander un devis</a>
    </nav>
    <div class="actions">
      <a class="call" href="tel:+{DATA['whatsapp_number']}" aria-label="Appeler">{PHONE_SVG}</a>
      <button class="burger" onclick="document.getElementById('menu').classList.toggle('open')" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>
"""

def footer():
    return """
<footer>
  <span>&copy; 2026 Averon Technologies</span>
  <span>Burkina Faso &middot; Afrique de l'Ouest &middot; +226 66603024 / 78190761</span>
  <a href="galerie.html" style="text-decoration:underline;">Galerie</a>
</footer>
"""

def page(slug, title, body, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} &middot; Averon Technologies</title>
<link rel="stylesheet" href="assets/style.css">
{extra_head}
</head>
<body>
{svg_filters()}
{nav(slug)}
{body}
{footer()}
{float_whatsapp()}
<script>
(function(){{
  var els = document.querySelectorAll('.scroll-expand');
  if(!('IntersectionObserver' in window)){{
    els.forEach(function(e){{ e.classList.add('in-view'); }});
    return;
  }}
  var io = new IntersectionObserver(function(entries){{
    entries.forEach(function(entry){{
      if(entry.isIntersecting){{
        entry.target.classList.add('in-view');
        io.unobserve(entry.target);
      }}
    }});
  }}, {{ threshold:0.2 }});
  els.forEach(function(e){{ io.observe(e); }});
}})();
</script>
</body>
</html>
"""

def hero_home():
    """Hero : triangle 3D + stats, page Accueil uniquement (video deplacee plus bas)."""
    return f"""
<section class="hero">
  <div class="hero-bg-photo"><img src="{PHOTOS['hero_photo'].lstrip('/')}" alt=""></div>
  <div class="stripe"></div>
  <div class="wrap">
    <div class="hero-text">
      <div class="status-badge"><span class="dot"></span>Disponible maintenant</div>
      <div class="kicker">{DATA['hero_kicker']}</div>
      <h1>{DATA['hero_title']}</h1>
      <p>{DATA['hero_subtitle']}</p>
      <div class="cta-row">
        <a class="btn primary" href="tel:+{DATA['whatsapp_number']}">Appeler maintenant</a>
        <a class="btn ghost" href="https://wa.me/{DATA['whatsapp_number']}" target="_blank">WhatsApp</a>
      </div>
    </div>
    {triangle()}
  </div>
</section>
<div class="stats">
  <div class="stat"><div class="n">{DATA['stat_1_value']}</div><div class="l">{DATA['stat_1_label']}</div></div>
  <div class="stat"><div class="n">{DATA['stat_2_value']}</div><div class="l">{DATA['stat_2_label']}</div></div>
  <div class="stat"><div class="n">{DATA['stat_3_value']}</div><div class="l">{DATA['stat_3_label']}</div></div>
  <div class="stat"><div class="n">{DATA['stat_4_value']}</div><div class="l">{DATA['stat_4_label']}</div></div>
</div>
"""

def video_section():
    """Section video dédiée, placee entre les 5 pôles et Pourquoi nous choisir."""
    return f"""
<section class="video-section">
  <div class="video-wrap">
    <video id="heroVideo" autoplay muted loop playsinline poster="assets/photos/portrait-solar-drill.jpg">
      <source src="assets/hero-video.mp4" type="video/mp4">
    </video>
    <button class="video-toggle" id="videoToggle" aria-label="Pause/lecture video">{PAUSE_SVG}</button>
    <div class="video-caption">
      <div class="kicker-sm" style="margin-bottom:6px;">En action</div>
      <h2 style="color:#fff; margin-bottom:0;">Nos équipes sur le terrain</h2>
    </div>
  </div>
</section>
<script>
(function(){{
  var v = document.getElementById('heroVideo');
  var btn = document.getElementById('videoToggle');
  if(!btn) return;
  btn.addEventListener('click', function(){{
    if(v.paused){{ v.play(); btn.innerHTML = '{PAUSE_SVG}'; }}
    else{{ v.pause(); btn.innerHTML = '{PLAY_SVG}'; }}
  }});
}})();
</script>
"""

def hero_inner(kicker_text, title, sub):
    """Hero sobre pour pages internes : badge triangle + texte, sans video."""
    return f"""
<section class="hero" style="min-height:auto;">
  <div class="stripe"></div>
  <div class="wrap">
    <div class="hero-text">
      {triangle("tri-badge")}
      <div class="kicker">{kicker_text}</div>
      <h1>{title}</h1>
      <p>{sub}</p>
    </div>
  </div>
</section>
"""

def contact_strip():
    return f"""
<section class="contact-strip">
  <div class="wrap">
    <h2>Un projet en tête ? Parlons-en.</h2>
    <div class="links">
      <a class="btn primary" href="tel:+{DATA['whatsapp_number']}">Appeler : {DATA['phone_1']}</a>
      <a class="btn ghost" href="https://wa.me/{DATA['whatsapp_number']}" target="_blank">WhatsApp</a>
    </div>
    {social_bar()}
  </div>
</section>
"""

def svc(num, title, desc, tags):
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    return f"""
<div class="svc">
  <div class="body">
    <div class="num">{num}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
    <div class="tags">{tag_html}</div>
  </div>
</div>
"""

def svc_photo(num, title, desc, tags, photo):
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    return f"""
<div class="svc with-photo">
  <div class="thumb"><img class="scroll-expand" src="assets/photos/{photo}" alt="{title}"></div>
  <div class="body">
    <div class="num">{num}</div>
    <h3>{title}</h3>
    <p>{desc}</p>
    <div class="tags">{tag_html}</div>
  </div>
</div>
"""

PHONE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>'
PIN_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>'
MAIL_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 6-10 7L2 6"/></svg>'
GLOBE_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>'

CERT_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="6"/><path d="M15.5 13.5 17 22l-5-3-5 3 1.5-8.5"/></svg>'
CLOCK_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>'
MAP_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M1 6v16l7-4 8 4 7-4V2l-7 4-8-4z"/><path d="M8 2v16M16 6v16"/></svg>'
HOME_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/></svg>'
GRAD_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 10 12 5 2 10l10 5 10-5z"/><path d="M6 12v5c0 1.5 2.5 3 6 3s6-1.5 6-3v-5"/></svg>'
CHECK_ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>'

def point_icon(icon, title, desc):
    return f"""
<div class="point point-icon">
  <div class="picon">{icon}</div>
  <h4>{title}</h4>
  <p>{desc}</p>
</div>
"""

def point(num, title, desc):
    return f"""
<div class="point">
  <div class="num">{num}</div>
  <h4>{title}</h4>
  <p>{desc}</p>
</div>
"""

def photo_section_open(photo, extra_class=""):
    return f"""
<section class="photo {extra_class}">
  <div class="photo-bg tint"><img src="assets/photos/{photo}" alt=""></div>
  <div class="wrap">
"""

def photo_section_close():
    return "</div></section>"

def pipeline():
    return """
<div class="pipeline">
  <svg viewBox="0 0 400 40" preserveAspectRatio="none">
    <line x1="0" y1="20" x2="400" y2="20" stroke="#33353D" stroke-width="6"/>
    <line class="flow" x1="0" y1="20" x2="400" y2="20" stroke="#0EA5D9" stroke-width="3"/>
    <circle class="spark" cx="60" cy="20" r="4" fill="#E31C64" style="animation:sparkPulse 1.2s ease-in-out infinite;"/>
    <circle class="spark" cx="200" cy="20" r="4" fill="#E31C64" style="animation:sparkPulse 1.2s ease-in-out 0.4s infinite;"/>
    <circle class="spark" cx="340" cy="20" r="4" fill="#E31C64" style="animation:sparkPulse 1.2s ease-in-out 0.8s infinite;"/>
  </svg>
</div>
"""

def people_card(photo, role, text):
    return f"""
<div class="people-card">
  <img class="scroll-expand" src="assets/photos/{photo}" alt="">
  <div>
    <div class="role">{role}</div>
    <p>{text}</p>
  </div>
</div>
"""

# =========================================================
# ACCUEIL
# =========================================================
body = hero_home()
body += "<section><div class=\"wrap\">"
body += '<div class="kicker-sm">Nos domaines</div><h2>Cinq pôles d\'expertise</h2><p class="lead">De la fourniture a la maintenance, un accompagnement complet sur vos installations industrielles et énergétiques.</p>'
body += '<div class="svc-grid">'
body += svc_photo("01", "Mécanique", "Pompes, compresseurs, ventilation, froid et climatisation, réseaux hydrauliques.", ["Pompes", "Compresseurs", "Climatisation"], "pump-industrial.jpg")
body += svc_photo("02", "Énergies fossiles et renouvelables", "Groupes électrogènes, installations solaires, lubrifiants, pièces de rechange.", ["Groupes électrogènes", "Solaire"], "generator-yellow-open.jpg")
body += svc_photo("03", "Automatisme", "Automates programmables, armoires de commande, câblage et supervision industrielle.", ["Automates", "Armoires"], "electrical-panel-plc.jpg")
body += svc_photo("04", "Sécurité incendie", "Matériel de sécurité, alarmes connectées, contrôle d'accès.", ["Incendie", "Alarmes"], "helmet-industrial.jpg")
body += '</div>'
body += "</div></section>"

body += video_section()

body += photo_section_open("portrait-hvac-rooftop.jpg")
body += '<div class="kicker-sm">Pourquoi nous</div><h2>Pourquoi choisir Averon Technologies</h2>'
body += '<div class="points">'
body += point("01", "Expertise certifiée", "Une équipe technique formée et qualifiée sur chaque domaine.")
body += point("02", "Réactivité 24/7", "Une disponibilité continue pour les urgences industrielles.")
body += point("03", "Maintenance locale", "Un service de proximité adapte au contexte africain.")
body += "</div>"
body += photo_section_close()

body += contact_strip()
open("index.html", "w").write(page("index", "Accueil", body))

# =========================================================
# NOS SERVICES
# =========================================================
body = hero_inner("Nos Services", "Une gamme complète, un seul interlocuteur", "Mécanique, énergies fossiles et renouvelables, automatisme : nos trois pôles techniques au service de vos installations.")

body += '<section id="mecanique"><div class="wrap"><div class="kicker-sm">01 — Mécanique</div><h2>Fourniture, pose, maintenance</h2><p class="lead">Une gamme complète d\'équipements mécaniques pour vos installations industrielles.</p>'
body += '<div class="svc-grid">'
body += svc_photo("1.1", "Pompes et compresseurs", "Pompes centrifuges, axiales, à vis, à pistons, immergées et de surface. Compresseurs à pistons, à vis, axiaux, centrifuges.", ["Pompes centrifuges", "Compresseurs"], "mecanique-station-pompage.jpg")
body += svc_photo("1.2", "Ventilateurs / extracteurs", "Ventilateurs centrifuges et axiaux. Renouvellement et traitement d'air, désenfumage, sécurité incendie.", ["Centrifuges", "Axiaux", "Désenfumage"], "mecanique-ventilateur.jpg")
body += svc_photo("1.3", "Froid et climatisation", "Systèmes VRV/VRF, splits et multisplits, centrales de traitement d'air, chambres froides, chillers.", ["VRV/VRF", "CTA", "Chillers"], "portrait-hvac-rooftop.jpg")
body += svc_photo("1.4", "Réseaux hydrauliques et aérauliques", "Alimentation en eau, réseau de lutte anti-incendie, gaines aérauliques, évacuation et assainissement.", ["Alimentation eau", "Anti-incendie"], "mecanique-reseaux-hdpe.jpg")
body += '</div>'
body += "</div></section>"
body += pipeline()

body += photo_section_open("generator-white.jpg", "alt")
body += '<div class="kicker-sm">02 — Énergies fossiles et renouvelables</div><h2>Alimenter vos installations, en continu</h2><p class="lead">Groupes électrogènes, solutions solaires et pièces de rechange pour une énergie fiable.</p>'
body += '<div class="svc-grid">'
body += svc_photo("2.1", "Groupes électrogènes", "Perkins, Caterpillar, Cummins. ATS/inverseurs automatiques, alimentation en carburant, mise à la terre.", ["Perkins", "Caterpillar", "ATS"], "generator-yellow-open.jpg")
body += svc_photo("2.2", "Installations solaires", "Panneaux photovoltaïques, onduleurs hybrides, batteries lithium, BMS.", ["Photovoltaique", "Batteries lithium"], "solar-installation.jpg")
body += '</div>'
body += '<div class="svc-grid">'
body += svc_photo("2.3", "Lubrifiants et graisses", "Gamme complète pour moteurs et équipements industriels.", ["Lubrifiants", "Graisses"], "compressor-blue.jpg")
body += svc_photo("2.4", "Pièces de rechange", "Groupes électrogènes, moteurs, radiateurs, turbos, produits d'entretien.", ["Moteurs", "Turbos", "Entretien"], "generator-white.jpg")
body += '</div>'
body += photo_section_close()
body += pipeline()

body += '<section id="automatisme"><div class="wrap"><div class="kicker-sm">03 — Automatisme</div><h2>Automates et armoires de commande</h2><p class="lead">Programmation, intégration et câblage d\'automates industriels pour le pilotage de vos installations.</p>'
body += '<div class="svc-grid">'
body += svc_photo("3.1", "Automates programmables (PLC)", "Intégration et configuration d'automates pour le contrôle et la supervision de vos équipements industriels.", ["PLC", "Supervision"], "portrait-plc-panel.jpg")
body += svc_photo("3.2", "Armoires de commande", "Câblage, montage et mise en service d'armoires électriques et de commande.", ["Câblage", "Armoires"], "portrait-electrical-panel.jpg")
body += svc_photo("3.3", "Installation et mise en service", "Pose et raccordement d'armoires de commande sur site, y compris en extérieur.", ["Installation", "Site"], "automatisme-armoire-exterieure.jpg")
body += '</div>'
body += "</div></section>"
body += pipeline()

body += photo_section_open("helmet-industrial.jpg")
body += '<div class="kicker-sm">04 — Sécurité incendie</div><h2>Fourniture de matériels liés à la sécurité</h2><p class="lead">Des équipements et systèmes de sécurité modernes, en partenariat avec Sécuriconfiance.</p>'
body += svc("4.1", "Matériel de sécurité incendie", "Extincteurs, dévidoirs, robinets d'incendie, réseaux de lutte anti-incendie.", ["Extincteurs", "Dévidoirs", "Réseaux"])
body += svc("4.2", "Alarmes connectées", "Systèmes reliés à internet (Wi-Fi, 3G/4G/GSM), surveillance et alertes en temps réel, gestion à distance.", ["Wi-Fi/GSM", "Temps réel"])
body += svc("4.3", "Contrôle d'accès et clôtures", "Systèmes biométriques, clôtures électrifiées, portails sécurisés.", ["Biométrie", "Clôtures"])
body += svc("4.4", "Partenariat Sécuriconfiance", "Expertise technique certifiée, réactivité 24/7, formation des équipes internes, conformité réglementaire.", ["Certifié", "24/7", "Formation"])
body += photo_section_close()

body += contact_strip()
open("services.html", "w").write(page("services", "Nos Services", body))

# =========================================================
# POURQUOI NOUS CHOISIR
# =========================================================
body = hero_inner("Pourquoi nous choisir", "Notre engagement", "Un partenaire technique fiable pour vos projets industriels et énergétiques.")
body += '<section><div class="wrap"><div class="points-grid">'
body += point_icon(CERT_ICON, "Expertise technique certifiée", "Une équipe formée et qualifiée sur chaque domaine.")
body += point_icon(CLOCK_ICON, "Réactivité 24/7", "Disponibilité continue pour vos urgences.")
body += point_icon(MAP_ICON, "Solutions adaptées au contexte africain", "Des réponses pensées pour les réalités locales.")
body += point_icon(HOME_ICON, "Maintenance purement locale", "Un service de proximité, sans dépendance à l'étranger.")
body += point_icon(GRAD_ICON, "Formation des équipes internes", "Transfert de compétences vers vos équipes.")
body += point_icon(CHECK_ICON, "Respect des normes et traçabilité", "Conformité réglementaire et suivi des équipements.")
body += "</div></div></section>"

body += '<section class="alt"><div class="wrap"><div class="kicker-sm">L\'équipe terrain</div><h2>Des techniciens Averon sur chaque intervention</h2>'
body += '<div class="people">'
body += people_card("portrait-vest-car.jpg", "Intervention terrain", "Equipement de sécurité complet, identification Averon visible sur chaque mission.")
body += people_card("portrait-electrical-panel.jpg", "Automatisme et électricité", "Maintenance et câblage d'armoires de commande sur site client.")
body += people_card("portrait-solar-drill.jpg", "Installations solaires", "Montage et raccordement de panneaux photovoltaïques en toiture.")
body += "</div></div></section>"

body += contact_strip()
open("pourquoi-nous-choisir.html", "w").write(page("pourquoi-nous-choisir", "Pourquoi nous choisir", body))

# =========================================================
# CONTACT
# =========================================================
body = hero_inner("Contact", "Parlons de votre projet", "Une question, un devis, une intervention urgente : contactez-nous directement.")
body += f"""
<section><div class="wrap">
  <div class="contact-card">
    <div class="contact-row">{PHONE_ICON}<div><span class="cc-label">Téléphone</span><span class="cc-value">{DATA['phone_1']} / {DATA['phone_2']}</span></div></div>
    <div class="contact-row">{PIN_ICON}<div><span class="cc-label">Localisation</span><span class="cc-value">{DATA['location']}</span></div></div>
    <div class="contact-row">{MAIL_ICON}<div><span class="cc-label">Email</span><span class="cc-value">{DATA['email']}</span></div></div>
    <div class="contact-row">{GLOBE_ICON}<div><span class="cc-label">Réseaux sociaux</span><span class="cc-value">Facebook et TikTok — Averon Technologies</span></div></div>
  </div>
</div></section>
"""

body += f"""
<section class="alt">
  <div class="wrap">
    <div class="form-wrap">
      <div class="form-badge">Demande de devis</div>
      <h2>Décrivez votre besoin</h2>
      <p class="lead">Envoyez-nous votre demande directement, ou continuez sur WhatsApp si vous préférez.</p>
      <form class="form-card" action="https://formspree.io/f/mojgwpza" method="POST">
        <label for="cf-name">Nom complet</label>
        <div class="field-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></svg>
          <input type="text" id="cf-name" name="name" required placeholder="Votre nom">
        </div>
        <label for="cf-phone">Téléphone</label>
        <div class="field-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.362 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.338 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <input type="tel" id="cf-phone" name="phone" required placeholder="+226 XX XX XX XX">
        </div>
        <label for="cf-subject">Domaine concerné</label>
        <div class="field-wrap">
          <svg viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="2"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/></svg>
          <input type="text" id="cf-subject" name="subject" placeholder="Mécanique, énergies, sécurité incendie...">
        </div>
        <label for="cf-message">Message</label>
        <textarea id="cf-message" name="message" required placeholder="Décrivez votre besoin"></textarea>
        <button type="submit">Envoyer la demande
          <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" width="16" height="16"><path d="M5 12h14M13 5l7 7-7 7"/></svg>
        </button>
      </form>
    </div>
  </div>
</section>
"""

body += contact_strip()
open("contact.html", "w").write(page("contact", "Contact", body))

# =========================================================
# GALERIE
# =========================================================
import glob
gallery_files = sorted(glob.glob("assets/photos/gallery/*.jpg"))
body = hero_inner("Galerie", "Nos réalisations", "Un aperçu du matériel et des interventions Averon Technologies sur le terrain.")
body += '<section><div class="wrap"><div class="gallery-grid">'
for gf in gallery_files:
    rel = gf.replace("\\", "/")
    body += f'<div class="gallery-item"><img class="scroll-expand" src="{rel}" alt="Réalisation Averon Technologies" loading="lazy"></div>'
body += '</div></div></section>'
body += contact_strip()
open("galerie.html", "w").write(page("galerie", "Galerie", body))

print("Pages generees :", [f for f in os.listdir(".") if f.endswith(".html")])
