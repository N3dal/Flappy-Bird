#!/usr/bin/python3
# -----------------------------------------------------------------
# simple floppy bird game;
#
#
#
# Author:N84.
#
# Create Date:Sun Mar 12 19:20:33 2023.
# ///
# ///
# ///
# -----------------------------------------------------------------

import pygame
from defaults import *
from utils import *

pygame.init()


class Pipe:
    """"""
    GREEN_PIPE_IMAGE = pygame.image.load(r"./assets/sprites/pipe-green.png")

    RED_PIPE_IMAGE = pygame.image.load(r"./assets/sprites/pipe-red.png")

    def __init__(self, *args):
        pass

    def change_color(self):
        """
            change the pipe color;

            return None;
        """

        return None


class Bird:
    """"""
    BLUE_BIRD_IMAGES = [
        pygame.image.load(r"./assets/sprites/bluebird-downflap.png"),
        pygame.image.load(r"./assets/sprites/bluebird-midflap.png"),
        pygame.image.load(r"./assets/sprites/bluebird-upflap.png")
    ]

    RED_BIRD_IMAGES = [
        pygame.image.load(r"./assets/sprites/redbird-downflap.png"),
        pygame.image.load(r"./assets/sprites/redbird-midflap.png"),
        pygame.image.load(r"./assets/sprites/redbird-upflap.png")
    ]

    YELLOW_BIRD_IMAGES = [
        pygame.image.load(r"./assets/sprites/yellowbird-downflap.png"),
        pygame.image.load(r"./assets/sprites/yellowbird-midflap.png"),
        pygame.image.load(r"./assets/sprites/yellowbird-upflap.png")
    ]

    def __init__(self, *args):
        pass

    def jump(self):
        """
            Docstring;

            return None;
        """

        return None

    def change_color(self):
        """
            change the bird color;

            return None;
        """

        return None

    def show(self):
        """
            show the bird on the screen;

            return None;
        """

        return None

    def hide(self):
        """
            hide the bird from the screen;

            return None;
        """

        return None


class Number:
    """"""
    NUMBER_IMAGES = [pygame.image.load(
        f"./assets/sprites/{num}.png") for num in range(10)]


class PointsBoard:
    """"""

    def __init__(self, *args):
        self.__points = 0

    def increment(self):
        """
            increment the board by one;
        """

    def reset(self):
        self.__points = 0

        return None

    def show(self):
        """
            show the points board;

            return None;
        """

        return None

    def hide(self):
        """
            hid the points board;

            return None;
        """

    @property
    def points(self):
        return self.__points


def main():

    window = pygame.display.set_mode(WINDOW_SIZE)

    # setup the game icon;
    pygame.display.set_icon(GAME_ICON)

    base_img_x = 0

    # create the game main event loop;
    game_running_state = True
    while game_running_state:

        window.fill(BACKGROUND_COLOR)
        # set the background image;
        window.blit(BACKGROUND_DAY_IMAGE, (0, 0))
        window.blit(BASE_IMAGE, (base_img_x, 450))

        if base_img_x == (WINDOW_SIZE[0] - BASE_IMAGE.get_width()):
            window.blit(BASE_IMAGE, (base_img_x + 388, 450))
            base_img_x = 0

        base_img_x -= 1

        window.blit(START_MSG, center(
            *WINDOW_SIZE, START_MSG.get_width(), START_MSG.get_height()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running_state = False
                break

        pygame.display.update()

        pygame.time.wait(5)

    # end of the game;
    pygame.quit()


if __name__ == "__main__":
    main()
