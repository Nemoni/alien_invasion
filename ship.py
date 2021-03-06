import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, screen, ai_settings):
        super().__init__()
        self.screen = screen
        # 获取图片对象
        self.image = pygame.image.load('images/ship.png')
        # 飞船位置
        self.rect = self.image.get_rect()
        # 屏幕位置
        self.screen_rect = screen.get_rect()
        # 飞船初始位置为屏幕底部居中
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.ai_settings = ai_settings
        # 带小数的飞船水平位置
        self.center = float(self.rect.centerx)
        # 飞船左右移动标记
        self.moving_left = False
        self.moving_right = False
        
    def change_image(self, image_url):
        self.image = pygame.image.load(image_url)
        self.rect = self.image.get_rect()
        
    def blitme(self):
        '''在指定位置绘制对象'''
        self.screen.blit(self.image, self.rect)
        
    def update(self):
        '''飞船左右移动'''
        if self.moving_left == True and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right == True and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
            
        self.rect.centerx = self.center
    def center_ship(self):
        self.center = self.screen_rect.centerx

        
