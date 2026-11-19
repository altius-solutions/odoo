#!/usr/bin/env python3
# Part of Altius ERP. See LICENSE file for full copyright and licensing details.
"""Regenerate the Altius wordmark and icon files.

Run from the repository root:

    python3 altius_addons/tools/render_brand_assets.py

Requires Pillow. Wordmark text is drawn with Inter when that font is
installed, then Liberation Sans, then DejaVu Sans.
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1] / "altius_branding" / "static"
IMG = ROOT / "src" / "img"
DESC = ROOT / "description"

NAVY = "#1E1B4B"
INDIGO = "#6366F1"
PRIMARY = "#4F46E5"
ON_NAVY = "#C7D2FE"
FONT_STACK = "Inter, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif"

FONT_CANDIDATES = (
    "/usr/share/fonts/truetype/macos/Inter-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
)


def font(size: int) -> ImageFont.FreeTypeFont:
    for path in FONT_CANDIDATES:
        if Path(path).is_file():
            return ImageFont.truetype(path, size)
    raise SystemExit("No sans-serif bold font found")


def tracked_width(face: ImageFont.FreeTypeFont, text: str, tracking: float) -> float:
    width = 0.0
    for char in text:
        width += face.getlength(char) + tracking
    return width - tracking


def draw_tracked(draw, text, origin, face, fill, tracking):
    x, y = origin
    for char in text:
        draw.text((x, y), char, font=face, fill=fill)
        x += face.getlength(char) + tracking
    return x


def icon_image(size: int) -> Image.Image:
    image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    radius = int(size * 0.22)
    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=PRIMARY)

    def point(x, y):
        return (x * size / 64, y * size / 64)

    # Stylized A: outer shape, then the counter punched in the icon color.
    draw.polygon(
        [
            point(32, 12),
            point(52, 52),
            point(42.2, 52),
            point(38.6, 42),
            point(25.4, 42),
            point(21.8, 52),
            point(12, 52),
        ],
        fill="white",
    )
    draw.polygon(
        [point(32, 24), point(36.2, 35.2), point(27.8, 35.2)],
        fill=PRIMARY,
    )
    return image


def icon_svg() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" role="img" aria-label="Altius">
  <rect width="64" height="64" rx="14" fill="#4F46E5"/>
  <path fill="#ffffff" d="M32 12 L52 52 H42.2 L38.6 42 H25.4 L21.8 52 H12 Z"/>
  <path fill="#4F46E5" d="M32 24 L36.2 35.2 H27.8 Z"/>
</svg>
"""


def wordmark_png(scale: int, left_fill: str, right_fill: str) -> Image.Image:
    face = font(64 * scale)
    tracking_left = -1.6 * scale
    tracking_right = 0.4 * scale
    gap = 18 * scale
    pad_x = 4 * scale
    pad_y = 8 * scale
    left = "ALTIUS"
    right = "SOLUTIONS"
    left_w = tracked_width(face, left, tracking_left)
    right_w = tracked_width(face, right, tracking_right)
    ascent, descent = face.getmetrics()
    width = int(pad_x * 2 + left_w + gap + right_w + 2)
    height = int(pad_y * 2 + ascent + descent)
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    baseline = pad_y
    end = draw_tracked(draw, left, (pad_x, baseline), face, left_fill, tracking_left)
    draw_tracked(draw, right, (end + gap, baseline), face, right_fill, tracking_right)
    return image


def wordmark_svg(left_fill: str, right_fill: str) -> str:
    face = font(64)
    tracking_left = -1.6
    tracking_right = 0.4
    gap = 18
    left_w = tracked_width(face, "ALTIUS", tracking_left)
    right_w = tracked_width(face, "SOLUTIONS", tracking_right)
    ascent, descent = face.getmetrics()
    # Extra padding so browser font engines, which don't match Pillow's
    # metrics exactly, don't clip the cap height.
    pad_top = 16
    width = round(left_w + gap + right_w + 8)
    height = ascent + descent + pad_top + 8
    right_x = round(left_w + gap)
    baseline = ascent + pad_top
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="Altius Solutions">
  <title>Altius Solutions</title>
  <text x="4" y="{baseline}" fill="{left_fill}" font-family="{FONT_STACK}" font-weight="700" font-size="64" letter-spacing="{tracking_left}">ALTIUS</text>
  <text x="{right_x + 4}" y="{baseline}" fill="{right_fill}" font-family="{FONT_STACK}" font-weight="700" font-size="64" letter-spacing="{tracking_right}">SOLUTIONS</text>
</svg>
"""


def main() -> None:
    IMG.mkdir(parents=True, exist_ok=True)
    DESC.mkdir(parents=True, exist_ok=True)

    (IMG / "icon.svg").write_text(icon_svg(), encoding="utf-8")
    (IMG / "wordmark.svg").write_text(wordmark_svg(NAVY, INDIGO), encoding="utf-8")
    (IMG / "wordmark-on-navy.svg").write_text(wordmark_svg("#FFFFFF", ON_NAVY), encoding="utf-8")

    icon_512 = icon_image(512)
    icon_512.save(IMG / "icon-512.png")
    icon_512.resize((192, 192), Image.Resampling.LANCZOS).save(IMG / "icon-192.png")
    icon_512.resize((180, 180), Image.Resampling.LANCZOS).save(IMG / "icon-180.png")
    icon_32 = icon_512.resize((32, 32), Image.Resampling.LANCZOS)
    icon_16 = icon_512.resize((16, 16), Image.Resampling.LANCZOS)
    icon_48 = icon_512.resize((48, 48), Image.Resampling.LANCZOS)
    icon_32.save(
        IMG / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)],
        append_images=[icon_16, icon_48],
    )
    icon_512.resize((128, 128), Image.Resampling.LANCZOS).save(DESC / "icon.png")

    wordmark_png(2, NAVY, INDIGO).save(IMG / "company_logo.png")
    print(f"Wrote brand assets under {IMG}")


if __name__ == "__main__":
    main()
