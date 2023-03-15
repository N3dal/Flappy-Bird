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


class Menu:
    pass


class MainWindow:
    """
        Game Main Window;
    """
    SIZE = [288, 512]
    WIDTH, HEIGHT = SIZE
    BACKGROUND_COLOR = (0, 0, 0)
    BACKGROUND_DAY_IMAGE = pygame.image.load(
        r"./assets/sprites/background-day.png")
    BACKGROUND_NIGHT_IMAGE = pygame.image.load(
        r"./assets/sprites/background-night.png")
    BASE_IMAGE = pygame.image.load(r"./assets/sprites/base.png")
    GAME_OVER_IMAGE = pygame.image.load(r"./assets/sprites/gameover.png")
    START_MSG = pygame.image.load(r"./assets/sprites/message.png")
    ICON = pygame.image.load(r"./assets/favicon.ico")

    def __init__(self):

        # set the window icon;
        pygame.display.set_icon(MainWindow.ICON)

        self.window = pygame.display.set_mode(MainWindow.SIZE)

        self.__running = True
        self.base_image_x_coordinates = 0

        # setup the default background;
        self.background_image = MainWindow.BACKGROUND_DAY_IMAGE

        # start image status;
        self.start_image_status = True

    def background_fill(self):
        """
            setup Window background and the base;
            and notice that we will move the base,
            image;

            return None;
        """

        self.window.fill(MainWindow.BACKGROUND_COLOR)

        # set the background image now and the base;
        self.window.blit(self.background_image, (0, 0))

        # set the base image;
        self.window.blit(MainWindow.BASE_IMAGE,
                         (self.base_image_x_coordinates, 450))

        if self.base_image_x_coordinates == (MainWindow.WIDTH - MainWindow.BASE_IMAGE.get_width()):
            self.window.blit(MainWindow.BASE_IMAGE,
                             (self.base_image_x_coordinates + 388, 450))
            self.base_image_x_coordinates = 0

        # in every call we will mines this var by one;
        self.base_image_x_coordinates -= 1

        if self.start_image_status:
            self.show_start_image()
        else:
            self.hide_start_image()

        return None

    def change_background(self, background: str = "day"):
        """
            change the background image;

                background:str => 'day' for day background;
                background:str => 'night' for night background;


            return None;
        """

        if background == "day":
            self.background_image = MainWindow.BACKGROUND_DAY_IMAGE
        elif background == "night":
            self.background_image = MainWindow.BACKGROUND_NIGHT_IMAGE

        else:
            raise Exception(
                f"choose only 'day' or 'night' {background} is not valid!!")

        return None

    def start(self):
        """
            start the game main-loop;

            return None;
        """

        while self.running:
            self.background_fill()

            # key loop;
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running = False
                    break
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.start_image_status = False

                if event.type == pygame.MOUSEWHEEL:
                    self.start_image_status = True

            pygame.display.update()
            pygame.time.wait(5)

    def show_start_image(self):
        """
            set the start image;

            return None;
        """
        # first show the image;
        MainWindow.START_MSG.set_alpha(255)

        self.window.blit(MainWindow.START_MSG, center(MainWindow.WIDTH, MainWindow.HEIGHT,
                         MainWindow.START_MSG.get_width(), MainWindow.START_MSG.get_height()))

        return None

    def hide_start_image(self):
        """
            hide the start image;

            return None;
        """

        MainWindow.START_MSG.set_alpha(0)

        return None

    @property
    def running(self):
        return self.__running


def main():

    game = MainWindow()
    game.start()

    # end of the game;
    pygame.quit()


if __name__ == "__main__":
    main()
