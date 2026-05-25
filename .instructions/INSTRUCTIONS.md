# Project Context: CachyOS On-Screen Keyboard (cokb)

## Architecture & Environment
* **OS:** CachyOS (Arch Linux), KDE Plasma (Wayland).
* **Stack:** Python 3, GTK4, Gtk4LayerShell, `uinput` (kernel-level `evdev` injection).
* **Environment:** Hybrid `uv` virtual environment using `--system-site-packages` to inherit host GObject Introspection (`.typelib`) data while maintaining local PyPI packages (to satisfy PEP 668).

## Resolved Architectural Hurdles
1. **Wayland Input Isolation:** Standard X11 input spoofing (`xdotool`, `XTestFakeKeyEvent`) fails across the Wayland boundary. Solved by bypassing the display server entirely and writing directly to `/dev/uinput` to synthesize hardware interrupts.
2. **Focus Stealing:** Standard `xdg-shell` surfaces steal keyboard focus, routing injected keystrokes back into the OSK. Solved by mapping the GUI to `wlr-layer-shell` via `gtk4-layer-shell` and explicitly defining `KeyboardMode.NONE`.
3. **Dynamic Linker Collision:** GObject Introspection dynamic loading (`dlopen`) of GTK4 initializes `libwayland-client` before the layer-shell bindings, locking the registry and causing the application to fall back to an `xdg-shell` window. Solved via early C-library linking using `ctypes.CDLL("libgtk4-layer-shell.so", mode=ctypes.RTLD_GLOBAL)` prior to any `gi` imports.

## Current State
* Core framework is functional.
* UI generates dynamically from a multi-dimensional matrix of tuples `(Label, uinput.KEY_CONSTANT)`.
* Alphanumeric keystroke injection works flawlessly via `uinput.Device.emit_click()` without stealing focus from the target Wayland/XWayland client.

## Pending Implementation Requirements
1. **Modifier Key State Machine:** `emit_click()` executes immediate press (1) and release (0) events, rendering modifier keys (Shift, Ctrl, Alt, Super) non-functional for combinations. Implement a state machine to hold the lock (press event), wait for the subsequent alphanumeric key execution, and then release the modifier lock.
2. **Visual State Feedback:** Implement `Gtk.CssProvider` to provide visual toggles (e.g., active/pressed state highlighting) for the locked modifier keys.
3. **Constraint:** Do not alter the GTK4 initialization sequence, the layer-shell semantics, or the `ctypes` preload block. Focus strictly on the modifier state logic and CSS implementation.