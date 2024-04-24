import pygame as pg
import random
from entity import Entity
from health_bar import HealthBar
from fish import Fish
pg.init()
pg.font.init()
clock = pg.time.Clock()
run = True
screen = pg.display.set_mode((600, 600))
coin_fish_count = 0
red_fish_count = 0
screamer_fish_count = 0
font = pg.font.SysFont("None", 80)
shop_text = font.render(f"Free", False, 'white')
font2 = pg.font.SysFont("None", 30)
space_key = font2.render(f"Space, чтобы поймать рыбу", False, 'green')
walk_sound = pg.mixer.Sound("audio-editor-output.mp3")
shop_sfx = pg.mixer.Sound("buy.wav")
shop_sfx.set_volume(0.30)
background = pg.transform.scale(pg.image.load("tile_ground_between_mix.png").convert(), (150, 150))
background_mix = pg.transform.scale(pg.image.load("tile_ground_new.png").convert(), (150, 150))
background_mix2 = pg.transform.scale(pg.image.load("tile_ground_mix2_new.png").convert(), (150, 150))
water_much_background = pg.transform.scale(pg.image.load("much_Water.png").convert(), (350, 150))
background_Shop = pg.transform.scale(pg.image.load("tile_shop.png").convert(), (100, 50))
shop_menu = pg.transform.scale(pg.image.load("shop_menu.png").convert(), (150, 600))
fishing_menu = pg.transform.scale(pg.image.load("fishing_menu.png").convert(), (600, 100))
fishing_pole = pg.transform.scale(pg.image.load("Fish-rod.png").convert(), (100, 100))
fish_arrow = pg.transform.scale(pg.image.load("arrow_fish_menu.png").convert(), (50, 50))
fight_menu = pg.transform.scale(pg.image.load("fight.psd.png").convert(), (400, 50))
run_menu = pg.transform.scale(pg.image.load("run.psd.png").convert(), (400, 50))
screamer_fish = pg.transform.scale(pg.image.load(f"fishes/hostile/screamer.jpg").convert(), (50, 50))
shark_1 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 2.png"), (50, 50))
shark_2 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 3.png"), (50, 50))
shark_3 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 4.png"), (50, 50))
shark_4 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 5.png"), (50, 50))
shark_5 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 6.png"), (50, 50))
shark_6 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 7.png"), (50, 50))
shark_7 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 8.png"), (50, 50))
shark_8 = pg.transform.scale(pg.image.load(f"fishes/hostile/shark/Слой 9.png"), (50, 50))
shark_ = [shark_1, shark_2, shark_3, shark_4, shark_5, shark_6, shark_7, shark_8]
shark_fight_1 = pg.transform.scale(pg.image.load(f"animations/shark_fight_1.png"), (270, 250))
shark_fight_2 = pg.transform.scale(pg.image.load(f"animations/shark_fight_2.png"), (270, 250))
shark_fight_ = [shark_fight_1, shark_fight_2]
hero_fight_1 = pg.transform.scale(pg.image.load(f"animations/fight/hero/Слой 15.png"), (184, 208))
hero_fight_2 = pg.transform.scale(pg.image.load(f"animations/fight/hero/Слой 18.png"), (184, 208))
hero_fight_3 = pg.transform.scale(pg.image.load(f"animations/fight/hero/Слой 19.png"), (184, 208))
hero_fight_ = [hero_fight_1, hero_fight_2, hero_fight_3]
red_fish_1 = pg.transform.scale(pg.image.load(f"fishes/peaceful/red/red_fish_1.png"), (50, 50))
red_fish_2 = pg.transform.scale(pg.image.load(f"fishes/peaceful/red/red_fish_2.png"), (50, 50))
red_fish_3 = pg.transform.scale(pg.image.load(f"fishes/peaceful/red/red_fish_3.png"), (50, 50))
red_fish_4 = pg.transform.scale(pg.image.load(f"fishes/peaceful/red/red_fish_4.png"), (50, 50))
red_fish_ = [red_fish_1, red_fish_2, red_fish_3, red_fish_4]
coin_fish_1 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 1.png"), (50, 50))
coin_fish_2 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 2.png"), (50, 50))
coin_fish_3 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 3.png"), (50, 50))
coin_fish_4 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 4.png"), (50, 50))
coin_fish_5 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 5.png"), (50, 50))
coin_fish_6 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 6.png"), (50, 50))
coin_fish_7 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 7.png"), (50, 50))
coin_fish_8 = pg.transform.scale(pg.image.load(f"fishes/peaceful/coin/Слой 8.png"), (50, 50))
coin_fish_ = [coin_fish_1, coin_fish_2, coin_fish_3, coin_fish_4, coin_fish_5, coin_fish_6, coin_fish_7, coin_fish_8]
shop_rect = pg.Rect((250, 50, 350, 100))
shop_surf = pg.Surface((100, 20))
shop_rect = shop_surf.get_rect(topleft=(250, 40))
fishing_pole_rect = pg.Rect((0, 0, 50, 50))
fishing_point_surf = pg.Surface((50, 50))
fishing_point_rect = fishing_point_surf.get_rect(topleft=(290, 499))
fish_point_rect = pg.Rect((300, 400, 300, 450))
fish_point_surf = pg.Surface((50, 100))
fish_point_surf.fill('green')
fish_point_rect = fishing_point_surf.get_rect(topleft=(270, 300))
fight_rect = pg.Rect((200, 450, 250, 600))
fight_bg = pg.transform.scale(pg.image.load(f"fight background.png"), (600, 600))
fight_surf = pg.Surface((400, 50))
fight_rect = fight_surf.get_rect(topleft=(200, 450))
run_rect = pg.Rect((200, 600, 250, 700))
run_surf = pg.Surface((400, 50))
run_rect = run_surf.get_rect(topleft=(200, 500))
x = 300
y = 600 // 2
pg.display.update()
open_menu = False
fishing_pole_bought = True  # remove
fishing_state = True
fight_state = False
entity1 = Entity(x, y)
fish1 = Fish(-50, 350, red_fish_1, 1.5)
healthbar = HealthBar(300, 50, 100)
fish_point_color = 'green'
all_sprite = pg.sprite.Group(entity1, fish1, healthbar)
grass_tile1_rect = pg.surface.Surface((50, 50))
while run:
    entity1.stay_still()
    keys = pg.key.get_pressed()
    screen.fill('black')

    fish_list_1 = font2.render(f"Поймано: Красная рыба x{red_fish_count}", False, 'purple')
    fish_list_2 = font2.render(f"Монета x{coin_fish_count}", False, 'purple')
    fish_list_3 = font2.render(f"Секретная рыба x{screamer_fish_count}", False, 'purple')

    screen.blit(background, (0, 400))
    screen.blit(background, (150, 400))
    screen.blit(background, (300, 400))
    screen.blit(background, (450, 400))
    screen.blit(background_mix2, (0, 300))
    screen.blit(background_mix2, (0, 150))
    screen.blit(background_mix2, (0, 0))
    screen.blit(background_mix2, (150, 300))
    screen.blit(background_mix2, (150, 150))
    screen.blit(background_mix2, (150, 0))
    screen.blit(background_mix2, (300, 300))
    screen.blit(background_mix2, (300, 150))
    screen.blit(background_mix2, (300, 0))
    screen.blit(background_mix2, (450, 300))
    screen.blit(background_mix2, (450, 150))
    screen.blit(background_mix2, (450, 0))
    screen.blit(water_much_background, (0, 550))
    screen.blit(water_much_background, (350, 550))
    screen.blit(background_Shop, (250, 40))

    clock.tick(60)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_menu:
            if fishing_pole_rect.collidepoint(event.pos) and not fishing_pole_bought:
                print('Bought a Fishing pole!')
                fishing_pole_bought = True
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and fight_state:
            if fight_rect.collidepoint(event.pos):
                print('fight')
            if run_rect.collidepoint(event.pos):
                entity1.rect.x = 290
                entity1.rect.y = 399
                fish1.rect.x = -50
                fish1.rect.y = 350
                fight_state = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            fish_point_color = 'brown'
            pg.time.set_timer(pg.USEREVENT, 200)
        if event.type == pg.USEREVENT:
            fish_point_color = 'green'

    if keys[pg.K_w] and not fight_state:
        entity1.move_up()
    if keys[pg.K_s] and not fight_state:
        entity1.move_down()
    if keys[pg.K_d] and not fight_state:
        entity1.move_right()
    if keys[pg.K_a] and not fight_state:
        entity1.move_left()
    if keys[pg.K_LSHIFT] and not fight_state:
        screen.blit(fish_list_1, (50, 100))
        screen.blit(fish_list_2, (50, 120))
        if screamer_fish_count != 0:
            screen.blit(fish_list_3, (50, 140))
    if entity1.rect.y > 465:
        entity1.rect.y = 465
    if entity1.rect.y < 0:
        entity1.rect.y = 0
    if entity1.rect.x < 0:
        entity1.rect.x = 0
    if entity1.rect.x > 560:
        entity1.rect.x = 560

    if fish1.rect.x >= 620:
        fishing_state = False
        fish1.rect.x = -50

    if fish1.image == shark_1 or fish1.image == shark_2 or fish1.image == shark_3 or fish1.image == shark_4 or fish1.image == shark_5 or fish1.image == shark_6 or fish1.image == shark_7 or fish1.image == shark_8:
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 8
        fish1.image = shark_[frame_index]
        fish1.speed = 3

    if fish1.image == red_fish_1 or fish1.image == red_fish_2 or fish1.image == red_fish_3 or fish1.image == red_fish_4:
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 4
        fish1.image = red_fish_[frame_index]
        fish1.speed = 1.5

    if fish1.image == coin_fish_1 or fish1.image == coin_fish_2 or fish1.image == coin_fish_3 or fish1.image == coin_fish_4 or fish1.image == coin_fish_5 or fish1.image == coin_fish_6 or fish1.image == coin_fish_7 or fish1.image == coin_fish_8:
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 8
        fish1.image = coin_fish_[frame_index]
        fish1.speed = 2
    if fish1.image == screamer_fish:
        fish1.speed = 5
    if fish1.rect.y == -50:
        if random.randint(1, 4) == 1:
            fish1.image = red_fish_1
        if random.randint(1, 4) == 2:
            fish1.image = screamer_fish
        if random.randint(1, 4) == 3:
            fish1.image = coin_fish_1
        if random.randint(1, 4) == 4:
            fish1.image = shark_1
        fish1.rect.y = 320
        fish1.rect.x = -50
    if fishing_point_rect.colliderect(entity1):
        if fishing_pole_bought and fishing_state:
            screen.blit(fishing_menu, (0, 300))
            screen.blit(fish_arrow, (270, 390))
            screen.blit(fish_point_surf, (270, 300))
            fish_point_surf.fill(fish_point_color)
            screen.blit(space_key, (170, 450))
    if fish_point_rect.colliderect(fish1.rect):
        if fish_point_color == 'brown':
            fish1.rect.y = -50
            if fish1.image == red_fish_1 or fish1.image == red_fish_2 or fish1.image == red_fish_3 or fish1.image == red_fish_4:
                red_fish_count += 1
            if fish1.image == coin_fish_1 or fish1.image == coin_fish_2 or fish1.image == coin_fish_3 or fish1.image == coin_fish_4 or fish1.image == coin_fish_5 or fish1.image == coin_fish_6 or fish1.image == coin_fish_7 or fish1.image == coin_fish_8:
                coin_fish_count += 1
            if fish1.image == screamer_fish:
                screamer_fish_count += 1
            if fish1.image == shark_1 or fish1.image == shark_2 or fish1.image == shark_3 or fish1.image == shark_4 or fish1.image == shark_5 or fish1.image == shark_6 or fish1.image == shark_7 or fish1.image == shark_8:
                fight_state = True
    current_time = pg.time.get_ticks()
    frame_duration = 300
    frame_index = (current_time // frame_duration) % 2
    if frame_index == 1:
        fish1.fish_update()

    if fishing_point_rect.colliderect(entity1):
        pass
    else:
        fish1.rect.y = -50
    if not fishing_point_rect.colliderect(entity1) or not fight_state:
        fishing_state = True
    if shop_rect.colliderect(entity1):
        open_menu = True
    else:
        screen.blit(shop_text, (1000, 1000))
        open_menu = False

    if open_menu:
        screen.blit(shop_menu, (0, 0))
        if not fishing_pole_bought:
            screen.blit(fishing_pole, (25, 30))
            screen.blit(shop_text, (20, 130))
        else:
            screen.blit(fishing_pole, (1000, 1000))
            screen.blit(shop_text, (1000, 1000))
    if fight_state:
        fishing_state = False
        screen.blit(fight_bg, (0, 0))
        screen.blit(run_menu, (200, 500))
        screen.blit(fight_menu, (200, 450))
        entity1.rect.x = 0
        entity1.rect.y = 380
        current_time = pg.time.get_ticks()
        frame_duration_entity = 200
        frame_duration_fish = 500
        frame_index_entity = (current_time // frame_duration_entity) % 3
        frame_index_fish = (current_time // frame_duration_fish) % 2
        entity1.image = hero_fight_[frame_index_entity]
        fish1.image = shark_fight_[frame_index_fish]

        fish1.rect.x = 225
        fish1.rect.y = 50
    else:
        if fish1.image == shark_fight_1 or fish1.image == shark_fight_2:
            fish1.image = red_fish_1
        screen.blit(fight_bg, (1000, 1000))

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()
pg.quit()
