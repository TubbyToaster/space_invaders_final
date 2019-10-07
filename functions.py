import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep
from explosion import Explode
from arch import Arch
import random


def load_high_Score_array(sb):
    hf = open(sb.high_score_file, "r")
    i = 0
    while True:
        line = hf.readline()
        if not line:
            break
        sb.high_score_array[i] = str(line.strip())
        i += 1
    hf.close()


def update_high_Score_array(sb, stats):
    for i in range(10):
        if int(sb.high_score_array[i]) < int(stats.score):
            temp = int(sb.high_score_array[i])
            sb.high_score_array[i] = int(stats.score)
            if sb.high_score_array[i] > temp:
                sb.high_score_array[i + 1] = temp
            break


def update_high_Score_file(sb):
    hf = open(sb.high_score_file, "w")
    for i in range(10):
        outstring = ""
        outstring += str(sb.high_score_array[i])
        outstring += "\n"
        hf.write(outstring)
    hf.close()


def display_high_scores(sb):
    for i in range(10):
        font1 = pygame.font.SysFont(None, 64)
        text_color1 = (150, 70, 70)
        rect4 = pygame.Rect(0, 0, sb.ai_settings.screen_width + 200, 170 + (i * 90))
        rect5 = pygame.Rect(0, 0, sb.ai_settings.screen_width - 200, 170 + (i * 90))
        _color1 = (0, 0, 0)
        msg_image2 = font1.render(str(sb.high_score_array[i]), True, text_color1, _color1)
        msg_image3 = font1.render(str(i + 1), True, text_color1, _color1)
        msg_image_rect2 = msg_image2.get_rect()
        msg_image_rect2.center = rect4.center
        sb.screen.blit(msg_image2, msg_image_rect2)
        msg_image_rect3 = msg_image3.get_rect()
        msg_image_rect3.center = rect5.center
        sb.screen.blit(msg_image3, msg_image_rect3)


def play_sound(snd):
    snd.play()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches):
    if stats.ships_left > 0:
        update_high_Score_array(sb, stats)
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        alien_bullets.empty()
        arches.empty()
        create_fleet(ai_settings, screen, ship, aliens, arches)
        ship.center_ship()
        sb.prep_ships()
        ai_settings.ufo_appear = random.randrange(100, 200)
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_events(ai_settings, screen, stats, sb, play_button, pause_button, high_score_button, reset_button,
                 back_button, ship,
                 aliens, bullets, arches):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y,
                              arches)
            check_reset_button(ai_settings, screen, stats, sb, reset_button, ship, aliens, bullets, mouse_x, mouse_y,
                               arches)
            check_pause_button(stats, pause_button, mouse_x, mouse_y)
            check_back_button(stats, back_button, mouse_x, mouse_y)
            check_highscore_button(stats, high_score_button, mouse_x, mouse_y, sb)


def check_highscore_button(stats, high_score_button, mouse_x, mouse_y, sb):
    update_high_Score_array(sb, stats)
    button_clicked = high_score_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.high_score_display:
        stats.high_score_display = True


def check_back_button(stats, back_button, mouse_x, mouse_y):
    button_clicked = back_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.high_score_display:
        stats.high_score_display = False


def check_pause_button(stats, pause_button, mouse_x, mouse_y):
    button_clicked = pause_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and stats.game_active:
        stats.game_active = False


def check_reset_button(ai_settings, screen, stats, sb, reset_button, ship, aliens, bullets, mouse_x, mouse_y, arches):
    button_clicked = reset_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        update_high_Score_array(sb, stats)
        stats.game_active = True
        stats.first_start = True
        ai_settings.initialize_dynamic_settings()
        stats.reset_stats()
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()
        aliens.empty()
        bullets.empty()
        arches.empty()
        create_fleet(ai_settings, screen, ship, aliens, arches)
        ship.center_ship()


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets, mouse_x, mouse_y, arches):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        stats.game_active = True
        if not stats.first_start:
            update_high_Score_array(sb, stats)
            stats.first_start = True
            ai_settings.initialize_dynamic_settings()
            # pygame.mouse.set_visible(False)
            stats.reset_stats()
            sb.prep_score()
            sb.prep_high_score()
            sb.prep_level()
            sb.prep_ships()
            aliens.empty()
            bullets.empty()
            arches.empty()
            create_fleet(ai_settings, screen, ship, aliens, arches)
            ship.center_ship()


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_allowed:
        pew = pygame.mixer.Sound('assets/pew.wav')
        pew.set_volume(.15)
        play_sound(pew)
        new_bullet = Bullet(ai_settings, screen, ship, "mine")
        bullets.add(new_bullet)


def alien_fire_bullet(ai_settings, screen, ship, alien_bullets, el):
    new_bullet = Bullet(ai_settings, screen, ship, "alien")
    new_bullet.rect.centerx = el.rect.centerx
    new_bullet.rect.top = el.rect.top
    new_bullet.rect1.centerx = el.rect.centerx
    new_bullet.rect1.top = el.rect.top
    new_bullet.y = float(el.rect.y)
    # new_bullet.rect1.x = float(el.rect.x)
    alien_bullets.add(new_bullet)


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, explosio, arches):
    bullets.update()
    alien_bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
            ai_settings.bullets_cur -= 1

    for bullet in alien_bullets.copy():
        if bullet.rect.bottom > 600:
            alien_bullets.remove(bullet)

    # collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, explosio, alien_bullets,
                                  arches)

    if len(aliens) == 0:
        bullets.empty()
        stats.level += 1
        ai_settings.alien_quick = 0
        sb.prep_level()
        ai_settings.level += 1
        ai_settings.ufo_appear = random.randrange(100, 200)
        create_fleet(ai_settings, screen, ship, aliens, arches)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets, explosio, alien_bullets,
                                  arches):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        ai_settings.bullets_cur -= 1
        for aliens in collisions.values():
            for el in aliens:
                oh = pygame.mixer.Sound('assets/alienexpl.wav')
                oh.set_volume(.25)
                play_sound(oh)
                stats.score += (el.value * ((stats.level - 1) + 1.2)) * len(aliens)
                ai_settings.alien_quick += 1
                sb.prep_score()
                exp = Explode(ai_settings, screen, "alien")
                explosio.add(exp)
                exp.rect.y = el.rect.y
                exp.x = el.x
                exp.rect.x = el.rect.x
                exp.score = int(el.value * ((stats.level - 1) + 1.2))
                exp.image = pygame.image.load('assets/alienexp1.bmp')
                exp.image0 = pygame.image.load('assets/alienexp1.bmp')
                exp.image1 = pygame.image.load('assets/alienexp1.bmp')
                exp.image2 = pygame.image.load('assets/alienexp2.bmp')
                exp.image3 = pygame.image.load('assets/alienexp3.bmp')
                exp.image4 = pygame.image.load('assets/alienexp4.bmp')

        check_high_score(stats, sb)

    collisions = pygame.sprite.spritecollide(ship, alien_bullets, True, False)

    if collisions:
        oh = pygame.mixer.Sound('assets/shipexplod.wav')
        oh.set_volume(.4)
        play_sound(oh)
        ship.struck = True

    collisions = pygame.sprite.groupcollide(bullets, arches, True, False)
    if collisions:
        for arch in collisions.values():
            for el in arch:
                el.image_index += 1
                el.screen.blit(el.image, el.rect)

    collisions = pygame.sprite.groupcollide(alien_bullets, arches, True, False)
    if collisions:
        for arch in collisions.values():
            for el in arch:
                el.image_index += 1
                el.screen.blit(el.image, el.rect)

    collisions = pygame.sprite.groupcollide(aliens, arches, False, True)
    if collisions:
        print("oh no!")

    if len(aliens) == 0:
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1
        sb.prep_level()
        create_fleet(ai_settings, screen, ship, aliens, arches)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_ufo(ai_settings, screen, aliens):
    alien = Alien(ai_settings, screen)
    alien.x = -50
    alien.rect.x = alien.x - 50
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * 1
    alien.image = pygame.image.load('assets/ufoalien2.bmp')
    alien.image1 = pygame.image.load('assets/ufoalien1.bmp')
    alien.image2 = pygame.image.load('assets/ufoalien2.bmp')
    alien.image_index = 1
    alien.type = "ufo"
    alien.value = (random.randrange(10, 30)) * 10
    aliens.add(alien)


def create_explosion(ai_settings, screen, explosio, type_):
    exp = Explode(ai_settings, screen)
    exp.type = type_
    explosio.add(exp)


def create_arches(ai_settings, screen, arches, ry, rx, xx, tp):
    arch = Arch(ai_settings, screen)
    arch.rect.y = ry
    arch.rect.x = rx
    arch.x = xx
    arches.add(arch)

    if tp == "l":
        arch.image1 = pygame.image.load('assets/arleft1.bmp')
        arch.image2 = pygame.image.load('assets/arleft2.bmp')
        arch.image3 = pygame.image.load('assets/arleft3.bmp')
    if tp == "r":
        arch.image1 = pygame.image.load('assets/armright1.bmp')
        arch.image2 = pygame.image.load('assets/armright2.bmp')
        arch.image3 = pygame.image.load('assets/armright3.bmp')
    if tp == "rd" or tp == "ld":
        arch.image1 = pygame.image.load('assets/arend1.bmp')
        arch.image2 = pygame.image.load('assets/arend2.bmp')
        arch.image3 = pygame.image.load('assets/arend3.bmp')


def create_alien(ai_settings, screen, aliens, alien_number, row_number, ind):
    if row_number != 6:
        alien = Alien(ai_settings, screen)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        if row_number == 0 or row_number == 1:
            alien.image = pygame.image.load('assets/tongalien2.bmp')
            alien.image1 = pygame.image.load('assets/tongalien1.bmp')
            alien.image2 = pygame.image.load('assets/tongalien2.bmp')
            alien.image_index = ind
            alien.type = "tong"
            alien.value = 100
        if row_number == 2 or row_number == 3:
            alien.image = pygame.image.load('assets/eyealien2.bmp')
            alien.image1 = pygame.image.load('assets/eyealien1.bmp')
            alien.image2 = pygame.image.load('assets/eyealien2.bmp')
            alien.image_index = ind
            alien.type = "eye"
            alien.value = 75
        if row_number == 4 or row_number == 5:
            alien.image_index = ind

        ai_settings.cur_aliens = len(aliens)
        aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens, arches):
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    create_arches(ai_settings, screen, arches, 500, 368, 400, "l")
    create_arches(ai_settings, screen, arches, 500, 400, 400, "m")
    create_arches(ai_settings, screen, arches, 500, 432, 400, "r")
    create_arches(ai_settings, screen, arches, 532, 368, 400, "ld")
    create_arches(ai_settings, screen, arches, 532, 432, 400, "rd")

    create_arches(ai_settings, screen, arches, 500, 368 - 250, 400, "l")
    create_arches(ai_settings, screen, arches, 500, 400 - 250, 400, "m")
    create_arches(ai_settings, screen, arches, 500, 432 - 250, 400, "r")
    create_arches(ai_settings, screen, arches, 532, 368 - 250, 400, "ld")
    create_arches(ai_settings, screen, arches, 532, 432 - 250, 400, "rd")

    create_arches(ai_settings, screen, arches, 500, 368 + 250, 400, "l")
    create_arches(ai_settings, screen, arches, 500, 400 + 250, 400, "m")
    create_arches(ai_settings, screen, arches, 500, 432 + 250, 400, "r")
    create_arches(ai_settings, screen, arches, 532, 368 + 250, 400, "ld")
    create_arches(ai_settings, screen, arches, 532, 432 + 250, 400, "rd")

    ind = 1
    create_ufo(ai_settings, screen, aliens)
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number, ind)
            ind += 1
            if ind > 2:
                ind = 1


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.type == "ufo" and alien.rect.right >= 800:
            aliens.remove(alien)
        if alien.check_edges() and alien.type != "ufo":
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.type != "ufo":
            alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches):
    check_fleet_edges(ai_settings, aliens)

    if ai_settings.get_frame() == 15:
        for alien in aliens:
            alien.image_up()
            alien.update_frame()
            # alien.rect = alien.image.get_rect()
            alien.blitme()

    aliens.update()

    tt = (len(aliens)) * 20
    ttt = tt  # round(5000*tt)
    for el in aliens:
        value = (random.randrange(1, ttt))
        if value == 1:
            alien_fire_bullet(ai_settings, screen, ship, alien_bullets, el)

    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
        ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches)

    check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches)


def check_aliens_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches)
            break


def check_high_score(stats, sb):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, play_button, pause_button,
                  high_score_button,
                  reset_button, back_button, explosio, arches):
    screen.fill(ai_settings.bg_color)
    sb.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for bullet in alien_bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    if ship.struck:
        ship.image_up()
        ship.update_frame()
        if ship.image_index == 10:
            ship.struck = False
            ship.image = ship.image_
            ship_hit(ai_settings, screen, stats, sb, ship, aliens, bullets, alien_bullets, arches)

    aliens.draw(screen)
    arches.draw(screen)

    for el in arches:
        el.blitme()
        el.update_frame()
        if el.image_index > 3:
            arches.remove(el)

    for exp in explosio:
        exp.image_up()
        exp.update_frame()
        if exp.image_index == 8 and exp.type == "alien":
            explosio.remove(exp)
        exp.blitme()
    ai_settings.update_frame()
    load_high_Score_array(sb)
    update_high_Score_array(sb, stats)
    update_high_Score_file(sb)

    if stats.game_active:
        pause_button.draw_button()
        song = 'assets/invade.wav'
        if len(aliens) > 40 and (stats.tempo == 1 or stats.tempo == 4):
            pygame.mixer.music.stop()
            song = 'assets/invade.wav'
            stats.tempo = 2
        if len(aliens) > 15 and len(aliens) < 30 and stats.tempo == 2:
            pygame.mixer.music.stop()
            song = 'assets/invade2.wav'
            stats.tempo = 3
        if len(aliens) < 15 and stats.tempo == 3:
            pygame.mixer.music.stop()
            song = 'assets/invade3.wav'
            stats.tempo = 4

        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(song)
            pygame.mixer.music.play(-1)

        # pygame.mixer.music(len(aliens) / ai_settings.cur_aliens)
        if ai_settings.ufo_appear > 0:
            ai_settings.ufo_appear -= 1

    if not stats.game_active:
        sb.draw_bk()
        pygame.mixer.music.stop()
        if not stats.high_score_display:
            sb.draw_title()
            play_button.draw_button()
            high_score_button.draw_button()
            if stats.first_start:
                reset_button.draw_button()
        if stats.high_score_display:
            back_button.draw_button()
            display_high_scores(sb)

    pygame.display.flip()
