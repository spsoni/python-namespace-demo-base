from namespace_demo.base.base_module import random_name
from namespace_demo.base.shared import hello_world


def main():
    name = random_name()
    hello_world(name)


if __name__ == '__main__':
    main()
