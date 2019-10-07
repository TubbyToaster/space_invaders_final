import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False
        self.moving_left = False
        self.image_index = 1
        self.image_cap = 10
        self.image_ = pygame.image.load('assets/ship.bmp')
        self.image0 = pygame.image.load('assets/shipex1.bmp')
        self.image1 = pygame.image.load('assets/shipex2.bmp')
        self.image2 = pygame.image.load('assets/shipex3.bmp')
        self.image3 = pygame.image.load('assets/shipex4.bmp')
        self.image4 = pygame.image.load('assets/shipex5.bmp')
        self.image5 = pygame.image.load('assets/shipex6.bmp')
        self.image6 = pygame.image.load('assets/shipex7.bmp')
        self.image7 = pygame.image.load('assets/shipex8.bmp')
        self.image8 = pygame.image.load('assets/shipex9.bmp')
        self.struck = False

    def update(self):
        if self.struck == False:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += self.ai_settings.ship_speed_factor
            if self.moving_left and self.rect.left > 0:
                self.center -= self.ai_settings.ship_speed_factor
            self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def image_up(self):
        self.image_index += .5
        if self.image_index > self.image_cap:
            self.image_index = 1

    def update_frame(self):
        if self.image_index == 0:
            self.image_index = self.image_
        if self.image_index == 1:
            self.image = self.image0
        elif self.image_index == 2:
            self.image = self.image1
        elif self.image_index == 3:
            self.image = self.image2
        elif self.image_index == 4:
            self.image = self.image3
        if self.image_index == 5:
            self.image = self.image4
        elif self.image_index == 6:
            self.image = self.image5
        elif self.image_index == 7:
            self.image = self.image6
        elif self.image_index == 8:
            self.image = self.image7
        elif self.image_index == 9:
            self.image = self.image8
