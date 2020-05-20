from libqtile import widget, bar
from libqtile.config import Screen

defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
    background="#18352e",
    foreground="#aeaeae"
)

extension_defaults = defaults.copy()

bar_colors = ["#00fc42", "#0095af", "#ca6048"]

widgets = [
    widget.GroupBox(
        disable_drag = True,
        highlight_method = "line",
        rounded = False,
        borderwidth = 2,
        inactive = "#027263",
        active = "#00ffdc",
        highlight_color = ["#18352e", "#18352e"],
        this_current_screen_border = "#00ffdc",
        fontsize = 12,
        ),
    widget.WindowName(),
    widget.TextBox(
        text = "",
        fontsize = 11,
        padding = 1,
        foreground = bar_colors[0]
        ),
    widget.Backlight(
        backlight_name = "intel_backlight",
        foreground = bar_colors[0]
        ),
    widget.Sep(padding = 7, linewidth = 0),
    widget.TextBox(
        text = "",
        fontsize = 11,
        foreground = bar_colors[1]
        ),
    widget.Volume(
        foreground = bar_colors[1]
        ),
    widget.Sep(padding = 7, linewidth = 0),
    widget.Battery(
        charge_char = "",
        discharge_char = "",
        empty_char = "",
        full_char = "",
        low_foreground = "#ff3333",
        show_short_text = False,
        format = "{char}",
        font = "Symbols Nerd Font",
        foreground = bar_colors[2]
        ),
    widget.Battery(
        low_foreground = "#ff3333",
        show_short_text = False,
        format = "{percent: 2.0%}",
        foreground = bar_colors[2]
        ),
    widget.Sep(padding = 7, linewidth = 0),
    widget.Wlan(
        disconnected_message = "睊",
        format = "",
        interface = "wlp2s0",
        foreground = bar_colors[0]
        ),
    widget.Net(
        format = "↓{down} ↑{up}",
        foreground = bar_colors[0]
        ),
    widget.Sep(padding = 7, linewidth = 0),
    widget.TextBox(
        text = "",
        padding = 1,
        foreground = bar_colors[1]
        ),
    widget.Clock(
        format = "%I:%M %p ",
        foreground = bar_colors[1]
        ),
    widget.Sep(padding = 7, linewidth = 0),
    widget.CurrentLayout(),
    widget.Systray(),
    ]

screens = [
    Screen(top = bar.Bar(widgets, size = 25))
]
