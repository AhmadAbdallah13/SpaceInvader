import random

import pygame


# initialize the game.
pygame.init()

# create the screen.
screen = pygame.display.set_mode((800, 600))

# change title and icon.
pygame.display.set_caption("Space Invader")
# todo: icon not working.
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load("player.png")
player_x_coordinates = 370
player_y_coordinates = 480
player_change = 0

# alien
alien_img = pygame.image.load("alien.png")
alien_x_coordinates = random.randint(64, 736)
alien_y_coordinates = random.randint(64, 150)
alien_x_change = 0.2
alien_y_change = 40


def player(x_coordinates, y_coordinates):
    screen.blit(
        player_img, (x_coordinates, y_coordinates)
    )


def alien(x_coordinates, y_coordinates):
    screen.blit(
        alien_img, (x_coordinates, y_coordinates)
    )


# game loop
running = True
while running:
    # change background color.
    # keep it first to be below all the images.
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change -= 0.2
            if event.key == pygame.K_RIGHT:
                player_change += 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT \
                    or event.key == pygame.K_RIGHT:
                player_change = 0

    player_x_coordinates += player_change
    if player_x_coordinates <= 0:
        player_x_coordinates = 0
    elif player_x_coordinates >= 736:
        player_x_coordinates = 736

    alien_x_coordinates += alien_x_change
    if alien_x_coordinates <= 0:
        alien_x_change = 0.2
        alien_y_coordinates += alien_y_change
    elif alien_x_coordinates >= 736:
        alien_x_change = -0.2
        alien_y_coordinates += alien_y_change

    player(player_x_coordinates, player_y_coordinates)
    alien(alien_x_coordinates, alien_y_coordinates)

    pygame.display.update()

