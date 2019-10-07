import pygame
from pygame.sprite import Group
from settings import Settings
from player import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard
import functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    play_button = Button(screen, "Play", ai_settings.screen_width / 2, 300, 200, 50)
    reset_button = Button(screen, "Reset", ai_settings.screen_width / 2, 400, 200, 50)
    high_score_button = Button(screen, "High Score", ai_settings.screen_width / 2, 500, 200, 50)
    pause_button = Button(screen, "Pause", 160, 30, 100, 40)
    back_button = Button(screen, "Back", 160, 30, 100, 40)
    ship = Ship(ai_settings, screen)
    Alien(ai_settings, screen)
    bullets = Group()
    alien_bullets = Group()
    arches = Group()
    # Explode(ai_settings, screen)
    explosio = Group()
    aliens = Group()  # Alien(ai_settings, screen)
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens, arches)


    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, pause_button, high_score_button, reset_button,
                        back_button, ship, aliens, bullets, arches)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, explosio, arches)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, play_button,
                         pause_button,
                         high_score_button, reset_button, back_button, explosio, arches)


run_game()
