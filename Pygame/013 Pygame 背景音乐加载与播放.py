"""
程序概述：实现Pygame窗口背景音乐的播放


工作逻辑：
背景音乐一般逻辑梳理
加载音乐文件mixer.music.load() → 播放音乐mixer.music.play()


API：
1.pygame.mixer.music.load(file)
  加载背景音乐文件
  file：填入字体文件的地址，使用方法与图片加载的方式相似，可以以绝对路径和相对路径的形式进行添加。     str


2.pygame.mixer.music.play(-1, 0.0)
  播放加载的背景音乐。
  第一个参数表示播放的次数。其中-1表示循环播放。           int
  第二个参数表示播放的开始时间。                           float
         
3.pygame.mixer.music.stop()
  停止背景音乐的播放


"""

import pygame
import sys
import time


pygame.init()
screen_size = (800,800)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Music Loader")
pygame.mixer.music.load("./sound//The.madpix.project_-_Wish_You_Were_Here.mp3")
font = pygame.font.Font("./font//SourceHanSansSC-Normal.otf", 40)   # 字体文件为思源黑体 开源字体
text = font.render("Wish You Were Here", True, (255,255,255))
text_rect = text.get_rect()
text_rect.centerx = 400
text_rect.centery = 400
screen.fill((0,0,0))
screen.blit(text, text_rect)
pygame.mixer.music.play(-1, 0.0)
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

