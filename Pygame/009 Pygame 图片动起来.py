"""
程序概述：加载图片并在窗口上动起来。


工作逻辑：
通过设置rect的坐标，不断的调整图片的位置。通过循环不断更改图片的位置，从而实现动起来的效果。


API：
1.time.sleep(float)
  等待x秒
"""

import pygame
import sys
import time


pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Image Loader")
screen.fill((0,0,0))
pygame.display.update()
pic = pygame.image.load("./images//007-1.png")
pic_rect = pic.get_rect()
pic_rect.centery = 400
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    for i in range(0, 801, 1):
        screen.fill((0,0,0))
        pic_rect.centerx = i
        screen.blit(pic, pic_rect)
        pygame.display.update()
        time.sleep(0.01)
    for j in range(800, -1, -1):
        screen.fill((0,0,0))
        pic_rect.centerx = j
        screen.blit(pic, pic_rect)
        pygame.display.update()
        time.sleep(0.01)








