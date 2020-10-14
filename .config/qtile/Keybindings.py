from libqtile.lazy import lazy
from libqtile.config import Key
from libqtile import extension

mod = "mod4"
browser = "firefox"
terminal = "termite"

def term_exec(command):
    cmd = terminal + " -e '" + command + "'"
    return cmd

run_bindings = [
    [mod, "Return", terminal],
    [mod, "space", "dmenu_run -nb '#161821' -nf '#c6c8d1' -sb '#b4be82' -sf '#002329' -h 25"],
    [mod, "b", browser],
    [mod, "shift", "Delete", "betterlockscreen -l"],
    [mod, "control", "Delete", "betterlockscreen -s"],
    [mod, "f", term_exec("ranger")],
    [mod, "control", "f", "pcmanfm"],
    [mod, "shift", "Return", "rofi -show drun -fullscreen"],
    [mod, "m", "java -jar /home/rexonull/My/minecraft/TLauncher-2.71.jar"],
    [mod, "mod1", "k", term_exec("less /home/rexonull/My/Coding/python3/keypresses.txt")],
    [mod, "control", "s", "scrot -e 'mv $f ~/Pictures/Screenshots && notify-send screenshot taken'"],
    [mod, "shift", "s", "scrot -e 'mv $f ~/Documents/notes && notify-send screenshot taken'"],
    [mod, "p", "love /home/rexonull/My/cs50_projects/pong/pong2"],
    [mod, "r", "sxiv /home/rexonull/Pictures/routine.jpg"],
    [mod, "v", term_exec("vim")],
    ["XF86AudioMute", "amixer -q set Master toggle"],
    ["XF86AudioLowerVolume", "amixer set Master 5%- unmute"],
    ["XF86AudioRaiseVolume", "amixer set Master 5%+ unmute"],
    ["XF86MonBrightnessUp", "xbacklight -inc 1"],
    ["XF86MonBrightnessDown", "xbacklight -dec 1"],
    ["shift", "XF86AudioLowerVolume", "amixer set Master 10%- unmute"],
    ["shift", "XF86AudioRaiseVolume", "amixer set Master 10%+ unmute"],
    ["shift", "XF86MonBrightnessUp", "xbacklight -inc 5"],
    ["shift", "XF86MonBrightnessDown", "xbacklight -dec 5"],
]

special_bindings = [
    # Switch between windows
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),

    # Move windows up or down
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Switch window focus
    Key([mod, "shift"], "space", lazy.layout.next()),

    # Toggle between layouts
    Key([mod], "Tab", lazy.next_layout()),

    # Kill a window
    Key([mod, "shift"], "c", lazy.window.kill()),

    # Increase and Decrease the size of the master window
    Key([mod, "control"], "k", lazy.layout.increase_ratio()),
    Key([mod, "control"], "j", lazy.layout.decrease_ratio()),

    # Restart and Shutdown qtile
    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift", "control", "mod1"], "q", lazy.shutdown()),

    # Toggle floating and fullscreen
    Key([mod], "s", lazy.window.toggle_floating()),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen()),

    # # Dmenu
    # Key([mod], 'r', lazy.run_extension(extension.DmenuRun(
        # dmenu_prompt=">",
        # dmenu_font="Comfortaa",
        # background="#18352e",
        # foreground="#aeaeae",
        # selected_background="#00ffdc",
        # selected_foreground="#aeaeae",
        # dmenu_height=25,  # Only supported by some dmenu forks
    # ))),
]
