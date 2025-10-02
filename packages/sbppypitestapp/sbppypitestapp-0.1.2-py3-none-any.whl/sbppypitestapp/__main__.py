from sbppypitestlib import hello as lib_hello

from .sbppypitestapp import hello as app_hello


def main() -> None:
    print(lib_hello())
    print(app_hello())


if __name__ == "__main__":
    main()
