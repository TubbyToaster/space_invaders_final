import pygame.font
from pygame.sprite import Group
from player import Ship


class Scoreboard:
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        self.text_color = (70, 70, 70)
        self.score_image = None
        self.score_rect = None
        self.high_score_image = None
        self.high_score_rect = None
        self.level_image = None
        self.level_rect = None
        self.ships = None
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        self.high_score_back_screen_rect = pygame.Rect(0, 0, 800, 600)
        self.hsbk_color = (0, 0, 0)
        self.high_score_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.high_score_file = "highScores.txt"
        self.high_score_file_w = "highScores.txt"

    def prep_score(self):
        # score_str = str(self.stats.score)
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.bg_color)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.ai_settings.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)


    """
    def update_high_Score_array(self):
        high_score_file = open("highScores.txt", "r")
        high_score_file_w = open("highScores.txt", "w")
        for i in range(10):
            if self.stats.score > self.high_score_array[i]:
                temp = self.high_score_array[i]
                self.high_score_array[i] = self.stats.score
                self.high_score_array[i - 1] = temp
            elif self.high_score_array[i] == 0:
                self.high_score_array[i] = self.stats.score

                high_score_file_w.write(str(i) + "\n")

        high_score_file.close()
    """


    def draw_bk(self):
        self.screen.fill(self.hsbk_color, self.high_score_back_screen_rect)

    def draw_title(self):
        font1 = pygame.font.SysFont(None, 128)
        text_color1 = (150, 70, 70)
        rect = pygame.Rect(0, 0, 800, 170)
        _color = (0, 0, 0)

        recc = pygame.Rect(200, 400, 10, 10)
        image1 = pygame.image.load('assets/redalien1.bmp')
        self.screen.blit(image1, recc)
        text = self.font.render(str(60), True, (100, 128, 0))
        recc = pygame.Rect(200, 350, 10, 10)
        self.screen.blit(text, recc)

        recc = pygame.Rect(100, 400, 10, 10)
        image1 = pygame.image.load('assets/tongalien1.bmp')
        self.screen.blit(image1, recc)
        text = self.font.render(str(120), True, (100, 128, 0))
        recc = pygame.Rect(100-10, 350, 10, 10)
        self.screen.blit(text, recc)

        recc = pygame.Rect(600, 400, 10, 10)
        image1 = pygame.image.load('assets/eyealien1.bmp')
        self.screen.blit(image1, recc)
        text = self.font.render(str(90), True, (100, 128, 0))
        recc = pygame.Rect(600, 350, 10, 10)
        self.screen.blit(text, recc)

        recc = pygame.Rect(700, 400, 10, 10)
        image1 = pygame.image.load('assets/ufoalien1.bmp')
        self.screen.blit(image1, recc)
        text = self.font.render("???", True, (100, 128, 0))
        recc = pygame.Rect(700-10, 350, 10, 10)
        self.screen.blit(text, recc)

        msg_image = font1.render("Space Invaders", True, text_color1, _color)
        msg_image_rect = msg_image.get_rect()
        msg_image_rect.center = rect.center
        self.screen.blit(msg_image, msg_image_rect)
