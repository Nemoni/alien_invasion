import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = 10
        
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.ai_settings = ai_settings

    def check_edges(self):
        '''到达边缘则返回True，否则返回False'''
        screen_rect = self.screen.get_rect()
        if self.rect.left <= 0 or self.rect.right >= screen_rect.right:
            return True
        else:
            return False

        
    def update(self, ai_settings):
        '''更新置'''
        self.x += ai_settings.alien_speed_factor * ai_settings.fleet_direction
        self.rect.x = self.x
        
    #def blitme(self):
        #'''在指定位置绘制对象'''
        #self.screen.blit(self.image, self.rect)

