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

pygame.init()


class Pipe:
    """"""
    pass


class Bird:
    """"""
    pass


class Number:
    """"""
    pass


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
