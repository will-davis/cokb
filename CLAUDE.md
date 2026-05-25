# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

CoKB (CachyOS On-Screen Keyboard) — a Wayland-native on-screen keyboard that injects keystrokes via the Linux kernel's `/dev/uinput` interface instead of the display server, bypassing Wayland's input isolation. Uses GTK4 Layer Shell to render as a non-focusable overlay so the target application retains keyboard focus.

## Running

```fish
uv run main.py
```

The venv uses `--system-site-packages` to inherit host GObject Introspection typelibs (PyGObject, GTK4 bindings) while keeping PyPI packages isolated.

Requires a Wayland session (KDE Plasma / Sway). Will not work under X11 or headless.

## Building the Arch Package

```fish
makepkg -f
```

Produces a `.pkg.tar.zst` installable via `pacman -U`. The PKGBUILD installs the script to `/usr/bin/cokb`, a udev rule for uinput access, a modules-load.d config, and a .desktop entry.

## System Requirements for /dev/uinput Access

The udev rule (`99-cokb-uinput.rules`) grants seat-based `uaccess` to `/dev/uinput`. The `uinput` kernel module must be loaded (`uinput-cokb.conf` handles this at boot). A reboot may be required after first install.

## Critical Initialization Constraint

**Do not reorder the startup sequence in `main.py`.** The `ctypes.CDLL("libgtk4-layer-shell.so", mode=ctypes.RTLD_GLOBAL)` call MUST execute before any `gi` imports. Without this, GObject Introspection's `dlopen` initializes `libwayland-client` first, locks the Wayland registry, and the app silently falls back to an `xdg-shell` window (stealing focus, defeating the entire purpose).

## Architecture (single-file: main.py)

`WaylandOSK` is a `Gtk.Application` subclass. Everything lives in one file.

**Layout definition:** Four class-level tuple arrays define the keyboard layout using a fractional grid system based on mechanical keycap units (1U = 4 grid columns). Each tuple is `(label, uinput_keycode, column_span, css_class)`:
- `MAIN_TOP` — function row (Esc, F1–F12, EXIT)
- `MAIN_BOT` — 5 rows: number row through spacebar row (standard ANSI TKL proportions)
- `EDIT_TOP` — 6 half-height corner-snap buttons (directional GUI controls)
- `EDIT_BOT` — nav cluster (Ins/Home/PgUp, arrows, volume, zoom)

To change the layout, modify these tuples. The GTK4 grid rebuilds proportionally from the column spans — no pixel coordinates to maintain.

**Grid structure:** `MAIN_TOP` and `MAIN_BOT` share a single `Gtk.Grid` (function row as row 0, keyboard rows as rows 1–5) so that columns align vertically. The edit cluster uses a separate grid with a nested sub-grid for the half-height snap buttons in row 0.

**Key injection:** `uinput.Device` is created at init with all keycodes from the layout tuples. Regular keys use `emit_click()` (press + release). Modifier keys (Shift, Ctrl, Alt, Super) use deferred emission — clicking a modifier only toggles UI state. When the next regular key is clicked, the full modifier+key sequence is emitted atomically using `syn=False` to batch events into minimal SYN_REPORT frames. Caps Lock XORs with Shift for correct case behavior.

**Scaling:** Three zoom levels (33%, 66%, 100%) controlled by Z-/Z+ buttons. `change_scale()` recalculates all button dimensions from a base unit `U = 48 * factor` and updates grid spacing. CSS classes `.scale-1/2/3` adjust font sizes. Starts at scale level 2 (66%).

**Positioning:** The window is permanently anchored to BOTTOM + LEFT. Position is controlled via `Gtk4LayerShell.set_margin()` on the LEFT and BOTTOM edges. A drag grip bar at the top of the keyboard enables smooth drag-to-reposition. The 6 `EDIT_TOP` snap buttons provide quick presets (corners + edge centers) by setting margin values.

**Styling:** Inline CSS in `do_activate()`. Key visual classes: `mod` (gray modifiers), `ctrl` (blue utility keys), `ctrl-half` (half-height controls), `exit` (red), `modifier-locked` (active modifier highlight).

## Dependencies

System packages (Arch): `python`, `python-gobject`, `gtk4`, `gtk4-layer-shell`, `python-uinput`

## Project Files

- `PKGBUILD` / `cokb.install` — Arch packaging
- `99-cokb-uinput.rules` — udev rule for uinput seat access
- `uinput-cokb.conf` — modules-load.d config to load uinput at boot
- `cokb.desktop` — XDG desktop entry
- `.instructions/` — design docs and prior task context (not shipped)
- `releases/` — archived release snapshots with built packages (gitignored)
