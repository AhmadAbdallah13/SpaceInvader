import pygame


class Bullet:
    bullet_img = pygame.image.load("static/bullet.png")

    def __init__(self):
        self.x_coordinates = 0  # x will not change
        self.x_change = 0  # x will not change
        self.y_coordinates = 480
        self.y_change = 3.5
        self.state = "ready"

    def fire_bullet(self, x_coordinates, y_coordinates):
        from game_screen import Screen
        self.state = "fire"
        Screen.screen.blit(
            self.bullet_img,
            (x_coordinates + 16, y_coordinates + 10)
        )

    def update_coordinates(self):
        if self.y_coordinates <= 0:
            self.y_coordinates = 480
            self.state = "ready"
        if self.state == "fire":
            self.fire_bullet(self.x_coordinates, self.y_coordinates)
            self.y_coordinates -= self.y_change
