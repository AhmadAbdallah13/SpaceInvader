import pygame
from game_screen import Screen


def is_collided(
        alien_x_coordinates, alien_y_coordinates,
        bullet_x_coordinates, bullet_y_coordinates):
    distance = (
        (alien_x_coordinates - bullet_x_coordinates)**2 +
        (alien_y_coordinates - bullet_y_coordinates)**2
    ) ** 0.5
    if distance < 27:
        return True
    return False


def show_score(score_value):
    font = pygame.font.Font('static/fonts/Alice_in_Wonderland.ttf', 32)
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    Screen.screen.blit(score, (10, 10))


def game_over():
    game_over_font = pygame.font.Font('static/fonts/Alice_in_Wonderland.ttf', 64)
    score = game_over_font.render("Game Over, You Lost :(", True, (255, 255, 255))
    Screen.screen.blit(score, (130, 250))
