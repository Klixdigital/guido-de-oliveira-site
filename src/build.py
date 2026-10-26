"""Génère le site statique de Guido De Oliveira (FR / NL / EN) dans site/.

    python src/images.py   # une fois, après ajout de photos d'œuvres
    python src/build.py

Le contenu (œuvres, liens, FAQ) est dans src/data.py ; ce fichier ne contient que l'interface
et les gabarits.
"""
from html import escape as e
from pathlib import Path
from urllib.parse import quote

import json

from data import FAQ, GOODIES, LIENS, LIVRAISON, OEUVRES, PRINT_FORMATS

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'site'
LANGS = ['fr', 'nl', 'en']
PAGES = ['home', 'about', 'gallery', 'prints', 'goodies', 'faq', 'contact', 'cart']
SLUGS = {
    'fr': {'home': 'index.html', 'about': 'a-propos.html', 'gallery': 'galerie.html', 'prints': 'prints.html', 'goodies': 'goodies.html', 'faq': 'faq.html', 'contact': 'contact.html', 'cart': 'panier.html'},
    'nl': {'home': 'index.html', 'about': 'over.html', 'gallery': 'galerij.html', 'prints': 'prints.html', 'goodies': 'goodies.html', 'faq': 'faq.html', 'contact': 'contact.html', 'cart': 'winkelmand.html'},
    'en': {'home': 'index.html', 'about': 'about.html', 'gallery': 'gallery.html', 'prints': 'prints.html', 'goodies': 'goodies.html', 'faq': 'faq.html', 'contact': 'contact.html', 'cart': 'cart.html'},
}
HTML_LANG = {'fr': 'fr-BE', 'nl': 'nl-BE', 'en': 'en'}

# Phrase de l'ancien site (EN, verbatim) ; FR et NL traduits par nos soins, à faire valider.
BIO = {
    'en': 'He grew up in Belgium within a multicultural family and cosmopolite atmosphere, which had a deep impact on his way of approaching art in its most varied alternatives, proof of the passion he uses at GUIARTE.',
    'fr': 'Il a grandi en Belgique, au sein d’une famille multiculturelle et dans une atmosphère cosmopolite, ce qui a profondément marqué sa façon d’aborder l’art sous ses formes les plus variées : la preuve de la passion qu’il met dans GUIARTE.',
    'nl': 'Hij groeide op in België, in een multiculturele familie en een kosmopolitische sfeer. Dat tekende diep zijn manier om kunst in al haar vormen te benaderen, het bewijs van de passie die hij in GUIARTE legt.',
}

T = {
    'fr': {
        'cart': 'Panier', 'add_cart': 'Ajouter au panier', 'in_cart': 'Dans le panier — voir', 'buy_now': 'Acheter maintenant',
        'added': 'Ajouté au panier.', 'see_cart': 'Voir le panier', 'unique': 'Pièce unique, signée, avec certificat',
        'cart_title': 'Votre panier', 'cart_empty': 'Votre panier est vide.', 'remove': 'Retirer', 'subtotal': 'Sous-total',
        'delivery': 'Livraison', 'total': 'Total', 'free': 'Offerte',
        'ship': {'be': 'Belgique, assurée', 'eu': 'Europe, assurée', 'pickup': 'Retrait à l’atelier, sur rendez-vous'},
        'details': 'Vos coordonnées', 'fn': 'Nom complet', 'fe': 'E-mail', 'fa': 'Adresse', 'fz': 'Code postal', 'fc': 'Ville',
        'err_req': 'Champ requis.', 'pay': 'Payer', 'secure': 'Paiement sécurisé par carte, Bancontact ou virement. Expédition sous 5 jours ouvrables.',
        'done_h': 'Merci pour votre commande !', 'done_p': 'Commande n°', 'done_mail': 'Un e-mail de confirmation vous est envoyé avec le suivi de livraison.',
        'demo': 'Boutique de démonstration : aucun paiement n’est encaissé tant que le prestataire de paiement n’est pas branché.',
        'nav': {'about': 'À propos', 'gallery': 'Galerie', 'prints': 'Prints', 'goodies': 'Goodies', 'faq': 'FAQ', 'contact': 'Contact'},
        'menu': 'Menu', 'skip': 'Aller au contenu', 'lang_label': 'Langue', 'main_nav': 'Navigation principale', 'home': 'Accueil',
        'title_home': 'Guido De Oliveira, artiste peintre', 'desc_home': 'Œuvres originales, prints et goodies de l’artiste peintre belge Guido De Oliveira.',
        'hero_1': 'L’art de', 'cta_gallery': 'Voir la galerie', 'cta_prints': 'Voir les prints',
        'video_h': 'Rencontre avec l’artiste', 'video_p': 'Quelques instants dans l’atelier, pinceau en main, sur « Premiers pas ».',
        'video_todo': 'Vidéo de présentation', 'video_todo_sub': 'Fichier à fournir, 3 minutes maximum',
        'recent_h': 'Œuvres récentes', 'recent_all': 'Toute la galerie',
        'prints_p': 'Les œuvres de la galerie en tirages d’art signés, du A4 au A2.', 'prints_go': 'Voir les prints',
        'goodies_p': 'Les œuvres sur t-shirts, pulls et cadres.', 'goodies_go': 'Voir les goodies',
        'news_h': 'Recevoir la newsletter', 'news_p': 'Nouvelles œuvres, expositions et sorties de prints, directement dans votre boîte mail.',
        'f_name': 'Nom', 'f_email': 'E-mail', 'f_submit': 'S’inscrire', 'f_err_name': 'Indiquez votre nom.',
        'f_err_email': 'Indiquez une adresse e-mail valide.', 'f_ok': 'Merci ! Votre inscription est bien prise en compte.',
        'f_note': 'Vous pouvez vous désinscrire à tout moment.', 'f_subject': 'Inscription à la newsletter',
        'g_title': 'Galerie', 'g_lead': 'Les œuvres originales, de la plus récente à la plus ancienne.', 'g_years': 'Années',
        'technique': 'Technique', 'dimensions': 'Dimensions', 'year': 'Année', 'story': 'L’histoire de l’œuvre',
        'buy': 'Acquérir l’original', 'see_prints': 'Voir le print', 'available': 'Disponible', 'sold': 'Vendue',
        'mail_subject': 'Original : {t}', 'mail_body': 'Bonjour Guido,\n\nJe souhaite acquérir l’œuvre « {t} » ({y}).\n\n',
        'zoom': 'Agrandir l’image', 'close': 'Fermer',
        'p_lead': 'Les œuvres de la galerie en tirages d’art signés, sur papier mat 230 g. Commandez en un clic sur Etsy.',
        'p_formats': 'Formats et prix', 'from': 'dès {p}', 'buy_etsy': 'Acheter sur Etsy', 'see_original': 'Voir l’original',
        'gd_lead': 'Les œuvres de la galerie sur t-shirts, pulls et cadres, imprimés et livrés par Redbubble.',
        'gd_types': {'tshirt': 'T-shirts', 'pull': 'Pulls', 'cadre': 'Cadres'},
        'gd_one': {'tshirt': 'T-shirt', 'pull': 'Pull à capuche', 'cadre': 'Cadre'},
        'buy_rb': 'Acheter sur Redbubble',
        'faq_title': 'Questions fréquentes', 'faq_lead': 'Tout ce qu’il faut savoir avant d’acheter une œuvre, un print ou un goodie.',
        'faq_more': 'Une autre question ?', 'faq_write': 'Écrivez-moi',
        'a_title': 'À propos', 'a_more': 'Biographie complète à fournir par l’artiste.', 'a_portrait': 'Guido De Oliveira, de dos, peint le léopard « Premiers pas » dans son atelier',
        'a_video': 'Regarder la vidéo',
        'c_title': 'Contact', 'c_lead': 'Une question sur une œuvre, une commande ou une exposition ? Écrivez-moi.',
        'c_email': 'E-mail', 'c_follow': 'Me suivre', 'c_shops': 'Boutiques', 'c_todo_email': 'Adresse e-mail à fournir',
        'footer_shops': 'Boutiques', 'footer_nav': 'Navigation', 'follow': 'Suivre Guido De Oliveira sur',
        'rights': 'Tous droits réservés.', 'todo_link': 'Lien à fournir par l’artiste',
    },
    'nl': {
        'cart': 'Winkelmand', 'add_cart': 'In winkelmand', 'in_cart': 'In je winkelmand — bekijken', 'buy_now': 'Nu kopen',
        'added': 'Toegevoegd aan je winkelmand.', 'see_cart': 'Bekijk winkelmand', 'unique': 'Uniek stuk, gesigneerd, met certificaat',
        'cart_title': 'Je winkelmand', 'cart_empty': 'Je winkelmand is leeg.', 'remove': 'Verwijderen', 'subtotal': 'Subtotaal',
        'delivery': 'Levering', 'total': 'Totaal', 'free': 'Gratis',
        'ship': {'be': 'België, verzekerd', 'eu': 'Europa, verzekerd', 'pickup': 'Afhalen in het atelier, op afspraak'},
        'details': 'Je gegevens', 'fn': 'Volledige naam', 'fe': 'E-mail', 'fa': 'Adres', 'fz': 'Postcode', 'fc': 'Gemeente',
        'err_req': 'Verplicht veld.', 'pay': 'Betalen', 'secure': 'Veilig betalen met kaart, Bancontact of overschrijving. Verzending binnen 5 werkdagen.',
        'done_h': 'Bedankt voor je bestelling!', 'done_p': 'Bestelling nr.', 'done_mail': 'Je ontvangt een bevestigingsmail met de opvolging van de levering.',
        'demo': 'Demowinkel: er wordt niets betaald zolang de betaaldienst niet gekoppeld is.',
        'nav': {'about': 'Over mij', 'gallery': 'Galerij', 'prints': 'Prints', 'goodies': 'Goodies', 'faq': 'FAQ', 'contact': 'Contact'},
        'menu': 'Menu', 'skip': 'Naar de inhoud', 'lang_label': 'Taal', 'main_nav': 'Hoofdnavigatie', 'home': 'Home',
        'title_home': 'Guido De Oliveira, kunstschilder', 'desc_home': 'Originele werken, prints en goodies van de Belgische kunstschilder Guido De Oliveira.',
        'hero_1': 'De kunst van', 'cta_gallery': 'Bekijk de galerij', 'cta_prints': 'Bekijk de prints',
        'video_h': 'Maak kennis met de kunstenaar', 'video_p': 'Even binnenkijken in het atelier, penseel in de hand, bij “Eerste stappen”.',
        'video_todo': 'Voorstellingsvideo', 'video_todo_sub': 'Bestand aan te leveren, maximaal 3 minuten',
        'recent_h': 'Recente werken', 'recent_all': 'Volledige galerij',
        'prints_p': 'De werken uit de galerij als gesigneerde kunstprints, van A4 tot A2.', 'prints_go': 'Bekijk de prints',
        'goodies_p': 'De werken op T-shirts, truien en kaders.', 'goodies_go': 'Bekijk de goodies',
        'news_h': 'Schrijf je in op de nieuwsbrief', 'news_p': 'Nieuwe werken, tentoonstellingen en nieuwe prints, rechtstreeks in je mailbox.',
        'f_name': 'Naam', 'f_email': 'E-mail', 'f_submit': 'Inschrijven', 'f_err_name': 'Vul je naam in.',
        'f_err_email': 'Vul een geldig e-mailadres in.', 'f_ok': 'Bedankt! Je inschrijving is genoteerd.',
        'f_note': 'Je kunt je op elk moment uitschrijven.', 'f_subject': 'Inschrijving nieuwsbrief',
        'g_title': 'Galerij', 'g_lead': 'De originele werken, van het meest recente tot het oudste.', 'g_years': 'Jaren',
        'technique': 'Techniek', 'dimensions': 'Afmetingen', 'year': 'Jaar', 'story': 'Het verhaal achter het werk',
        'buy': 'Het origineel kopen', 'see_prints': 'Bekijk de print', 'available': 'Beschikbaar', 'sold': 'Verkocht',
        'mail_subject': 'Origineel: {t}', 'mail_body': 'Hallo Guido,\n\nIk wil het werk “{t}” ({y}) graag kopen.\n\n',
        'zoom': 'Afbeelding vergroten', 'close': 'Sluiten',
        'p_lead': 'De werken uit de galerij als gesigneerde kunstprints op mat papier van 230 g. Bestel met één klik op Etsy.',
        'p_formats': 'Formaten en prijzen', 'from': 'vanaf {p}', 'buy_etsy': 'Kopen op Etsy', 'see_original': 'Bekijk het origineel',
        'gd_lead': 'De werken uit de galerij op T-shirts, truien en kaders, gedrukt en geleverd door Redbubble.',
        'gd_types': {'tshirt': 'T-shirts', 'pull': 'Truien', 'cadre': 'Kaders'},
        'gd_one': {'tshirt': 'T-shirt', 'pull': 'Hoodie', 'cadre': 'Kader'},
        'buy_rb': 'Kopen op Redbubble',
        'faq_title': 'Veelgestelde vragen', 'faq_lead': 'Alles wat u moet weten voor u een werk, print of goodie koopt.',
        'faq_more': 'Nog een vraag?', 'faq_write': 'Schrijf me',
        'a_title': 'Over mij', 'a_more': 'Volledige biografie aan te leveren door de kunstenaar.', 'a_portrait': 'Guido De Oliveira, op de rug gezien, schildert de luipaard “Eerste stappen” in zijn atelier',
        'a_video': 'Bekijk de video',
        'c_title': 'Contact', 'c_lead': 'Een vraag over een werk, een bestelling of een tentoonstelling? Schrijf me.',
        'c_email': 'E-mail', 'c_follow': 'Volg mij', 'c_shops': 'Winkels', 'c_todo_email': 'E-mailadres aan te leveren',
        'footer_shops': 'Winkels', 'footer_nav': 'Navigatie', 'follow': 'Volg Guido De Oliveira op',
        'rights': 'Alle rechten voorbehouden.', 'todo_link': 'Link aan te leveren door de kunstenaar',
    },
    'en': {
        'cart': 'Cart', 'add_cart': 'Add to cart', 'in_cart': 'In your cart — view', 'buy_now': 'Buy now',
        'added': 'Added to your cart.', 'see_cart': 'View cart', 'unique': 'One-off piece, signed, with certificate',
        'cart_title': 'Your cart', 'cart_empty': 'Your cart is empty.', 'remove': 'Remove', 'subtotal': 'Subtotal',
        'delivery': 'Delivery', 'total': 'Total', 'free': 'Free',
        'ship': {'be': 'Belgium, insured', 'eu': 'Europe, insured', 'pickup': 'Studio pick-up, by appointment'},
        'details': 'Your details', 'fn': 'Full name', 'fe': 'Email', 'fa': 'Address', 'fz': 'Postcode', 'fc': 'City',
        'err_req': 'Required field.', 'pay': 'Pay', 'secure': 'Secure payment by card, Bancontact or bank transfer. Ships within 5 working days.',
        'done_h': 'Thank you for your order!', 'done_p': 'Order no.', 'done_mail': 'A confirmation email with delivery tracking is on its way.',
        'demo': 'Demo shop: no payment is taken until the payment provider is connected.',
        'nav': {'about': 'About', 'gallery': 'Gallery', 'prints': 'Prints', 'goodies': 'Goodies', 'faq': 'FAQ', 'contact': 'Contact'},
        'menu': 'Menu', 'skip': 'Skip to content', 'lang_label': 'Language', 'main_nav': 'Main navigation', 'home': 'Home',
        'title_home': 'Guido De Oliveira, painter', 'desc_home': 'Original paintings, prints and goodies by Belgian painter Guido De Oliveira.',
        'hero_1': 'The Art of', 'cta_gallery': 'View the gallery', 'cta_prints': 'See the prints',
        'video_h': 'Meet the artist', 'video_p': 'A few moments in the studio, brush in hand, on “First Steps”.',
        'video_todo': 'Presentation video', 'video_todo_sub': 'File to be supplied, 3 minutes maximum',
        'recent_h': 'Recent works', 'recent_all': 'Full gallery',
        'prints_p': 'The works from the gallery as signed art prints, from A4 to A2.', 'prints_go': 'See the prints',
        'goodies_p': 'The works on T-shirts, hoodies and frames.', 'goodies_go': 'See the goodies',
        'news_h': 'Join the newsletter', 'news_p': 'New works, exhibitions and print releases, straight to your inbox.',
        'f_name': 'Name', 'f_email': 'Email', 'f_submit': 'Subscribe', 'f_err_name': 'Please enter your name.',
        'f_err_email': 'Please enter a valid email address.', 'f_ok': 'Thank you! You’re on the list.',
        'f_note': 'You can unsubscribe at any time.', 'f_subject': 'Newsletter subscription',
        'g_title': 'Gallery', 'g_lead': 'The original works, from the most recent to the oldest.', 'g_years': 'Years',
        'technique': 'Technique', 'dimensions': 'Dimensions', 'year': 'Year', 'story': 'The story behind the work',
        'buy': 'Buy the original', 'see_prints': 'See the print', 'available': 'Available', 'sold': 'Sold',
        'mail_subject': 'Original: {t}', 'mail_body': 'Hello Guido,\n\nI would like to buy “{t}” ({y}).\n\n',
        'zoom': 'Enlarge image', 'close': 'Close',
        'p_lead': 'The works from the gallery as signed art prints on 230 g matte paper. Order in one click on Etsy.',
        'p_formats': 'Sizes and prices', 'from': 'from {p}', 'buy_etsy': 'Buy on Etsy', 'see_original': 'See the original',
        'gd_lead': 'The works from the gallery on T-shirts, hoodies and frames, printed and shipped by Redbubble.',
        'gd_types': {'tshirt': 'T-shirts', 'pull': 'Hoodies', 'cadre': 'Frames'},
        'gd_one': {'tshirt': 'T-shirt', 'pull': 'Hoodie', 'cadre': 'Frame'},
        'buy_rb': 'Buy on Redbubble',
        'faq_title': 'Frequently asked questions', 'faq_lead': 'Everything to know before buying a painting, a print or a goodie.',
        'faq_more': 'Another question?', 'faq_write': 'Write to me',
        'a_title': 'About', 'a_more': 'Full biography to be supplied by the artist.', 'a_portrait': 'Guido De Oliveira, seen from behind, painting the leopard “First Steps” in his studio',
        'a_video': 'Watch the video',
        'c_title': 'Contact', 'c_lead': 'A question about a work, a commission or an exhibition? Write to me.',
        'c_email': 'Email', 'c_follow': 'Follow me', 'c_shops': 'Shops', 'c_todo_email': 'Email address to be supplied',
        'footer_shops': 'Shops', 'footer_nav': 'Navigation', 'follow': 'Follow Guido De Oliveira on',
        'rights': 'All rights reserved.', 'todo_link': 'Link to be supplied by the artist',
    },
}

LOGO = (OUT / 'assets' / 'img' / 'logo.svg').read_text(encoding='utf-8').strip()
LOGO = LOGO.replace('<svg ', '<svg aria-hidden="true" focusable="false" ', 1)
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Philosopher:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">')

# Icônes des réseaux (pied de page), tracées sur une grille de 24.
SOCIAL_ICONS = {
    'instagram': '<rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="12" cy="12" r="4.2" fill="none" stroke="currentColor" stroke-width="1.8"/><circle cx="17.3" cy="6.7" r="1.15"/>',
    'facebook': '<path d="M14 8h2.5V4.5H14c-2.5 0-4 1.6-4 4.2V11H7.5v3.5H10V21h3.5v-6.5H16l.5-3.5h-3V9c0-.6.4-1 1-1Z"/>',
    'tiktok': '<path d="M16.6 3c.3 2.3 1.8 3.9 4 4.1v3.3c-1.5 0-2.9-.4-4-1.2v6.3a5.5 5.5 0 1 1-5.5-5.5c.3 0 .6 0 .9.1v3.4a2.2 2.2 0 1 0 1.3 2V3h3.3Z"/>',
    'youtube': '<path fill-rule="evenodd" d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4a2.6 2.6 0 0 0-1.8 1.8A27 27 0 0 0 2 12a27 27 0 0 0 .4 4.8 2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.4-4.8ZM10 15V9l5.2 3L10 15Z"/>',
}
SOCIAL_NAMES = {'instagram': 'Instagram', 'facebook': 'Facebook', 'tiktok': 'TikTok', 'youtube': 'YouTube'}


def price(n, lang):
    s = f'{n:,}'
    if lang == 'fr':
        return s.replace(',', ' ') + ' €'
    if lang == 'nl':
        return '€ ' + s.replace(',', '.')
    return '€' + s


def img(o, size=''):
    stem = o['image'].rsplit('.', 1)[0]
    return f'../assets/img/oeuvres/{stem}{size}.jpg'


def wh(o, full=False):
    """Dimensions réelles des fichiers (évite les sauts de mise en page au chargement)."""
    w, h = (1280, 1600) if o['ratio'] == 'p' else (1600, 1280)
    if not full:
        w, h = w * 600 // max(w, h), h * 600 // max(w, h)
    return f'width="{w}" height="{h}"'


def ext(key, t):
    url = LIENS.get(key)
    if url:
        return f'href="{e(url)}" target="_blank" rel="noopener"'
    return f'href="#" data-todo="{e(t["todo_link"])}"'


def by_id(i):
    return next(o for o in OEUVRES if o['id'] == i)


# ── Gabarit commun ────────────────────────────────────────────────

def page(lang, key, title, desc, body):
    t, s = T[lang], SLUGS[lang]
    nav = ''.join(
        f'<li><a href="{s[k]}"{" aria-current=\"page\"" if k == key else ""}>{e(t["nav"][k])}</a></li>'
        for k in ('about', 'gallery', 'prints', 'goodies', 'faq', 'contact'))
    langs = ''.join(
        f'<li><a href="../{l}/{SLUGS[l][key]}" hreflang="{l}" lang="{l}"{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a></li>'
        for l in LANGS)
    alternates = ''.join(f'<link rel="alternate" hreflang="{HTML_LANG[l]}" href="../{l}/{SLUGS[l][key]}">' for l in LANGS)
    footer_nav = ''.join(f'<li><a href="{s[k]}">{e(t["home"] if k == "home" else t["nav"][k])}</a></li>' for k in ('home', 'about', 'gallery', 'faq', 'contact'))
    footer_shops = (f'<li><a href="{s["prints"]}">{e(t["nav"]["prints"])}</a></li>'
                    f'<li><a href="{s["goodies"]}">{e(t["nav"]["goodies"])}</a></li>'
                    f'<li><a {ext("etsy", t)}>Etsy</a></li><li><a {ext("redbubble", t)}>Redbubble</a></li>')
    socials = ''.join(
        f'<li><a {ext(k, t)} aria-label="{e(t["follow"])} {SOCIAL_NAMES[k]}"><svg viewBox="0 0 24 24" width="22" height="22" fill="currentColor" aria-hidden="true">{SOCIAL_ICONS[k]}</svg></a></li>'
        for k in ('instagram', 'facebook', 'tiktok', 'youtube'))
    return f'''<!doctype html>
<html lang="{HTML_LANG[lang]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<link rel="icon" href="../assets/img/logo.svg" type="image/svg+xml">
{alternates}
{FONTS}
<link rel="stylesheet" href="../assets/css/style.css">
</head>
<body>
<a class="sr-only" href="#contenu">{e(t["skip"])}</a>
<header class="header">
  <div class="wrap header-in">
    <a class="brand" href="{s["home"]}">{LOGO}<span>Guido De Oliveira</span></a>
    <nav class="nav" aria-label="{e(t["main_nav"])}"><ul>{nav}</ul></nav>
    <div class="header-right">
      <ul class="langs" aria-label="{e(t["lang_label"])}">{langs}</ul>
      <a class="cart-link" href="{s["cart"]}">{e(t["cart"])}<span data-cart-count></span></a>
      <button class="menu-btn" type="button" aria-expanded="false" aria-controls="drawer">{e(t["menu"])}</button>
    </div>
  </div>
  <div class="drawer" id="drawer" hidden><div class="wrap"><ul>{nav}</ul><ul class="langs" aria-label="{e(t["lang_label"])}">{langs}</ul></div></div>
</header>
<main id="contenu">
{body}
</main>
<footer class="footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a class="brand" href="{s["home"]}">{LOGO}<span>Guido De Oliveira</span></a>
        <ul class="social-icons">{socials}</ul>
      </div>
      <nav aria-label="{e(t["footer_nav"])}"><h2>{e(t["footer_nav"])}</h2><ul>{footer_nav}</ul></nav>
      <div><h2>{e(t["footer_shops"])}</h2><ul>{footer_shops}</ul></div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 Guido De Oliveira. {e(t["rights"])}</p>
      <ul class="langs" aria-label="{e(t["lang_label"])}">{langs}</ul>
    </div>
  </div>
</footer>
<script>window.GDO = {shop_cfg(lang)};</script>
<script src="../assets/js/site.js" defer></script>
<script src="../assets/js/cart.js" defer></script>
</body>
</html>
'''


LOCALE = {'fr': 'fr-BE', 'nl': 'nl-BE', 'en': 'en-IE'}


def shop_cfg(lang):
    """Données de la boutique transmises au script du panier."""
    t, s = T[lang], SLUGS[lang]
    products = {o['id']: {'title': o['titre'][lang], 'price': o['prix'], 'sold': o['vendue'], 'img': img(o, '-600'),
                          'meta': f"{o['tech'][lang]}, {o['dim']}, {o['annee']}"} for o in OEUVRES}
    cfg = {'locale': LOCALE[lang], 'cartUrl': s['cart'], 'checkoutUrl': LIENS['checkout'] or '', 'products': products,
           't': {'addCart': t['add_cart'], 'inCart': t['in_cart'], 'added': t['added'], 'seeCart': t['see_cart'],
                 'remove': t['remove'], 'unique': t['unique'], 'free': t['free']}}
    return json.dumps(cfg, ensure_ascii=False).replace('</', '<\\/')


def head(title, lead):
    return f'<div class="wrap page-head"><h1>{e(title)}</h1><p class="lead">{e(lead)}</p></div>'


def newsletter(lang, idp):
    t = T[lang]
    return f'''<form class="form" data-newsletter data-action="{e(LIENS["newsletter"] or "")}" data-email="{e(LIENS["email"] or "")}" data-subject="{e(t["f_subject"])}" novalidate>
  <div class="form-row">
    <div class="field"><label for="{idp}-name">{e(t["f_name"])}</label><input id="{idp}-name" name="name" type="text" autocomplete="name" required><p class="error" hidden>{e(t["f_err_name"])}</p></div>
    <div class="field"><label for="{idp}-email">{e(t["f_email"])}</label><input id="{idp}-email" name="email" type="email" autocomplete="email" required><p class="error" hidden>{e(t["f_err_email"])}</p></div>
  </div>
  <div class="actions form-actions"><button class="btn" type="submit">{e(t["f_submit"])}</button><p class="note">{e(t["f_note"])}</p></div>
  <p class="form-ok" role="status" hidden>{e(t["f_ok"])}</p>
</form>'''


# ── Maquettes produits : l'œuvre réelle posée sur le support ──

DARK = ('#1c1b19', '#2d4a40', '#33415c')


def mock_print(o, lang):
    return f'<div class="mock mock-print"><div class="mock-frame"><div class="mock-mat"><img src="{img(o, "-600")}" {wh(o)} alt="{e(o["alt"][lang])}" loading="lazy"></div></div></div>'


def mock_tshirt(o, lang, color, n):
    shade = 'rgba(255,255,255,.07)' if color in DARK else 'rgba(0,0,0,.07)'
    body = 'M100 22 Q150 52 200 22 L262 46 L296 112 L252 132 L236 106 L236 318 L64 318 L64 106 L48 132 L4 112 L38 46 Z'
    return f'''<svg class="mock mock-garment" viewBox="0 0 300 330" role="img" aria-label="{e(o["alt"][lang])}">
  <defs><clipPath id="c{n}"><rect x="106" y="92" width="88" height="110" rx="2"/></clipPath>
  <linearGradient id="g{n}" x1="0" x2="1"><stop offset="0" stop-color="{shade}"/><stop offset=".5" stop-color="rgba(0,0,0,0)"/><stop offset="1" stop-color="{shade}"/></linearGradient></defs>
  <path d="{body}" fill="{color}"/><path d="{body}" fill="url(#g{n})"/>
  <path d="M100 22 Q150 52 200 22" fill="none" stroke="{shade}" stroke-width="6"/>
  <image href="{img(o, "-600")}" x="106" y="92" width="88" height="110" preserveAspectRatio="xMidYMid slice" clip-path="url(#c{n})"/>
</svg>'''


def mock_pull(o, lang, color, n):
    line = 'rgba(255,255,255,.14)' if color in DARK else 'rgba(0,0,0,.1)'
    return f'''<svg class="mock mock-garment" viewBox="0 0 300 330" role="img" aria-label="{e(o["alt"][lang])}">
  <defs><clipPath id="c{n}"><rect x="108" y="98" width="84" height="96" rx="2"/></clipPath></defs>
  <path d="M96 44 Q100 4 150 4 Q200 4 204 44 Q150 70 96 44 Z" fill="{color}"/>
  <path d="M96 44 Q100 4 150 4 Q200 4 204 44" fill="none" stroke="{line}" stroke-width="3"/>
  <path d="M96 44 Q150 80 204 44 L254 62 Q286 84 292 150 L300 296 L264 302 L252 168 L246 318 L54 318 L48 168 L36 302 L0 296 L8 150 Q14 84 46 62 Z" fill="{color}"/>
  <path d="M96 44 Q150 80 204 44" fill="none" stroke="{line}" stroke-width="3"/>
  <path d="M138 70 L136 112 M162 70 L164 112" stroke="{line}" stroke-width="2"/>
  <path d="M94 232 L206 232 L220 296 L80 296 Z" fill="none" stroke="{line}" stroke-width="2.5"/>
  <path d="M54 306 L246 306" stroke="{line}" stroke-width="2.5"/>
  <image href="{img(o, "-600")}" x="108" y="98" width="84" height="96" preserveAspectRatio="xMidYMid slice" clip-path="url(#c{n})"/>
</svg>'''


def mock_cadre(o, lang, color):
    return f'<div class="mock mock-wall"><div class="mock-cadre" style="--frame:{color}"><img src="{img(o, "-600")}" {wh(o)} alt="{e(o["alt"][lang])}" loading="lazy"></div></div>'


# ── Pages ─────────────────────────────────────────────────────────

def video_block(lang):
    t, v = T[lang], LIENS['video']
    if v and ('youtube' in v or 'vimeo' in v):
        inner = f'<iframe src="{e(v)}" title="{e(t["video_h"])}" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe>'
    elif v and (OUT / v).exists():
        inner = f'<video src="../{e(v)}" poster="../assets/video/presentation-poster.jpg" controls preload="none" playsinline></video>'
    elif (OUT / 'assets/video/presentation-poster.jpg').exists():
        # Fichier vidéo pas encore livré : l'image de l'atelier tient la place, sans lecteur cassé.
        inner = f'<img src="../assets/video/presentation-poster.jpg" alt="" class="video-still">'
    else:
        inner = f'<div class="video-todo"><strong>{e(t["video_todo"])}</strong><span>{e(t["video_todo_sub"])}</span></div>'
    return f'<div class="video-frame">{inner}</div>'


def work_card(o, lang, href):
    t = T[lang]
    tag = f'<span class="sold-tag">{e(t["sold"])}</span>' if o['vendue'] else f'<span class="price">{price(o["prix"], lang)}</span>'
    return f'''<li class="work-card"><a href="{href}">
  <div class="frame"><img src="{img(o, "-600")}" {wh(o)} alt="{e(o["alt"][lang])}" loading="lazy"></div>
  <h3>{e(o["titre"][lang])}</h3>
  <p>{o["annee"]} — {tag}</p></a></li>'''


def home(lang):
    t, s = T[lang], SLUGS[lang]
    hero = OEUVRES[0]
    recent = sorted(OEUVRES, key=lambda o: -o['annee'])[:4]
    cards = ''.join(work_card(o, lang, f'{s["gallery"]}#{o["id"]}') for o in recent)
    tee, pull = by_id('roi-du-couchant'), by_id('l-ombre-verte')
    body = f'''
<section class="wrap hero">
  <div>
    <div class="hero-mark">{LOGO}</div>
    <h1>{e(t["hero_1"])} <strong>Guido De Oliveira.</strong></h1>
    <p class="lead">{e(BIO[lang])}</p>
    <div class="actions">
      <a class="btn" href="{s["gallery"]}">{e(t["cta_gallery"])}</a>
      <a class="btn btn-line" href="{s["prints"]}">{e(t["cta_prints"])}</a>
    </div>
  </div>
  <figure class="hero-art">
    <a href="{s["gallery"]}#{hero["id"]}"><img src="{img(hero)}" {wh(hero, True)} alt="{e(hero["alt"][lang])}" fetchpriority="high"></a>
    <figcaption class="caption">{e(hero["titre"][lang])}, {hero["annee"]}</figcaption>
  </figure>
</section>

<section class="section section-wall" id="video">
  <div class="wrap">
    <div class="video-head"><h2>{e(t["video_h"])}</h2><p class="lead">{e(t["video_p"])}</p></div>
    {video_block(lang)}
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head"><h2>{e(t["recent_h"])}</h2><a class="link" href="{s["gallery"]}">{e(t["recent_all"])}</a></div>
    <ul class="works">{cards}</ul>
  </div>
</section>

<section class="section" style="padding-top:0">
  <div class="wrap shops">
    <a class="shop" href="{s["prints"]}">
      <div><h3>{e(t["nav"]["prints"])}</h3><p>{e(t["prints_p"])}</p></div>
      <div class="shop-visual">{mock_print(by_id("braises-du-soir"), lang)}</div>
      <span class="go">{e(t["prints_go"])}</span>
    </a>
    <a class="shop shop-alt" href="{s["goodies"]}">
      <div><h3>{e(t["nav"]["goodies"])}</h3><p>{e(t["goodies_p"])}</p></div>
      <div class="shop-visual shop-visual-duo">{mock_tshirt(tee, lang, "#f5f4f0", 900)}{mock_pull(pull, lang, "#33415c", 901)}</div>
      <span class="go">{e(t["goodies_go"])}</span>
    </a>
  </div>
</section>

<section class="section section-wall">
  <div class="wrap news">
    <div><h2>{e(t["news_h"])}</h2><p class="lead">{e(t["news_p"])}</p></div>
    {newsletter(lang, "nl-home")}
  </div>
</section>'''
    return page(lang, 'home', t['title_home'], t['desc_home'], body)


def gallery(lang):
    t, s = T[lang], SLUGS[lang]
    years = sorted({o['annee'] for o in OEUVRES}, reverse=True)
    year_nav = ''.join(f'<li><a href="#annee-{y}">{y}</a></li>' for y in years)
    sections = []
    for y in years:
        items = []
        for o in [o for o in OEUVRES if o['annee'] == y]:
            title = o['titre'][lang]
            if o['vendue']:
                buy_block = f'<p class="status sold">{e(t["sold"])}</p><div class="actions"><a class="btn btn-line" href="{s["prints"]}#print-{o["id"]}">{e(t["see_prints"])}</a></div>'
            else:
                buy_block = (f'<span class="price">{price(o["prix"], lang)}</span><p class="status">{e(t["unique"])}</p>'
                             f'<div class="actions"><button type="button" class="btn" data-add="{o["id"]}">{e(t["add_cart"])}</button>'
                             f'<button type="button" class="btn btn-line" data-buy-now="{o["id"]}">{e(t["buy_now"])}</button></div>'
                             f'<p class="also"><a class="link" href="{s["prints"]}#print-{o["id"]}">{e(t["see_prints"])}</a></p>')
            items.append(f'''<article class="artwork" id="{o["id"]}">
  <button class="zoom" type="button" data-full="{img(o)}" aria-label="{e(t["zoom"])} : {e(title)}"><img src="{img(o, "-600")}" srcset="{img(o, "-600")} 600w, {img(o)} 1600w" sizes="(min-width: 900px) 50vw, 100vw" {wh(o, True)} alt="{e(o["alt"][lang])}" loading="lazy"></button>
  <div>
    <h3>{e(title)}</h3>
    <dl class="specs">
      <dt>{e(t["technique"])}</dt><dd>{e(o["tech"][lang])}</dd>
      <dt>{e(t["dimensions"])}</dt><dd>{e(o["dim"])}</dd>
      <dt>{e(t["year"])}</dt><dd>{y}</dd>
    </dl>
    <p class="desc">{e(o["desc"][lang])}</p>
    <div class="story"><h4>{e(t["story"])}</h4><p>{e(o["histoire"][lang])}</p></div>
    <div class="buy">{buy_block}</div>
  </div>
</article>''')
        sections.append(f'<section class="year" id="annee-{y}"><div class="wrap"><h2 class="year-num">{y}</h2>{"".join(items)}</div></section>')
    body = f'''
{head(t["g_title"], t["g_lead"])}
<nav class="years" aria-label="{e(t["g_years"])}"><div class="wrap"><ul>{year_nav}</ul></div></nav>
{"".join(sections)}
<dialog class="lightbox"><img src="" alt=""><button type="button">{e(t["close"])}</button></dialog>'''
    return page(lang, 'gallery', f'{t["g_title"]} | Guido De Oliveira', t['g_lead'], body)


def prints(lang):
    t, s = T[lang], SLUGS[lang]
    formats = ''.join(f'<li><span>{f}</span><strong>{price(p, lang)}</strong></li>' for f, p in PRINT_FORMATS)
    cards = ''.join(f'''<li class="product" id="print-{o["id"]}">
  {mock_print(o, lang)}
  <h3>{e(o["titre"][lang])}</h3>
  <p class="meta">{e(t["from"].format(p=price(PRINT_FORMATS[0][1], lang)))}</p>
  <div class="product-actions"><a class="btn" {ext("etsy", t)}>{e(t["buy_etsy"])}</a><a class="link" href="{s["gallery"]}#{o["id"]}">{e(t["see_original"])}</a></div>
</li>''' for o in OEUVRES)
    body = f'''
{head(t["nav"]["prints"], t["p_lead"])}
<div class="wrap"><div class="formats"><h2>{e(t["p_formats"])}</h2><ul>{formats}</ul></div></div>
<section class="section products-section"><div class="wrap"><ul class="products">{cards}</ul></div></section>'''
    return page(lang, 'prints', f'{t["nav"]["prints"]} | Guido De Oliveira', t['p_lead'], body)


def goodies(lang):
    t = T[lang]
    tabs = ''.join(f'<li><a href="#{g["type"]}">{e(t["gd_types"][g["type"]])}</a></li>' for g in GOODIES)
    sections, n = [], 0
    for g in GOODIES:
        cards = []
        for i, o in enumerate(OEUVRES):
            color = g['couleurs'][i % len(g['couleurs'])]
            n += 1
            mock = (mock_tshirt(o, lang, color, n) if g['type'] == 'tshirt'
                    else mock_pull(o, lang, color, n) if g['type'] == 'pull'
                    else mock_cadre(o, lang, color))
            cards.append(f'''<li class="product">
  {mock}
  <h3>{e(o["titre"][lang])}</h3>
  <p class="meta">{e(t["gd_one"][g["type"]])} — {e(t["from"].format(p=price(g["prix"], lang)))}</p>
  <div class="product-actions"><a class="btn" {ext("redbubble", t)}>{e(t["buy_rb"])}</a></div>
</li>''')
        sections.append(f'<section class="goodies-type" id="{g["type"]}"><div class="wrap"><h2>{e(t["gd_types"][g["type"]])}</h2><ul class="products">{"".join(cards)}</ul></div></section>')
    body = f'''
{head(t["nav"]["goodies"], t["gd_lead"])}
<nav class="years" aria-label="{e(t["nav"]["goodies"])}"><div class="wrap"><ul>{tabs}</ul></div></nav>
{"".join(sections)}'''
    return page(lang, 'goodies', f'{t["nav"]["goodies"]} | Guido De Oliveira', t['gd_lead'], body)


def faq(lang):
    t, s = T[lang], SLUGS[lang]
    items = ''.join(f'<details class="qa"><summary>{e(q)}</summary><p>{e(a)}</p></details>' for q, a in FAQ[lang])
    body = f'''
{head(t["faq_title"], t["faq_lead"])}
<section class="wrap faq-grid">
  <div class="faq-list">{items}</div>
  <aside class="faq-aside"><h2>{e(t["faq_more"])}</h2><a class="btn" href="{s["contact"]}">{e(t["faq_write"])}</a></aside>
</section>'''
    return page(lang, 'faq', f'{t["faq_title"]} | Guido De Oliveira', t['faq_lead'], body)


def about(lang):
    t, s = T[lang], SLUGS[lang]
    body = f'''
<div class="wrap page-head"><h1>{e(t["a_title"])}</h1></div>
<section class="wrap about">
  <div class="portrait"><img src="../assets/img/portrait.jpg" width="1024" height="1280" alt="{e(t["a_portrait"])}"></div>
  <div class="prose">
    <p class="first">{e(BIO[lang])}</p>
    <p><span class="todo">{e(t["a_more"])}</span></p>
    <div class="actions" style="margin-top:2.5rem">
      <a class="btn" href="{s["gallery"]}">{e(t["cta_gallery"])}</a>
      <a class="btn btn-line" href="#video">{e(t["a_video"])}</a>
    </div>
  </div>
</section>

<section class="section section-wall" id="video">
  <div class="wrap">
    <div class="video-head"><h2>{e(t["video_h"])}</h2><p class="lead">{e(t["video_p"])}</p></div>
    {video_block(lang)}
  </div>
</section>'''
    return page(lang, 'about', f'{t["a_title"]} | Guido De Oliveira', BIO[lang], body)


def contact(lang):
    t, s = T[lang], SLUGS[lang]
    email = LIENS['email']
    email_html = f'<a class="link" href="mailto:{e(email)}">{e(email)}</a>' if email else f'<span class="todo">{e(t["c_todo_email"])}</span>'
    soc = ''.join(f'<li><a {ext(k, t)}>{SOCIAL_NAMES[k]}</a></li>' for k in ('instagram', 'facebook', 'tiktok', 'youtube'))
    shp = (f'<li><a href="{s["prints"]}">Etsy <small>{e(t["nav"]["prints"])}</small></a></li>'
           f'<li><a href="{s["goodies"]}">Redbubble <small>{e(t["nav"]["goodies"])}</small></a></li>')
    body = f'''
{head(t["c_title"], t["c_lead"])}
<section class="wrap contact-grid">
  <div>
    <h2>{e(t["c_email"])}</h2>
    <p class="contact-email">{email_html}</p>
    <h2 class="mt">{e(t["c_follow"])}</h2>
    <ul class="socials">{soc}</ul>
    <h2 class="mt">{e(t["c_shops"])}</h2>
    <ul class="socials">{shp}</ul>
  </div>
  <div>
    <h2>{e(t["news_h"])}</h2>
    <p class="lead" style="margin:1rem 0 2rem">{e(t["news_p"])}</p>
    {newsletter(lang, "nl-contact")}
  </div>
</section>'''
    return page(lang, 'contact', f'{t["c_title"]} | Guido De Oliveira', t['c_lead'], body)


def splash():
    links = ''.join(f'<a class="btn{" btn-line" if l != "fr" else ""}" href="{l}/index.html" hreflang="{l}">{name}</a>'
                    for l, name in (('fr', 'Français'), ('nl', 'Nederlands'), ('en', 'English')))
    return f'''<!doctype html>
<html lang="fr-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Guido De Oliveira</title>
<link rel="icon" href="assets/img/logo.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="assets/css/style.css">
<script>
  // Va directement à la langue du navigateur (ou au dernier choix), sinon affiche le choix.
  try {{
    var saved = localStorage.getItem('lang');
    var nav = (navigator.language || 'fr').slice(0, 2);
    var l = saved || (['fr', 'nl', 'en'].indexOf(nav) > -1 ? nav : null);
    if (l) location.replace(l + '/index.html');
  }} catch (e) {{}}
</script>
</head>
<body>
<main class="splash">
  {LOGO}
  <h1>Guido De Oliveira</h1>
  <div class="actions">{links}</div>
</main>
</body>
</html>
'''


def cart(lang):
    t, s = T[lang], SLUGS[lang]
    ship = ''.join(
        f'<label class="ship"><input type="radio" name="delivery" value="{k}" data-price="{v}"{" checked" if i == 0 else ""}>'
        f'<span>{e(t["ship"][k])}</span><strong>{price(v, lang) if v else e(t["free"])}</strong></label>'
        for i, (k, v) in enumerate(LIVRAISON))

    def field(n, label, typ='text', auto='', addr=False):
        err = t['f_err_email'] if n == 'email' else t['err_req']
        return (f'<div class="field"{" data-address" if addr else ""}><label for="co-{n}">{e(label)}</label>'
                f'<input id="co-{n}" name="{n}" type="{typ}" autocomplete="{auto}" required><p class="error" hidden>{e(err)}</p></div>')

    demo = '' if LIENS['checkout'] else f'<p class="demo-note">{e(t["demo"])}</p>'
    body = f"""
<div class="wrap page-head"><h1>{e(t["cart_title"])}</h1></div>
<section class="wrap cart-page">
  <div id="cart-empty" hidden><p class="lead">{e(t["cart_empty"])}</p><p class="spaced"><a class="btn" href="{s["gallery"]}">{e(t["cta_gallery"])}</a></p></div>
  <div id="cart-full" class="cart-grid" hidden>
    <div>
      <ul id="cart" class="cart-list"></ul>
      <form id="checkout" class="form checkout" novalidate>
        <h2 id="commande">{e(t["details"])}</h2>
        {field("name", t["fn"], auto="name")}
        {field("email", t["fe"], "email", "email")}
        <fieldset class="ships"><legend>{e(t["delivery"])}</legend>{ship}</fieldset>
        {field("address", t["fa"], auto="street-address", addr=True)}
        <div class="form-row">{field("zip", t["fz"], auto="postal-code", addr=True)}{field("city", t["fc"], auto="address-level2", addr=True)}</div>
        <button class="btn btn-pay" type="submit">{e(t["pay"])}&nbsp;<span id="pay-amount"></span></button>
        <p class="note">{e(t["secure"])}</p>
        {demo}
      </form>
    </div>
    <aside class="summary">
      <dl>
        <div><dt>{e(t["subtotal"])}</dt><dd id="sum-sub"></dd></div>
        <div><dt>{e(t["delivery"])}</dt><dd id="sum-ship"></dd></div>
        <div class="sum-total"><dt>{e(t["total"])}</dt><dd id="sum-total"></dd></div>
      </dl>
      <p class="note">{e(t["unique"])}</p>
    </aside>
  </div>
  <div id="order-done" class="order-done" hidden>
    <h2>{e(t["done_h"])}</h2>
    <p class="lead">{e(t["done_p"])} <strong id="order-number"></strong></p>
    <p>{e(t["done_mail"])}</p>
    {demo}
    <p class="spaced"><a class="btn" href="{s["gallery"]}">{e(t["cta_gallery"])}</a></p>
  </div>
</section>"""
    return page(lang, 'cart', f'{t["cart_title"]} | Guido De Oliveira', t['cart_title'], body)


BUILDERS = {'home': home, 'about': about, 'gallery': gallery, 'prints': prints, 'goodies': goodies, 'faq': faq, 'contact': contact, 'cart': cart}


def main():
    for lang in LANGS:
        d = OUT / lang
        d.mkdir(parents=True, exist_ok=True)
        for p in PAGES:
            (d / SLUGS[lang][p]).write_text(BUILDERS[p](lang), encoding='utf-8')
    (OUT / 'index.html').write_text(splash(), encoding='utf-8')
    print('Pages :', sum(1 for _ in OUT.rglob('*.html')))


if __name__ == '__main__':
    main()
