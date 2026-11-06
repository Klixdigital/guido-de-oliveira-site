# Guido De Oliveira — site d'artiste peintre

Site vitrine, **HTML/CSS/JS pur** (aucun framework), en **FR / NL / EN**. Commencé le 2026-10-16,
contenu réel de l'artiste intégré le 2026-11-05.
Références de l'artiste : Chuck Black et Stéphane Alsac (simplicité), Raffaela Lerch (boutique Etsy).
Objectif : le moins de clics possible entre le coup de cœur et l'achat.

## Structure

```
Oeuvres originales disponibles/   fichiers de l'artiste, un dossier par série — hors git, lus par images.py
Logos/                            logo noir et logo blanc (PNG) — hors git ; vectorisé dans site/assets/img/logo.svg
more info/                        notes de l'artiste sur la maquette, FAQ, book, CV, CGV, vie privée, photos — hors git
site/                  le site à mettre en ligne tel quel
  index.html           redirige vers la langue du navigateur, sinon choix FR / NL / EN
  fr/ nl/ en/          accueil, à propos, galerie, prints, goodies, FAQ, contact, CGV, confidentialité
  assets/img/oeuvres/  <id>.webp (1600 px max) et <id>-600.webp, proportions d'origine
source/                bruts hors ligne : photo d'atelier, photos Redbubble du montage goodies (source/goodies/)
src/data.py            CONTENU : séries, œuvres, liens, formats de prints, FAQ, expositions et presse
src/legal.py           CGV et politique de confidentialité (textes de l'artiste ; NL/EN = traductions de courtoisie)
src/build.py           gabarits et textes d'interface des 3 langues
src/images.py          œuvres → WebP, photo d'atelier, photomontage goodies
```

```bash
python src/images.py   # après ajout ou remplacement d'une œuvre
python src/build.py    # (sans -I : le script importe data.py)
```

Menu : À propos · Galerie · Prints · Goodies · FAQ · Contact (plus de panier depuis le 2026-11-06). Pied de page : CGV · Politique de confidentialité.
« À propos » se termine par **Expositions et distinctions** (book 2025 p. 19 + CV), puis **Sur Instagram** : carrousel
rempli depuis `LIENS['instagram_feed']` (flux JSON type Behold, à relier au compte de Guido) ; vide = bouton « Suivre » seul.
Textes des œuvres : `DESCRIPTIONS` (CV, 4 œuvres) et `HISTOIRES` (book, 8 œuvres) dans `data.py`.

## Pages légales (2026-11-05)

Reprises des deux .docx de l'artiste, sans rien ajouter de juridique. Écarts, listés en tête de `legal.py` :
section « Vendeur » ajoutée (adresse et n° d'entreprise « À fournir »), téléphone retiré du contact (aucun sur le
site), e-mail inséré à la place du `[adresse e-mail de contact]` laissé vide. **À faire valider avant toute vente** :
la politique parle de comptes clients, de panier et de cookies d'analyse que le site n'a pas ; les CGV décrivent une
commande et un paiement en ligne (Stripe) alors que, depuis le 2026-11-06, l'achat d'un original se fait par demande
directe à l'artiste.

## Ce que l'artiste a demandé (more info/NotesSiteWeb_2.odt)

- **Accueil** : logo noir, « The Art of Guido De Oliveira. » (en anglais dans les 3 langues), son texte d'intro,
  « Wave at Sunset » à droite **sans titre** en attendant sa vidéo de présentation.
- **Galerie classée par série**, dans cet ordre : Phares, Glories of the Past, Message in a Bottle, Peluches, Divers.
- **Prints** : bouton « Acheter » (pas « Acheter sur Etsy ») ; formats Petit 30×40 / Moyen 40×50 / Grand 45×61 /
  Très grand 61×81, prix « à partir de », provisoires.
- **Goodies** : un seul photomontage de ses produits Redbubble puis le lien vers la boutique, pas de catalogue.
  Montage refait le 2026-11-05 depuis sa boutique (150 motifs, 169 produits), porté à 24 produits (6 rangées de 4) le 2026-11-06 ;
  l'accueil garde un carré des 16 premiers (`goodies-carte.webp`). Produits réels,
  uniquement ses propres œuvres ; le texte liste toutes les catégories en vente, sans prix (ils changent avec les
  promos Redbubble). Pas de sac à dos dans sa boutique, contrairement à ses notes. Ancien montage gardé dans
  `source/goodies-ancien-2026-11-05/`. Sa boutique contient aussi du fan art (Star Wars, Iron Man, Shaun le mouton) :
  ne jamais le montrer sur le site (droits de Disney, Marvel, Aardman).
- **Contact** : info@guidodeoliveira.com ; Instagram, TikTok, YouTube @guiarteofficial ; Pinterest ; pas de Facebook.

## État du contenu

- **20 œuvres réelles**. Année, technique et format repris du book 2025 et du CV pour 8 d'entre elles ;
  le reste s'affiche « À fournir ». **Prix, descriptions et histoires : sur une fiche séparée de l'artiste, pas
  encore reçue.** Les cartes « Œuvres récentes » de l'accueil n'affichent pas l'année (demande du 2026-11-06).
- 7 fichiers sources font moins de 1 000 px (Glory II, IV, V ; Lighthouse 3, 4, 5 ; Sunset at Mar Menor) :
  affichés à leur taille réelle, jamais étirés. Demander les versions HD.
- Le léopard de l'ancien site (« Leo the leopard » sur Redbubble, « Leo is going out for a walk » dans le book)
  n'est pas dans le dossier des œuvres disponibles : retiré de la galerie.
- Plus aucune image générée : photo d'atelier = `Mepainting.webp` de l'artiste, vidéo = `Section_a_propos.mp4` (4 s).
- Traductions NL et EN (intro, bio, FAQ, textes alternatifs) faites par nos soins, à faire valider.

## Vente (plus d'e-commerce depuis le 2026-11-06)

- **Pas de panier ni de paiement en ligne** (décision du 2026-11-06) : page panier, `cart.js`, frais de livraison et
  lien de paiement supprimés. Chaque original se vend par demande directe à l'artiste, prix affiché s'il est connu.
- Les CGV et la politique de confidentialité de l'artiste décrivent encore une commande en ligne (paiement Stripe,
  « produits ajoutés au panier ») : à faire adapter par l'artiste, ne pas réécrire son texte légal de notre propre chef.
- « Acquérir l'original » ouvre **directement un e-mail** pré-rempli (choix du 2026-11-06, la fenêtre Gmail/Outlook
  a été retirée) : série, année, technique, dimensions, prix et description quand ils sont connus. Pas de photo : un
  lien e-mail ne peut pas joindre d'image. Limite connue : sur un ordinateur sans logiciel de messagerie configuré
  (cas du poste KLIX), le clic ne fait rien ; l'adresse reste affichée en page Contact.
- Prints → Etsy (lien à venir), avec un menu des 4 formats par print qui met à jour le prix « dès … » ; un clic sur
  le cadre agrandit l'œuvre (même fenêtre que la galerie, version `-zoom` filigranée).
- Goodies → Redbubble (boutique Guiarte SMS).

## Protection des œuvres (demande de l'artiste, 2026-11-05)

- **Filigrane intégré** par `images.py` aux images publiées, jamais aux originaux : logo + « © Guido De Oliveira »
  en **bas à gauche** sur toutes les versions (l'artiste peint sa signature en bas à droite, ne pas la couvrir) ;
  grand logo pâle (13 %) au centre de `<id>-zoom.webp`, la seule version ouverte par le zoom de la galerie.
  Droits d'auteur aussi dans les métadonnées EXIF. Le filigrane se règle dans `mark_corner` / `mark_center`.
  Il dépend de `Logos/` et de `source/fonts/Philosopher-Regular.ttf` (hors git, à garder sur le poste).
- **Clic droit, glisser et appui long bloqués** sur les œuvres (`site.js` + fin de `style.css`). Dissuasif
  seulement : une capture d'écran reste possible, d'où le filigrane. Ne pas présenter ça au client comme infaillible.

## Vidéo de présentation (essais du 2026-11-06, section temporaire dans « À propos »)

Trois versions de ~30 s, `site/assets/video/presentation-v1/2/3.mp4`, affichées l'une sous l'autre (`VIDEO_VERSIONS` dans
`build.py`) pour choisir. Montées à partir des **œuvres réelles** : chaque toile posée sur un mur de galerie 16:9 (jamais
recadrée), animée par Higgsfield (Kling 3.0, mouvement de caméra seul), musiques instrumentales ElevenLabs Music,
cartons logo + « The Art of Guido De Oliveira. ». Clips vérifiés image par image : peintures intactes ; Kling ajoute du
décor (fenêtre, interrupteur, second cadre). Le clip d'atelier animé déforme le visage de Guido après ~3 s : seul le
passage 1-3,5 s est gardé (V3), précédé de son vrai clip. Une fois la version choisie : la mettre sur l'accueil (demande
de l'artiste) et retirer la section temporaire.

## Règles

- Police **Philosopher** (celle de l'ancien site), via Google Fonts.
- Icônes uniquement pour les réseaux sociaux du pied de page (demande du client).
- Une œuvre n'est jamais recadrée : vignettes en `contain` sur fond mur, galerie à ses proportions.
- Liens non fournis (`None`) : un message « lien à fournir » s'affiche au clic.

## À fournir par l'artiste

Fiche des œuvres (prix, descriptions, histoires, techniques et formats manquants) ; versions HD des 7 petites
images ; lien Etsy ; service de newsletter ; vidéo de présentation pour l'accueil.
À trancher : retours 15 jours (FAQ) ou 14 jours (CGV) ; Pinterest @atguiarteofficial (notes) ou @guiarteofficial
(book) ; la FAQ renvoie à une rubrique actualités qui n'existe pas ; expositions 2017-2019 (FAQ) ou 2020 seulement
(book, CV) ; galerie « Mundoarti » (book) ou « Munduarti » (CV) ; adresse et numéro d'entreprise pour les CGV.
