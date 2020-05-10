from libqtile import widget, bar
from libqtile.config import Screen

defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
    background="#272727",
    foreground="#747474"
)

extension_defaults = defaults.copy()

bar_colors = ["#14a76c", "#ffe400", "#ff652f"]

widgets = [
    widget.GroupBox(
        disable_drag = True,
        highlight_method = "line",
        rounded = False,
        borderwidth = 2,
        inactive = "#9b2a01",
        active = "#ff652f",
        highlight_color = ["#272727", "#272727"],
        this_current_screen_border = "#ff652f",
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
