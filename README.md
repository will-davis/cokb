# Project: CachyOS On-Screen Keyboard (CoKB)

<div align="center">
  <img width="700" height="255" alt="CoKB-img" src="https://github.com/user-attachments/assets/dc4d6962-fded-414c-b4fb-4d230cf699c9" />
</div>

## Architecture & Environment
* **OS:** CachyOS (Arch Linux), KDE Plasma (Wayland).
* **Stack:** Python 3, GTK4, Gtk4LayerShell, `uinput`.
* **Environment:** Hybrid `uv` virtual environment.

https://github.com/user-attachments/assets/94a5205b-519d-45f9-b3c1-6a983725493b

## Resolved Architectural Hurdles
- **Focus Stealing:** Standard `xdg-shell` surfaces steal keyboard focus, routing injected keystrokes back into the OSK. Solved by mapping the GUI to `wlr-layer-shell` via `gtk4-layer-shell` and explicitly defining `KeyboardMode.NONE`. This is the magic trick.

## Current State
* It works! For me at least and in general with CachyOS. Last tested: "Linux 6.19.10-1-cachyos".
* Keystroke injection works via `uinput.Device.emit_click()` without stealing focus from the target Wayland/XWayland client.
* Considering adding a less '3D' theme. My default attempt is a little busy when the keyboard is minimum size.
* For an unidentified reason the application does not want to populate the task manager as showing that is is running. There is also no way to minimize this type of GTK window. I recommend linking it somewhere easy and just closing it instead of minimizing. It is lightweight.
