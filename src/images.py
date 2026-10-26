"""Prépare les photos d'œuvres : site/assets/img/oeuvres/raw-<nom>.(png|jpg) → <nom>.jpg (1600 px) et <nom>-600.jpg.

    python src/images.py
"""
from pathlib import Path
from PIL import Image

DIR = Path(__file__).resolve().parent.parent / 'site' / 'assets' / 'img' / 'oeuvres'

for src in sorted(DIR.glob('raw-*')):
    name = src.stem[4:]
    im = Image.open(src).convert('RGB')
    for size, suffix, q in ((1600, '', 84), (600, '-600', 80)):
        out = im.copy()
        out.thumbnail((size, size), Image.LANCZOS)
        out.save(DIR / f'{name}{suffix}.jpg', quality=q, optimize=True, progressive=True)
    print(name, im.size, '->', (DIR / f'{name}.jpg').stat().st_size // 1024, 'Ko')
