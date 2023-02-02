import pygame
import random

pygame.init()
best_score = 0
music = pygame.mixer.Sound("game_music.mp3")
lose_music = pygame.mixer.Sound("lose.mp3")
hero_images = [pygame.transform.scale(pygame.image.load('hero1.png'), (76, 120)),
               pygame.transform.scale(pygame.image.load('hero3.png'), (76, 120))]
stars = []


def start_screen():
    global best_score

    s = pygame.mixer.Sound("start_screen.mp3")
    s.play()

    size = 1920, 1080

    screen = pygame.display.set_mode(size)
    font = pygame.font.Font('retro-land-mayhem.ttf', 80)
    fon = pygame.image.load('fon.jpg')
    screen.blit(fon, (0, 0))
    floor = pygame.transform.scale(pygame.image.load('floor.jpg'), (1920, 455))
    screen.blit(floor, (0, 760))

    hero = pygame.transform.scale(pygame.image.load('hero1.png'), (76, 120))
    hero_rect = hero.get_rect(midbottom=(400, 760)).inflate(5, 5)

    rum = pygame.transform.scale(pygame.image.load('rum.png'), (30, 70))
    rum_rect = rum.get_rect(midbottom=(500, 760))

    screen.blit(hero, hero_rect)
    screen.blit(rum, rum_rect)

    text_1 = font.render(f"""Welcome to""", False, 'white')
    text_2 = font.render(f"""The Search of Jack Sparrow's Rum!""", False, 'white')
    text_3 = font.render(f"""Press "Space" to start""", False, 'white')

    screen.blit(text_1, (700, 100))
    screen.blit(text_2, (100, 220))
    screen.blit(text_3, (440, 340))

    for i in range(40):
        star = pygame.image.load('star.png')
        stars.append([star, star.get_rect(midbottom=(random.randint(30, 1900), random.randint(30, 500)))])
    for star, rect in stars:
        screen.blit(star, rect)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                s.stop()
                new_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if hero_rect.collidepoint(event.pos):
                    captain_jack_sparrow = pygame.mixer.Sound("captain_jack_sparrow_quote.mp3")
                    captain_jack_sparrow.play()
        pygame.display.update()
    pygame.quit()


def new_game():
    global best_score

    lose_music.stop()
    pygame.init()
    music.play()
    game_continue = True

    score = 0
    run_counter = 0
    lose_counter = 0
    parrot_counter = 0
    rum_counter = 0
    size = 1920, 1080
    screen = pygame.display.set_mode(size)
    fps = 60

    font = pygame.font.Font('retro-land-mayhem.ttf', 50)
    clock = pygame.time.Clock()
    fon = pygame.image.load('fon.jpg')
    floor = pygame.transform.scale(pygame.image.load('floor.jpg'), (1920, 455))

    parrot = pygame.transform.scale(pygame.image.load('parrot.png'), (150, 150))
    parrot_rect = parrot.get_rect(midbottom=(8000, 1050))

    coins = pygame.transform.scale(pygame.image.load('coins.png'), (140, 160))
    coins_rect = coins.get_rect(midbottom=(1800, 1050))

    rope = pygame.transform.scale(pygame.image.load('rope.png'), (160, 160))
    rope_rect = rope.get_rect(midbottom=(2500, 1020))

    barrel = pygame.transform.scale(pygame.image.load('barrel_2.png'), (200, 200))
    barrel_rect = barrel.get_rect(midbottom=(1600, 1050))

    octopus = pygame.transform.scale(pygame.image.load('oct.png'), (120, 115))
    oct_rect = octopus.get_rect(midbottom=(3000, 760)).inflate(0, 0)

    rum = pygame.transform.scale(pygame.image.load('rum.png'), (30, 70))
    rum_rect = rum.get_rect(midbottom=(260, 80))
    score_rum_rect = rum.get_rect(midbottom=(2500, 760)).inflate(0, 0)

    enemy_pirate = pygame.transform.scale(pygame.image.load('enemy_pirate.png'), (76, 125))
    enemy_pirate_rect = enemy_pirate.get_rect(midbottom=(10000, 760)).inflate(0, 0)

    hero = pygame.transform.scale(pygame.image.load('hero1.png'), (76, 120))
    hero_rect = hero.get_rect(midbottom=(400, 760)).inflate(0, 0)

    jumping_music = pygame.mixer.Sound("jump.mp3")
    jumping_music.play()
    hero_gravity = -25

    text = font.render(f'Score: {score}', False, 'white')

    running = True
    while running:

        if score % 5100 == 0:
            parrot_counter = 0
            music.stop()
            music.play()

        if score % 40 == 0:
            run_counter += 1

        if run_counter == 2:
            run_counter = 0

        text_score = font.render(f'Score: {score}', False, 'white')
        text_best_score = font.render(f'Your best: {best_score}', False, 'white')
        rum_counter_text = font.render(f'Rum: {rum_counter}', False, 'white')

        if hero_rect.bottom > 760:
            hero_rect.bottom = 760

        if score_rum_rect.left <= -100:
            score_rum_rect.left += random.randint(3000, 3500)
            if score_rum_rect.colliderect(enemy_pirate_rect) or score_rum_rect.colliderect(oct_rect):
                score_rum_rect.left += random.randint(3000, 3500)

        if oct_rect.left <= -100:
            oct_rect.left += random.randint(2000, 3000)
            if not oct_rect.colliderect(enemy_pirate_rect) and not oct_rect.colliderect(score_rum_rect):
                oct_rect.left += random.randint(2000, 3000)

        if enemy_pirate_rect.left <= -100:
            enemy_pirate_rect.left += random.randint(5000, 6500)
            if not enemy_pirate_rect.colliderect(oct_rect) and not enemy_pirate_rect.colliderect(score_rum_rect):
                enemy_pirate_rect.left += random.randint(5000, 6500)

        if barrel_rect.left <= -100:
            barrel_rect.left += random.randint(7000, 7800)
            if not barrel_rect.colliderect(parrot_rect) and not barrel_rect.colliderect(coins_rect):
                barrel_rect.left += random.randint(7000, 7800)

        if coins_rect.left <= -100:
            coins_rect.left += random.randint(8500, 10000)
            if not coins_rect.colliderect(parrot_rect) and not coins_rect.colliderect(barrel_rect):
                coins_rect.left += random.randint(8500, 10000)

        if rope_rect.left <= -100:
            rope_rect.left += random.randint(12000, 14000)
            if not rope_rect.colliderect(parrot_rect) and not rope_rect.colliderect(coins_rect):
                rope_rect.left += random.randint(12000, 14000)

        if parrot_rect.left <= -100:
            parrot_rect.left += random.randint(17000, 17500)
            if not parrot_rect.colliderect(barrel_rect) and not parrot_rect.colliderect(coins_rect):
                parrot_rect.left += random.randint(17000, 17500)

        for star, rect in stars:
            if rect.left <= -100:
                rect.left += 2200

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_continue:
                if event.type == pygame.KEYDOWN and hero_rect.bottom == 760 and event.key == pygame.K_SPACE:
                    hero_gravity = -25
                    jumping_music = pygame.mixer.Sound("jump.mp3")
                    jumping_music.play()

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    new_game()

        if game_continue:
            screen.fill('black')
            screen.blit(fon, (0, 0))
            screen.blit(floor, (0, 760))

            screen.blit(text_score, (1300, 10))
            screen.blit(text_best_score, (1300, 70))
            screen.blit(rum_counter_text, (10, 24))

            screen.blit(octopus, oct_rect)

            screen.blit(barrel, barrel_rect)
            screen.blit(coins, coins_rect)
            screen.blit(rope, rope_rect)
            screen.blit(parrot, parrot_rect)
            screen.blit(enemy_pirate, enemy_pirate_rect)
            screen.blit(rum, rum_rect)
            screen.blit(rum, score_rum_rect)

            if hero_rect.bottom == 760:
                screen.blit(hero_images[run_counter], hero_rect)
            else:
                screen.blit(pygame.transform.scale(pygame.image.load('hero2.png'), (76, 120)), hero_rect)

            for elem in stars:
                screen.blit(elem[0], elem[1])

            hero_gravity += 1
            hero_rect.bottom += hero_gravity

            if hero_rect.bottom > 760:
                hero_rect.bottom = 760

            oct_rect.left -= 10
            enemy_pirate_rect.left -= 12
            barrel_rect.left -= 7
            coins_rect.left -= 7
            rope_rect.left -= 7
            parrot_rect.left -= 7
            score_rum_rect.left -= 7
            hero_rect.left += 1
            hero_rect.left -= 1

            for rect in stars:
                rect[1].left -= 7

            if parrot_rect.x <= 1920:
                parrot_counter += 1
                if parrot_counter == 1:
                    parrot_sound = pygame.mixer.Sound("parrot_sound.mp3")
                    parrot_sound.play(1)

            if hero_rect.colliderect(score_rum_rect):
                rum_collecting_sound = pygame.mixer.Sound("rum_sound.mp3")
                rum_collecting_sound.play()
                rum_counter += 1
                score_rum_rect.left += random.randint(4000, 4500)

            if hero_rect.colliderect(oct_rect) or hero_rect.colliderect(enemy_pirate_rect):
                game_continue = False

            score += 1

        else:
            hero = pygame.transform.scale(pygame.image.load('hero4.png'), (120, 76))
            hero_rect = hero.get_rect(midbottom=(400, 760))
            hero_rect.bottom = 760

            lose_counter += 1

            if score > best_score:
                best_score = score

            music.stop()
            if lose_counter == 1:
                lose_music.play(1)

            screen.blit(text, (770, 305))
            screen.fill('black')
            screen.blit(fon, (0, 0))
            screen.blit(floor, (0, 760))
            screen.blit(hero, hero_rect)

            lose_message_1 = font.render(f'You lost', False, 'white')
            lose_message_2 = font.render(f'Your score: {score}', False, 'white')
            lose_message_3 = font.render(f'Your best: {best_score}', False, 'white')
            lose_message_4 = font.render(f'Press "R" to restart', False, 'white')

            screen.blit(lose_message_1, (770, 100))
            screen.blit(lose_message_2, (640, 190))
            screen.blit(lose_message_3, (640, 280))
            screen.blit(lose_message_4, (550, 370))

        pygame.display.update()
        pygame.display.flip()
        clock.tick(fps)
    pygame.quit()


start_screen()
