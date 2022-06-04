import pygame
from game_screen import Screen
from player import Player
from alien import Alien

# initialize the game.
pygame.init()
screen = Screen()
player = Player(370, 480)
alien = Alien()

# bullet
bullet_img = pygame.image.load("static/bullet.png")
bullet_x_coordinates = 0  # x will not change
bullet_y_coordinates = 480
bullet_x_change = 0  # x will not change
bullet_y_change = 3.5
bullet_state = "ready"


def fire_bullet(x_coordinates, y_coordinates):
    global bullet_state
    bullet_state = "fire"
    screen.screen.blit(
        bullet_img,
        (x_coordinates + 16, y_coordinates + 10)
    )


# game loop
running = True
while running:
    # change background color.
    # keep it first to be below all the images.
    screen.screen.fill((0, 0, 0))
    screen.screen.blit(screen.stars_background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_change -= 4
            if event.key == pygame.K_RIGHT:
                player.player_change += 4
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x_coordinates = player.x_coordinates
                fire_bullet(bullet_x_coordinates, bullet_y_coordinates)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT \
                    or event.key == pygame.K_RIGHT:
                player.player_change = 0

    player.update_coordinates()
    alien.update_coordinates()

    # bullet movement
    if bullet_y_coordinates <= 0:
        bullet_y_coordinates = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x_coordinates, bullet_y_coordinates)
        bullet_y_coordinates -= bullet_y_change

    player.player_coordinates(player.x_coordinates, player.y_coordinates)
    alien.alien_coordinates(alien.x_coordinates, alien.y_coordinates)

    pygame.display.update()

