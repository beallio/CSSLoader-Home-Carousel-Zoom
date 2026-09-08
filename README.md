# Home Carousel Zoom

A [CSS Loader](https://docs.deckthemes.com/CSSLoader/) theme for SteamOS Gaming Mode. Enlarge a Home carousel cover when you hover over it with a pointer or select it with a controller.

**Zoom size: 100%–130%, in 5% steps. Default: 115%.**

The focus ring and attached title move with the cover. The Library grid is not changed. This is a CSS-only theme, not a separate Decky plugin.

## Screenshots at every size

These are separate captures from a Steam Deck, not resized copies of one image. Each capture uses the same selected game and screen resolution. Click an image to open it at full size.

The screenshots use **Art Hero**, **Centered Game Text**, **Game Header Text Stroke**, **Darken Unfocused Games**, and **Round**, with other installed plugins supplying badges. Those appearance changes are not part of Home Carousel Zoom and are not required or bundled. The theme was also checked with these appearance themes disabled.

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
- The animation takes 160 ms. It is disabled when the Steam browser reports a reduced-motion preference.
- Disable the theme to remove its styling and return to your previous theme setup.

## Compatibility and validation

Live validation was performed on a Steam Deck on **2026-09-07**:

| Component | Observed version or setting |
| --- | --- |
| SteamOS | 3.8.16, build `20260716.1` |
| Steam client channel | `steamdeck_stable` |
| CSS Loader | 2.1.2 |
| Theme | v1.0.0, manifest version 8 |

Checks completed:

- All seven size settings were applied and measured on the same focused cover.
- Pointer hover and pointer release.
- Controller navigation across the Home carousel.
- Controller input changed the CSS Loader slider in both directions and saved the result.
- The 100%, 115%, and 130% settings with the existing Art Hero setup; 115% and 130% with the other active themes temporarily disabled.
- Horizontal scrolling, the wide first card, and the end of the carousel.
- The Library grid remained unchanged.
- CSS Loader refresh retained the selected size, with no theme load errors.
- Reduced-motion mode produced a zero-duration transition.

**This is not a claim of validation on every Steam release or theme combination.** Steam's UI classes and layout can change. CSS Loader translates the readable Steam class selectors used by this theme to the installed client's classes. Keep CSS Loader's translations current.

## CSS Loader store submission

This repository is structured for DeckThemes' preferred **Git submission** method. See the [official submission requirements](https://docs.deckthemes.com/Submission/).

| Submission field | Value |
| --- | --- |
| Theme name | Home Carousel Zoom |
| Repository URL | `https://github.com/beallio/CSSLoader-Home-Carousel-Zoom` |
| Commit ID | Use the full commit SHA referenced by the `v1.0.0` release tag, or the newer commit you have validated |
| Subfolder | `Home Carousel Zoom` |
| Target | Home |
| Preview image | [`assets/preview.png`](assets/preview.png), showing the default 115% setting |
| ZIP alternative | The release ZIP has `theme.json` directly at its root, as required by the ZIP submission method |

The installable folder contains only the theme files and their license. Screenshots and repository documentation stay outside it. No other themes, scripts, fonts, or game artwork are bundled in the installable theme. The CSS variable `--hcz-scale` uses a theme-specific prefix. The required `!important` declarations override Steam's inline scroll-container sizing and theme padding without changing the Library grid.

```text
CSSLoader-Home-Carousel-Zoom/
├── README.md
├── LICENSE
├── Home Carousel Zoom/       ← Git submission subfolder
│   ├── theme.json
│   ├── shared.css
│   └── LICENSE
└── assets/                   ← Repository/store previews; not installed
    ├── preview.png
    └── screenshots/
        ├── zoom-100.webp
        ├── zoom-105.webp
        ├── zoom-110.webp
        ├── zoom-115.webp
        ├── zoom-120.webp
        ├── zoom-125.webp
        └── zoom-130.webp
```

**Submission status: prepared, not submitted or approved.** DeckThemes requires testing against the latest stable and beta releases of SteamOS, Decky Loader, and CSS Loader. The installed stable-channel environment was tested; a separate latest-beta check and confirmation that every installed component is the latest release have not been completed. Do not attest to that requirement until those checks are done. The repository and archive structure do not replace that compatibility requirement.

## Existing-theme research

**Search date: 2026-09-07. Related focus-enlargement themes already exist.** In particular, Tilted Home includes a fixed 102% scale on focused Home covers. No matching **standalone, user-adjustable Home-cover zoom theme with both pointer hover and controller focus** was found in the catalog and source searches below. This does not prove that no similar private, unlisted, renamed, or newly published theme exists.

The behavior being compared is **extra enlargement of the selected or pointer-hovered Home carousel card, with a user-adjustable size**. Steam already supplies a small native focus effect; this theme does not claim to invent that effect.

| Existing theme | What it changes | Difference from Home Carousel Zoom |
| --- | --- | --- |
| [Mini Carousel](https://deckthemes.com/themes/view?themeId=4788b3d9-f4f3-40f2-ae0e-a80afa9fce5b) | Adjustable scaling of the entire Home carousel; its manifest provides 0.5–0.9 size settings | Resizes all carousel items together, not only the hovered or selected card |
| [Tilted Home](https://deckthemes.com/themes/view?themeId=231c969d-b16f-41a0-98a1-cec8aeb557ba) | Tilts Home covers and applies a fixed `scale(1.02)` to focused covers | **Does include selected-cover enlargement.** Its controls adjust tilt angle/method, not zoom size; the inspected focus-scale rules do not include pointer `:hover` |
| [Art Hero](https://deckthemes.com/themes/view?themeId=994360e7-cfca-46d3-9337-80d28ad169ba) | Changes hero/carousel layout and focus-label/glow presentation; depends on Mini Carousel | The inspected CSS and controls do not provide selected-cover zoom |
| [No Focused Library Item Scale](https://deckthemes.com/themes/view?themeId=aae7ed32-d7a5-4d1e-a5f8-436bc492e116) | Removes the native focus scale in Home and Library | The opposite effect, without an enlargement slider |
| [Proper Hero Scaling](https://deckthemes.com/themes/view?themeId=475be8fd-39df-431f-b589-dfdaad205d99) | Corrects hero/background sizing in Home and game views | Changes the background, not selected carousel covers |
| [Hero Zoom Eradication](https://deckthemes.com/themes/view?themeId=d544438d-6d94-4520-a5ce-ea53577c8937) | Removes hero zoom | Changes the background, not selected carousel covers |
| [Game Cover Reflections](https://deckthemes.com/themes/view?themeId=26e6a114-4513-4440-9e81-65460ce54884) | Replaces the glow behind covers with reflections | A visual effect, not adjustable card enlargement |
| [Focus Animation Border](https://deckthemes.com/themes/view?themeId=6e9d2439-905b-40d9-a633-7785a76cb612) | Changes focus-border animation | Changes the border, not the card size |

Catalog research used the [public BPM-CSS listing](https://deckthemes.com/themes?type=BPM-CSS), the [approved CSS export](https://api.deckthemes.com/themes/legacy/css?approved=true), and individual theme records. Names and descriptions were checked for terms including zoom, hover, focus, selected, cover, card, capsule, carousel, size, scale, expand, enlarge, and highlight. The site displayed 269 entries while the filtered API reported 266; those counts are not a claim that every theme's source code was reviewed.

Source inspection included [Tilted Home's focused-cover rule](https://github.com/TheRensei/SteamDeckCSSThemes/blob/main/Tilted%20Home%20Theme/tilt-oneway.css) and [controls](https://github.com/TheRensei/SteamDeckCSSThemes/blob/main/Tilted%20Home%20Theme/theme.json), [Mini Carousel's whole-carousel scale](https://github.com/fishingminigame/deck-themes/blob/main/Mini%20Carousel/shared.css) and [slider](https://github.com/fishingminigame/deck-themes/blob/main/Mini%20Carousel/theme.json), [Art Hero](https://github.com/Metagawa/Steam-Deck-Themes/blob/main/Art%20Hero/shared.css), [Switch Like Banners](https://github.com/MSeys/Steam-Deck-Themes/blob/main/Switch%20Like%20Banners/home.css), and [No Focused Library Item Scale](https://github.com/smithumble/Steam-Deck-Themes/blob/main/No%20Focused%20Library%20Item%20Scale/shared.css). [Cartridge Theme](https://github.com/ChrisAnd1998/SteamDeckCartridgeTheme/blob/main/Cartridge%20Theme/shared.css) also contains fixed focus-scale declarations, but its transform animation can override them; it was not counted as a verified working equivalent. These third-party sources were reviewed, not installed and retested on a current Steam client. GitHub code-search coverage is incomplete, so no “first” or “only” claim is made.

## License and credits

The theme code is licensed under the [MIT License](LICENSE).

Steam and its interface belong to Valve. Game artwork, names, and logos visible in the screenshots belong to their respective owners; the MIT license does not grant rights to that artwork. The selected game in the comparison is *Teenage Mutant Ninja Turtles: Splintered Fate*. Screenshots document this theme's behavior, not ownership of the depicted artwork.

Art Hero is by Metagawa. Centered Game Text is by SuchMeme. These and the other appearance themes shown in the screenshots are separate projects, not included in this theme. CSS Loader and Decky Loader are separate projects; this theme is not an official Valve product.
