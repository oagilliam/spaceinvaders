import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen, variables are screen size (width, height)
screen = pygame.display.set_mode((700, 600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Spaceship1.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("spaceship.png")
playerX = 350
playerY = 520
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0,681)
enemyY = random.randint(50,150)
enemyX_change = 0.1
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


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
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checks for boundaries of spaceship to prevent it from going out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    # 700 - 32 pixels (size of the image) is 698.
    elif playerX >= 668:
        playerX = 668

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.1
        enemyY += enemyY_change
    elif enemyX >= 668:
        enemyX_change = -0.1
        enemyY += enemyY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # This will update the screen/display/game window
    pygame.display.update()
