# Guido De Oliveira — site d'artiste peintre avec e-shop

Site vitrine et boutique, **HTML/CSS/JS pur** (aucun framework), en **FR / NL / EN**. Commencé le 2026-10-16.
Références de l'artiste : Chuck Black et Stéphane Alsac (simplicité), Raffaela Lerch (boutique Etsy).
Objectif : le moins de clics possible entre le coup de cœur et l'achat.

## Structure

```
site/                  le site à mettre en ligne tel quel
  index.html           redirige vers la langue du navigateur, sinon choix FR / NL / EN
  fr/ nl/ en/          accueil, à propos, galerie (e-shop), prints, goodies, FAQ, contact, panier
  assets/js/cart.js    panier (stockage local du navigateur), compteur, commande
  assets/img/oeuvres/  <nom>.jpg (1600 px) et <nom>-600.jpg
source/                fichiers bruts des œuvres (PNG), capture d'origine — hors ligne
src/data.py            CONTENU : œuvres, prix, liens, livraison, FAQ
src/build.py           gabarits et textes d'interface des 3 langues
src/images.py          raw-*.png → JPEG optimisés
```

```bash
python src/images.py   # après ajout de raw-<nom>.png dans site/assets/img/oeuvres/
python src/build.py    # (sans -I : le script importe data.py)
```

Menu : À propos · Galerie · Prints · Goodies · FAQ · Contact · Panier.

## Contenu de démonstration (à remplacer)

À la demande de l'agence (2026-10-16), sont **inventés** pour la maquette : 11 des 12 œuvres (images
générées avec Higgsfield, gpt_image_2_5), leurs titres, histoires, dimensions et prix ; les formats et prix
des prints et goodies ; les frais de livraison ; les 9 questions de la FAQ ; le portrait de l'artiste
(`assets/img/portrait.jpg`, vu de dos, visage jamais montré) et la vidéo de présentation de 15 s
(`assets/video/presentation.mp4`, Seedance 2.5, réencodée en H.264 1280 px, 2,5 Mo ; brut dans `source/`). **Seul le léopard « Premiers
pas » est une vraie œuvre de l'artiste** (agrandie depuis une capture de son ancien site).
Les maquettes t-shirt / pull / cadre sont des SVG/CSS qui posent la vraie image de l'œuvre.

## E-shop

- Chaque original disponible : « Ajouter au panier » et « Acheter maintenant ». Une œuvre vendue ne peut pas
  être ajoutée ; une œuvre ne peut être qu'une fois dans le panier (pièce unique).
- Paiement : `LIENS['checkout']` dans `data.py`. Vide = **mode démonstration** (commande simulée, bandeau
  jaune affiché). Brancher Stripe Checkout (petite fonction serveur) ou Snipcart avant la mise en ligne.
- Prints → Etsy, goodies → Redbubble : liens `LIENS['etsy']` et `LIENS['redbubble']`.

## Règles

- Police **Philosopher** (celle de l'ancien site), via Google Fonts.
- Icônes uniquement pour les réseaux sociaux du pied de page (demande du client).
- Bio d'accueil : phrase de l'ancien site (EN verbatim) ; FR et NL traduits par nos soins, à faire valider.
- Liens non fournis (`None`) : un message « lien à fournir » s'affiche au clic.

## À fournir par l'artiste

Liens Etsy, Redbubble, Instagram, Facebook, TikTok, YouTube ; e-mail ; service de newsletter ; compte de
paiement ; vidéo de présentation (≤ 3 min) ; photos HD et informations réelles des originaux ; FAQ réelle ;
portrait et biographie.
