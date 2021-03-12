"""
程序概述：给窗口染个颜色




API说明：
1.screen.fill(tuple)
  给定义的窗口填充颜色，通过RGB值设置窗口颜色，以元组的形式进行设置。

2.pygame.display.update()
  刷新窗口，在Pygame当中，如果对窗口内容做出任何改变，都需要配合update才能使其生效。
"""

import pygame
import sys

pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("First Pygame programe")
screen.fill((255,255,255))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

