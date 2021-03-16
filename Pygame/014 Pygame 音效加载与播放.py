"""
程序概述：实现Pygame窗口音效文件的播放


工作逻辑：
背景音乐一般逻辑梳理
加载音乐文件mixer.Sound() → 播放音乐play()


API：
1.sound_1 = pygame.mixer.Sound(file)
  加载音效文件
  file：填入字体文件的地址，使用方法与图片加载的方式相似，可以以绝对路径和相对路径的形式进行添加。  str


2.sound_1.play()
  播放sound_1加载的音效

3.sound_1.stop()
  停止sound_1加载的音效播放

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
pygame.display.set_caption("Music Loader")
sound_1 = pygame.mixer.Sound("./sound//Technology Electronic Cell Phone Ring Beeps 01.wav")
sound_2 = pygame.mixer.Sound("./sound//Technology Electronic Cell Phone Ring Tone 03.wav")
font = pygame.font.Font("./font//SourceHanSansSC-Normal.otf", 40)   # 字体文件为思源黑体 开源字体

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    word_text("Ring Beeps")
    sound_1.play()
    time.sleep(2)
    word_text("Ring Tone")
    sound_2.play()
    time.sleep(2)

