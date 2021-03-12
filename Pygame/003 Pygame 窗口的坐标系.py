"""
程序概述：窗口中的坐标系介绍 并绘制一个图案

Pygame窗口的坐标系。
窗口坐标系的大小是根据编写者定义的大小变化而变化的。窗口越大则坐标系越大。即display.set_mode(tuple)
如果设置的窗口大小为(800,800),则窗口当中左上角的坐标是(0,0),右下角的坐标则是(800,800)。




API说明：
1.pygame.draw.line(surface, color, startpoint, endpoint, width)
  surface指向的是窗口，如果你写的代码是screen = pygame.display.set_mode(screen_size)
  那么surface参数填入screen
  color:表示线段绘制的颜色,以RGB和元组的形式进行填入。
  startpoint：表示线段绘制的起始坐标，以元组的形式进行填入。
  endpoint：表示线段绘制的终点坐标，以元组的形式进行填入。 即两点确定一条直线。
  width：表示线段绘制的宽度，以数值的形式进行填入。

"""

import pygame
import sys

pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("First Pygame programe")
screen.fill((255,255,255))
pygame.draw.line(screen, (0, 0, 255), (100, 100), (500, 500), 5)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
