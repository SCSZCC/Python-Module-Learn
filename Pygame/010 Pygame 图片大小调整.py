"""
程序概述：程序用于解决加载的图片过大的问题。


工作逻辑：
窗口的大小是在编写程序时定义好的。但是当图片的分辨率大于窗口大小的时候，就会出现图片显示全的问题。
针对这种情况，需要对图片的大小进行缩放。


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
pic = pygame.image.load("./images//010-1.png")
pic_rect = pic.get_rect()
pic_rect.centerx = 400
pic_rect.centery = 400
screen.fill((0,0,0))
screen.blit(pic, pic_rect)
pygame.display.update()
time.sleep(5)
new_pic = pygame.image.load("./images//010-1.png")
new_pic_scale = pygame.transform.scale(new_pic, (400,400))
new_pic_rect = new_pic_scale.get_rect()
new_pic_rect.centerx = 400
new_pic_rect.centery = 400
screen.fill((0,0,0))
screen.blit(new_pic_scale, new_pic_rect)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()





