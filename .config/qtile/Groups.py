from libqtile.config import Group

names = [("1", {'layout': 'monadtall'}),
         ("2", {'layout': 'monadtall'}),
         ("3", {'layout': 'monadtall'}),
         ("4", {'layout': 'monadtall'}),
         ("5", {'layout': 'monadtall'}),
         ("6", {'layout': 'monadtall'}),
         ("7", {'layout': 'monadtall'}),
         ("8", {'layout': 'monadtall'})]


groups = [Group(name, **kwargs) for name, kwargs in names]
