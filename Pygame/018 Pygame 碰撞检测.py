"""
程序概述：实现角色之间的碰撞检测


工作逻辑：
检测碰撞


API：
1.rect1.colliderect(rect2)
检测两个角色之间是否发生了碰撞，返回True or False


"""

import pygame
import sys


pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Image Loader")
red = pygame.image.load("./images//red_plane.png")
red_plane = pygame.transform.scale(red, (100,100))
blue = pygame.image.load("./images//blue_plane.png")
blue_plane = pygame.transform.scale(blue, (100,100))
explosion = pygame.image.load("./images//explosion.png")
explosion_rect = explosion.get_rect()
explosion_rect.centerx = 400
explosion_rect.centery = 400
red_rect = red_plane.get_rect()
blue_rect = blue_plane.get_rect()
red_rect.centery = 400
blue_rect.centery = 400
red_rect.centerx = 0
blue_rect.centerx = 800
myclock = pygame.time.Clock()
myclock.tick(60)
count = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    if red_rect.colliderect(blue_rect):
        screen.blit(explosion, explosion_rect)
        pygame.display.update()
    else:
        screen.fill((0,0,0))
        red_rect.centerx = 0 + count
        blue_rect.centerx = 800 -count
        screen.blit(red_plane, red_rect)
        screen.blit(blue_plane, blue_rect)
        pygame.display.update()
        myclock.tick(60)
        count += 1 
        
