from libqtile import widget, bar
from libqtile.config import Screen

defaults = dict(
    font="Cantarell",
    fontsize=12,
    padding=3,
    background="#282c34",
    foreground="#abb2bf"
)

extension_defaults = defaults.copy()
bar_colors = ["#98c379", "#61afef", "#e06c75"]

def init_widgets_list():
    widgets_list = [
        widget.GroupBox(
            disable_drag = True,
            highlight_method = "line",
            padding_x = 6,
            rounded = False,
            borderwidth = 2,
            inactive = "#3e4452",
            active = "#abb2bf",
            highlight_color = ["#282c34", "#282c34"],
            this_current_screen_border = "#abb2bf",
            fontsize = 12,
            visible_groups = ['web', 'code', 'mail', 'chat', 'game'],
            ),
        widget.GroupBox(
            disable_drag = True,
            highlight_method = "line",
            padding_x = 3,
            rounded = False,
            borderwidth = 2,
            inactive = "#3e4452",
            active = "#abb2bf",
            highlight_color = ["#282c34", "#282c34"],
            this_current_screen_border = "#abb2bf",
            fontsize = 12,
            visible_groups = ['6', '7', '8'],
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
    return widgets_list

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2

screens = [
    Screen(top = bar.Bar(init_widgets_screen1(), size = 25)),
    Screen(top = bar.Bar(init_widgets_screen2(), size = 25))
]
