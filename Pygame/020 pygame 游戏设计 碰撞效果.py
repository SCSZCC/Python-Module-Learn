"""
程序概述：一个控制角色躲避障碍物的游戏 加入碰撞爆炸效果。


工作逻辑：
通过键盘控制角色移动，障碍物随机从上方掉落。障碍物碰撞到飞机后重置位置。



API：
1.pygame.key.set_repeat(delay, interval)                    
    控制重复响应持续按下按键的时间，就是可以按下按键后持续效应，而不是一次又一次的按
    delay和interval使用的单位是毫秒
    delay表示表示按键事件间的间隔，即多久触发一次按键
    interval表示发送两个事件之间的事件间隔


"""
import pygame
import sys
import random
import time

 
def status_check():                              # 实现小飞机在桌面边缘的检测，避免飞出窗口
    if plane_rect.bottom > 800:
        plane_rect.bottom = 800
    if plane_rect.top < 0:
        plane_rect.top = 0
    if plane_rect.left < 0:
        plane_rect.left = 0
    if plane_rect.right > 800:
        plane_rect.right = 800


def star_check(s):                              # 分别判定小星星是否碰撞到飞机或者位置已经到了屏幕的最下方，返回不同的数值。
    if s > 800:
        return 0
    if star_rect.colliderect(plane_rect):
        return 1

 
x = 400                                         # x、y用于控制飞机的位置
y = 800
s_x = random.randint(10,790)                    # s_x、s_y用于控制小星星的位置
s_y = 0
pygame.init()                                   # pygame进行初始化
pygame.key.set_repeat(10, 15)                   # 控制重复响应持续按下按键的时间，就是可以按下按键后持续响应，而不是一次又一次的按
size = (800,800)
pygame.display.set_caption("My First Game")
screen = pygame.display.set_mode(size)
screen.fill((0,0,0))
plane = pygame.image.load("./images//plane.png")   # 加载图片
star = pygame.image.load("./images//star.png")
explosion = pygame.image.load("./images//explosion.png")
exp = pygame.transform.scale(explosion, (120,120))   # 调整爆炸图的尺寸
exp_rect = exp.get_rect()                            # 生成矩形
plane_rect = plane.get_rect()
star_rect = star.get_rect()
myclock = pygame.time.Clock()
myclock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:      # 通过键盘按键调整x、y的值，从而实现对飞机的控制
            if event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10
            elif event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
    s_y += 10                                   # 通过循环自动增加s_y的值实现小星星的掉落
    screen.fill((0,0,0))
    plane_rect.midbottom = (x, y)
    status_check()                              # 判断飞机在窗口中的位置
    if star_check(s_y) == 0:                    # 判定返回值是否为0，若成立则将小星星回到屏幕上方
        s_x = random.randint(10,790)
        s_y = 0
    elif star_check(s_y) == 1:                  # 否则判定返回值是否为1，若成立屏幕显示爆炸图，并结束当前循环，结束游戏。
        exp_rect.center = (x, y)
        screen.blit(exp, exp_rect)
        pygame.display.update()
        time.sleep(10)
        break
    star_rect.center = (s_x,s_y)              
    screen.blit(star,star_rect)                 # 根据位置刷新屏幕
    screen.blit(plane,plane_rect)
    pygame.display.update()
    myclock.tick(60)                            # 设置刷新帧速率为60
   


