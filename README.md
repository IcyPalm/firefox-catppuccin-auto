# Catppuccin Auto for Firefox

A Firefox theme that follows your system appearance: [Catppuccin](https://catppuccin.com)
**Latte** in light mode, **Mocha** in dark mode, both with the **Mauve** accent.

The official [catppuccin/firefox](https://github.com/catppuccin/firefox) port ships one flavor at a
time through Firefox Color, so it can't switch with the OS. This theme uses the
[`dark_theme`](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/manifest.json/dark_theme)
manifest key instead: Firefox picks the light or dark variant itself. No extra add-on or script needed.

**[Download the signed .xpi from the latest release](https://github.com/IcyPalm/firefox-catppuccin-auto/releases/latest)** and open it in Firefox.

## Requirements

- Firefox 142 or later
- Python 3 (standard library only) to build
- Node.js (`npx`) to lint and sign

## Build

```sh
make build   # -> dist/manifest.json, dist/catppuccin-auto-<version>.xpi
make lint    # Mozilla's web-ext linter
```

## Install

Release Firefox only installs signed add-ons.

**Sign (unlisted, private)**: create API credentials at
<https://addons.mozilla.org/developers/addon/api/key/>, then:

```sh
export AMO_JWT_ISSUER=...
export AMO_JWT_SECRET=...
make sign    # signed .xpi lands in web-ext-artifacts/
```

Or upload `dist/catppuccin-auto-<version>.xpi` by hand in the
[Developer Hub](https://addons.mozilla.org/developers/) → *Submit a New Add-on* → *On your own*.

Install the signed file via `about:addons` → ⚙️ → *Install Add-on From File…*

**Testing unsigned** (Developer Edition / Nightly only): set
`xpinstall.signatures.required` to `false` in `about:config`.

## Customizing

Colors and the accent live in `PALETTES` in [`build.py`](build.py); the mapping onto Firefox theme
keys is in `theme()`. After changing anything, bump `VERSION`; AMO rejects re-uploads of an existing version.

## Credits

Colors from [Catppuccin](https://github.com/catppuccin/catppuccin) (MIT). Not an official Catppuccin port.

## License

[MIT](LICENSE)
