def hello_world(name: str = None):
    if not name:
        name = 'World'

    print(f'Hello {name}')
