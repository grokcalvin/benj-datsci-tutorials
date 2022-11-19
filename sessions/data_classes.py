from dataclasses import dataclass

"""
These two classes are the same. 
"""


@dataclass
class POS:
    x: int
    y: int


class POSSame:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
