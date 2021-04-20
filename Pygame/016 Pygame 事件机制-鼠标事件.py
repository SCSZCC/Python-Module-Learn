"""
程序概述：了解如何在Pygame当中调用键盘的功能。
在程序当中，实现按下上下左右键后，在窗口上能够显示对应的文字

工作逻辑：
键盘事件的使用逻辑：
判定键盘事件event.type == pygame.KEYDOWN → 判定按键 event.key == 按键名称


API：
1.event.type ==pygame.MOUSEBUTTONDOWN
  event.type:表示pygame侦测到的事件机制
  pygame.MOUSEBUTTONDOWN鼠标按下事件
       在pygame.MOUSEBUTTONDOWN事件下可以对鼠标按键进行判定：
           event.button 接收按下按键的常量名称，值为1、2、3对应鼠标左键、滚轮、右键
        示例：判定鼠标左键是否按下 if event.button == 1:

2.event.type ==pygame.MOUSEBUTTONUP
  event.type:表示pygame侦测到的事件机制
  pygame.MOUSEBUTTONUP鼠标松开事件
       在pygame.MOUSEBUTTONUP事件下可以对鼠标松开按键进行判定：
           event.button 接收松开按键的常量名称，值为1、2、3对应鼠标左键、滚轮、右键
        示例：判定鼠标左键是否按下 if event.button == 1:

3.event.type ==pygame.MOUSEMOTION
  event.type:表示pygame侦测到的事件机制
  pygame.MOUSEMOTION鼠标移动事件
       在pygame.MOUSEMOTION可以获得鼠标在当前窗口的坐标值：
           event.pos 接收鼠标在窗口的坐标值
        示例：获取鼠标当前的坐标值 print(event.pos)
        

        
    """

import pygame
import sys
import time


def word_text(word):
  text = font.render(word, True, (255,255,255))
  text_rect = text.get_rect()
  text_rect.centerx = 400
  text_rect.centery = 400
  screen.fill((0,0,0))
  screen.blit(text, text_rect)
  pygame.display.update()


pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Mouse Event")
font = pygame.font.Font("./font//SourceHanSansSC-Normal.otf", 40)   # 字体文件为思源黑体 开源字体

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            word_text(str(event.pos))
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                word_text("左键按下了")
            elif event.button == 2:
                word_text("滚轮按下了")
            elif event.button == 3:
                word_text("右键按下了")
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                word_text("左键松开了")
            elif event.button == 2:
                word_text("滚轮松开了")
            elif event.button == 3:
                word_text("右键松开了")
            
            