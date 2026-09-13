#!/usr/bin/env python3
"""Build the standard theme ZIP and a separate local-install ZIP."""

import argparse
import json
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parents[1]
THEME_NAME = "Home Carousel Zoom"
THEME_FILES = ("theme.json", "shared.css", "focus.css", "artwork.css", "LICENSE")
INSTALL_HELP = """Home Carousel Zoom — local installation

You need Decky Loader and its CSS Loader plugin installed first.

1. Switch the Steam Deck to Desktop Mode and extract this ZIP.
2. Open the extracted folder that contains install.sh.
3. Right-click an empty area in that folder and choose Open Terminal Here.
4. Run: bash install.sh
5. Return to Gaming Mode. Open Decky > CSS Loader, select Refresh,
   and turn Home Carousel Zoom on.

The installer uses your home folder: ~/homebrew/themes/Home Carousel Zoom/
It replaces only the five theme files. Saved settings and other themes stay
unchanged. Do not run it with sudo. You can delete this extracted package
after installation.
"""


def add_file(archive: ZipFile, name: str, content: bytes, mode: int = 0o644) -> None:
    entry = ZipInfo(name)
    entry.create_system = 3
    entry.external_attr = (0o100000 | mode) << 16
    entry.compress_type = ZIP_DEFLATED
    archive.writestr(entry, content)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir", type=Path, default=ROOT / "dist", help="ZIP output directory"
    )
    args = parser.parse_args()
    payload = {name: (ROOT / THEME_NAME / name).read_bytes() for name in THEME_FILES}
    version = json.loads(payload["theme.json"])["version"]
    package_name = f"Home-Carousel-Zoom-{version}"
    installer = (ROOT / "scripts" / "install.sh").read_bytes()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    standard_zip = args.output_dir / f"{package_name}.zip"
    with ZipFile(standard_zip, "w") as archive:
        for name, content in payload.items():
            add_file(archive, name, content)

    local_name = f"{package_name}-local-install"
    local_zip = args.output_dir / f"{local_name}.zip"
    with ZipFile(local_zip, "w") as archive:
        add_file(archive, f"{local_name}/install.sh", installer, 0o755)
        add_file(archive, f"{local_name}/INSTALL.txt", INSTALL_HELP.encode("utf-8"))
        for name, content in payload.items():
            add_file(archive, f"{local_name}/{THEME_NAME}/{name}", content)

    print(standard_zip.resolve())
    print(local_zip.resolve())


if __name__ == "__main__":
    main()
