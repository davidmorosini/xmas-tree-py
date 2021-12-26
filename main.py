import os
from random import choice
import time

from colors import get_colored_string, get_color_names


light = "0"
leaf = "1"
trunk = "|"
leaf_color = "green"
tree_elements = [ # "random" disposition
    leaf,
    leaf,
    leaf,
    light,
    leaf,
    leaf,
    leaf,
    leaf,
    leaf,
    light,
    leaf,
    leaf,
    leaf,
    leaf,
    leaf,
    leaf,
    light,
    leaf,
    leaf
]



def clear_bash():
    os.system("cls" if os.name == "nt" else "clear")

def get_bash_center() -> int:
    columns = os.get_terminal_size().columns
    return int(columns/ 2)


def get_tree_levels(level_number: int) -> list:
    level = []
    color_names = list(get_color_names())
    for level_ in range(level_number):
        element = choice(tree_elements)
        color  = leaf_color if element == leaf else choice(color_names)
        colored_str = get_colored_string(element, color)
        level.append(colored_str)
        if level_ + 1 < level_number:
            level.append(" ")
    return level


def draw_tree(
    height: int = 12,
    trunk_height_rate: float = 0.25,
    trunk_width_rate: float = 0.4,
    custom_phrase: str = "Happy Xmas! =)"
):
    center_column = get_bash_center()
    stair_on_off = choice(["light-yellow", "gray"])
    stair = get_colored_string("X", stair_on_off)
    print(" " * (center_column - 3), stair, end="")

    for row_number in range(height):
        row = get_tree_levels(row_number)
        spaces = " " * (center_column - (row_number + 1))
        print(spaces, end="")
        for char in row:
            print(char, end="")
        print()

    trunk_height = int(height * trunk_height_rate)
    trunk_width = int(height * trunk_width_rate)
    if trunk_width % 2 == 0:
        trunk_width += 1

    trunk_start_position = int((trunk_width - 1) / 2) + 3
    for i in range(trunk_height):
        trunk_draw = trunk * trunk_width
        print(" " * (center_column - trunk_start_position), trunk_draw)


    dist = center_column - int((len(custom_phrase) / 2)) - 3
    print("\n")
    print(" " * dist, custom_phrase)



if __name__ == "__main__":

   while True:
        clear_bash()
        draw_tree(height=15)
        time.sleep(1)
