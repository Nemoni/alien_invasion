import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard():
    def __init__(self, screen, ai_settings, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont("arial", 36)
        
        self.prep_score()
        self.prep_level()
        self.prep_high_score()
        self.prep_ships()
        
    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score:" + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
            self.ai_settings.bg_color)
            
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 5
        
    def prep_level(self):
        level_str = "Level:" + str(self.stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
            self.ai_settings.bg_color)
            
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = 40
        
    def prep_high_score(self):
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = "High score:" + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color,
            self.ai_settings.bg_color)
            
        self.hight_score_rect = self.high_score_image.get_rect()
        self.hight_score_rect.centerx = self.screen_rect.centerx
        self.hight_score_rect.top = 10
        
    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.screen, self.ai_settings)
            ship.change_image('images/display_ship.png')
            ship.rect.x = 5 + ship_number *ship.rect.width*1.1
            ship.rect.y = 5
            self.ships.add(ship)
        
    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.high_score_image, self.hight_score_rect)
        self.ships.draw(self.screen)
