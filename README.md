# CachyOS On-Screen Keyboard (CoKB)
<br>
<div align="center">
  <img width="700" height="255" alt="CoKB-img" src="https://github.com/user-attachments/assets/dc4d6962-fded-414c-b4fb-4d230cf699c9" />
</div>
<br>

This repository was created after spending days trying to find a functional on screen keyboard for Arch and then CachyOS then eventually building my own with the features I wanted to have in an OSK. You can see more about the development in my linked blog post at the bottom.

## Architecture & Environment
* **OS:** CachyOS (Arch Linux), KDE Plasma (Wayland).
* **Stack:** Python 3, GTK4, Gtk4LayerShell, `uinput`.
* **Environment:** Hybrid `uv` virtual environment.

https://github.com/user-attachments/assets/94a5205b-519d-45f9-b3c1-6a983725493b

## Resolved Architectural Hurdles
- **Focus Stealing:** Standard `xdg-shell` surfaces steal keyboard focus, routing injected keystrokes back into the OSK. This loop completely defeats the purpose of having a keyboard on the screen. It can literally only send keys to itself because as you click it, it takes focus. This was fixed (**the magic trick**) by mapping the GUI to `wlr-layer-shell` via `gtk4-layer-shell` and explicitly defining `KeyboardMode.NONE`. 

## Current State
* It works! For me at least and in general with CachyOS. Last tested: "Linux 6.19.10-1-cachyos".
* Keystroke injection works via `uinput.Device.emit_click()` without stealing focus from the target Wayland/XWayland client.
* Considering adding a less '3D' theme. My default attempt is a little busy when the keyboard is minimum size.
* For an unidentified reason the application does not want to populate the task manager as showing that is is running. There is also no way to minimize this type of GTK window. I recommend linking it somewhere easy and just closing it instead of minimizing. It is lightweight.

[blog post - will-davis.com/blog](https://will-davis.com/blog/) - Yes this was made with the help of AI. I am comfortable with Python. I am not comfortable with the tedium of coding out an entire dictionary of keys and their associated geometries on my day off.
