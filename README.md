# Home Carousel Zoom

A [CSS Loader](https://docs.deckthemes.com/CSSLoader/) theme for SteamOS Gaming Mode. Enlarge a Home carousel cover when you hover over it with a pointer or select it with a controller.

**Zoom size: 100%–130%, in 5% steps. Default: 115%.**

The focus ring and attached title move with the cover. The Library grid is not changed. 

## Screenshots at every size

The screenshots use **Art Hero**, **Centered Game Text**, **Game Header Text Stroke**, **Darken Unfocused Games**, and **Round**, with other installed plugins supplying badges. Those appearance changes are not part of Home Carousel Zoom and are not required or bundled.

Percentages apply to the selected card's existing appearance. **100% keeps Steam's normal focus effect**; it does not remove that effect.

| Zoom size | Added enlargement | Steam Deck screenshot |
| --- | --- | --- |
| 100% | None | [![Home carousel at 100% zoom](assets/screenshots/zoom-100.webp)](assets/screenshots/zoom-100.webp) |
| 105% | 5% | [![Home carousel at 105% zoom](assets/screenshots/zoom-105.webp)](assets/screenshots/zoom-105.webp) |
| 110% | 10% | [![Home carousel at 110% zoom](assets/screenshots/zoom-110.webp)](assets/screenshots/zoom-110.webp) |
| **115% — default** | **15%** | [![Home carousel at the default 115% zoom](assets/screenshots/zoom-115.webp)](assets/screenshots/zoom-115.webp) |
| 120% | 20% | [![Home carousel at 120% zoom](assets/screenshots/zoom-120.webp)](assets/screenshots/zoom-120.webp) |
| 125% | 25% | [![Home carousel at 125% zoom](assets/screenshots/zoom-125.webp)](assets/screenshots/zoom-125.webp) |
| 130% | 30% | [![Home carousel at 130% zoom](assets/screenshots/zoom-130.webp)](assets/screenshots/zoom-130.webp) |

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

Open **… → Decky → CSS Loader → Home Carousel Zoom**, expand the theme's settings, and adjust **Zoom size**.

- Use left/right controller input on the slider to decrease/increase the size.
- Pointer hover and controller focus both trigger zoom. A touchscreen has no persistent hover state.
- Covers grow over adjacent cards rather than pushing them apart. Large values can cover more of a neighboring card or title, particularly with other carousel layouts.

## License and credits

The theme code is licensed under the [MIT License](LICENSE).

Steam and its interface belong to Valve. Game artwork, names, and logos visible in the screenshots belong to their respective owners; the MIT license does not grant rights to that artwork. The selected game in the comparison is *Teenage Mutant Ninja Turtles: Splintered Fate*. Screenshots document this theme's behavior, not ownership of the depicted artwork.

Art Hero is by Metagawa. Centered Game Text is by SuchMeme. These and the other appearance themes shown in the screenshots are separate projects, not included in this theme. CSS Loader and Decky Loader are separate projects; this theme is not an official Valve product.
