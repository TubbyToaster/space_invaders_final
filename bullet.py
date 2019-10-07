import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_settings, screen, ship, type_):
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        self.type_ = type_
        self.image = pygame.image.load('assets/alienexp4.bmp')
        self.rect1 = self.image.get_rect()
        self.rect1.y = self.rect1.height
        self.x = float(self.rect1.x)
        self.ship = ship

    def update(self):
        if self.type_ == "mine":
            self.y -= self.speed_factor
            self.rect.y = self.y
            self.rect1.y = self.y
        else:
            #self.y = float(self.rect1.y)
            self.y += self.speed_factor / 1.4
            self.rect.y = self.y
            self.rect1.y = self.y

    def draw_bullet(self):
        if self.type_ == "mine":
            pygame.draw.rect(self.screen, self.color, self.rect)
        else:
            #pygame.draw.rect(self.screen, self.color, self.rect)
            self.screen.blit(self.image, self.rect1)
