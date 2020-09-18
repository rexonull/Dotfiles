from libqtile import layout

theme = {
    "border_width": 2,
    "margin": 10,
    "border_focus": "#e06c75",
    "border_normal": "#abb2bf"
}
theme_m = {
    "border_width": 0,
    "margin": 2,
}

layouts = [
    layout.Max(**theme),
    layout.MonadTall(**theme),
    layout.Floating(**theme),
]

floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
], **theme)
