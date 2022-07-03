import pygame
import random

# Initialize the pygame
pygame.init()

# create the screen, variables are screen size (width, height)
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load("background.png")

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("Spaceship1.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("battleship.png")
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("alien.png")
enemyX = random.randint(0,681)
enemyY = random.randint(50,150)
enemyX_change = 0.9
enemyY_change = 40

# Laser
# ready, means the player can't see the laser on the screen
# fire means the laser is shooting
laserImg = pygame.image.load("yellowlaserbeam.png")
laserX = 0
laserY = 480
laserY_change = 10
laser_state = "ready"

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_laser(x,y):
    global laser_state
    laser_state = 'fire'
    screen.blit(laserImg, (x + 16,y + 10))

# Game Loop
running = True
while running:
    # RGB values: Red, Green, Blue
    screen.fill((0, 25, 52))
    # background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # If keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                fire_laser(playerX, laserY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checks for boundaries of spaceship to prevent it from going out of bounds
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    # 800 - 64 pixels (size of the image) is 736.
    elif playerX >= 736:
        playerX = 736

    # Enemy movement
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.9
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.9
        enemyY += enemyY_change

    # Laser Movment
    if laser_state is 'fire':
        fire_laser(playerX,laserY)
        laserY -= laserY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # This will update the screen/display/game window
    pygame.display.update()
