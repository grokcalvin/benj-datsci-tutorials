from enum import Enum
from pprint import pprint
from dataclasses import dataclass


class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    YELLOW = 'yellow'


# all the enumeration namas and values
# for color in Color:
#     print(color)
#     print(color.name)
#     print(color.value)

# all the enumeration namas and values
# for color in Color:
#     print(color)
#     print(color.name)
#     print(color.value)


# for color_string in ['red', 'green', 'yellow']:
#     color = Color(color_string)
#     print(color)




class StopSignBad:
    def __init__(self, color: str) -> None:
        self.color = color
    
    def show_light(self):
        print(self.color)


class StopSignBetter:
    def __init__(self, color: str) -> None:
        self.color = Color(color)
    
    def show_light(self):
        print(self.color)


class StopSignBest:
    def __init__(self, color: Color) -> None:
        self.color = color
    
    def show_light(self):
        if self.color == Color.RED:
            print('Please Stop!')
        elif self.color == Color.YELLOW:
            print('Please slow down!')
        elif self.color == Color.GREEN:
            print('Please continue!')
        else:
            raise ValueError("color not properly handled")



def main_examples():
    inputs = [
        'red',
        'green',
        'yellow',
        # 'yelow',
    ]
    # for color in inputs:
    #     stop_sign = StopSignBad(color=color)
    #     stop_sign.show_light()

    # for color in inputs:
    #     stop_sign = StopSignBetter(color=color)
    #     stop_sign.show_light()

    for color_string in inputs:
        color = Color(color_string)
        stop_sign = StopSignBetter(color=color)
        stop_sign.show_light()


def get_color():
    color = None
    while True:
        color_str = input(f"Give stop sign color: ").lower()

        try:
            color = Color(color_str)
        except Exception as e:
            print('Invalid color, try again!')

        if color is not None:
            return color


def main():
    color = get_color()
    stop_sign = StopSignBest(color=color)
    stop_sign.show_light()

if __name__ == '__main__':
    # main_examples()
    main()
