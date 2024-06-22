import time
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'       
#student_code_starts
import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# 加载背景图片
bg = pygame.image.load('pic/背景.png')
# 加载冰弹音效
sound_ice = pygame.mixer.Sound('music/玩家射击.wav')

# 加载瞄准器图片和矩形框
sight = pygame.image.load('pic/瞄准器.png')
sight_rect = sight.get_rect()

# 加载小火鸟朝右的图片，装进列表里
right = []
for i in range(10):
    right.append(pygame.image.load(f'pic/小鸟朝右{i}.png'))

# 获取小火鸟矩形框
bird_rect = right[0].get_rect()

# 创建循环变量
tag = 0

# 加载小火鸟冰冻图片
ice = pygame.image.load('pic/小鸟冰冻.png')

# 初始化小火鸟状态
status = 'fly'

# 主循环模块
while True:
    # 遍历事件队列
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # 鼠标按下事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound_ice.play()  # 播放冰弹音效
            if bird_rect.collidepoint(sight_rect.center):
                status = 'freeze'  # 修改状态为冰冻

    # 绘制背景
    screen.blit(bg, (0, 0))
    x = random.randint(0, 750)
    y = random.randint(0, 550)
    z = (x, y)
    # ———————————————————————————————————————————————————
    # 【你需要根据小火鸟状态，切换图片】
    if status == 'fly':
        screen.blit(right[tag % 10], bird_rect)
        tag += 1
    else:
        screen.blit(ice,bird_rect)
        time.sleep(0.1)
        bird_rect.center = z
        status = 'fly'

    # ---------------------------------------------------

    # 获取鼠标坐标
    pos = pygame.mouse.get_pos()
    # 移动瞄准器矩形框
    sight_rect.center = pos
    # 绘制瞄准器
    screen.blit(sight, sight_rect)

    clock.tick(40)  # 设置刷新率
    pygame.display.update()  # 重绘界面



#student_code_ends
