import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
import audio
import os

def check_keydown_events(event, screen, ai_settings, ship, bullets, stats):
    if event.key == pygame.K_LEFT:
        # 飞船向左移动
        ship.moving_left = True
    elif event.key == pygame.K_RIGHT:
        # 飞船向右移动
        ship.moving_right = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(bullets, screen, ai_settings, ship)
    elif event.key == pygame.K_q:
        write_high_score_to_file(stats)
        sys.exit()
            
def fire_bullet(bullets, screen, ai_settings, ship):
    audio.play_shoot()
    # 添加一枚子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ai_settings, ship)
        bullets.add(new_bullet)
        
def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        # 飞船停止向左移动
        ship.moving_left = False
    elif event.key == pygame.K_RIGHT:
        # 飞船停止向右移动
        ship.moving_right = False
        
def check_play_button(screen, ai_settings, stats, ship, bullets, aliens, play_button, sboard, mouse_x, mouse_y):
    button_click = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_click and not stats.game_active:
        ai_settings.init_dynamic_settings()
        stats.game_active = True;
        stats.reset_stats()
        bullets.empty()
        aliens.empty()
        sboard.prep_score()
        sboard.prep_ships()
        sboard.prep_level()
    
        create_fleet(screen, ai_settings, ship, aliens)
        ship.center_ship()
        
def check_events(screen, ai_settings, ship, bullets, aliens,play_button, stats, sboard):
    '''监视键盘和鼠标事件'''
    for event in pygame.event.get():
        # 关闭窗口事件
        if event.type == pygame.QUIT:
            write_high_score_to_file(stats)
            sys.exit()
        # 按键按下事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ai_settings, ship, bullets, stats)
        # 按键放开事件
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        # 鼠标点击事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, ai_settings, stats, ship, bullets, aliens, play_button, sboard, mouse_x, mouse_y)

def check_bullets_aliens_collisions(screen, ai_settings, ship, bullets, aliens, sboard, stats):
    # 子弹击中外星人则删除子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for coll_aliens in collisions.values():
            audio.play_hit_alien()
            stats.score += ai_settings.alien_points * len(coll_aliens)
            sboard.prep_score()
    # 屏幕上的外星人已被全部消灭
    if len(aliens) == 0:
        next_level(screen, ai_settings, ship, bullets, aliens, stats, sboard)
        
def update_bullets(screen, ai_settings, ship, bullets, aliens, sboard, stats):
    '''更新子弹位置，超出范围则删除'''
    bullets.update()
    # 子弹超出屏幕后删除
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullets_aliens_collisions(screen, ai_settings, ship, bullets, aliens, sboard, stats)
    
            
def get_number_liens_x(ai_settings, alien_width):
    '''计算一行可容纳的外星人数'''
    available_space_x = ai_settings.screen_width - alien_width*2
    number_aliens_x = int(available_space_x/(alien_width*2))
    return number_aliens_x
    
def get_number_row(ai_settings, alien_height, ship):
    '''计算屏幕可容纳多少行外星人'''
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship.rect.height
    number_aliens_row = int(available_space_y/(alien_height * 1.2))
    return number_aliens_row
    
def create_alien(screen, ai_settings, alien_number, alien_row, aliens):
    '''创建一个外星人并加入编组'''
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    alien.x = alien_width + alien_width * 2 * alien_number
    alien.y = alien_row * alien_height * 1.2 + 80
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)
        
def create_fleet(screen, ai_settings, ship, aliens):
    '''创建外星人舰队'''
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    number_aliens_x = get_number_liens_x(ai_settings, alien_width)
    number_aliens_row = get_number_row(ai_settings, alien_height, ship)
    
    for alien_row in range(number_aliens_row):
        for alien_number in range(number_aliens_x):
            create_alien(screen, ai_settings, alien_number, alien_row, aliens)

def fleet_change_direction(aliens, ai_settings):
    '''改变方向并下降一段距离'''
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def check_fleet_edges(aliens, ai_settings):
    '''检测是否到达边缘并处理'''
    for alien in aliens.sprites():
        if alien.check_edges():
            fleet_change_direction(aliens, ai_settings)
            break
    
def ship_hit(screen, ai_settings, aliens, bullets, ship, stats, sboard):
    aliens.empty()
    bullets.empty()
    # 飞船数减一并重新准备显示板
    stats.ships_left -= 1
    sboard.prep_ships()
    audio.play_dead()
    # 飞船方向初始化
    ai_settings.fleet_direction = 1
    if stats.ships_left > 0:
        next_life(screen, ai_settings, ship, aliens)
    else:
        game_over(stats, sboard)
    sleep(1)
    
def check_aliens_bottom(screen, ai_settings, aliens, bullets, ship, stats, sboard):
    '''外星人到达屏幕底端'''
    screen_rect = screen.get_rect()
    for alien in aliens:
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(screen, ai_settings, aliens, bullets, ship, stats, sboard)
            break
            
def update_aliens(screen, ai_settings, aliens, bullets, ship, stats, sboard):
    '''更新外星人舰队位置'''
    check_fleet_edges(aliens, ai_settings)
    aliens.update(ai_settings)
    # 外星人碰到飞船
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(screen, ai_settings, aliens, bullets, ship, stats, sboard)
    # 外星人到达屏幕底端
    check_aliens_bottom(screen, ai_settings, aliens, bullets, ship, stats, sboard)
    
def read_high_score_from_file(stats):
    filename = 'alien_invasion.txt'
    if os.path.isfile(filename):
        with open(filename) as file_object:
            contents = file_object.read()
            str_high_score = contents.strip()
            if str_high_score != '':
                stats.high_score = float(str_high_score)
    
def write_high_score_to_file(stats):
    filename = 'alien_invasion.txt'
    old_high_score = 0
    if os.path.isfile(filename):
        with open(filename) as file_object:
            contents = file_object.read()
            str_high_score = contents.strip()
            if str_high_score != '':
                old_high_score = float(str_high_score)
    if stats.score > old_high_score:
        with open(filename, 'w') as file_object:
            file_object.write(str(stats.score))

def update_screen(screen, settings, ship, bullets, aliens, play_button, stats, sboard):
    '''更新屏幕'''
    # 填充背景色
    screen.fill(settings.bg_color)
    # 绘制飞船
    ship.blitme()
    # 绘制子弹
    for bullet in bullets:
        bullet.draw_bullet()
    # 绘制外星人
    aliens.draw(screen)
    
    sboard.show_score()
    if stats.game_active == False:
        play_button.draw_button()

    # 刷新屏幕
    pygame.display.flip()
    
def game_over(stats, sboard):
    stats.game_active = False
    audio.play_gameover()
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sboard.prep_high_score()
        write_high_score_to_file(stats)
    
def next_life(screen, ai_settings, ship, aliens):
    create_fleet(screen, ai_settings, ship, aliens)
    ship.center_ship()
    
def next_level(screen, ai_settings, ship, bullets, aliens, stats, sboard):
    '''外星人被全部消灭，进入下一关'''
    bullets.empty()
    ai_settings.increase_speed()
    create_fleet(screen, ai_settings, ship, aliens)
    ship.center_ship()
    stats.level += 1
    sboard.prep_level() 
    audio.play_next_level()
    sleep(1)
    
