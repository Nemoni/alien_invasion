import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, screen, ai_settings, ship, bullets):
    if event.key == pygame.K_LEFT:
        # 飞船向左移动
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        # 飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        # 添加一枚子弹
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        # 飞船停止向左移动
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        # 飞船停止向右移动
        ship.moving_right = False

def check_events(screen, ai_settings, ship, bullets):
    '''监视键盘和鼠标事件'''
    for event in pygame.event.get():
        # 关闭窗口事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键按下事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ai_settings, ship, bullets)
        # 按键放开事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def update_screen(screen, settings, ship, bullets):
    '''更新屏幕'''
    # 填充背景色
    screen.fill(settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 刷新屏幕
    pygame.display.flip()
