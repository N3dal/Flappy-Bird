"""
    all utilities needed for the game;
"""


def center_horizontally(parent_width, obj_width):
    """
        center any pic or object in the x axis;

        return int;
    """

    return (parent_width - obj_width) // 2


def center_vertically(parent_height, obj_height):
    """
        center any pic or object in the y axis;

        return int;
    """

    return (parent_height - obj_height) // 2


def center(parent_width, parent_height, obj_width, obj_height):
    """
        center any pic or obj in the middle of the window;

        return tuple;
    """

    return (center_horizontally(parent_width, obj_width), center_vertically(parent_height, obj_height))
