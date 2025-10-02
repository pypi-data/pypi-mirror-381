from sbppypitestlib import hello as lib_hello

from .sbppypitestapp import hello as app_hello

print(lib_hello())
print(app_hello())
