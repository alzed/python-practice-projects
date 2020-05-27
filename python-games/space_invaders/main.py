from random import randint
from math import sqrt

import pygame, sys
pygame.init()

size = 800, 600
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Space invader")
icon = pygame.image.load('./assets/transport.png')
pygame.display.set_icon(icon)

player_img = pygame.image.load('./assets/player.png')
playerX, playerY = 370, 480
playerX_change = 0

score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX, textY = 10, 10

enemy_img = pygame.image.load('./assets/alien.png')
enemyX, enemyY = 370, 30
enemyX_change = 1
enemyY_change = 10

bullet_img = pygame.image.load('./assets/bullet.png')
bulletX, bulletY = playerX+16, playerY-64 
bulletY_change = 1

def display_score(score_value):
    score = font.render(f'Score: {score_value}', True, (0, 0, 0))
    screen.blit(score, (textX, textY))

def player(playerX, playerY):
    screen.blit(player_img, (playerX, playerY))

def enemy(enemyX, enemyY):
    screen.blit(enemy_img, (enemyX, enemyY))

fire = False
def bullet(bulletX, bulletY):
    screen.blit(bullet_img, (bulletX, bulletY))

def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = sqrt((enemyX-bulletX)**2 + (enemyY-bulletY)**2)
    return True if distance <= 32 else False

while 1:
    bg = 255, 255, 255
    screen.fill(bg)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_change = -0.5
                if event.key == pygame.K_RIGHT:
                    playerX_change = 0.5
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not fire:
                    fire = True
                    bulletX = playerX + 16
                    bulletY = playerY - 64
                    bullet(bulletX, bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                playerX_change = 0

    playerX += playerX_change
    
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736
    
    player(playerX, playerY)
    
    enemyX += enemyX_change
    
    if enemyX < 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX > 736:
        enemyX_change = -1
        enemyY += enemyY_change

    enemy(enemyX, enemyY)

    if fire:
        bulletY -= bulletY_change
        bullet(bulletX, bulletY)
    if bulletY < 0:
        bulletY = playerY - 64
        fire = False

    collision = is_collision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = playerY - 64
        fire = False
        score_value += 1
        enemyX = randint(0, 736)
        enemyY = 30
    
    display_score(score_value)
    pygame.display.update()
    