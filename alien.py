import pygame
# from player import Ship
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('assets/redalien2.bmp')
        self.image1 = pygame.image.load('assets/redalien1.bmp')
        self.image2 = pygame.image.load('assets/redalien2.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.image_index = 1
        self.value = 50
        self.type = "red"

    def __del__(self):
        self.type = "dead"

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def image_up(self):
        self.image_index += 1
        if self.image_index > 2:
            self.image_index = 1

    def update(self):

        if self.type != "ufo":
            self.x += (((.001 * self.ai_settings.alien_quick) + (self.ai_settings.level * 1.3) +
                        self.ai_settings.alien_speed_factor) * self.ai_settings.fleet_direction)
            self.rect.x = self.x
        if self.type == "ufo" and self.ai_settings.ufo_appear == 0:
            self.x += (self.ai_settings.alien_speed_factor / 2 * 1)
            self.rect.x = self.x

    def blitme(self):
        if self.type != "ufo":
            self.screen.blit(self.image, self.rect)

    def update_frame(self):
        if self.image_index == 1:
            self.image = self.image2
        elif self.image_index == 2:
            self.image = self.image1
