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


def player():
    screen.blit(player_img, (player_x_coordinates , player_y_coordinates))


# game loop
running = True
while running:
    # change background color.
    # keep it first to be below all the images.
    screen.fill((150, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()

