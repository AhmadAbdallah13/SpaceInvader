import pygame
import random


class Alien:
    alien_img = pygame.image.load("static/alien.png")

    def __init__(self):
        self.x_coordinates = random.randint(64, 736)
        self.y_coordinates = random.randint(64, 150)
        self.x_change = 2.5
        self.y_change = 20

    def alien_coordinates(self, x_coordinates, y_coordinates):
        from game_screen import Screen
        Screen.screen.blit(
            self.alien_img, (x_coordinates, y_coordinates)
        )

    def update_coordinates(self):
        self.x_coordinates += self.x_change
        if self.x_coordinates <= 0:
            self.x_change = 2.5
            self.y_coordinates += self.y_change
        elif self.x_coordinates >= 736:
            self.x_change = -2.5
            self.y_coordinates += self.y_change
