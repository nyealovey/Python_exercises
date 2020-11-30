import pygame
from Game_Aliens.game_stats import GameStats
from Game_Aliens.settings import Settings
from Game_Aliens.ship import Ship
import Game_Aliens.game_functions as gf
from pygame.sprite import Group
from Game_Aliens.button import Button
from Game_Aliens.scoreboard import Scoreboard


def run_gmae():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()

    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("雷电垃圾版本")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 创建一个外星人编组
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 创建 记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一个按钮 PLAY

    play_button = Button(ai_settings, screen, "Play")

    # 开始游戏的主循环
    while True:

        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens,
                        bullets)

        if stats.game_active:
            # 移动飞船
            ship.update()
            # 更新子弹
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets)

            # 更新外星人
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets)

        # 每次循环时都重绘屏幕,并让最近绘制的屏幕可见
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button)


run_gmae()
