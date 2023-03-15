from sessions.example.module2 import foo

foo(x=10)

from sessions.example.module3 import foo

foo(y=10)


def foo(z: int):
    print(z)


foo(z=10)
