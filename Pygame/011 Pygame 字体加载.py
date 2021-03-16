"""
程序概述：解决Pygame窗口显示中文的问题


工作逻辑：
字体显示一般逻辑梳理
加载字体文件并设置字体大小 font.Font() → 设置文字内容、颜色、底纹render() → 生成矩形框get_rect() → 贴图blit() → 显示


API：
1.font = pygame.font.Font(file, size)
  Pygame默认的字体是不支持中文的，因此需要指定字体文件，用以实现中文字体的呈现。    
  file：填入字体文件的地址，使用方法与图片加载的方式相似，可以以绝对路径和相对路径的形式进行添加。  str
  size:用以设置字体的大小                                                                         int

2.text = font.render(text, antialias, color, background = None)
  利用字体生成内容
  text:填入文本内容                               str 
  antialias:设置字体是否平滑,填入True 或False     boolean
  color:填入字体颜色                              tuple
  background:填入字体背景颜色，相当于word当中设置文字底纹,默认为None。    tuple

3.text_rect = text.get_rect()
  作用与图片的get_rect一样，根据字体内容生成一个矩形框，通过矩形框对字体在窗口中的位置进行定位。




"""

import pygame
import sys


pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Font Loader")
font = pygame.font.Font("./font//SourceHanSansSC-Normal.otf", 40)   # 字体文件为思源黑体 开源字体
text = font.render("你好啊", True, (255,255,255))
text_rect = text.get_rect()
text_rect.centerx = 400
text_rect.centery = 400
screen.fill((0,0,0))
screen.blit(text, text_rect)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
