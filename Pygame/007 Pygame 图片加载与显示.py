"""
程序概述：加载图片文件，在Pygame窗口当中进行显示。


工作逻辑：
通过加载图片，定位、贴图的方式，将图片显示在窗口当中。


API：
1.pygame.image.load("文件路径")
  通过该API可以对外部图片文件进行加载。需要结合变量进行使用。通过变量进行实例化。
  文件路径可以填入相对路径和绝对路径。
    相对路径：即文件相对于当前程序文件的位置。如images文件夹与程序文件在同一个文件目录下，
              可以使用"./images"的方式指向该文件夹，如果要找到文件加当中的图片文件，需要
              通过//的方式找到，即"./images//007-1.png"。
    绝对路径：即常见的"C://programe//"
    
    使用示例：pic = pygame.image.load("./images//007-1.png")

    注意：由于/在Python当中时起到转义字符的作用，因此在Python中表示斜杠使用"//"
    
2. pic_rect = pic.get_rect()
  可以简单的理解为这是将加载的图片转换成一个跟其大小一样的“矩形”，通过设置矩形点的坐标可以调整图片在窗口当中的位置。
  一般默认会将矩形左上角的位置设置在(0,0)

3.screen.blit(pic, pic_rect)
  将图片pic,贴在pic_rect的位置上。  
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
screen.blit(pic, pic_rect)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()





