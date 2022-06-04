# #############  ORDER OF IMPORTS MATTER  #############
import pygame

from game_screen import Screen
from player import Player
from alien import Alien
from bullet import Bullet
from utils import is_collided, show_score

# #############  END OF IMPORTS   #############

# initialize the game.
pygame.init()
screen = Screen()
player = Player(370, 480)
bullet = Bullet()
aliens = []
for _ in range(6):
    alien = Alien()
    aliens.append(alien)


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
            if event.key == pygame.K_SPACE and bullet.state == "ready":
                bullet.x_coordinates = player.x_coordinates
                bullet.fire_bullet(bullet.x_coordinates, bullet.y_coordinates)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT \
                    or event.key == pygame.K_RIGHT:
                player.player_change = 0

    for alien in aliens:
        collision = is_collided(
            alien.x_coordinates,
            alien.y_coordinates,
            bullet.x_coordinates,
            bullet.y_coordinates,
        )
        if collision:
            bullet.y_coordinates = 480
            bullet.state = "ready"
            player.score += 1
            alien.respawn()

        alien.update_coordinates()
        alien.alien_coordinates(alien.x_coordinates, alien.y_coordinates)

    player.update_coordinates()
    bullet.update_coordinates()

    player.player_coordinates(player.x_coordinates, player.y_coordinates)
    show_score(player.score)
    pygame.display.update()
