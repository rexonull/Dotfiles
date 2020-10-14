from libqtile.config import Group

names = [
        ("web",     {'layout': 'max'}),
        ("code",    {'layout': 'monadtall'}),
        ("chat",    {'layout': 'max'}),
        ("game",    {'layout': 'floating'}),
        ("mail",    {'layout': 'max'}),
        ("6",       {'layout': 'monadtall'}),
        ("7",       {'layout': 'monadtall'}),
        ("8",       {'layout': 'monadtall'}),
        ]


# names = [
        # ("one",    {'layout': 'max'}),
        # ("two",    {'layout': 'monadtall'}),
        # ("three",  {'layout': 'floating'}),
        # ("four",   {'layout': 'max'}),
        # ("five",   {'layout': 'max'}),
        # ("six",    {'layout': 'monadtall'}),
        # ("seven",  {'layout': 'monadtall'}),
        # ("eight",  {'layout': 'monadtall'}),
        # ]

groups = [Group(name, **kwargs) for name, kwargs in names]


