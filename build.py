#!/usr/bin/env python3
"""Build the Catppuccin Auto Firefox theme.

Generates dist/manifest.json and dist/catppuccin-auto-<version>.xpi.
Latte is used as the light theme (`theme`), Mocha as the dark theme
(`dark_theme`); Firefox switches between them with the system appearance.
"""
import json
import zipfile
from pathlib import Path

VERSION = "1.1"
ADDON_ID = "catppuccin-auto@marijnpool.nl"
MIN_FIREFOX = "142.0"

ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"

# Catppuccin palette subset (https://catppuccin.com/palette), mauve accent.
PALETTES = {
    "latte": {
        "crust": "#dce0e8", "mantle": "#e6e9ef", "base": "#eff1f5",
        "surface0": "#ccd0da", "surface1": "#bcc0cc",
        "subtext0": "#6c6f85", "text": "#4c4f69", "accent": "#8839ef",
    },
    "mocha": {
        "crust": "#11111b", "mantle": "#181825", "base": "#1e1e2e",
        "surface0": "#313244", "surface1": "#45475a",
        "subtext0": "#a6adc8", "text": "#cdd6f4", "accent": "#cba6f7",
    },
}


def theme(p: dict) -> dict:
    """Map a palette onto Firefox theme color keys."""
    colors = {
        "frame": p["crust"],
        "frame_inactive": p["crust"],
        "tab_background_text": p["subtext0"],
        "tab_background_separator": p["surface1"],
        "tab_selected": p["base"],
        "tab_text": p["text"],
        "tab_line": p["accent"],
        "tab_loading": p["accent"],
        "toolbar": p["base"],
        "toolbar_text": p["text"],
        "toolbar_top_separator": p["crust"],
        "toolbar_bottom_separator": p["crust"],
        "toolbar_vertical_separator": p["surface1"],
        "toolbar_field": p["mantle"],
        "toolbar_field_text": p["text"],
        "toolbar_field_border": p["surface0"],
        "toolbar_field_focus": p["mantle"],
        "toolbar_field_text_focus": p["text"],
        "toolbar_field_border_focus": p["accent"],
        "toolbar_field_highlight": p["accent"],
        "toolbar_field_highlight_text": p["base"],
        "toolbar_field_separator": p["surface1"],
        "button_background_hover": p["surface0"],
        "button_background_active": p["surface1"],
        "icons": p["text"],
        "icons_attention": p["accent"],
        "popup": p["base"],
        "popup_text": p["text"],
        "popup_border": p["surface0"],
        "popup_highlight": p["surface0"],
        "popup_highlight_text": p["text"],
        "sidebar": p["mantle"],
        "sidebar_text": p["text"],
        "sidebar_border": p["surface0"],
        "sidebar_highlight": p["surface0"],
        "sidebar_highlight_text": p["text"],
        "ntp_background": p["base"],
        "ntp_text": p["text"],
        "ntp_card_background": p["mantle"],
    }
    return {
        "colors": colors,
        "properties": {"color_scheme": "system", "content_color_scheme": "system"},
    }


def manifest() -> dict:
    return {
        "manifest_version": 2,
        "name": "Catppuccin Auto (Latte/Mocha)",
        "version": VERSION,
        "description": "Catppuccin Latte in light mode, Mocha in dark mode (mauve accent).",
        "browser_specific_settings": {
            "gecko": {
                "id": ADDON_ID,
                "strict_min_version": MIN_FIREFOX,
                "data_collection_permissions": {"required": ["none"]},
            }
        },
        "theme": theme(PALETTES["latte"]),
        "dark_theme": theme(PALETTES["mocha"]),
    }


def main() -> None:
    DIST.mkdir(exist_ok=True)
    manifest_path = DIST / "manifest.json"
    manifest_path.write_text(json.dumps(manifest(), indent=2) + "\n")

    xpi = DIST / f"catppuccin-auto-{VERSION}.xpi"
    with zipfile.ZipFile(xpi, "w", zipfile.ZIP_DEFLATED) as z:
        z.write(manifest_path, "manifest.json")
    print(f"Built {xpi.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
