import pygame
from pygame import mixer


class Screen:
    screen = pygame.display.set_mode((800, 600))

    def __init__(self):
        self.stars_background = pygame.image.load("static/stars.png")
        # todo: icon not working.
        self.icon = pygame.image.load("static/spaceship.png").convert()

        # change title and icon.
        pygame.display.set_caption("Space Invader")
        pygame.display.set_icon(self.icon)

        # play background music
        mixer.music.load("static/sounds/background.wav")
        mixer.music.play(-1)
