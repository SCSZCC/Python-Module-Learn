"""
程序概述：一个控制角色躲避障碍物的游戏 加入碰撞爆炸效果。


工作逻辑：
通过键盘控制角色移动，障碍物随机从上方掉落。障碍物碰撞到飞机后重置位置。



API：
1.Star(pygame.sprite.Sprite)
  定义一个叫做Star的pygame精灵类，并继承自pygame.sprite.Sprite
  super().__init__() 初始化方法继承父类的方法
  主要定义初始化方法与update方法
  初始化方法主要进行图形文件的加载与rect的生成
  update方法主要定义图像的“动作”及画面刷新

2.group = pygame.sprite.Group(sprite)
  精灵组可以将通过精灵类，如Star类创建的对象添加到精灵组当中。
  通过group.draw()、group.update()的方式对角色精灵统一的处理。


"""
import pygame
import sys
import random
import time

class Star(pygame.sprite.Sprite):                               # 创建精灵类Star，继承自pygame.sprite.Sprite
    def __init__(self):                                         # 定义初始化方法
        super().__init__()                                      # 继承父类的初始化方法
        self.image = pygame.image.load("./images//star.png")    
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(10, 790)
        self.rect.bottom = 0
        self.speed = random.randint(3, 10)

    def update(self, *args):
        self.rect.bottom += self.speed
        if self.rect.top > 800:
            self.rect.bottom = 0
            self.speed = random.randint(3, 10)
            self.rect.centerx = random.randint(10, 790)
        if self.rect.colliderect(plane_rect):
            exp_rect.center = self.rect.center
            screen.blit(exp, exp_rect)
            pygame.mixer.music.stop()               # 停止背景音乐的播放 
            sound_1.play()                          # 播放碰撞后爆炸音效
            pygame.display.update()
            time.sleep(10)
        

 
def status_check():                              # 实现小飞机在桌面边缘的检测，避免飞出窗口
    if plane_rect.bottom > 800:
        plane_rect.bottom = 800
    if plane_rect.top < 0:
        plane_rect.top = 0
    if plane_rect.left < 0:
        plane_rect.left = 0
    if plane_rect.right > 800:
        plane_rect.right = 800


 
x = 400                                         # x、y用于控制飞机的位置
y = 800
pygame.init()                                   # pygame进行初始化
pygame.key.set_repeat(10, 15)                   # 控制重复响应持续按下按键的时间，就是可以按下按键后持续响应，而不是一次又一次的按
size = (800,800)
pygame.display.set_caption("My First Game")
screen = pygame.display.set_mode(size)
screen.fill((0,0,0))
plane = pygame.image.load("./images//plane.png")     # 加载图片
explosion = pygame.image.load("./images//explosion.png")
pygame.mixer.music.load("./sound//The.madpix.project_-_Wish_You_Were_Here.mp3")   # 加载背景音乐
sound_1 = pygame.mixer.Sound("./sound//boom.wav")    # 加载音效
exp = pygame.transform.scale(explosion, (120,120))   # 调整爆炸图的尺寸
exp_rect = exp.get_rect()                            # 生成矩形
myclock = pygame.time.Clock()
myclock.tick(60)
pygame.mixer.music.play(-1, 0.0)
star_list = []                                      # 创建空列表
for i in range(1, 10):                              # 通过for循环，使用Star类创建多个对象，并将对象存放于列表当中
    i = Star()
    star_list.append(i)

start_group = pygame.sprite.Group(star_list)        # 使用列表当中的对象用于创建精灵组。
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:      # 通过键盘按键调整x、y的值，从而实现对飞机的控制
            if event.key == pygame.K_UP:
                y -= 8
            elif event.key == pygame.K_DOWN:
                y += 8
            elif event.key == pygame.K_LEFT:
                x -= 8
            elif event.key == pygame.K_RIGHT:
                x += 8
    screen.fill((0,0,0))
    plane_rect.midbottom = (x, y)
    status_check()                              # 判断飞机在窗口中的位置
    start_group.update()                        # 调用精灵组update方法,作用就像display.update()
    start_group.draw(screen)                    # 绘制screen的窗口上
    screen.blit(plane,plane_rect)              
    pygame.display.update()
    myclock.tick(60)                            # 设置刷新帧速率为60
   