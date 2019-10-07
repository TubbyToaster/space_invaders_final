class GameStats:
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.first_start = False
        self.game_active = False
        self.high_score_display = False
        self.high_score = 0
        self.ships_left = 3
        self.score = 0
        self.level = 1
        self.tempo = 1

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        self.high_score = 0
