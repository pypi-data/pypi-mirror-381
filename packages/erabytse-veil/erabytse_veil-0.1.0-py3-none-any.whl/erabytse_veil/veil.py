#!/usr/bin/env python3
"""
erabytse-veil v0.1
An ethical veil for image metadata — not deletion, but intentional protection.
"""

import argparse
from pathlib import Path
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif_data(image_path):
    """Extrait les métadonnées EXIF d'une image."""
    image = Image.open(image_path)
    exifdata = image.getexif()
    if not exifdata:
        return {}

    exif = {}
    for tag_id, value in exifdata.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == "GPSInfo":
            gps_info = {}
            for gps_key in value.keys():
                gps_tag = GPSTAGS.get(gps_key, gps_key)
                gps_info[gps_tag] = value[gps_key]
            exif[tag] = gps_info
        else:
            exif[tag] = value
    return exif


def remove_sensitive_exif(exif_data):
    """Retire les métadonnées sensibles, garde les créatives."""
    sensitive = {
        'GPSInfo', 'DateTime', 'DateTimeOriginal', 'DateTimeDigitized',
        'Make', 'Model', 'SerialNumber', 'HostComputer'
    }
    creative = {
        'FNumber', 'ExposureTime', 'ISOSpeedRatings', 'FocalLength',
        'LensModel', 'Artist', 'Copyright'
    }

    # On garde uniquement ce qui est créatif
    safe_exif = {}
    for key in creative:
        if key in exif_data:
            safe_exif[key] = exif_data[key]

    return safe_exif


def apply_veil(input_path: Path, output_path: Path):
    """Applique le voile : sauvegarde l'image sans métadonnées sensibles."""
    # Ouvre l'image originale
    image = Image.open(input_path)

    # Récupère les EXIF complets
    exif_full = get_exif_data(input_path)

    # Filtre les EXIF
    exif_safe = remove_sensitive_exif(exif_full)

    # Sauvegarde sans les métadonnées sensibles
    if exif_safe:
        # Recrée un dictionnaire compatible EXIF
        exif_dict = {}
        for tag, value in exif_safe.items():
            tag_id = next((k for k, v in TAGS.items() if v == tag), None)
            if tag_id:
                exif_dict[tag_id] = value
        image.save(output_path, exif=exif_dict)
    else:
        # Pas de métadonnées créatives → sauvegarde sans EXIF
        image.save(output_path)

    return exif_full, exif_safe


def main():
    parser = argparse.ArgumentParser(
        description="🧵 erabytse-veil: an ethical veil for image metadata.",
        epilog="This is not deletion. This is intentional protection."
    )
    parser.add_argument("--input", type=Path, required=True, help="Input image file")
    parser.add_argument("--output", type=Path, required=True, help="Output image file")

    args = parser.parse_args()

    print("🧵 erabytse-veil v0.1 — a ritual of ethical protection")
    print(f"   Veiling: {args.input}\n")

    if not args.input.exists():
        print("❌ Input file not found.")
        return

    try:
        exif_full, exif_safe = apply_veil(args.input, args.output)
        removed = set(exif_full.keys()) - set(exif_safe.keys())

        print(f"✅ Veil applied. Saved to: {args.output}")
        print(f"   Kept creative metadata: {list(exif_safe.keys()) or 'none'}")
        print(f"   Veiled sensitive data: {list(removed) or 'none'}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()