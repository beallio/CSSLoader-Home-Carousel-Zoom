# Home Carousel Zoom

A [CSS Loader](https://docs.deckthemes.com/CSSLoader/) theme for SteamOS Gaming Mode. Enlarge a Home carousel cover when you hover over it with a pointer or select it with a controller.

**Two sliders set the size: Base zoom (%) from 100 to 200 in steps of 10, and Fine adjustment from +0 to +10 in steps of 1. The two values are added, which gives 100% to 210% total. Default: 110 + 5 = 115%.**

The focus ring and attached title move with the cover. The Library grid is not changed, and the **View more in your Library** card at the end of the row keeps its normal size.

## Screenshots

The screenshots use **Art Hero**, **Centered Game Text**, **Game Header Text Stroke**, **Darken Unfocused Games**, and **Round**, with other installed plugins supplying badges. Those appearance changes are not part of Home Carousel Zoom and are not required or bundled.

Percentages apply to the selected card's existing appearance. **100% keeps Steam's normal focus effect**; it does not remove that effect. These screenshots cover 100% to 130%; the sliders now reach 210%.

| Total zoom | Slider values | Steam Deck screenshot |
| --- | --- | --- |
| 100% | 100 + 0 | [![Home carousel at 100% zoom](assets/screenshots/zoom-100.webp)](assets/screenshots/zoom-100.webp) |
| 105% | 100 + 5 | [![Home carousel at 105% zoom](assets/screenshots/zoom-105.webp)](assets/screenshots/zoom-105.webp) |
| 110% | 110 + 0 | [![Home carousel at 110% zoom](assets/screenshots/zoom-110.webp)](assets/screenshots/zoom-110.webp) |
| **115% — default** | **110 + 5** | [![Home carousel at the default 115% zoom](assets/screenshots/zoom-115.webp)](assets/screenshots/zoom-115.webp) |
| 120% | 120 + 0 | [![Home carousel at 120% zoom](assets/screenshots/zoom-120.webp)](assets/screenshots/zoom-120.webp) |
| 125% | 120 + 5 | [![Home carousel at 125% zoom](assets/screenshots/zoom-125.webp)](assets/screenshots/zoom-125.webp) |
| 130% | 130 + 0 | [![Home carousel at 130% zoom](assets/screenshots/zoom-130.webp)](assets/screenshots/zoom-130.webp) |

## Install

You need [Decky Loader](https://decky.xyz/) and its CSS Loader plugin.

### From a release

1. Download `Home-Carousel-Zoom-v1.0.0.zip` from [Releases](https://github.com/beallio/CSSLoader-Home-Carousel-Zoom/releases).
2. In Desktop Mode, create `~/homebrew/themes/Home Carousel Zoom/`.
3. Extract the ZIP into that folder. `theme.json`, `shared.css`, and `LICENSE` must be directly inside it, not inside another nested folder.
4. Return to Gaming Mode. Open **… → Decky → CSS Loader**, then select **Refresh**.
5. Enable **Home Carousel Zoom**.

### From this repository

Copy the complete [`Home Carousel Zoom`](Home%20Carousel%20Zoom) folder into `~/homebrew/themes/`, then refresh CSS Loader and enable the theme. Do not copy the repository root into the themes folder.

## Adjust the size

Open **… → Decky → CSS Loader → Home Carousel Zoom** and expand the theme's settings. There are two sliders:

| Slider | Range | Step | Default |
| --- | --- | --- | --- |
| **Base zoom (%)** | 100 to 200 | 10 | 110 |
| **Fine adjustment** | +0 to +10 | 1 | +5 |

**Total zoom = Base zoom + Fine adjustment.** For example, `110 + 5` gives 115%, `130 + 7` gives 137%, and `200 + 10` gives 210%.

- Use left/right controller input on each slider to decrease/increase its value.
- Different combinations can give the same total. `100 + 10` and `110 + 0` both give 110%.
- Pointer hover and controller focus both trigger zoom. A touchscreen has no persistent hover state.
- Covers grow over adjacent cards rather than pushing them apart. Large values cover more of a neighboring card or title, and above approximately 150% the selected cover reaches the top of the screen and hides part of the status bar.
- If you used the earlier single **Zoom size** slider, your saved value does not transfer. The theme starts at the 115% default, so set the two sliders again after the update.

## License and credits

The theme code is licensed under the [MIT License](LICENSE).

Steam and its interface belong to Valve. Game artwork, names, and logos visible in the screenshots belong to their respective owners; the MIT license does not grant rights to that artwork. The selected game in the comparison is *Teenage Mutant Ninja Turtles: Splintered Fate*. Screenshots document this theme's behavior, not ownership of the depicted artwork.

Art Hero is by Metagawa. Centered Game Text is by SuchMeme. These and the other appearance themes shown in the screenshots are separate projects, not included in this theme. CSS Loader and Decky Loader are separate projects; this theme is not an official Valve product.
