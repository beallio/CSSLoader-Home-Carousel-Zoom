# Home Carousel Zoom

A [CSS Loader](https://docs.deckthemes.com/CSSLoader/) theme for SteamOS Gaming Mode. Enlarge a Home carousel cover when you hover over it with a pointer or select it with a controller.

**Two sliders set the size: Base zoom (%) from 100 to 200 in steps of 10, and Fine adjustment from +0 to +10 in steps of 1. The two values are added, which gives 100% to 210% total. Default: 110 + 5 = 115%.**

The focus ring and attached title move with the cover. The Library grid is not changed, and the **View more in your Library** card at the end of the row keeps its normal size. Selecting that card no longer makes the Home page jump vertically; normal horizontal scrolling remains.

## Screenshots

[![Home Carousel Zoom at 115% with a cyan custom halo](assets/preview.png)](assets/preview.png)

Current preview: **115% zoom**, cyan Custom highlight at 80% alpha, **2 px outline**, **15 px halo**, and **0% artwork opacity**. Home Carousel Zoom was the only enabled CSS Loader theme. Cover badges come from other installed plugins and are not included.

### Size comparisons

The size-comparison screenshots below use **Art Hero**, **Centered Game Text**, **Game Header Text Stroke**, **Darken Unfocused Games**, and **Round**, with other installed plugins supplying badges. Those appearance changes are not part of Home Carousel Zoom and are not required or bundled.

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

The two sliders, artwork glow, and custom focus controls require **v1.1.0 or later**.

### From a release

1. Download the theme ZIP from [Releases](https://github.com/beallio/CSSLoader-Home-Carousel-Zoom/releases).
2. In Desktop Mode, create `~/homebrew/themes/Home Carousel Zoom/`.
3. Extract all files into that folder, without another nested folder. For v1.1.0, it must contain `theme.json`, `shared.css`, `focus.css`, `artwork.css`, and `LICENSE`.
4. Return to Gaming Mode. Open **… → Decky → CSS Loader**, then select **Refresh**.
5. Enable **Home Carousel Zoom**.

### From this repository

Copy the complete [`Home Carousel Zoom`](Home%20Carousel%20Zoom) folder into `~/homebrew/themes/`, then refresh CSS Loader and enable the theme. Do not copy the repository root into the themes folder.

## Adjust the size

Open **… → Decky → CSS Loader → Home Carousel Zoom** and expand the theme's settings. The two zoom sliders are:

| Slider | Range | Step | Default |
| --- | --- | --- | --- |
| **Base zoom (%)** | 100 to 200 | 10 | 110 |
| **Fine adjustment** | +0 to +10 | 1 | +5 |

**Total zoom = Base zoom + Fine adjustment.** For example, `110 + 5` gives 115%, `130 + 7` gives 137%, and `200 + 10` gives 210%.

- Use left/right controller input on each slider to decrease/increase its value.
- Different combinations can give the same total. `100 + 10` and `110 + 0` both give 110%.
- Pointer hover and controller focus both trigger zoom. A touchscreen has no persistent hover state.
- Covers grow over adjacent cards rather than pushing them apart. Large values can cover neighboring cards, titles, or the status bar. On the stock Steam layout, high zoom can extend above the screen and cut off the cover. Lower the zoom if the cover does not fit.
- If you used the earlier single **Zoom size** slider, your saved value does not transfer. The theme starts at the 115% default, so set the two sliders again after the update.

## Adjust the highlight and glow

The **Focus appearance** selector controls the Home cover's outline:

- **Steam default** (default) leaves Steam's outline in place. Other enabled themes can still change its appearance; this option does not disable them.
- **Custom** adds a fixed-color outline and an optional halo, and hides the cover's animated sheen. It does not remove the artwork-colored glow.

The two glows are separate. **Artwork glow** is the broad, translucent effect that takes its colors from the cover art. **Halo size** controls the blur radius of the added glow around the custom outline.

Outline thickness, Artwork opacity, and Halo size use numeric sliders. Use left/right controller input to adjust them. Artwork opacity and Halo size use coarse steps so their complete scales fit in CSS Loader. Focus appearance remains a Steam default / Custom selector, and Highlight color still uses the color picker.

| Setting | Works when | Range or choices | Default |
| --- | --- | --- | --- |
| **Use Steam's artwork glow** | Both focus modes | On / Off | On |
| **Artwork opacity (%, override only)** | Use Steam's artwork glow is Off, in either focus mode | 0–100%, step 10% | 50% |
| **Highlight color** | Custom only | Hue, saturation, lightness, and alpha | White at 60% alpha (`#ffffff99`) |
| **Outline thickness (px, Custom only)** | Custom only | 1–10 px, step 1 px | 2 px |
| **Halo size (px, Custom only)** | Custom only | 0–30 px, step 5 px | 0 px |

- **Use Steam's artwork glow → On** leaves Steam's and your other themes' artwork effect unchanged. The Artwork opacity slider keeps its saved value but has no effect.
- Turn that toggle **Off** to use the numeric Artwork opacity slider. **0%** hides the artwork glow; **100%** makes its layer fully opaque. This does not change the artwork's colors.
- **Halo size → 0** removes only the added custom halo. It keeps the custom outline and does not change Artwork opacity.
- Halo size sets the blur radius. Its spread increases by 1 px for each 5 px of blur. For example, size 15 uses 15 px blur and 3 px spread.
- Color-picker alpha controls the opacity of the custom outline and halo, not Artwork opacity. Alpha zero makes the custom outline and halo invisible.
- CSS Loader shows the color picker only in Custom mode. Its current theme format cannot hide or disable the separate numeric sliders when they are inactive. Their labels state **Custom only** or **override only**.
- Switching back to **Steam default** removes the custom outline and halo without discarding your custom settings. The artwork toggle and opacity keep their separate settings. CSS Loader saves settings across refreshes.
- These effects follow pointer hover and controller focus, scale with the cover, and leave the Library shortcut and Library grid unchanged.

### Why the glow differs between games

Steam creates the broad artwork glow from a copy of the selected cover. Its current filter multiplies saturation by three and brightness by two, then applies a 3 px blur. Bright colors and large bright areas in the cover therefore produce different glow colors and brightness, even at the same Artwork opacity.

The custom halo has a fixed color, but its background changes how visible it is. For example, a white halo blends into Deadpool's white background more than it does into the colored backgrounds of Wobbly Life or Transformers Fall of Cybertron. A stronger-looking glow does not necessarily mean a stronger setting.

For a single-color effect, turn **Use Steam's artwork glow Off**, set **Artwork opacity to 0%**, and choose a Custom halo size above zero. This removes the artwork-dependent glow, but background contrast still affects the halo's appearance.

### Defaults and manual reset

The Custom starting values use Steam's current base outline color and width: white at 60% alpha, 2 px thick, with no added custom halo. These values do not recreate Steam's animated outline, outline offset, shadow, or artwork effect. For the native focus effects, select **Focus appearance → Steam default** and turn **Use Steam's artwork glow On**; other enabled themes remain in effect.

The installed CSS Loader has no button to reset this group of settings, and its theme format cannot add one. To reset Custom manually:

1. Select **Custom** and open **Highlight color**.
2. Set Hue to **0**, Saturation to **0**, Lightness to **100**, and Alpha to **0.6**, then select **Confirm**.
3. Set **Outline thickness to 2 px** and **Halo size to 0 px**.
4. To reset the artwork controls too, set **Artwork opacity to 50%** and turn **Use Steam's artwork glow On**. The stored 50% value applies only if you later turn the toggle Off.

These steps leave both zoom sliders unchanged.

## License and credits

The theme code is licensed under the [MIT License](LICENSE).

Steam and its interface belong to Valve. Game artwork, names, and logos visible in the screenshots belong to their respective owners; the MIT license does not grant rights to that artwork. The selected game in the comparison is *Teenage Mutant Ninja Turtles: Splintered Fate*. Screenshots document this theme's behavior, not ownership of the depicted artwork.

Art Hero is by Metagawa. Centered Game Text is by SuchMeme. These and the other appearance themes shown in the screenshots are separate projects, not included in this theme. CSS Loader and Decky Loader are separate projects; this theme is not an official Valve product.
