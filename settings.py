class Settings():

    def __init__(self):
        # 屏幕宽高
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色
        self.bg_color = (255, 204, 255)
        # 飞船移动速度
        self.ships_limit = 3
        # 设置子弹属性
        self.bullet_width = 1200
        self.bullet_height = 18
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        # 设置外星人属性
        self.fleet_drop_speed = 100
        # 设置速度提升率
        self.speedup_scale = 1.1
        self.points_raise_scale = 1.5
        
    def init_dynamic_settings(self):
        self.bullet_speed_factor = 1
        self.ship_speed_factor = 1.5
        self.alien_speed_factor = 1
        self.alien_points = 1.5
        
        self.fleet_direction = 1
        
    def increase_speed(self):
        '''提升速度'''
        self.bullet_speed_factor *= self.speedup_scale
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points *= self.points_raise_scale
