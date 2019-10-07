import pygame
from pygame.sprite import Sprite


class Arch(Sprite):
    def __init__(self, ai_settings, screen):
        super(Arch, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('assets/armid1.bmp')
        self.image1 = pygame.image.load('assets/armid1.bmp')
        self.image2 = pygame.image.load('assets/armid2.bmp')
        self.image3 = pygame.image.load('assets/armid3.bmp')
        self.rect = self.image.get_rect()
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.image_index = 1


    def image_up(self):
        self.image_index += 1
        #if self.image_index > 2:
            #self.image_index = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_frame(self):
        if self.image_index == 1:
            self.image = self.image1
        elif self.image_index == 2:
            self.image = self.image2
        elif self.image_index == 3:
            self.image = self.image3
