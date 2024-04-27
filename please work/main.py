import pygame as pg
import random
from entity import Entity
from fish import Fish

pg.init()
pg.font.init()
pg.mixer.init()
clock = pg.time.Clock()
run = True
screen = pg.display.set_mode((600, 600))
coin_fish_count = 10 + 15 + 19
red_fish_count = 1
screamer_fish_count = 0
gold_fish_count = 0
font = pg.font.SysFont("None", 35)
shop_text_fish_pole = font.render(f"Бесплатно", False, 'white')
shop_text_red_fish = font.render(f"Продать 1", False, 'white')
shop_text_fish_line = font.render(f"10 монет", False, 'white')
shop_text_fish_bait = font.render(f"15 монет", False, 'white')
shop_text_loot_magnet = font.render(f"20 монет", False, 'white')
font2 = pg.font.SysFont("None", 30)
space_key = font2.render(f"Space, чтобы поймать рыбу", False, 'green')
shop_sfx = pg.mixer.Sound("buy.wav")
shop_sfx.set_volume(0.30)
current_time = pg.time.get_ticks()
frame_duration_entity = 200
frame_duration_fish = 500
frame_index_entity = (current_time // frame_duration_entity) % 3
frame_index_fish = (current_time // frame_duration_fish) % 2

background = pg.transform.scale(pg.image.load("tile_ground_between_mix.png").convert(), (150, 150))
background_mix = pg.transform.scale(pg.image.load("tile_ground_new.png").convert(), (150, 150))
background_mix2 = pg.transform.scale(pg.image.load("tile_ground_mix2_new.png").convert(), (150, 150))
water_much_background = pg.transform.scale(pg.image.load("much_Water.png").convert(), (350, 150))
background_Shop = pg.transform.scale(pg.image.load("tile_shop.png").convert(), (100, 50))

shop_menu = pg.transform.scale(pg.image.load("shop_menu.png").convert(), (150, 600))
shop_red_fish = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_1.png"), (100, 100))
shop_fishing_line = pg.transform.scale(pg.image.load(f"fishing_line.png"), (100, 100))
shop_fish_bait = pg.transform.scale(pg.image.load(f"fish_bait.png"), (100, 100))
shop_loot_magnet = pg.transform.scale(pg.image.load(f"loot_magnet.png"), (100, 100))
fishing_menu = pg.transform.scale(pg.image.load("fishing_menu_new.png").convert(), (600, 100))
fishing_pole = pg.transform.scale(pg.image.load("Fish-rod.png").convert(), (100, 100))
fish_arrow = pg.transform.scale(pg.image.load("arrow_fish_menu.png").convert(), (50, 50))

screamer_fish = pg.transform.scale(pg.image.load(f"fishes/screamer.jpg").convert(), (50, 50))
red_fish_1 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_1.png"), (50, 50))
red_fish_2 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_2.png"), (50, 50))
red_fish_3 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_3.png"), (50, 50))
red_fish_4 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_4.png"), (50, 50))
red_fish_ = [red_fish_1, red_fish_2, red_fish_3, red_fish_4]

coin_fish_1 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 1.png"), (50, 50))
coin_fish_2 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 2.png"), (50, 50))
coin_fish_3 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 3.png"), (50, 50))
coin_fish_4 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 4.png"), (50, 50))
coin_fish_5 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 5.png"), (50, 50))
coin_fish_6 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 6.png"), (50, 50))
coin_fish_7 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 7.png"), (50, 50))
coin_fish_8 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 8.png"), (50, 50))
coin_fish_ = [coin_fish_1, coin_fish_2, coin_fish_3, coin_fish_4, coin_fish_5, coin_fish_6, coin_fish_7, coin_fish_8]

gold_fish = pg.transform.scale(pg.image.load(f"fishes/gold fish.png"), (50, 50))
shop_rect = pg.Rect((250, 50, 350, 100))
shop_surf = pg.Surface((100, 20))
shop_rect = shop_surf.get_rect(topleft=(250, 40))

fishing_pole_rect = pg.Rect((0, 0, 150, 150))
red_fish_shop_rect = pg.Rect((0, 150, 300, 150))
fish_line_shop_rect = pg.Rect((0, 300, 150, 400))
fish_bait_shop_rect = pg.Rect((0, 470, 150, 600))
loot_magnet_shop_rect = pg.Rect((0, 300, 150, 400))

fishing_point_surf = pg.Surface((50, 50))
fishing_point_rect = fishing_point_surf.get_rect(topleft=(290, 499))
fish_point_rect = pg.Rect((300, 400, 300, 450))
fish_point_surf = pg.Surface((50, 100))
fish_point_rect = fishing_point_surf.get_rect(topleft=(270, 300))
fight_rect = pg.Rect((200, 450, 250, 600))
fight_surf = pg.Surface((400, 50))
fight_rect = fight_surf.get_rect(topleft=(200, 450))
run_rect = pg.Rect((200, 600, 250, 700))
run_surf = pg.Surface((400, 50))
run_rect = run_surf.get_rect(topleft=(200, 500))
x = 300
y = 600 // 2
pg.display.update()
open_menu = False
fishing_pole_bought = False  # remove
fishing_line_bought = False
fish_bait_bought = False
loot_magnet_bought = True
fishing_state = True
entity1 = Entity(x, y)
fish1 = Fish(-50, 350, gold_fish, 1.5)

fish_point_color = 'green'
all_sprite = pg.sprite.Group(entity1, fish1)
grass_tile1_rect = pg.surface.Surface((50, 50))
while run:
    clock.tick(60)
    entity1.stay_still()
    keys = pg.key.get_pressed()
    screen.fill('black')
    fish_list_1 = font2.render(f"Красная рыба x{red_fish_count}", False, 'purple')
    fish_list_2 = font2.render(f"Монета x{coin_fish_count}", False, 'purple')
    fish_list_3 = font2.render(f"Секретная рыба x{screamer_fish_count}", False, 'purple')
    fish_list_4 = font2.render(f"Золотая Рыбка x{gold_fish_count}", False, 'purple')
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

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_menu:
            if fishing_pole_rect.collidepoint(event.pos) and not fishing_pole_bought:
                print('Удочка куплена!')
                fishing_pole_bought = True
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_menu:
            if fish_line_shop_rect.collidepoint(event.pos) and not fishing_line_bought and coin_fish_count >= 10:
                print('Улучшенная леска куплена!')
                fishing_line_bought = True
                coin_fish_count -= 10
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_menu:
            if fish_bait_shop_rect.collidepoint(event.pos) and not fish_bait_bought and coin_fish_count >= 15:
                print('Приманка куплена!')
                fish_bait_bought = True
                coin_fish_count -= 15
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_menu:
            if loot_magnet_shop_rect.collidepoint(event.pos) and not loot_magnet_bought and coin_fish_count >= 20:
                print('Магнит лута куплена!')
                loot_magnet_bought = True
                coin_fish_count -= 20
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_menu:
            if red_fish_shop_rect.collidepoint(event.pos) and not red_fish_count <= 0:
                print('Рыба продана!')
                red_fish_count -= 1
                coin_fish_count += 1
                shop_sfx.play()
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            fish_point_color = 'brown'
            pg.time.set_timer(pg.USEREVENT, 200)
        if event.type == pg.USEREVENT:
            fish_point_color = 'green'

    if keys[pg.K_w]:
        entity1.move_up()
    if keys[pg.K_s]:
        entity1.move_down()
    if keys[pg.K_d]:
        entity1.move_right()
    if keys[pg.K_a]:
        entity1.move_left()
    if keys[pg.K_LSHIFT] or keys[pg.K_TAB]:
        screen.blit(fish_list_1, (400, 50))
        screen.blit(fish_list_2, (400, 70))
        if screamer_fish_count != 0:
            screen.blit(fish_list_3, (400, 90))
        if gold_fish_count != 0:
            screen.blit(fish_list_4, (400, 110))
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
    current_time = pg.time.get_ticks()
    frame_duration = 300
    if fish1.image == red_fish_1 or fish1.image == red_fish_2 or fish1.image == red_fish_3 or fish1.image == red_fish_4:
        frame_index = (current_time // frame_duration) % 4
        fish1.image = red_fish_[frame_index]
        if fish_bait_bought:
            fish1.speed = 4
        else:
            fish1.speed = 2
    if fish1.image == coin_fish_1 or fish1.image == coin_fish_2 or fish1.image == coin_fish_3 or fish1.image == coin_fish_4 or fish1.image == coin_fish_5 or fish1.image == coin_fish_6 or fish1.image == coin_fish_7 or fish1.image == coin_fish_8:
        frame_index = (current_time // frame_duration) % 8
        fish1.image = coin_fish_[frame_index]
        if fish_bait_bought:
            fish1.speed = 5
        else:
            fish1.speed = 2.5
    if fish1.image == screamer_fish:
        if fish_bait_bought:
            fish1.speed = 6
        else:
            fish1.speed = 3
    if fish1.image == gold_fish:
        if fish_bait_bought:
            fish1.speed = 14
        else:
            fish1.speed = 7
    if fish1.rect.x == -50:
        if not loot_magnet_bought:
            if random.randint(1, 10) > 3:
                fish1.image = red_fish_1
            if random.randint(1, 10) < 2:
                fish1.image = screamer_fish
            if random.randint(1, 10) < 3:
                fish1.image = coin_fish_1
        else:
            if random.randint(1, 10) <= 2:
                fish1.image = red_fish_1
            elif random.randint(1, 10) <= 3:
                fish1.image = screamer_fish
            elif random.randint(1, 10) <= 4:
                fish1.image = coin_fish_1
            else:
                fish1.image = gold_fish
        fish1.rect.y = 320
        fish1.rect.x = -50
    if fishing_point_rect.colliderect(entity1):
        if fishing_pole_bought and fishing_state:
            screen.blit(fishing_menu, (0, 300))
            screen.blit(fish_arrow, (270, 390))
            screen.blit(fish_point_surf, (270, 300))
            fish_point_surf.fill(fish_point_color)
            screen.blit(space_key, (170, 450))
            current_time = pg.time.get_ticks()
            frame_duration = 300
            frame_index = (current_time // frame_duration) % 2
            if fish1.image == gold_fish and fishing_state:
                fish1.fish_update()
            elif frame_index == 1 and fishing_state:
                fish1.fish_update()


    else:
        fish1.rect.x = -50
    if fish_point_rect.colliderect(fish1.rect):
        if fish_point_color == 'brown':
            fish1.rect.x = -50
            if not fishing_line_bought:
                if random.randint(1, 2) == 2:
                    if fish1.image == red_fish_1 or fish1.image == red_fish_2 or fish1.image == red_fish_3 or fish1.image == red_fish_4:
                        red_fish_count += 1
                    if fish1.image == coin_fish_1 or fish1.image == coin_fish_2 or fish1.image == coin_fish_3 or fish1.image == coin_fish_4 or fish1.image == coin_fish_5 or fish1.image == coin_fish_6 or fish1.image == coin_fish_7 or fish1.image == coin_fish_8:
                        coin_fish_count += 1
                    if fish1.image == screamer_fish:
                        screamer_fish_count += 1
                    if fish1.image == gold_fish:
                        gold_fish_count += 1

                else:
                    print('Рыба сорвалась с лески!')
            else:
                if fish1.image == red_fish_1 or fish1.image == red_fish_2 or fish1.image == red_fish_3 or fish1.image == red_fish_4:
                    red_fish_count += 1
                if fish1.image == coin_fish_1 or fish1.image == coin_fish_2 or fish1.image == coin_fish_3 or fish1.image == coin_fish_4 or fish1.image == coin_fish_5 or fish1.image == coin_fish_6 or fish1.image == coin_fish_7 or fish1.image == coin_fish_8:
                    coin_fish_count += 1
                if fish1.image == screamer_fish:
                    screamer_fish_count += 1
                if fish1.image == gold_fish:
                    gold_fish_count += 1
    if not fishing_point_rect.colliderect(entity1):
        fishing_state = True
    if shop_rect.colliderect(entity1):
        open_menu = True
    else:
        screen.blit(shop_text_fish_pole, (1000, 1000))
        open_menu = False

    if open_menu:
        screen.blit(shop_menu, (0, 0))
        if not fish_bait_bought:
            screen.blit(shop_fish_bait, (30, 465))
            screen.blit(shop_text_fish_bait, (25, 560))
        if not fishing_line_bought:
            screen.blit(shop_fishing_line, (30, 350))
            screen.blit(shop_text_fish_line, (25, 440))
        else:
            if not loot_magnet_bought:
                screen.blit(shop_loot_magnet, (30, 350))
                screen.blit(shop_text_loot_magnet, (25, 440))
        if not fishing_pole_bought:
            screen.blit(fishing_pole, (23, 30))
            screen.blit(shop_text_fish_pole, (15, 130))
        if not red_fish_count <= 0:
            screen.blit(shop_red_fish, (20, 200))
            screen.blit(shop_text_red_fish, (20, 300))

        else:
            screen.blit(fishing_pole, (1000, 1000))
            screen.blit(shop_text_fish_pole, (1000, 1000))
    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()
pg.quit()
