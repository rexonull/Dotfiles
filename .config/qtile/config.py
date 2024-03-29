import os
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget, extension, hook

import mainConfig

mainConfig.start()

mod = "mod4"

### KEYBINDINGS ###
keys = mainConfig.keys

### GROUPS ###
groups = mainConfig.groups

### LAYOUTS ###
layouts = mainConfig.layouts

### WIDGETS ###
widget_defaults = mainConfig.widget_defaults
extension_defaults = mainConfig.extension_defaults
screens = mainConfig.screens

### MOUSE CONTROL ###
mouse = mainConfig.mouse

dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

### FLOATING WINDOWS ###
floating_layout = mainConfig.floating_layout
auto_fullscreen = True
focus_on_window_activation = "smart"

### STARTUP ###
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
