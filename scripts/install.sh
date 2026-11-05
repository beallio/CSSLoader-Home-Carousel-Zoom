#!/usr/bin/env bash
set -euo pipefail

if (( EUID == 0 )); then
    printf 'Run this installer as your normal user, without sudo.\n' >&2
    exit 1
fi

package_dir=$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
source_dir="$package_dir/Home Carousel Zoom"
destination="${HOME:?Your HOME environment variable must be set}/homebrew/themes/Home Carousel Zoom"
files=(theme.json shared.css focus.css artwork.css performance.css LICENSE)

# Check the complete package before changing the installed theme.
for file in "${files[@]}"; do
    if [[ ! -f "$source_dir/$file" ]]; then
        printf 'Missing package file: %s\nExtract the complete ZIP before installing.\n' "$source_dir/$file" >&2
        exit 1
    fi
done

mkdir -p -- "$destination"
for file in "${files[@]}"; do
    install -m 0644 -- "$source_dir/$file" "$destination/$file"
done

printf 'Installed Home Carousel Zoom into:\n%s\n\n' "$destination"
printf 'Saved settings and other themes were left unchanged.\n'
printf 'In Gaming Mode, open Decky > CSS Loader, select Refresh, and turn the theme on.\n'
