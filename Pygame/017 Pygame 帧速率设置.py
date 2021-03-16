"""
程序概述：利用时钟模块代替time模块，实现屏幕的刷新


工作逻辑：
在不使用time模块的基础上，加入时钟模块，控制画面的刷新。


API：
1.myclock = pygame.time.Clock()
创建帧速率对象

2.myclock.tick(FPS)
设置刷新帧速率，帧率大，速度越快。一般放在display.update后面进行调用。
FPS：填入刷新帧速率。   int
  
"""

import pygame
import sys


pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Image Loader")
screen.fill((0,0,0))
pygame.display.update()
pic = pygame.image.load("./images//007-1.png")
pic_rect = pic.get_rect()
pic_rect.centery = 400
myclock = pygame.time.Clock()
myclock.tick(60)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for i in range(0, 801, 1):
        screen.fill((0,0,0))
        pic_rect.centerx = i
        screen.blit(pic, pic_rect)
        pygame.display.update()
        myclock.tick(120)
    for j in range(800, -1, -1):
        screen.fill((0,0,0))
        pic_rect.centerx = j
        screen.blit(pic, pic_rect)
        pygame.display.update()
        myclock.tick(60)

