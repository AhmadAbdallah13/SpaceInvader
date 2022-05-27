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

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # change background color.
    screen.fill((150, 0, 0))

    pygame.display.update()

