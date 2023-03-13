"""
    contain all the game defaults including the pictures,
    and sounds;
"""

from pygame import image


# window defaults;
WINDOW_SIZE = [288, 512]
BACKGROUND_COLOR = (0, 0, 0)


BACKGROUND_DAY_IMAGE = image.load(r"./assets/sprites/background-day.png")
BACKGROUND_NIGHT_IMAGE = image.load(r"./assets/sprites/background-night.png")
BASE_IMAGE = image.load(r"./assets/sprites/base.png")
GAME_OVER_IMAGE = image.load(r"./assets/sprites/gameover.png")
START_MSG = image.load(r"./assets/sprites/message.png")
GAME_ICON = image.load(r"./assets/favicon.ico")
