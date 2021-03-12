"""
程序概述：创建一个Pygame窗口。

这个程序构成了Pygame的基础开发框架。


API说明：
1.pygame.init()
  对Pygame的功能进行初始化操作

2.pygame.display.set_mode(tuple)
  设置窗口模式,以元组的形式设置窗口的尺寸大小。

3.pygame.display.set_caption(str)
  设置窗口名称

4.pygame.event.get()
  Pygame的侦测到的行为和时间。

5.Pygame.QUIT
  Pygame退出事件。

"""

import pygame
import sys

pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("First Pygame programe")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()





