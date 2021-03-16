"""
程序概述：通过绘制线段的方式显示电脑CPU使用率情况。


工作逻辑：
通过使用psutil库获取电脑CPU的使用状况，并将获取到的数值作为绘制直线时的Y轴的值，从而实现折线图的绘制。


API：
1.psutil.cpu_percent()
  获取电脑CPU当前的使用率状态
"""

import pygame
import sys
import time
import psutil

pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("CPU percent")
screen.fill((0,0,0))
pygame.display.update()

x = 0
y = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    y1 = psutil.cpu_percent()
    pygame.draw.line(screen, (0, 0, 255), (x, y + 400),(x+1, y1+400),1)
    y = y1
    x += 1
    pygame.display.update()
    time.sleep(0.2)





