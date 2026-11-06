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

from PIL import Image

from data import (COLLABORATIONS, DISTINCTIONS, EXPOSITIONS, FAQ, LIENS, OEUVRES, PRESSE,
                  PRINT_FORMATS, SERIES)
from legal import CGV, COURTESY, PRIVACY, UPDATED

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'site'
LANGS = ['fr', 'nl', 'en']
PAGES = ['home', 'about', 'gallery', 'prints', 'goodies', 'faq', 'contact', 'cgv', 'privacy']
SLUGS = {
    'fr': {'home': 'index.html', 'about': 'a-propos.html', 'gallery': 'galerie.html', 'prints': 'prints.html', 'goodies': 'goodies.html', 'faq': 'faq.html', 'contact': 'contact.html',
           'cgv': 'conditions-generales-de-vente.html', 'privacy': 'politique-de-confidentialite.html'},
    'nl': {'home': 'index.html', 'about': 'over.html', 'gallery': 'galerij.html', 'prints': 'prints.html', 'goodies': 'goodies.html', 'faq': 'faq.html', 'contact': 'contact.html',
           'cgv': 'algemene-verkoopvoorwaarden.html', 'privacy': 'privacybeleid.html'},
    'en': {'home': 'index.html', 'about': 'about.html', 'gallery': 'gallery.html', 'prints': 'prints.html', 'goodies': 'goodies.html', 'faq': 'faq.html', 'contact': 'contact.html',
           'cgv': 'terms-of-sale.html', 'privacy': 'privacy-policy.html'},
}
HTML_LANG = {'fr': 'fr-BE', 'nl': 'nl-BE', 'en': 'en'}

# Textes de l'artiste (NotesSiteWeb_2, 2026-11-05) : FR fourni ; NL et EN traduits par nos soins, à faire valider.
TAGLINE = ('The Art of', 'Guido De Oliveira.')  # en anglais dans les trois langues, comme sur l'ancien site

INTRO = {
    'fr': 'À travers notre histoire en tant que civilisation et l’incertitude du futur, la vie sauvage, des objets chargés de mémoire et des visions cosmiques, Guido de Oliveira explore la relation entre l’humain, la nature et un monde en constante transformation. Ses œuvres invitent à être témoin de sa vision du monde tout en éveillant une réflexion sur le climat, les effets de l’activité humaine et la fragilité du vivant.',
    'nl': 'Via onze geschiedenis als beschaving en de onzekerheid van de toekomst, via het wilde leven, voorwerpen beladen met herinneringen en kosmische visioenen, verkent Guido de Oliveira de relatie tussen de mens, de natuur en een wereld die voortdurend verandert. Zijn werken nodigen uit om getuige te zijn van zijn kijk op de wereld en zetten aan tot nadenken over het klimaat, de gevolgen van menselijk handelen en de kwetsbaarheid van het leven.',
    'en': 'Through our history as a civilisation and the uncertainty of the future, through wildlife, objects charged with memory and cosmic visions, Guido de Oliveira explores the relationship between humankind, nature and a world in constant transformation. His works invite you to witness his vision of the world while prompting reflection on the climate, the effects of human activity and the fragility of life.',
}

BIO = {
    'fr': 'Né en 1976, Guido de Oliveira est un artiste peintre d’origine portugaise, avec des racines allemandes, aujourd’hui basé à Bruxelles. Sa pratique s’est construite depuis l’enfance au contact de l’aquarelle, de l’acrylique et d’un apprentissage constant par l’expérimentation. Ses voyages et ses influences, du surréalisme à l’hyperréalisme, nourrissent un univers personnel où se rencontrent précision, imaginaire et sensibilité. Il développe une pratique professionnelle depuis 2015.',
    'nl': 'Guido de Oliveira, geboren in 1976, is een kunstschilder van Portugese afkomst met Duitse wortels, die vandaag in Brussel woont. Zijn praktijk groeide sinds zijn kindertijd met aquarel, acryl en een voortdurend leren door te experimenteren. Zijn reizen en invloeden, van het surrealisme tot het hyperrealisme, voeden een persoonlijke wereld waarin precisie, verbeelding en gevoeligheid elkaar ontmoeten. Sinds 2015 werkt hij als professioneel kunstenaar.',
    'en': 'Born in 1976, Guido de Oliveira is a painter of Portuguese origin with German roots, now based in Brussels. His practice has been shaped since childhood by watercolour, acrylic and constant learning through experimentation. His travels and influences, from surrealism to hyperrealism, feed a personal world where precision, imagination and sensitivity meet. He has worked as a professional artist since 2015.',
}

T = {
    'fr': {
        'unique': 'Pièce unique, signée, avec certificat',
        'nav': {'about': 'À propos', 'gallery': 'Galerie', 'prints': 'Prints', 'goodies': 'Goodies', 'faq': 'FAQ', 'contact': 'Contact'},
        'menu': 'Menu', 'skip': 'Aller au contenu', 'lang_label': 'Langue', 'main_nav': 'Navigation principale', 'home': 'Accueil',
        'title_home': 'Guido De Oliveira, artiste peintre', 'desc_home': 'Œuvres originales, prints et goodies de l’artiste peintre belge Guido De Oliveira.',
        'cta_gallery': 'Voir la galerie', 'cta_prints': 'Voir les prints',
        'video_h': 'Rencontre avec l’artiste', 'video_p': 'Quelques instants dans l’atelier, pinceau en main.',
        'video_todo': 'Vidéo de présentation', 'video_todo_sub': 'Fichier à fournir, 3 minutes maximum',
        'recent_h': 'Œuvres récentes', 'recent_all': 'Toute la galerie',
        'prints_p': 'Les œuvres de la galerie en tirages d’art signés, du 30 × 40 au 61 × 81 cm.', 'prints_go': 'Voir les prints',
        'goodies_p': 'Les œuvres sur mugs, t-shirts, stickers, coussins et bien d’autres.', 'goodies_go': 'Voir les goodies',
        'news_h': 'Recevoir la newsletter', 'news_p': 'Nouvelles œuvres, expositions et sorties de prints, directement dans votre boîte mail.',
        'f_name': 'Nom', 'f_email': 'E-mail', 'f_submit': 'S’inscrire', 'f_err_name': 'Indiquez votre nom.',
        'f_err_email': 'Indiquez une adresse e-mail valide.', 'f_ok': 'Merci ! Votre inscription est bien prise en compte.',
        'f_note': 'Vous pouvez vous désinscrire à tout moment.',
        'f_consent': 'En vous inscrivant, vous acceptez de recevoir la newsletter de Guido De Oliveira par e-mail.','f_subject': 'Inscription à la newsletter',
        'g_title': 'Galerie', 'g_lead': 'Les œuvres originales, classées par série.', 'g_years': 'Séries', 'todo': 'À fournir', 'price_todo': 'Prix à fournir',
        'technique': 'Technique', 'dimensions': 'Dimensions', 'year': 'Année', 'story': 'L’histoire de l’œuvre',
        'buy': 'Acquérir l’original', 'see_prints': 'Voir le print', 'available': 'Disponible', 'sold': 'Vendue',
        'mail_subject': 'Original : {t}', 'mail_body': 'Bonjour Guido,\n\nJe souhaite acquérir l’œuvre « {t} » ({y}).\n\n',
        # Demande d'achat d'un original (fenêtre de la galerie) ; {url} et {img} deviennent des liens complets dans site.js.
        'inq_intro': 'Je souhaite acquérir l’œuvre originale « {t} ».', 'serie_l': 'Série',
        'inq_see': 'Voir l’œuvre', 'inq_photo': 'Photo', 'inq_ask': 'Pouvez-vous m’indiquer son prix et les modalités d’achat ?',
        'inq_bye': 'Cordialement,', 'inq_h': 'Acquérir l’original',
        'inq_lead': 'Votre demande est prête : elle contient les détails de l’œuvre, son lien et sa photo. Choisissez comment l’envoyer à Guido.',
        'inq_app': 'Application de messagerie', 'inq_copy': 'Copier le message', 'inq_copied': 'Message copié. Collez-le dans un e-mail à',
        'inq_or': 'Ou écrivez directement à',
        'zoom': 'Agrandir l’image', 'close': 'Fermer',
        'p_lead': 'Les œuvres de la galerie en tirages d’art signés, sur papier mat 230 g. Commandez en un clic sur Etsy.',
        'p_formats': 'Formats et prix', 'from': 'dès {p}', 'buy_etsy': 'Acheter', 'p_size': 'Format', 'see_original': 'Voir l’original',
        # Catégories et nombre de motifs relevés sur sa boutique Redbubble le 2026-11-05 (150 motifs, 169 produits).
        'gd_lead': 'T-shirts, sweats et vestes à capuche, stickers, posters, impressions artistiques et photo, toiles, mugs, coussins, coques de téléphone, tapis de souris, carnets, tote bags, pochettes, casquettes et bobs, chaussettes, magnets et badges : les œuvres en objets du quotidien, imprimés et livrés par Redbubble.',
        'gd_alt': 'Photomontage de 16 produits de la boutique Guiarte SMS décorés des œuvres de Guido De Oliveira : t-shirt, mug, poster, sticker, coussin, veste à capuche, coque de téléphone, impression artistique, tote bag, casquette, tapis de souris, toile, carnet, chaussettes, magnet et bob',
        'gd_go': 'Voir la boutique sur Redbubble', 'gd_note': 'Plus de 150 motifs dans la boutique Guiarte SMS.',
        'gd_types': {'tshirt': 'T-shirts', 'pull': 'Pulls', 'cadre': 'Cadres'},
        'gd_one': {'tshirt': 'T-shirt', 'pull': 'Pull à capuche', 'cadre': 'Cadre'},
        'buy_rb': 'Acheter sur Redbubble',
        'faq_title': 'Questions fréquentes', 'faq_lead': 'Tout ce qu’il faut savoir avant d’acheter une œuvre, un print ou un goodie.',
        'faq_more': 'Une autre question ?', 'faq_write': 'Écrivez-moi',
        'a_title': 'À propos', 'a_portrait': 'Guido De Oliveira peint dans son atelier, casque sur les oreilles, entouré de ses toiles',
        'a_video': 'Regarder la vidéo',
        'ex_h': 'Expositions et distinctions', 'ex_shows': 'Expositions collectives', 'ex_awards': 'Distinction',
        'ex_press': 'Œuvres parues dans', 'ex_collab': 'Collaborations', 'legal': 'Informations légales',
        'months': ('janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'),
        'c_title': 'Contact', 'c_lead': 'Une question sur une œuvre, une commande ou une exposition ? Écrivez-moi.',
        'c_email': 'E-mail', 'c_follow': 'Me suivre', 'c_shops': 'Boutiques', 'c_todo_email': 'Adresse e-mail à fournir',
        'footer_shops': 'Boutiques', 'footer_nav': 'Navigation', 'follow': 'Suivre Guido De Oliveira sur',
        'rights': 'Tous droits réservés.', 'todo_link': 'Lien à fournir par l’artiste',
    },
    'nl': {
        'unique': 'Uniek stuk, gesigneerd, met certificaat',
        'nav': {'about': 'Over mij', 'gallery': 'Galerij', 'prints': 'Prints', 'goodies': 'Goodies', 'faq': 'FAQ', 'contact': 'Contact'},
        'menu': 'Menu', 'skip': 'Naar de inhoud', 'lang_label': 'Taal', 'main_nav': 'Hoofdnavigatie', 'home': 'Home',
        'title_home': 'Guido De Oliveira, kunstschilder', 'desc_home': 'Originele werken, prints en goodies van de Belgische kunstschilder Guido De Oliveira.',
        'cta_gallery': 'Bekijk de galerij', 'cta_prints': 'Bekijk de prints',
        'video_h': 'Maak kennis met de kunstenaar', 'video_p': 'Even binnenkijken in het atelier, penseel in de hand.',
        'video_todo': 'Voorstellingsvideo', 'video_todo_sub': 'Bestand aan te leveren, maximaal 3 minuten',
        'recent_h': 'Recente werken', 'recent_all': 'Volledige galerij',
        'prints_p': 'De werken uit de galerij als gesigneerde kunstprints, van 30 × 40 tot 61 × 81 cm.', 'prints_go': 'Bekijk de prints',
        'goodies_p': 'De werken op mokken, T-shirts, stickers, kussens en nog veel meer.', 'goodies_go': 'Bekijk de goodies',
        'news_h': 'Schrijf je in op de nieuwsbrief', 'news_p': 'Nieuwe werken, tentoonstellingen en nieuwe prints, rechtstreeks in je mailbox.',
        'f_name': 'Naam', 'f_email': 'E-mail', 'f_submit': 'Inschrijven', 'f_err_name': 'Vul je naam in.',
        'f_err_email': 'Vul een geldig e-mailadres in.', 'f_ok': 'Bedankt! Je inschrijving is genoteerd.',
        'f_note': 'Je kunt je op elk moment uitschrijven.',
        'f_consent': 'Door je in te schrijven, ga je ermee akkoord de nieuwsbrief van Guido De Oliveira per e-mail te ontvangen.','f_subject': 'Inschrijving nieuwsbrief',
        'g_title': 'Galerij', 'g_lead': 'De originele werken, per reeks.', 'g_years': 'Reeksen', 'todo': 'Aan te leveren', 'price_todo': 'Prijs aan te leveren',
        'technique': 'Techniek', 'dimensions': 'Afmetingen', 'year': 'Jaar', 'story': 'Het verhaal achter het werk',
        'buy': 'Het origineel kopen', 'see_prints': 'Bekijk de print', 'available': 'Beschikbaar', 'sold': 'Verkocht',
        'mail_subject': 'Origineel: {t}', 'mail_body': 'Hallo Guido,\n\nIk wil het werk “{t}” ({y}) graag kopen.\n\n',
        'inq_intro': 'Ik wil het originele werk “{t}” graag kopen.', 'serie_l': 'Reeks',
        'inq_see': 'Bekijk het werk', 'inq_photo': 'Foto', 'inq_ask': 'Kun je me de prijs en de aankoopvoorwaarden laten weten?',
        'inq_bye': 'Met vriendelijke groeten,', 'inq_h': 'Het origineel kopen',
        'inq_lead': 'Je aanvraag staat klaar: met de details van het werk, de link en de foto. Kies hoe je ze naar Guido stuurt.',
        'inq_app': 'Mailprogramma', 'inq_copy': 'Bericht kopiëren', 'inq_copied': 'Bericht gekopieerd. Plak het in een e-mail aan',
        'inq_or': 'Of schrijf rechtstreeks naar',
        'zoom': 'Afbeelding vergroten', 'close': 'Sluiten',
        'p_lead': 'De werken uit de galerij als gesigneerde kunstprints op mat papier van 230 g. Bestel met één klik op Etsy.',
        'p_formats': 'Formaten en prijzen', 'from': 'vanaf {p}', 'buy_etsy': 'Kopen', 'p_size': 'Formaat', 'see_original': 'Bekijk het origineel',
        'gd_lead': 'T-shirts, sweaters en hoodies met rits, stickers, posters, kunst- en fotoprints, canvasprints, mokken, kussens, telefoonhoesjes, muismatten, notitieboeken, draagtassen, etuis, petten en bucket hats, sokken, magneten en buttons: de werken als alledaagse voorwerpen, gedrukt en geleverd door Redbubble.',
        'gd_alt': 'Fotomontage van 16 producten uit de winkel Guiarte SMS met de werken van Guido De Oliveira: T-shirt, mok, poster, sticker, kussen, hoodie met rits, telefoonhoesje, kunstprint, draagtas, pet, muismat, canvasprint, notitieboek, sokken, magneet en bucket hat',
        'gd_go': 'Bekijk de winkel op Redbubble', 'gd_note': 'Meer dan 150 ontwerpen in de winkel Guiarte SMS.',
        'gd_types': {'tshirt': 'T-shirts', 'pull': 'Truien', 'cadre': 'Kaders'},
        'gd_one': {'tshirt': 'T-shirt', 'pull': 'Hoodie', 'cadre': 'Kader'},
        'buy_rb': 'Kopen op Redbubble',
        'faq_title': 'Veelgestelde vragen', 'faq_lead': 'Alles wat u moet weten voor u een werk, print of goodie koopt.',
        'faq_more': 'Nog een vraag?', 'faq_write': 'Schrijf me',
        'a_title': 'Over mij', 'a_portrait': 'Guido De Oliveira schildert in zijn atelier, met een koptelefoon op, omringd door zijn doeken',
        'a_video': 'Bekijk de video',
        'ex_h': 'Tentoonstellingen en onderscheidingen', 'ex_shows': 'Groepstentoonstellingen', 'ex_awards': 'Onderscheiding',
        'ex_press': 'Werk verschenen in', 'ex_collab': 'Samenwerkingen', 'legal': 'Juridische informatie',
        'months': ('januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november', 'december'),
        'c_title': 'Contact', 'c_lead': 'Een vraag over een werk, een bestelling of een tentoonstelling? Schrijf me.',
        'c_email': 'E-mail', 'c_follow': 'Volg mij', 'c_shops': 'Winkels', 'c_todo_email': 'E-mailadres aan te leveren',
        'footer_shops': 'Winkels', 'footer_nav': 'Navigatie', 'follow': 'Volg Guido De Oliveira op',
        'rights': 'Alle rechten voorbehouden.', 'todo_link': 'Link aan te leveren door de kunstenaar',
    },
    'en': {
        'unique': 'One-off piece, signed, with certificate',
        'nav': {'about': 'About', 'gallery': 'Gallery', 'prints': 'Prints', 'goodies': 'Goodies', 'faq': 'FAQ', 'contact': 'Contact'},
        'menu': 'Menu', 'skip': 'Skip to content', 'lang_label': 'Language', 'main_nav': 'Main navigation', 'home': 'Home',
        'title_home': 'Guido De Oliveira, painter', 'desc_home': 'Original paintings, prints and goodies by Belgian painter Guido De Oliveira.',
        'cta_gallery': 'View the gallery', 'cta_prints': 'See the prints',
        'video_h': 'Meet the artist', 'video_p': 'A few moments in the studio, brush in hand.',
        'video_todo': 'Presentation video', 'video_todo_sub': 'File to be supplied, 3 minutes maximum',
        'recent_h': 'Recent works', 'recent_all': 'Full gallery',
        'prints_p': 'The works from the gallery as signed art prints, from 30 × 40 to 61 × 81 cm.', 'prints_go': 'See the prints',
        'goodies_p': 'The works on mugs, T-shirts, stickers, cushions and much more.', 'goodies_go': 'See the goodies',
        'news_h': 'Join the newsletter', 'news_p': 'New works, exhibitions and print releases, straight to your inbox.',
        'f_name': 'Name', 'f_email': 'Email', 'f_submit': 'Subscribe', 'f_err_name': 'Please enter your name.',
        'f_err_email': 'Please enter a valid email address.', 'f_ok': 'Thank you! You’re on the list.',
        'f_note': 'You can unsubscribe at any time.',
        'f_consent': 'By subscribing, you agree to receive Guido De Oliveira’s newsletter by email.','f_subject': 'Newsletter subscription',
        'g_title': 'Gallery', 'g_lead': 'The original works, by series.', 'g_years': 'Series', 'todo': 'To be supplied', 'price_todo': 'Price to be supplied',
        'technique': 'Technique', 'dimensions': 'Dimensions', 'year': 'Year', 'story': 'The story behind the work',
        'buy': 'Buy the original', 'see_prints': 'See the print', 'available': 'Available', 'sold': 'Sold',
        'mail_subject': 'Original: {t}', 'mail_body': 'Hello Guido,\n\nI would like to buy “{t}” ({y}).\n\n',
        'inq_intro': 'I would like to buy the original work “{t}”.', 'serie_l': 'Series',
        'inq_see': 'See the work', 'inq_photo': 'Photo', 'inq_ask': 'Could you let me know its price and how to proceed?',
        'inq_bye': 'Kind regards,', 'inq_h': 'Buy the original',
        'inq_lead': 'Your request is ready: it includes the details of the work, its link and its photo. Choose how to send it to Guido.',
        'inq_app': 'Email app', 'inq_copy': 'Copy the message', 'inq_copied': 'Message copied. Paste it into an email to',
        'inq_or': 'Or write directly to',
        'zoom': 'Enlarge image', 'close': 'Close',
        'p_lead': 'The works from the gallery as signed art prints on 230 g matte paper. Order in one click on Etsy.',
        'p_formats': 'Sizes and prices', 'from': 'from {p}', 'buy_etsy': 'Buy', 'p_size': 'Size', 'see_original': 'See the original',
        'gd_lead': 'T-shirts, sweatshirts and zip hoodies, stickers, posters, art and photo prints, canvas prints, mugs, cushions, phone cases, mouse pads, notebooks, tote bags, pouches, caps and bucket hats, socks, magnets and badges: the works on everyday objects, printed and shipped by Redbubble.',
        'gd_alt': 'Photo montage of 16 products from the Guiarte SMS shop featuring Guido De Oliveira’s works: T-shirt, mug, poster, sticker, cushion, zip hoodie, phone case, art print, tote bag, cap, mouse pad, canvas print, notebook, socks, magnet and bucket hat',
        'gd_go': 'Visit the shop on Redbubble', 'gd_note': 'Over 150 designs in the Guiarte SMS shop.',
        'gd_types': {'tshirt': 'T-shirts', 'pull': 'Hoodies', 'cadre': 'Frames'},
        'gd_one': {'tshirt': 'T-shirt', 'pull': 'Hoodie', 'cadre': 'Frame'},
        'buy_rb': 'Buy on Redbubble',
        'faq_title': 'Frequently asked questions', 'faq_lead': 'Everything to know before buying a painting, a print or a goodie.',
        'faq_more': 'Another question?', 'faq_write': 'Write to me',
        'a_title': 'About', 'a_portrait': 'Guido De Oliveira painting in his studio, headphones on, surrounded by his canvases',
        'a_video': 'Watch the video',
        'ex_h': 'Exhibitions and awards', 'ex_shows': 'Group exhibitions', 'ex_awards': 'Award',
        'ex_press': 'Work featured in', 'ex_collab': 'Collaborations', 'legal': 'Legal information',
        'months': ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'),
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
    'pinterest': '<path d="M12 2a10 10 0 0 0-3.64 19.31c-.09-.79-.16-2 .03-2.86l1.17-4.97s-.3-.6-.3-1.48c0-1.39.81-2.43 1.81-2.43.85 0 1.27.64 1.27 1.41 0 .86-.55 2.14-.83 3.33-.24 1 .5 1.81 1.48 1.81 1.78 0 3.15-1.88 3.15-4.59 0-2.4-1.73-4.08-4.19-4.08-2.85 0-4.53 2.14-4.53 4.36 0 .86.33 1.79.75 2.29.08.1.09.19.07.29l-.28 1.13c-.04.18-.15.22-.34.13-1.25-.58-2.03-2.41-2.03-3.88 0-3.16 2.29-6.06 6.62-6.06 3.47 0 6.17 2.48 6.17 5.79 0 3.45-2.18 6.23-5.2 6.23-1.02 0-1.97-.53-2.3-1.15l-.62 2.38c-.23.87-.84 1.96-1.25 2.62A10 10 0 1 0 12 2Z"/>',
    'tiktok': '<path d="M16.6 3c.3 2.3 1.8 3.9 4 4.1v3.3c-1.5 0-2.9-.4-4-1.2v6.3a5.5 5.5 0 1 1-5.5-5.5c.3 0 .6 0 .9.1v3.4a2.2 2.2 0 1 0 1.3 2V3h3.3Z"/>',
    'youtube': '<path fill-rule="evenodd" d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4a2.6 2.6 0 0 0-1.8 1.8A27 27 0 0 0 2 12a27 27 0 0 0 .4 4.8 2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8A27 27 0 0 0 22 12a27 27 0 0 0-.4-4.8ZM10 15V9l5.2 3L10 15Z"/>',
}
SOCIAL_NAMES = {'instagram': 'Instagram', 'tiktok': 'TikTok', 'pinterest': 'Pinterest', 'youtube': 'YouTube'}
SOCIALS = ('instagram', 'tiktok', 'pinterest', 'youtube')


def price(n, lang):
    s = f'{n:,}'
    if lang == 'fr':
        return s.replace(',', ' ') + ' €'
    if lang == 'nl':
        return '€ ' + s.replace(',', '.')
    return '€' + s


def img(o, size=''):
    return f'../assets/img/oeuvres/{o["id"]}{size}.webp'


_SIZES = {}


def size_of(o, full=False):
    """Dimensions réelles du fichier généré par images.py."""
    f = OUT / 'assets' / 'img' / 'oeuvres' / f'{o["id"]}{"" if full else "-600"}.webp'
    if f not in _SIZES:
        with Image.open(f) as im:
            _SIZES[f] = im.size
    return _SIZES[f]


def wh(o, full=False):
    """width/height réels (évite les sauts de mise en page au chargement)."""
    w, h = size_of(o, full)
    return f'width="{w}" height="{h}"'


def srcset(o):
    small, big = size_of(o)[0], size_of(o, True)[0]
    if big <= small:
        return ''
    return f' srcset="{img(o, "-600")} {small}w, {img(o)} {big}w" sizes="(min-width: 900px) 50vw, 100vw"'


def cap(o):
    """Une source plus étroite que la colonne garde sa taille réelle au lieu d'être étirée (et floue)."""
    w = size_of(o, True)[0]
    return f' style="max-width:{w}px"' if w < 1000 else ''


def series_name(key, lang):
    return dict(SERIES)[key][lang]


def todo(t):
    return f'<span class="todo">{e(t["todo"])}</span>'


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
        for k in SOCIALS)
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
      <nav aria-label="{e(t["legal"])}"><ul class="legal-links"><li><a href="{s["cgv"]}">{e(CGV[lang]["title"])}</a></li><li><a href="{s["privacy"]}">{e(PRIVACY[lang]["title"])}</a></li></ul></nav>
      <ul class="langs" aria-label="{e(t["lang_label"])}">{langs}</ul>
    </div>
  </div>
</footer>
<script src="../assets/js/site.js" defer></script>
</body>
</html>
'''


def head(title, lead):
    return f'<div class="wrap page-head"><h1>{e(title)}</h1><p class="lead">{e(lead)}</p></div>'


def newsletter(lang, idp):
    t = T[lang]
    return f'''<form class="form" data-newsletter data-action="{e(LIENS["newsletter"] or "")}" data-email="{e(LIENS["email"] or "")}" data-subject="{e(t["f_subject"])}" novalidate>
  <div class="form-row">
    <div class="field"><label for="{idp}-name">{e(t["f_name"])}</label><input id="{idp}-name" name="name" type="text" autocomplete="name" required><p class="error" hidden>{e(t["f_err_name"])}</p></div>
    <div class="field"><label for="{idp}-email">{e(t["f_email"])}</label><input id="{idp}-email" name="email" type="email" autocomplete="email" required><p class="error" hidden>{e(t["f_err_email"])}</p></div>
  </div>
  <div class="hp" aria-hidden="true"><label for="{idp}-website">Website</label><input id="{idp}-website" name="website" type="text" tabindex="-1" autocomplete="off"></div>
  <div class="actions form-actions"><button class="btn" type="submit">{e(t["f_submit"])}</button></div>
  <p class="note consent">{e(t["f_consent"])} {e(t["f_note"])} <a class="link" href="{SLUGS[lang]["privacy"]}">{e(PRIVACY[lang]["title"])}</a></p>
  <p class="form-ok" role="status" hidden>{e(t["f_ok"])}</p>
</form>'''


# ── Maquettes produits : l'œuvre réelle posée sur le support ──

def mock_print(o, lang):
    return f'<div class="mock mock-print"><div class="mock-frame"><div class="mock-mat"><img src="{img(o, "-600")}" {wh(o)} alt="{e(o["alt"][lang])}" loading="lazy"></div></div></div>'


# ── Pages ─────────────────────────────────────────────────────────

def video_block(lang):
    t, v = T[lang], LIENS['video']
    if v and ('youtube' in v or 'vimeo' in v):
        inner = f'<iframe src="{e(v)}" title="{e(t["video_h"])}" loading="lazy" allow="fullscreen; picture-in-picture" allowfullscreen></iframe>'
    elif v and (OUT / v).exists():
        inner = f'<video src="../{e(v)}" controls preload="metadata" playsinline></video>'
    else:
        inner = f'<div class="video-todo"><strong>{e(t["video_todo"])}</strong><span>{e(t["video_todo_sub"])}</span></div>'
    return f'<div class="video-frame">{inner}</div>'


def work_card(o, lang, href):
    t = T[lang]
    meta = [e(series_name(o['serie'], lang))]  # sans l'année (demande du 2026-11-06)
    if o['vendue']:
        meta.append(f'<span class="sold-tag">{e(t["sold"])}</span>')
    elif o['prix']:
        meta.append(f'<span class="price">{price(o["prix"], lang)}</span>')
    return f'''<li class="work-card"><a href="{href}">
  <div class="frame"><img src="{img(o, "-600")}" {wh(o)} alt="{e(o["alt"][lang])}" loading="lazy"></div>
  <h3>{e(o["titre"])}</h3>
  <p>{" — ".join(meta)}</p></a></li>'''


def inquiry_dialog(lang):
    """Fenêtre « Acquérir l'original » : la demande pré-remplie, à envoyer par le moyen du visiteur."""
    t = T[lang]
    email = e(LIENS['email'] or '')
    return f'''<dialog class="inquire" aria-labelledby="inq-h">
  <div class="inq-work"><img src="" alt="" width="96" height="96"><div><p class="kicker">{e(t["inq_h"])}</p><h2 id="inq-h"></h2><p class="inq-meta"></p></div></div>
  <p class="inq-lead">{e(t["inq_lead"])}</p>
  <div class="inq-actions">
    <a class="btn" data-inq="gmail" target="_blank" rel="noopener">Gmail</a>
    <a class="btn btn-line" data-inq="outlook" target="_blank" rel="noopener">Outlook</a>
    <a class="btn btn-line" data-inq="app">{e(t["inq_app"])}</a>
    <button type="button" class="btn btn-line" data-inq="copy">{e(t["inq_copy"])}</button>
  </div>
  <p class="inq-copied" role="status" hidden>{e(t["inq_copied"])} <strong>{email}</strong></p>
  <p class="note">{e(t["inq_or"])} <a class="link" href="mailto:{email}">{email}</a></p>
  <button type="button" class="inq-close link">{e(t["close"])}</button>
</dialog>'''


def buy_mail(o, lang):
    """Sans prix en ligne, l'achat passe par un e-mail pré-rempli à l'artiste."""
    t = T[lang]
    subject = t['mail_subject'].format(t=o['titre'])
    body = t['mail_body'].format(t=o['titre'], y=o['annee'] or '').replace(' ()', '')
    if not LIENS['email']:
        return f'href="{SLUGS[lang]["contact"]}"'
    # Sans JavaScript : simple lien e-mail. Avec : site.js ouvre la fenêtre de demande (Gmail, Outlook, appli, copie),
    # car un lien mailto ne fait rien sur un ordinateur sans logiciel de messagerie configuré.
    sep = ' : ' if lang == 'fr' else ': '
    details = [(t['serie_l'], series_name(o['serie'], lang)), (t['year'], o['annee']),
               (t['technique'], o['tech'] and o['tech'][lang]), (t['dimensions'], o['dim'])]
    lines = [t['mail_body'].split('\n')[0], '', t['inq_intro'].format(t=o['titre']), '']
    lines += [f'{k}{sep}{v}' for k, v in details if v]
    if o['desc']:
        lines += ['', o['desc'][lang]]
    lines += ['', f'{t["inq_see"]}{sep}{{url}}', f'{t["inq_photo"]}{sep}{{img}}', '', t['inq_ask'], '', t['inq_bye']]
    meta = ' · '.join(str(v) for _, v in details if v)
    return (f'href="mailto:{LIENS["email"]}?subject={quote(subject)}&amp;body={quote(body)}" data-inquire="{o["id"]}" '
            f'data-to="{e(LIENS["email"])}" data-subject="{e(subject)}" data-body="{e(chr(10).join(lines))}" '
            f'data-title="{e(o["titre"])}" data-meta="{e(meta)}" data-img="{img(o, "-600")}"')


def home(lang):
    t, s = T[lang], SLUGS[lang]
    hero = by_id('wave-at-sunset')  # choix de l'artiste, sans titre, en attendant sa vidéo de présentation
    recent = [o for o in sorted(OEUVRES, key=lambda o: -(o['annee'] or 0)) if o is not hero][:4]
    cards = ''.join(work_card(o, lang, f'{s["gallery"]}#{o["id"]}') for o in recent)
    body = f'''
<section class="wrap hero">
  <div>
    <div class="hero-mark">{LOGO}</div>
    <h1 lang="en">{e(TAGLINE[0])} <strong>{e(TAGLINE[1])}</strong></h1>
    <p class="lead">{e(INTRO[lang])}</p>
    <div class="actions">
      <a class="btn" href="{s["gallery"]}">{e(t["cta_gallery"])}</a>
      <a class="btn btn-line" href="{s["prints"]}">{e(t["cta_prints"])}</a>
    </div>
  </div>
  <figure class="hero-art">
    <a href="{s["gallery"]}#{hero["id"]}"><img src="{img(hero)}" {wh(hero, True)} alt="{e(hero["alt"][lang])}" fetchpriority="high"></a>
  </figure>
</section>

<section class="section section-wall">
  <div class="wrap">
    <div class="section-head"><h2>{e(t["recent_h"])}</h2><a class="link" href="{s["gallery"]}">{e(t["recent_all"])}</a></div>
    <ul class="works">{cards}</ul>
  </div>
</section>

<section class="section">
  <div class="wrap shops">
    <a class="shop" href="{s["prints"]}">
      <div><h3>{e(t["nav"]["prints"])}</h3><p>{e(t["prints_p"])}</p></div>
      <div class="shop-visual">{mock_print(by_id("lighthouse-2"), lang)}</div>
      <span class="go">{e(t["prints_go"])}</span>
    </a>
    <a class="shop shop-alt" href="{s["goodies"]}">
      <div><h3>{e(t["nav"]["goodies"])}</h3><p>{e(t["goodies_p"])}</p></div>
      <div class="shop-visual"><img class="shop-montage" src="../assets/img/goodies-800.webp" width="800" height="800" alt="{e(t["gd_alt"])}" loading="lazy"></div>
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
    series = [(k, [o for o in OEUVRES if o['serie'] == k]) for k, _ in SERIES]
    series = [(k, works) for k, works in series if works]
    nav = ''.join(f'<li><a href="#serie-{k}">{e(series_name(k, lang))}</a></li>' for k, _ in series)
    sections = []
    for k, works in series:
        items = []
        for o in works:
            title = o['titre']
            if o['vendue']:
                buy_block = f'<p class="status sold">{e(t["sold"])}</p><div class="actions"><a class="btn btn-line" href="{s["prints"]}#print-{o["id"]}">{e(t["see_prints"])}</a></div>'
            else:
                price_html = (f'<span class="price">{price(o["prix"], lang)}</span>' if o['prix'] else
                              f'<p class="price-todo"><span class="todo">{e(t["price_todo"])}</span></p>')
                buy_block = (f'{price_html}<p class="status">{e(t["unique"])}</p>'
                             f'<div class="actions"><a class="btn" {buy_mail(o, lang)}>{e(t["buy"])}</a>'
                             f'<a class="btn btn-line" href="{s["prints"]}#print-{o["id"]}">{e(t["see_prints"])}</a></div>')
            specs = (f'<dt>{e(t["technique"])}</dt><dd>{e(o["tech"][lang]) if o["tech"] else todo(t)}</dd>'
                     f'<dt>{e(t["dimensions"])}</dt><dd>{e(o["dim"]) if o["dim"] else todo(t)}</dd>'
                     f'<dt>{e(t["year"])}</dt><dd>{o["annee"] or todo(t)}</dd>')
            desc = f'<p class="desc">{e(o["desc"][lang])}</p>' if o['desc'] else ''
            story = f'<div class="story"><h4>{e(t["story"])}</h4><p>{e(o["histoire"][lang])}</p></div>' if o['histoire'] else ''
            items.append(f'''<article class="artwork" id="{o["id"]}">
  <button class="zoom" type="button" data-full="{img(o, "-zoom")}" aria-label="{e(t["zoom"])} : {e(title)}"><img src="{img(o, "-600")}"{srcset(o)}{cap(o)} {wh(o, True)} alt="{e(o["alt"][lang])}" loading="lazy"></button>
  <div>
    <h3>{e(title)}</h3>
    <dl class="specs">{specs}</dl>
    {desc}{story}
    <div class="buy">{buy_block}</div>
  </div>
</article>''')
        sections.append(f'<section class="year" id="serie-{k}"><div class="wrap"><h2 class="year-num series-name">{e(series_name(k, lang))}</h2>{"".join(items)}</div></section>')
    body = f'''
{head(t["g_title"], t["g_lead"])}
<nav class="years" aria-label="{e(t["g_years"])}"><div class="wrap"><ul>{nav}</ul></div></nav>
{"".join(sections)}
<dialog class="lightbox"><img src="" alt=""><button type="button">{e(t["close"])}</button></dialog>
{inquiry_dialog(lang)}'''
    return page(lang, 'gallery', f'{t["g_title"]} | Guido De Oliveira', t['g_lead'], body)


def size_select(o, lang):
    """Menu des formats d'un print ; site.js met à jour le prix « dès … » affiché sous le menu."""
    t = T[lang]
    opts = ''.join(f'<option value="{i}" data-price="{e(t["from"].format(p=price(p, lang)))}">{e(n[lang])}, {d}</option>'
                   for i, (n, d, p) in enumerate(PRINT_FORMATS))
    return f'<select id="size-{o["id"]}" data-size>{opts}</select>'


def prints(lang):
    t, s = T[lang], SLUGS[lang]
    formats = ''.join(f'<li><span>{e(n[lang])} <small>{d}</small></span><strong>{e(t["from"].format(p=price(p, lang)))}</strong></li>'
                      for n, d, p in PRINT_FORMATS)
    cards = ''.join(f'''<li class="product" id="print-{o["id"]}">
  {mock_print(o, lang)}
  <h3>{e(o["titre"])}</h3>
  <div class="size-field"><label for="size-{o["id"]}">{e(t["p_size"])}</label>{size_select(o, lang)}</div>
  <p class="meta" data-size-price>{e(t["from"].format(p=price(PRINT_FORMATS[0][2], lang)))}</p>
  <div class="product-actions"><a class="btn" {ext("etsy", t)}>{e(t["buy_etsy"])}</a><a class="link" href="{s["gallery"]}#{o["id"]}">{e(t["see_original"])}</a></div>
</li>''' for o in OEUVRES)
    body = f'''
{head(t["nav"]["prints"], t["p_lead"])}
<div class="wrap"><div class="formats"><h2>{e(t["p_formats"])}</h2><ul>{formats}</ul></div></div>
<section class="section products-section"><div class="wrap"><ul class="products">{cards}</ul></div></section>'''
    return page(lang, 'prints', f'{t["nav"]["prints"]} | Guido De Oliveira', t['p_lead'], body)


def goodies(lang):
    t = T[lang]
    body = f'''
{head(t["nav"]["goodies"], t["gd_lead"])}
<section class="wrap goodies-shop">
  <a class="goodies-montage" {ext("redbubble", t)}><img src="../assets/img/goodies.webp" srcset="../assets/img/goodies-800.webp 800w, ../assets/img/goodies.webp 1600w" sizes="(min-width: 900px) 46rem, 100vw" width="1600" height="1600" alt="{e(t["gd_alt"])}"></a>
  <div class="goodies-cta">
    <a class="btn" {ext("redbubble", t)}>{e(t["gd_go"])}</a>
    <p class="note">{e(t["gd_note"])}</p>
  </div>
</section>'''
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
  <div class="portrait"><img src="../assets/img/atelier.webp" width="1080" height="1080" alt="{e(t["a_portrait"])}"></div>
  <div class="prose">
    <p class="first">{e(BIO[lang])}</p>
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
</section>
{exhibitions(lang)}'''
    return page(lang, 'about', f'{t["a_title"]} | Guido De Oliveira', BIO[lang], body)


def month_year(d, lang):
    """'2020-04' -> « avril 2020 »."""
    y, m = d[:7].split('-')
    return f'{T[lang]["months"][int(m) - 1]} {y}'


def date_range(a, b, lang):
    """('2020-03-06', '2020-04-06') -> « 6 mars – 6 avril 2020 » (même année : l'année une seule fois)."""
    da, db = (f'{int(d[8:10])} {month_year(d, lang)}' for d in (a, b))
    return f'{da.rsplit(" ", 1)[0] if a[:4] == b[:4] else da} – {db}'


def exhibitions(lang):
    """Section « Expositions et distinctions » de la page À propos (la FAQ de l'artiste y renvoie)."""
    t = T[lang]

    def item(year, main, sub=''):
        sub = f'<span class="cv-sub">{sub}</span>' if sub else ''
        return f'<li><span class="cv-year">{year}</span><div><span class="cv-main">{main}</span>{sub}</div></li>'

    def group(title, items):
        return f'<div class="cv-group"><h3>{e(title)}</h3><ul class="cv-list">{"".join(items)}</ul></div>'

    shows = [item(a[:4], e(name), f'{e(place[lang])} · {date_range(a, b, lang)}') for name, place, a, b in EXPOSITIONS]
    awards = [item(d[:4], e(txt[lang]), month_year(d, lang)) for txt, d in DISTINCTIONS]
    press = [item(y, f'<cite>{e(mag)}</cite>') for mag, y in sorted(PRESSE, key=lambda p: -p[1])]
    collab = ''.join(f'<li>{e(c)}</li>' for c in COLLABORATIONS[lang])
    return f'''<section class="section" id="expositions">
  <div class="wrap">
    <div class="section-head"><h2>{e(t["ex_h"])}</h2></div>
    <div class="cv">
      {group(t["ex_shows"], shows)}
      <div>
        {group(t["ex_awards"], awards)}
        {group(t["ex_press"], press)}
        <div class="cv-group"><h3>{e(t["ex_collab"])}</h3><ul class="cv-plain">{collab}</ul></div>
      </div>
    </div>
  </div>
</section>'''


def legal_page(lang, key, doc):
    """CGV et politique de confidentialité : textes de l'artiste, dans src/legal.py."""
    t = T[lang]
    sep = ' : ' if lang == 'fr' else ': '

    def rich(txt):
        email = LIENS['email']
        return (e(txt)
                .replace('{email}', f'<a class="link" href="mailto:{e(email)}">{e(email)}</a>' if email else todo(t))
                .replace('{redbubble}', f'<a class="link" {ext("redbubble", t)}>Guiarte SMS (Redbubble)</a>')
                .replace('{todo}', todo(t)))

    sections = []
    for h, blocks in doc['sections']:
        out, items = [], []
        for b in blocks + [('end',)]:
            if b[0] == 'li':
                label = f'<strong>{e(b[1])}</strong>{sep}' if b[1] else ''
                items.append(f'<li>{label}{rich(b[2])}</li>')
                continue
            if items:
                out.append(f'<ul>{"".join(items)}</ul>')
                items = []
            if b[0] == 'p':
                out.append(f'<p>{rich(b[1])}</p>')
        sections.append(f'<h2>{e(h)}</h2>{"".join(out)}')
    note = e(UPDATED[lang])
    if lang in COURTESY:
        note += f'<br>{e(COURTESY[lang])} <a class="link" href="../fr/{SLUGS["fr"][key]}" hreflang="fr" lang="fr">Version française</a>'
    body = f'''
{head(doc["title"], doc["lead"])}
<section class="wrap"><div class="legal">
  <p class="note">{note}</p>
  {"".join(sections)}
</div></section>'''
    return page(lang, key, f'{doc["title"]} | Guido De Oliveira', doc['lead'], body)


def contact(lang):
    t, s = T[lang], SLUGS[lang]
    email = LIENS['email']
    email_html = f'<a class="link" href="mailto:{e(email)}">{e(email)}</a>' if email else f'<span class="todo">{e(t["c_todo_email"])}</span>'
    soc = ''.join(f'<li><a {ext(k, t)}>{SOCIAL_NAMES[k]}</a></li>' for k in SOCIALS)
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


BUILDERS = {'home': home, 'about': about, 'gallery': gallery, 'prints': prints, 'goodies': goodies, 'faq': faq, 'contact': contact,
            'cgv': lambda lang: legal_page(lang, 'cgv', CGV[lang]),
            'privacy': lambda lang: legal_page(lang, 'privacy', PRIVACY[lang])}


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
