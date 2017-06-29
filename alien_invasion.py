import sys
import pygame
from settings import Settings

def run_game():
    # 初始化屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("外星入侵")
        
    # 游戏主循环
    while True:
        
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        # 填充背景色
        screen.fill(ai_settings.bg_color)
        
        # 刷新屏幕
        pygame.display.flip()
        
run_game()
