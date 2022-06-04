import pygame


class Player:
    player_img = pygame.image.load("static/player.png")

    def __init__(self, x_coordinates, y_coordinates):
        self.x_coordinates = x_coordinates
        self.y_coordinates = y_coordinates
        self.player_change = 0

    def player_coordinates(self, x_coordinates, y_coordinates):
        from game_screen import Screen
        Screen.screen.blit(
            self.player_img, (x_coordinates, y_coordinates)
        )

    def update_coordinates(self):
        self.x_coordinates += self.player_change
        if self.x_coordinates <= 0:
            self.x_coordinates = 0
        elif self.x_coordinates >= 736:
            self.x_coordinates = 736
