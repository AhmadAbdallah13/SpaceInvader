import pygame


class Screen:
    # create the screen.
    screen = pygame.display.set_mode((800, 600))
    # add background image
    stars_background = pygame.image.load("static/stars.png")

    # change title and icon.
    pygame.display.set_caption("Space Invader")
    # todo: icon not working.
    icon = pygame.image.load("static/spaceship.png").convert()

    def __init__(self):
        pygame.display.set_icon(self.icon)
