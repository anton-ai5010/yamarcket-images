"""
Convert all PNG files in main_cards/ and instructions_v2/ to JPEG.
Preserves directory structure. Removes original PNGs after conversion.
"""
from PIL import Image
from pathlib import Path
import sys

ROOT = Path(__file__).parent
DIRS = ["main_cards", "instructions_v2"]
QUALITY = 92

def convert_dir(folder: Path):
    pngs = list(folder.rglob("*.png"))
    print(f"\n{folder.name}/: {len(pngs)} PNG files")
    ok = skip = fail = 0
    for i, png in enumerate(pngs):
        jpg = png.with_suffix(".jpg")
        if jpg.exists():
            skip += 1
            continue
        try:
            with Image.open(png) as img:
                rgb = img.convert("RGB")
                rgb.save(jpg, "JPEG", quality=QUALITY, optimize=True)
            png.unlink()
            ok += 1
            if (i + 1) % 200 == 0:
                print(f"  [{i+1}/{len(pngs)}] converted...")
        except Exception as e:
            print(f"  FAIL {png.name}: {e}")
            fail += 1
    print(f"  Done: {ok} converted, {skip} skipped, {fail} failed")

for d in DIRS:
    convert_dir(ROOT / d)

print("\nAll done!")
