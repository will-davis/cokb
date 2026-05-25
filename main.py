#!/usr/bin/env python3
import gi
import uinput
import time
import ctypes
import sys

# Force early linking of the layer-shell shared object
try:
    ctypes.CDLL("libgtk4-layer-shell.so", mode=ctypes.RTLD_GLOBAL)
except OSError:
    print("CRITICAL: libgtk4-layer-shell.so not found in system path.", file=sys.stderr)
    sys.exit(1)

gi.require_version('Gtk', '4.0')
gi.require_version('Gtk4LayerShell', '1.0')
from gi.repository import Gtk, Gdk, GLib, Gtk4LayerShell

class WaylandOSK(Gtk.Application):
    MAIN_TOP = [
        ("Esc", uinput.KEY_ESC, 4, "mod"), ("EXIT", None, 4, "exit"),
        ("F1", uinput.KEY_F1, 4, ""), ("F2", uinput.KEY_F2, 4, ""), ("F3", uinput.KEY_F3, 4, ""), ("F4", uinput.KEY_F4, 4, ""),
        ("Blank", None, 2, ""),
        ("F5", uinput.KEY_F5, 4, ""), ("F6", uinput.KEY_F6, 4, ""), ("F7", uinput.KEY_F7, 4, ""), ("F8", uinput.KEY_F8, 4, ""),
        ("Blank", None, 2, ""),
        ("F9", uinput.KEY_F9, 4, ""), ("F10", uinput.KEY_F10, 4, ""), ("F11", uinput.KEY_F11, 4, ""), ("F12", uinput.KEY_F12, 4, "")
    ]

    EDIT_TOP = [
        ("↖", "tl", 0, 0, 4, "ctrl-half"), ("↑", "tc", 4, 0, 4, "ctrl-half"), ("↗", "tr", 8, 0, 4, "ctrl-half"),
        ("↙", "bl", 0, 1, 4, "ctrl-half"), ("↓", "bc", 4, 1, 4, "ctrl-half"), ("↘", "br", 8, 1, 4, "ctrl-half")
    ]

    MAIN_BOT = [
        [
            ("`", uinput.KEY_GRAVE, 4, ""), ("1", uinput.KEY_1, 4, ""), ("2", uinput.KEY_2, 4, ""), ("3", uinput.KEY_3, 4, ""),
            ("4", uinput.KEY_4, 4, ""), ("5", uinput.KEY_5, 4, ""), ("6", uinput.KEY_6, 4, ""), ("7", uinput.KEY_7, 4, ""),
            ("8", uinput.KEY_8, 4, ""), ("9", uinput.KEY_9, 4, ""), ("0", uinput.KEY_0, 4, ""), ("-", uinput.KEY_MINUS, 4, ""),
            ("=", uinput.KEY_EQUAL, 4, ""), ("Backspace", uinput.KEY_BACKSPACE, 8, "mod")
        ],
        [
            ("Tab", uinput.KEY_TAB, 6, "mod"), ("q", uinput.KEY_Q, 4, ""), ("w", uinput.KEY_W, 4, ""), ("e", uinput.KEY_E, 4, ""),
            ("r", uinput.KEY_R, 4, ""), ("t", uinput.KEY_T, 4, ""), ("y", uinput.KEY_Y, 4, ""), ("u", uinput.KEY_U, 4, ""),
            ("i", uinput.KEY_I, 4, ""), ("o", uinput.KEY_O, 4, ""), ("p", uinput.KEY_P, 4, ""), ("[", uinput.KEY_LEFTBRACE, 4, ""),
            ("]", uinput.KEY_RIGHTBRACE, 4, ""), ("\\", uinput.KEY_BACKSLASH, 6, "")
        ],
        [
            ("Caps Lock", uinput.KEY_CAPSLOCK, 7, "mod"), ("a", uinput.KEY_A, 4, ""), ("s", uinput.KEY_S, 4, ""), ("d", uinput.KEY_D, 4, ""),
            ("f", uinput.KEY_F, 4, ""), ("g", uinput.KEY_G, 4, ""), ("h", uinput.KEY_H, 4, ""), ("j", uinput.KEY_J, 4, ""),
            ("k", uinput.KEY_K, 4, ""), ("l", uinput.KEY_L, 4, ""), (";", uinput.KEY_SEMICOLON, 4, ""), ("'", uinput.KEY_APOSTROPHE, 4, ""),
            ("Enter", uinput.KEY_ENTER, 9, "mod")
        ],
        [
            ("Shift", uinput.KEY_LEFTSHIFT, 9, "mod"), ("z", uinput.KEY_Z, 4, ""), ("x", uinput.KEY_X, 4, ""), ("c", uinput.KEY_C, 4, ""),
            ("v", uinput.KEY_V, 4, ""), ("b", uinput.KEY_B, 4, ""), ("n", uinput.KEY_N, 4, ""), ("m", uinput.KEY_M, 4, ""),
            (",", uinput.KEY_COMMA, 4, ""), (".", uinput.KEY_DOT, 4, ""), ("/", uinput.KEY_SLASH, 4, ""), ("Shift", uinput.KEY_RIGHTSHIFT, 11, "mod")
        ],
        [
            ("Ctrl", uinput.KEY_LEFTCTRL, 5, "mod"), ("Super", uinput.KEY_LEFTMETA, 5, "mod"), ("Alt", uinput.KEY_LEFTALT, 5, "mod"),
            ("Space", uinput.KEY_SPACE, 25, ""), ("Alt", uinput.KEY_RIGHTALT, 5, "mod"), ("Super", uinput.KEY_RIGHTMETA, 5, "mod"),
            ("Play/Pause", uinput.KEY_PLAYPAUSE, 5, "mod"), ("Ctrl", uinput.KEY_RIGHTCTRL, 5, "mod")
        ]
    ]

    EDIT_BOT = [
        [ ("Ins", uinput.KEY_INSERT, 4, "mod"), ("Home", uinput.KEY_HOME, 4, "mod"), ("PgUp", uinput.KEY_PAGEUP, 4, "mod") ],
        [ ("Del", uinput.KEY_DELETE, 4, "mod"), ("End", uinput.KEY_END, 4, "mod"), ("PgDn", uinput.KEY_PAGEDOWN, 4, "mod") ],
        [ ("VOL-", uinput.KEY_VOLUMEDOWN, 4, "ctrl"), ("MUTE", uinput.KEY_MUTE, 4, "ctrl"), ("VOL+", uinput.KEY_VOLUMEUP, 4, "ctrl") ],
        [ ("Z-", None, 4, "ctrl"), ("↑", uinput.KEY_UP, 4, "mod"), ("Z+", None, 4, "ctrl") ],
        [ ("←", uinput.KEY_LEFT, 4, "mod"), ("↓", uinput.KEY_DOWN, 4, "mod"), ("→", uinput.KEY_RIGHT, 4, "mod") ]
    ]

    SHIFT_MAP = {
        "`": "~", "1": "!", "2": "@", "3": "#", "4": "$", "5": "%", "6": "^",
        "7": "&", "8": "*", "9": "(", "0": ")", "-": "_", "=": "+",
        "[": "{", "]": "}", "\\": "|", ";": ":", "'": '"', ",": "<", ".": ">", "/": "?"
    }

    MODIFIER_KEYS = {
        uinput.KEY_LEFTSHIFT, uinput.KEY_RIGHTSHIFT,
        uinput.KEY_LEFTCTRL, uinput.KEY_RIGHTCTRL,
        uinput.KEY_LEFTALT, uinput.KEY_RIGHTALT,
        uinput.KEY_LEFTMETA, uinput.KEY_RIGHTMETA
    }

    def __init__(self):
        super().__init__(application_id="com.custom.osk")
        self.locked_modifiers = {}

        events = []
        for l, k, s, c in self.MAIN_TOP:
            if k is not None: events.append(k)
        for row in self.MAIN_BOT:
            for l, k, s, c in row:
                if k is not None: events.append(k)
        for row in self.EDIT_BOT:
            for l, k, s, c in row:
                if k is not None: events.append(k)

        events = list(set(events))
        self.device = uinput.Device(events)
        time.sleep(0.1)

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self)

        css_provider = Gtk.CssProvider()
        css_provider.load_from_data(b"""
        .keyboard-frame {
            background-color: #1a1a1b;
            padding: 2px;
        }
        .grip-bar {
            background-color: #2a2a2b;
            border-radius: 4px;
            min-height: 10px;
        }
        .grip-bar:hover {
            background-color: #3e3e40;
        }
        button {
            transition: all 0.1s ease-in-out;
            min-height: 0px;
            min-width: 0px;
            padding: 0px;
            margin: 0px;
            background-color: #2d2d2e;
            color: #e2e2e2;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
        }
        button:hover {
            transform: scale(1.05);
        }
        button:active {
            transform: scale(0.95);
        }
        button.mod {
            background-color: #3e3e40;
        }
        button.ctrl, button.ctrl-half {
            background-color: #1f2638;
        }
        button.exit {
            background-color: #4c2e2e;
        }
        button.modifier-locked {
            background-color: #3584e4;
            color: white;
        }
        .scale-3 button { font-size: 13px; }
        .scale-2 button { font-size: 9px; }
        .scale-1 button { font-size: 6px; }
        .scale-3 button.ctrl-half { font-size: 10px; }
        .scale-2 button.ctrl-half { font-size: 7px; }
        .scale-1 button.ctrl-half { font-size: 5px; }
        """)
        Gtk.StyleContext.add_provider_for_display(
            Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

        Gtk4LayerShell.init_for_window(window)
        Gtk4LayerShell.set_keyboard_mode(window, Gtk4LayerShell.KeyboardMode.NONE)
        Gtk4LayerShell.set_layer(window, Gtk4LayerShell.Layer.TOP)
        Gtk4LayerShell.set_anchor(window, Gtk4LayerShell.Edge.BOTTOM, True)
        Gtk4LayerShell.set_anchor(window, Gtk4LayerShell.Edge.LEFT, True)

        main_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
        main_vbox.add_css_class("keyboard-frame")
        self.main_vbox = main_vbox

        self.all_keys = []
        self.all_grids = []
        self.scale_level = 2
        self.caps_locked = False

        def attach_btn(grid, col, row, span, label, keycode, css_class, type_="full", pos_code=None):
            if label == "Blank":
                blank = Gtk.DrawingArea()
                grid.attach(blank, col, row, span, 1)
                self.all_keys.append({"btn": blank, "label": "Blank", "span": span, "type": "blank"})
                return

            btn = Gtk.Button()
            initial_label = label
            if len(label) == 1 and label.isalpha():
                initial_label = label.lower()
            btn.set_label(initial_label)

            if css_class:
                btn.add_css_class(css_class)

            btn.set_hexpand(True)
            btn.set_vexpand(True)

            if label == "EXIT":
                btn.connect("clicked", lambda b: sys.exit(0))
            elif label == "Z-":
                self.btn_resize_dn = btn
                btn.connect("clicked", lambda b: self.change_scale(-1))
            elif label == "Z+":
                self.btn_resize_up = btn
                btn.connect("clicked", lambda b: self.change_scale(1))
            elif pos_code is not None:
                btn.connect("clicked", lambda b, p=pos_code: self.snap_to_corner(window, p))
            else:
                btn.connect("clicked", lambda b, k=keycode: self.on_key_clicked(b, k))

            grid.attach(btn, col, row, span, 1)
            self.all_keys.append({"btn": btn, "label": label, "span": span, "type": type_})

        # Grip bar for drag-to-reposition
        grip = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        grip.set_size_request(-1, 10)
        grip.add_css_class("grip-bar")
        drag_gesture = Gtk.GestureDrag.new()
        drag_gesture.connect("drag-begin", self.on_drag_begin)
        drag_gesture.connect("drag-update", self.on_drag_update)
        grip.add_controller(drag_gesture)
        main_vbox.append(grip)

        # Main content: single hbox with main_grid + edit_grid
        content_hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=24)

        # Main grid: function row (row 0) + keyboard rows (rows 1-5)
        main_grid = Gtk.Grid()
        self.all_grids.append(main_grid)

        col = 0
        for label, keycode, span, css_class in self.MAIN_TOP:
            attach_btn(main_grid, col, 0, span, label, keycode, css_class)
            col += span

        for r_idx, row in enumerate(self.MAIN_BOT):
            col = 0
            for label, keycode, span, css_class in row:
                attach_btn(main_grid, col, r_idx + 1, span, label, keycode, css_class)
                col += span

        content_hbox.append(main_grid)

        # Edit grid: snap buttons (nested sub-grid in row 0) + nav rows (rows 1-5)
        edit_grid = Gtk.Grid()
        self.all_grids.append(edit_grid)

        snap_grid = Gtk.Grid()
        self.all_grids.append(snap_grid)
        for label, pos_code, c, r, span, css_class in self.EDIT_TOP:
            attach_btn(snap_grid, c, r, span, label, None, css_class, "half", pos_code)
        edit_grid.attach(snap_grid, 0, 0, 12, 1)

        for r_idx, row in enumerate(self.EDIT_BOT):
            col = 0
            for label, keycode, span, css_class in row:
                attach_btn(edit_grid, col, r_idx + 1, span, label, keycode, css_class)
                col += span

        content_hbox.append(edit_grid)
        main_vbox.append(content_hbox)

        self.change_scale(0)

        window.set_child(main_vbox)
        window.connect("map", lambda w: GLib.idle_add(self._initial_position, w))
        window.present()

    def change_scale(self, direction):
        target = self.scale_level + direction
        if target > 3 or target < 1:
            return

        self.scale_level = target

        if hasattr(self, "btn_resize_up"):
            self.btn_resize_up.set_sensitive(self.scale_level < 3)
            self.btn_resize_dn.set_sensitive(self.scale_level > 1)

        factor = {3: 1.0, 2: 0.66, 1: 0.33}[self.scale_level]
        U = int(48 * factor)
        gap = int(4 * factor)
        if gap < 2: gap = 2

        C = (U - 3.0 * gap) / 4.0

        for grid in self.all_grids:
            grid.set_column_spacing(gap)
            grid.set_row_spacing(gap)

        self.main_vbox.remove_css_class("scale-1")
        self.main_vbox.remove_css_class("scale-2")
        self.main_vbox.remove_css_class("scale-3")
        self.main_vbox.add_css_class(f"scale-{self.scale_level}")

        for data in self.all_keys:
            btn = data["btn"]
            span = data["span"]
            type_ = data["type"]

            width = int(round(span * C + (span - 1) * gap))

            if type_ == "half":
                height = int(round(U / 2.0 - gap / 2.0))
            else:
                height = U

            btn.set_size_request(width, height)

        window = self.main_vbox.get_root()
        if window:
            window.set_default_size(-1, -1)
            window.get_child().queue_resize()

    def update_key_labels(self):
        shift_active = uinput.KEY_LEFTSHIFT in self.locked_modifiers or uinput.KEY_RIGHTSHIFT in self.locked_modifiers

        for data in self.all_keys:
            btn = data["btn"]
            base_label = data["label"]

            if base_label == "Blank":
                continue

            if len(base_label) == 1 and base_label.isalpha():
                upper = shift_active ^ self.caps_locked
                btn.set_label(base_label.upper() if upper else base_label.lower())
            else:
                if shift_active and base_label in self.SHIFT_MAP:
                    btn.set_label(self.SHIFT_MAP[base_label])
                else:
                    if base_label in self.SHIFT_MAP:
                        btn.set_label(base_label)

    def _initial_position(self, window):
        if window.get_width() > 1:
            self.snap_to_corner(window, "br")
            return GLib.SOURCE_REMOVE
        return GLib.SOURCE_CONTINUE

    def get_monitor_geometry(self):
        display = Gdk.Display.get_default()
        monitors = display.get_monitors()
        return monitors.get_item(0).get_geometry()

    def snap_to_corner(self, window, corner):
        geo = self.get_monitor_geometry()
        kb_w = window.get_width()
        kb_h = window.get_height()

        left_positions = {"tl": 0, "bl": 0, "tc": (geo.width - kb_w) // 2, "bc": (geo.width - kb_w) // 2, "tr": geo.width - kb_w, "br": geo.width - kb_w}
        bottom_positions = {"bl": 0, "bc": 0, "br": 0, "tl": geo.height - kb_h, "tc": geo.height - kb_h, "tr": geo.height - kb_h}

        Gtk4LayerShell.set_margin(window, Gtk4LayerShell.Edge.LEFT, max(0, left_positions[corner]))
        Gtk4LayerShell.set_margin(window, Gtk4LayerShell.Edge.BOTTOM, max(0, bottom_positions[corner]))

    def on_drag_begin(self, gesture, start_x, start_y):
        pass

    def on_drag_update(self, gesture, offset_x, offset_y):
        window = self.main_vbox.get_root()
        geo = self.get_monitor_geometry()
        kb_w = window.get_width()
        kb_h = window.get_height()

        current_left = Gtk4LayerShell.get_margin(window, Gtk4LayerShell.Edge.LEFT)
        current_bottom = Gtk4LayerShell.get_margin(window, Gtk4LayerShell.Edge.BOTTOM)

        new_left = current_left + int(offset_x)
        new_bottom = current_bottom - int(offset_y)

        new_left = max(0, min(new_left, geo.width - kb_w))
        new_bottom = max(0, min(new_bottom, geo.height - kb_h))

        Gtk4LayerShell.set_margin(window, Gtk4LayerShell.Edge.LEFT, new_left)
        Gtk4LayerShell.set_margin(window, Gtk4LayerShell.Edge.BOTTOM, new_bottom)

    def on_key_clicked(self, button, key_code):
        if key_code in self.MODIFIER_KEYS:
            if key_code in self.locked_modifiers:
                button.remove_css_class("modifier-locked")
                del self.locked_modifiers[key_code]
            else:
                button.add_css_class("modifier-locked")
                self.locked_modifiers[key_code] = button
            self.update_key_labels()
        else:
            if key_code == uinput.KEY_CAPSLOCK:
                self.caps_locked = not self.caps_locked
                if self.caps_locked:
                    button.add_css_class("modifier-locked")
                else:
                    button.remove_css_class("modifier-locked")
                self.device.emit_click(key_code)
                self.update_key_labels()
                return

            if self.locked_modifiers:
                for mod_key in self.locked_modifiers:
                    self.device.emit(mod_key, 1, syn=False)
                self.device.emit(key_code, 1, syn=True)
                self.device.emit(key_code, 0, syn=False)
                for mod_key in self.locked_modifiers:
                    self.device.emit(mod_key, 0, syn=False)
                self.device.syn()
                for mod_button in self.locked_modifiers.values():
                    mod_button.remove_css_class("modifier-locked")
                self.locked_modifiers.clear()
            else:
                self.device.emit_click(key_code)

            self.update_key_labels()

if __name__ == "__main__":
    app = WaylandOSK()
    app.run(None)
