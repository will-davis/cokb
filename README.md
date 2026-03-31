# Project: CachyOS On-Screen Keyboard (CoKB)

## Architecture & Environment
* **OS:** CachyOS (Arch Linux), KDE Plasma (Wayland).
* **Stack:** Python 3, GTK4, Gtk4LayerShell, `uinput`.
* **Environment:** Hybrid `uv` virtual environment.

## Resolved Architectural Hurdles

- **Focus Stealing:** Standard `xdg-shell` surfaces steal keyboard focus, routing injected keystrokes back into the OSK. Solved by mapping the GUI to `wlr-layer-shell` via `gtk4-layer-shell` and explicitly defining `KeyboardMode.NONE`. This is the magic trick.

## Current State
* It works! For me at least and in general with CachyOS. Last tested: "Linux 6.19.10-1-cachyos".
* Keystroke injection works via `uinput.Device.emit_click()` without stealing focus from the target Wayland/XWayland client.
