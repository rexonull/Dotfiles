from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
browser = "firefox"
terminal = "urxvt"

def term_exec(command):
    cmd = terminal + " -e " + command
    return cmd

run_bindings = [
    [mod, "Return", "urxvt"],
    [mod, "space", "rofi -show run"],
    [mod, "b", browser],
    [mod, "shift", "Delete", "betterlockscreen -l dimblur"],
    [mod, "f", term_exec("ranger")],
    [mod, "shift", "Return", "rofi -show drun -fullscreen"],
    ["XF86AudioMute", "amixer -q set Master toggle"],
    ["XF86AudioLowerVolume", "amixer set Master 5%- unmute"],
    ["XF86AudioRaiseVolume", "amixer set Master 5%+ unmute"],
    ["XF86MonBrightnessUp", "xbacklight -inc 10"],
    ["XF86MonBrightnessDown", "xbacklight -dec 10"],
]

special_bindings = [
    # Switch between windows
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Switch window focus
    Key([mod, "shift"], "space", lazy.layout.next()),

    # Toggle between layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Kill a window
    Key([mod], "w", lazy.window.kill()),

    # Increase and Decrease the size of the master window
    Key([mod, "control"], "k", lazy.layout.increase_ratio()),
    Key([mod, "control"], "j", lazy.layout.decrease_ratio()),

    # Restart and Shutdown qtile
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),

    # Toggle floating and fullscreen
    Key([mod], "s", lazy.window.toggle_floating()),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),
]
