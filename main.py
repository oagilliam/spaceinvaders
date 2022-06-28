import pygame

# Initialize the pygame
pygame.init()

# create the screen, variables are screen size (width, height)
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Spaceship1.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 400
playerY = 520
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))


# Game Loop
running = True
while running:
    # RGB values: Red, Green, Blue
    screen.fill((0, 25, 52))
    playerY -= 0.2

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player(playerX,playerY)
    # This will update the screen/display/game window
    pygame.display.update()
