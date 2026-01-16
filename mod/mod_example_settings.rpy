init python:
    build.archive("mod", "all")

    build.classify('game/mod_example/**.png', 'mod')
    build.classify('game/mod_example/**.jpg', 'mod')
    build.classify('game/mod_example/**.ogg', 'mod')
    build.classify('game/mod_example/**.ogv', 'mod')
    build.classify('game/mod_example/**.otf', 'mod')
    build.classify('game/mod_example/**.ttf', 'mod')
    build.classify('game/mod_example/**.mp3', 'mod')
    build.classify('game/mod_example/**.webm', 'mod')
    build.classify('game/mod_example/**.rpyc', 'mod')
    build.classify('game/mod_example/**.rpymc', 'mod')
    build.classify('game/mod_example/**.mpg', 'mod')

    pass