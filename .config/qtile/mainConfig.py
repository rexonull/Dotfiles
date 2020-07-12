import Keybindings
import Groups
import Layouts
import Widgets
import Mouse

from libqtile.config import Key
from libqtile.lazy import lazy

keys = []
groups = Groups.groups
layouts = Layouts.layouts
floating_layout = Layouts.floating_layout
widget_defaults = Widgets.defaults
extension_defaults = Widgets.extension_defaults
screens = Widgets.screens
mouse = Mouse.mouse

def start():
    for binding in Keybindings.run_bindings:
        modif = []
        for i in range(len(binding) - 2):
            modif.append(binding[i])
        keys.append(Key(modif, binding[-2], lazy.spawn(binding[-1])))

    for binding in Keybindings.special_bindings:
        keys.append(binding)

    for i, (name, kwargs) in enumerate(Groups.names, 1):
        keys.append(Key(["mod4"], str(i), lazy.group[name].toscreen()))
        keys.append(Key(["mod4", "shift"], str(i), lazy.window.togroup(name))) 

    Groups.names.append(("password", {'layout': 'max'}))
    keys.append(Key(["mod4", "control"], "p", lazy.group["password"].toscreen()))
    keys.append(Key(["mod4", "control", "shift"], "p", lazy.window.togroup("password")))
