from dataclasses import dataclass
from enum import Enum

"""
Easy and Hard ways to print your class to the screen. 

"""


@dataclass
class POSEasyWay:
    x: int
    y: int


class POSHardWay:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return(f"POSHardWay(x={self.x}, y={self.y})")


def main():
    easy = POSEasyWay(x=1, y=2)
    hard = POSHardWay(x=1, y=2)
    print(easy)
    print(hard)


if __name__ == '__main__':
    main()
