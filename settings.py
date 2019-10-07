import random


class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (1, 0, 0)
        self.ship_speed_factor = 6
        self.bullet_speed_factor = 12
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 00, 0, 240
        self.bullets_allowed = 5
        self.bullets_cur = 0
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 8
        self.fleet_direction = 1
        self.ship_limit = 3
        self.speedup_scale = 1.5
        self.initialize_dynamic_settings()
        self.score_scale = 1.5
        self.high_score = 0
        self.alien_points = 0
        self.frame = 0
        self.frame_end = 20
        self.ufo_ex = 1
        self.ufo_appear = random.randrange(100, 200)
        self.alien_quick = 0
        self.level = 1
        self.cur_aliens = 1

    def update_frame(self):
        self.frame += 1
        if self.frame > self.frame_end:
            self.frame = 0

    def get_frame(self):
        return self.frame

    def initialize_dynamic_settings(self):
        self.ufo_ex = 1
        self.ufo_appear = random.randrange(100, 200)
        self.ship_speed_factor += 1
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 2.5
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        self.ufo_ex = 1
        self.ufo_appear = random.randrange(100, 200)
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
