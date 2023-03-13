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

NUMBER_IMAGES = [image.load(
    f"./assets/sprites/{num}.png") for num in range(10)]

GREEN_PIPE_IMAGE = image.load(r"./assets/sprites/pipe-green.png")
RED_PIPE_IMAGE = image.load(r"./assets/sprites/pipe-red.png")

BLUE_BIRD_IMAGES = [
    image.load(r"./assets/sprites/bluebird-downflap.png"),
    image.load(r"./assets/sprites/bluebird-midflap.png"),
    image.load(r"./assets/sprites/bluebird-upflap.png")
]


RED_BIRD_IMAGES = [
    image.load(r"./assets/sprites/redbird-downflap.png"),
    image.load(r"./assets/sprites/redbird-midflap.png"),
    image.load(r"./assets/sprites/redbird-upflap.png")
]


YELLOW_BIRD_IMAGES = [
    image.load(r"./assets/sprites/yellowbird-downflap.png"),
    image.load(r"./assets/sprites/yellowbird-midflap.png"),
    image.load(r"./assets/sprites/yellowbird-upflap.png")
]


# Used to hide images;
TRANSPARENT = (0, 0, 0, 0)
