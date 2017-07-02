import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import audio

def run_game():
    # 初始化屏幕对象
    pygame.init()
    # 初始化音效
    pygame.init()
    pygame.mixer.init()
    # 初始化设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星入侵")
    # 初始化飞船
    ship = Ship(screen, ai_settings)
    
    bullets = Group()
    # 初始化外星人组
    aliens = Group()
    gf.create_fleet(screen, ai_settings, ship, aliens)
    # 飞船的统计信息
    stats = GameStats(ai_settings)
    gf.read_high_score_from_file(stats)
    # 显示板
    sboard = Scoreboard(screen, ai_settings, stats)
    
    play_button = Button(ai_settings, screen, "Play")
    audio.play_bg_music()
    # 游戏主循环
    while True:
        gf.check_events(screen, ai_settings, ship, bullets, aliens, play_button, stats, sboard)
        if stats.game_active == True:
            ship.update()
            # 更新子弹位置
            gf.update_bullets(screen, ai_settings, ship, bullets, aliens, sboard, stats)
            gf.update_aliens(screen, ai_settings, aliens, bullets, ship, stats, sboard)
        gf.update_screen(screen, ai_settings, ship, bullets, aliens, play_button, stats, sboard)

run_game()
