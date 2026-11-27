# Slerkray Typeface

Source files and build pipeline for the **Slerkray** typeface.

## Setup

```sh
make setup      # create .venv and install fontmake, fonttools, ufo2ft, glyphsLib, gftools, fontbakery
```

## Workflow

- `sources/Slerkray-Regular.ufo` — the UFO source. Edit it in any UFO-capable editor (Glyphs, FontLab, RoboFont, Fontra, FontForge).
- `make source` — regenerate the starter placeholder UFO (overwrites it!).
- `make build` — compile OTF + TTF into `fonts/`.
- `make test` — build and run Font Bakery checks.
