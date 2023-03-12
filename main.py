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
from time import sleep

WINDOW_SIZE = [350, 600]
BACKGROUND_COLOR = (158, 145, 232)

pygame.init()


def main():

    window = pygame.display.set_mode(WINDOW_SIZE)

    var = 0
    state = True

    # create the game main event loop;
    game_running_state = True
    while game_running_state:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running_state = False
                break

        window.fill(BACKGROUND_COLOR)

        pygame.display.update()

    # end of the game;
    pygame.quit()


if __name__ == "__main__":
    main()
