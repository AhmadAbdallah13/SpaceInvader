import random

import pygame


# initialize the game.
pygame.init()

# create the screen.
screen = pygame.display.set_mode((800, 600))
# add background image
stars_background = pygame.image.load("static/stars.png")

# change title and icon.
pygame.display.set_caption("Space Invader")
# todo: icon not working.
icon = pygame.image.load("static/spaceship.png").convert()
pygame.display.set_icon(icon)

# player
player_img = pygame.image.load("static/player.png")
player_x_coordinates = 370
player_y_coordinates = 480
player_change = 0

# alien
alien_img = pygame.image.load("static/alien.png")
alien_x_coordinates = random.randint(64, 736)
alien_y_coordinates = random.randint(64, 150)
alien_x_change = 2.5
alien_y_change = 20

# bullet
bullet_img = pygame.image.load("static/bullet.png")
bullet_x_coordinates = 0  # x will not change
bullet_y_coordinates = 480
bullet_x_change = 0  # x will not change
bullet_y_change = 3.5
bullet_state = "ready"


def player(x_coordinates, y_coordinates):
    screen.blit(
        player_img, (x_coordinates, y_coordinates)
    )


def alien(x_coordinates, y_coordinates):
    screen.blit(
        alien_img, (x_coordinates, y_coordinates)
    )


def fire_bullet(x_coordinates, y_coordinates):
    global bullet_state
    bullet_state = "fire"
    screen.blit(
        bullet_img,
        (x_coordinates + 16, y_coordinates + 10)
    )


# game loop
running = True
while running:
    # change background color.
    # keep it first to be below all the images.
    screen.fill((0, 0, 0))
    screen.blit(stars_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change -= 4
            if event.key == pygame.K_RIGHT:
                player_change += 4
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x_coordinates = player_x_coordinates
                fire_bullet(bullet_x_coordinates, bullet_y_coordinates)
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
        alien_x_change = 2.5
        alien_y_coordinates += alien_y_change
    elif alien_x_coordinates >= 736:
        alien_x_change = -2.5
        alien_y_coordinates += alien_y_change

    # bullet movement
    if bullet_y_coordinates <= 0:
        bullet_y_coordinates = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x_coordinates, bullet_y_coordinates)
        bullet_y_coordinates -= bullet_y_change

    player(player_x_coordinates, player_y_coordinates)
    alien(alien_x_coordinates, alien_y_coordinates)

    pygame.display.update()

