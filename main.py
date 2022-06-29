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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.2
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    player(playerX,playerY)
    # This will update the screen/display/game window
    pygame.display.update()
