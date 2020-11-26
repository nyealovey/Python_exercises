class Settings():
    """
    存储 进击的思聪 中所有设置的类
    """

    def __init__(self):

        """ 初始化游戏的静态设置 """
        # 屏幕设置
        self.screen_width = 600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船的移动速度因子
        self.ship_speed_factor = 1
        self.ship_limit = 3

        # 子弹设置

        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # 外星人设置

        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        # 定义外星人移动方向，1表示向右，-1 表示向左
        self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initalize_dynamic_settings()

        # 计分

        self.alien_points = 50
        self.score_scale = 1.5


    def initalize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""

        self.ship_speed_factor = 1
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5
        self.alien_points = 50

        # fleet_direction 为1标男士向右，为-1 表示向左
        self.fleet_direction = 1


    def increase_speed(self):
        """提高速度设置"""

        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.score_scale * self.alien_points)


