import pygame
import random
import math
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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemy = 6

for i in range(num_of_enemy):
    enemyImg.append(pygame.image.load("alien.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Laser
# ready, means the player can't see the laser on the screen
# fire means the laser is shooting
laserImg = pygame.image.load("yellowlaserbeam.png")
laserX = 0
laserY = 480
laserY_change = 10
laser_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))

def fire_laser(x,y):
    global laser_state
    laser_state = 'fire'
    screen.blit(laserImg, (x + 30,y + 10)) # This changes laser starting position

def isCollision(enemyX,enemyY,laserX,laserY):
    distance = math.sqrt((math.pow(enemyX-laserX,2)) + (math.pow(enemyY-laserY,2)))
    if distance < 27:
        return True
    else:
        return False


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
                if laser_state is "ready":
                    # Gets the current x coordinate of the ship
                    laserX = playerX
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
    for i in range(num_of_enemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.9
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.9
            enemyY[i] += enemyY_change[i]
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], laserX[i], laserY[i])
        if collision:
            laserY = 480
            laser_state = "ready"
            score += 1
            print(score)
            enemyX = random.randint(0, 735)
            enemyY = random.randint(50, 150)

    # Laser Movment
    if laserY <=0:
        laserY = 480
        laser_state = 'ready'

    if laser_state is 'fire':
        fire_laser(laserX,laserY)
        laserY -= laserY_change

    # Collision
    collision = isCollision(enemyX,enemyY,laserX,laserY)
    if collision:
        laserY = 480
        laser_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # This will update the screen/display/game window
    pygame.display.update()
