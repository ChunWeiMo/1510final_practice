def repeater(*stuff, **more_stuff):
    for name in stuff:
        print(name)
    for key, value in more_stuff.items():
        print(key, value)


repeater('name_a', 'name_b', 'name_c', name='name_d')
