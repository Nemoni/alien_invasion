class Settings():

    def __init__(self):
        # 屏幕宽高
        self.screen_width = 1200
        self.screen_height = 800
        # 设置背景色
        self.bg_color = (255, 204, 255)
        # 飞船移动速度
        self.ship_speed_factor = 1.5
        # 设置子弹属性
        self.bullet_speed_factor = 1
        self.bullet_width = 6
        self.bullet_height = 18
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 30
        
