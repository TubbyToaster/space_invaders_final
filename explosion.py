import pygame
from pygame.sprite import Sprite


class Explode(Sprite):
    def __init__(self, ai_settings, screen, type_):
        super(Explode, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('assets/shipex1.bmp')
        self.image0 = pygame.image.load('assets/shipex1.bmp')
        self.image1 = pygame.image.load('assets/shipex2.bmp')
        self.image2 = pygame.image.load('assets/shipex3.bmp')
        self.image3 = pygame.image.load('assets/shipex4.bmp')
        self.image4 = pygame.image.load('assets/shipex5.bmp')
        self.image5 = pygame.image.load('assets/shipex6.bmp')
        self.image6 = pygame.image.load('assets/shipex7.bmp')
        self.image7 = pygame.image.load('assets/shipex8.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.image_index = 1
        self.image_cap = 5
        self.type = type_
        self.score = 0
        self.font = pygame.font.SysFont(None, 48)
        self.text = self.font.render(" ", True, (0, 128, 0))

    def __del__(self):
        self.type = "dead"

    def image_up(self):
        self.image_index += .5
        # if self.image_index > self.image_cap:
        # self.image_index = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_frame(self):
        if self.type == "alien":
            self.image4 = pygame.image.load('assets/nosprite.bmp')

        if self.image_index == 1:
            self.image = self.image0
        elif self.image_index == 2:
            self.image = self.image1
        elif self.image_index == 3:
            self.image = self.image2
        elif self.image_index == 4:
            self.image = self.image3
        elif self.image_index == 5:
            self.image = self.image4
        elif self.image_index == 6:
            self.image = self.image5
        elif self.image_index == 7:
            self.image = self.image6
        elif self.image_index == 8:
            self.image = self.image7

        if self.image_index > 4 and self.type == "alien":
            self.image = self.image4
            self.text = self.font.render(str(self.score), True, (100, 128, 0))
            self.screen.blit(self.text, self.rect)
