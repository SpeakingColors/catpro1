# Sharing patches

The patch book site lives in `docs/` and is served by GitHub Pages (once Pages is switched on, see below). It is static: no server, no accounts of our own.

## For players
- Open the site, pick a patch from the list, set your Pro-1 knobs to match the on-screen panel.
- Move the on-screen knobs, save the result as a `.json` file, or copy it.
- Import a file with the Import button; nothing leaves your browser.

## Sharing your patch
1. Export your patch as JSON (format in [PATCH-FORMAT.md](PATCH-FORMAT.md)).
2. Easiest: open a "Submit a patch" issue on the repo and paste the JSON. A maintainer adds it.
3. Or send a pull request: add the file to `docs/patches/` and add its entry to `docs/patches/index.json`.
4. By submitting you license the patch as CC0-1.0 or CC-BY-4.0 (your choice, put it in the file).

Only submit your own patches. Do not paste patches copied from commercial books, forums with a no-reuse rule, or preset packs.

## Switching on GitHub Pages (one time, by the repo owner)
- Repo Settings, Pages, Source: "Deploy from a branch", branch `main`, folder `/docs`, Save.
- The site then appears at `https://speakingcolors.github.io/catpro1/`.

## Later ideas
- A GitHub Action that checks every submitted patch against the format and rebuilds `index.json`.
- Ratings and comments through GitHub Discussions.
- The same book for the Behringer Cat (needs its panel list first).
