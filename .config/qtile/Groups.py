from libqtile.config import Group

names = [
        ("web",     {'layout': 'max'}),
        ("code",    {'layout': 'monadtall'}),
        ("game",    {'layout': 'max'}),
        ("mail",    {'layout': 'max'}),
        ("chat",    {'layout': 'max'}),
        ("6",       {'layout': 'monadtall'}),
        ("7",       {'layout': 'monadtall'}),
        ("8",       {'layout': 'monadtall'}),
        ]


groups = [Group(name, **kwargs) for name, kwargs in names]
