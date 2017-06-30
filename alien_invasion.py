import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # 初始化屏幕对象
    pygame.init()
    # 初始化设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星入侵")
    # 初始化飞船
    ship = Ship(screen, ai_settings)
    
    bullets = Group()
    
    # 游戏主循环
    while True:
        gf.check_events(screen, ai_settings, ship, bullets)
        ship.update()
        # 自动调用编组当中每个成员的update函数
        bullets.update()
        gf.update_screen(screen, ai_settings, ship, bullets)

        
run_game()
