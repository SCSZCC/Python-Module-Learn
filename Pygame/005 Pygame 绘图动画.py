"""
程序概述：结合for循环使用直线工具绘制一个矩形。


工作逻辑：
利用for循环和pygame.display.update(),在使用矩形绘制直线的过程当中每绘制一条直线，就update一次。
从而实现“逐帧”显示的效果，进而让我们觉得这是一个“动”的过程。


"""

import pygame
import sys
import time

pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("First Pygame programe")
screen.fill((255,255,255))
pygame.display.update()
x = [200, 400, 400 , 200, 200]
y = [200, 200, 400, 400, 200]
for i in range(0, 4, 1):
    pygame.draw.line(screen, (0, 0, 255), (x[i], y[i]), (x[i+1], y[i+1]), 1)
    pygame.display.update()
    time.sleep(0.2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()




