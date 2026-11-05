"""Prépare les images du site depuis les fichiers fournis par l'artiste.

    python src/images.py

- Œuvres : « Oeuvres originales disponibles/<chemin de data.py> » → assets/img/oeuvres/<id>.webp (1600 px max),
  <id>-600.webp et <id>-zoom.webp (vue agrandie). Proportions d'origine, jamais d'agrandissement : un fichier
  de 500 px reste à 500 px. Filigrane : logo + « © Guido De Oliveira » en coin partout, grand logo pâle au centre
  de la vue agrandie ; droits d'auteur dans les métadonnées. Police : source/fonts/Philosopher-Regular.ttf.
- Atelier : source/raw-atelier-reel.webp (Mepainting.webp de l'artiste) → assets/img/atelier.webp
- Goodies : source/goodies/* (photos de sa boutique Redbubble, 600 × 600, une par catégorie de produit,
  relevées le 2026-11-05) → assets/img/goodies.webp, photomontage de 4 colonnes dans l'ordre des noms de fichiers.
"""
from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

from data import OEUVRES

Image.MAX_IMAGE_PIXELS = None
ROOT = Path(__file__).resolve().parent.parent
ORIG = ROOT / 'Oeuvres originales disponibles'
IMG = ROOT / 'site' / 'assets' / 'img'
LOGO_PNG = ROOT / 'Logos' / 'Logo blanc sur fond transparent.png'
FONT = ROOT / 'source' / 'fonts' / 'Philosopher-Regular.ttf'
SIGNATURE = '© Guido De Oliveira'

# Droits d'auteur inscrits dans chaque fichier d'œuvre (balises EXIF Artist et Copyright).
EXIF = Image.Exif()
EXIF[0x013B] = 'Guido De Oliveira'
EXIF[0x8298] = 'Copyright Guido De Oliveira. All rights reserved.'


# ── Filigrane ─────────────────────────────────────────────────────────
# Posé sur les images publiées, après réduction (il reste net à toutes les tailles).
# Les fichiers originaux de l'artiste ne sont jamais modifiés.

@lru_cache(None)
def logo_mask():
    """Masque du logo (canal alpha du PNG blanc), recadré au plus juste."""
    a = Image.open(LOGO_PNG).getchannel('A')
    return a.crop(a.getbbox())


def stamp(im, mask, xy, opacity, shadow):
    """Applique `mask` en blanc à `opacity`, sur une ombre sombre floue qui le garde lisible sur fond clair."""
    w, h = mask.size
    blur = max(1, round(h * 0.06))
    sh = Image.new('L', (w + 4 * blur, h + 4 * blur), 0)
    sh.paste(mask, (2 * blur, 2 * blur))
    sh = sh.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: round(v * shadow))
    im.paste((20, 19, 17), (xy[0] - 2 * blur, xy[1] - 2 * blur), sh)
    im.paste((255, 255, 255), xy, mask.point(lambda v: round(v * opacity)))


def mark_corner(im):
    """Logo + « © Guido De Oliveira » en bas à gauche, sur toutes les œuvres
    (à gauche : l'artiste peint sa propre signature en bas à droite, il ne faut pas la couvrir)."""
    w, h = im.size
    lh = max(20, round(min(w, h) * 0.055))       # hauteur du logo
    logo = logo_mask().resize((round(lh * logo_mask().width / logo_mask().height), lh), Image.LANCZOS)
    font = ImageFont.truetype(str(FONT), max(11, round(lh * 0.5)))
    l, t, r, b = font.getbbox(SIGNATURE)
    gap = round(lh * 0.3)
    mask = Image.new('L', (logo.width + gap + r - l, lh), 0)
    mask.paste(logo, (0, 0))
    ImageDraw.Draw(mask).text((logo.width + gap - l, (lh - (b - t)) // 2 - t), SIGNATURE, fill=255, font=font)
    m = round(min(w, h) * 0.03) + 2
    stamp(im, mask, (m, h - mask.height - m), opacity=0.72, shadow=0.45)


def mark_center(im):
    """Grand logo très pâle au centre : ne disparaît pas en recadrant une capture d'écran."""
    w, h = im.size
    lh = round(min(w, h) * 0.42)
    logo = logo_mask().resize((round(lh * logo_mask().width / logo_mask().height), lh), Image.LANCZOS)
    stamp(im, logo, ((w - logo.width) // 2, (h - logo.height) // 2), opacity=0.13, shadow=0.10)


def save(im, path, size, q, marks=(), exif=None):
    out = im.copy()
    out.thumbnail((size, size), Image.LANCZOS)  # ne réduit que si nécessaire
    for mark in marks:
        mark(out)
    out.save(path, 'WEBP', quality=q, method=6, **({'exif': exif.tobytes()} if exif else {}))
    return out.size


def oeuvres():
    (IMG / 'oeuvres').mkdir(parents=True, exist_ok=True)
    for o in OEUVRES:
        im = ImageOps.exif_transpose(Image.open(ORIG / o['source'])).convert('RGB')
        out = IMG / 'oeuvres'
        big = save(im, out / f'{o["id"]}.webp', 1600, 82, (mark_corner,), EXIF)
        save(im, out / f'{o["id"]}-600.webp', 600, 80, (mark_corner,), EXIF)
        save(im, out / f'{o["id"]}-zoom.webp', 1600, 82, (mark_corner, mark_center), EXIF)  # agrandissement
        flag = '  <- source trop petite' if max(im.size) < 1200 else ''
        print(f'{o["id"]:24} {im.size[0]:>5}×{im.size[1]:<5} -> {big[0]}×{big[1]}{flag}')


def atelier():
    src = ROOT / 'source' / 'raw-atelier-reel.webp'
    if src.exists():
        print('atelier', save(Image.open(src).convert('RGB'), IMG / 'atelier.webp', 1080, 82))


def goodies(cols=4, tile=600, gap=12, bg=(244, 243, 241)):
    tiles = sorted(p for p in (ROOT / 'source' / 'goodies').iterdir() if p.suffix.lower() in ('.jpg', '.jpeg', '.png', '.webp'))
    if not tiles:
        return
    rows = -(-len(tiles) // cols)
    sheet = Image.new('RGB', (cols * tile + (cols - 1) * gap, rows * tile + (rows - 1) * gap), bg)
    for i, f in enumerate(tiles):
        t = ImageOps.fit(Image.open(f).convert('RGB'), (tile, tile), Image.LANCZOS)
        sheet.paste(t, ((i % cols) * (tile + gap), (i // cols) * (tile + gap)))
    print('goodies', save(sheet, IMG / 'goodies.webp', 1600, 80), save(sheet, IMG / 'goodies-800.webp', 800, 78))


if __name__ == '__main__':
    oeuvres()
    atelier()
    goodies()
