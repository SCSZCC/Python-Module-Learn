"""
程序概述：了解如何在Pygame当中调用键盘的功能。
在程序当中，实现按下上下左右键后，在窗口上能够显示对应的文字

工作逻辑：
键盘事件的使用逻辑：
判定键盘事件event.type == pygame.KEYDOWN → 判定按键 event.key == 按键名称


API：
1.event.type ==pygame.KEYDOWN
  event.type:表示pygame侦测到的事件机制
  pygame.KEYDOWN键盘按下事件
       在pygame.KEYDOWN事件下可以对按键进行判定：
           event.key 接收按下按键的常量名称
           event.mod 接收按下按键的修饰符组合值
           event.unicode 接收按下按键的unicode码
        示例：判定按键A是否按下 if event.key == K_a:

2.event.type ==pygame.KEYUP
  event.type:表示pygame侦测到的事件机制
  pygame.KEYUP键盘松开事件
       在pygame.KEYUP事件下可以对按键进行判定：
           event.key 接收松开按键的常量名称
           event.mod 接收松开按键的修饰符组合值
           event.unicode 接收松开按键的unicode码
        示例：判定按键A是否按下 if event.key == K_a:

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
pygame.display.set_caption("Keyboard Event")
font = pygame.font.Font("./font//SourceHanSansSC-Normal.otf", 40)   # 字体文件为思源黑体 开源字体

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                word_text("UP")
            elif event.key == pygame.K_DOWN:
                word_text("Down")
            elif event.key == pygame.K_LEFT:
                word_text("LEFT")
            elif event.key == pygame.K_RIGHT:
                word_text("RIGHT")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                word_text("UP off")
            elif event.key == pygame.K_DOWN:
                word_text("Down off")
            elif event.key == pygame.K_LEFT:
                word_text("LEFT off")
            elif event.key == pygame.K_RIGHT:
                word_text("RIGHT off")
            
    