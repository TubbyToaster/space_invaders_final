import pygame.font


class Button:

    def __init__(self, screen, msg, x_loc, y_loc, wid, heg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width, self.height = wid, heg
        self.button_color = (0, 100, 0)
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x_loc, y_loc)
        self.msg_image = None
        self.msg_image_rect = None
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
