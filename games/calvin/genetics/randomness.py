import random
from enum import Enum

class Size(Enum):
    SHORT = "short"
    AVERAGE = "average"
    TALL = "tall"

DEFAULT_WEIGHTS = {
    Size.SHORT: .25,
    Size.AVERAGE: .50,
    Size.TALL: .25
}


class Range:
    def __init__(self, min: float, max:float):
        self.min = min
        self.max = max

    def random_value(self):
        return random.uniform(self.min, self.max)


DEFAULT_SCALE = {
    Size.SHORT: Range(min=0.8, max=0.96),
    Size.AVERAGE: Range(min=0.96, max=1.05),
    Size.TALL: Range(min=1.05, max=1.25)
}


def get_random_size():
    population = list(Size)
    weights = list(DEFAULT_WEIGHTS.values())
    size = random.choices(population, weights)[0]  # get first random choice
    return size


def get_scale(size: Size):
    scale_range = DEFAULT_SCALE[size]
    scale = scale_range.random_value()
    return scale

def random_scale_3(size: Size, base_multiplier: int=1):
    output = get_scale(size=size)
    return output*base_multiplier

def main():
    size = get_random_size()
    output = random_scale_3(size=size)
    print("--------------------------")
    print(size)
    print(output)

if __name__ == '__main__':
    main()
