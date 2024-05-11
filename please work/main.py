import pygame as pg
import random
from entity import Entity
from fish import Fish
from progress_bar import HealthBar

pg.init()
pg.font.init()
pg.mixer.init()
clock = pg.time.Clock()
run = True
screen = pg.display.set_mode((600, 600))

coin_fish_count = 0
red_fish_count = 0

total_red_fish_count = 25
total_gold_fish_count = 25
total_clam_count = 25
clam_count = 1
pearl_count = 1
gold_fish_count = 0

mission_red_count = 15
mission_gold_fish_count = 15
mission_clam_count = 15

lava_fish_count = 0
obsidian_fish_count = 0
lava_jellyfish_count = 0
font3 = pg.font.SysFont("None", 50)
game_over_text = font3.render(f"Вы прошли игру,", False, 'white')
game_over_text2 = font3.render(f"Поздравляем!", False, 'white')
font = pg.font.SysFont("None", 35)

endless_game = font.render(f"(Бесконечная игра)", False, 'white')

shop_text_fish_pole = font.render(f"Бесплатно", False, 'white')

shop_text_pearl = font.render(f"5 монет за 1", False, 'white')
skip_tutorial = font.render(f"Esc + Space, чтобы пропустить туториал", False, 'white')

work_bench_text1 = font.render(f"Верстак", False, 'white')
work_bench_text2 = font.render(f"Верстак", False, 'black')

missions_text1 = font.render(f"Миссии", False, 'white')
missions_text2 = font.render(f"Мисcии", False, 'black')

shop_text_fish_line = font.render(f"10 монет", False, 'white')
work_bench_ring_text2 = font.render(f"5 монет", False, 'white')
shop_text_red_fish = font.render(f"Продать 1", False, 'white')
font2 = pg.font.SysFont("None", 30)

mission_text1 = font2.render(f"Не готово", False, 'white')
mission_text2 = font2.render(f"Готово", False, 'white')
mission_text_max = font2.render(f"Макс.", False, 'white')

fish_bait_text = font2.render(f"Рыба двигается быстрее", False, 'white')
fish_pole_text = font2.render(f"Позволяет рыбачить", False, 'white')
fish_line_text = font2.render(f"Рыба больше не уплывает", False, 'white')
loot_magnet_text = font2.render(f"Притягвает редких рыб", False, 'white')

discount_card_text = font2.render(f"Всё в магазине 50% дешевле", False, 'white')
ring_text = font2.render(f"Рыбы стали в 5 раз прибыльнее", False, 'white')
lucky_coin_ring_text = font2.render(f"Вы становитесь самым богатым и открываете миссии", False, 'white')

work_bench_discount_card_text1 = font2.render(f"1 Жемчужина", False, 'white')
work_bench_ring_text1 = font2.render(f"10 Жемчужин", False, 'white')
work_bench_coin_ring_text1 = font2.render(f"20 Жемчужин", False, 'white')
work_bench_lucky_coin_ring_text1 = font2.render(f"50 Жемчужин", False, 'white')
work_bench_coin_ring_text2 = font2.render(f"15 Золотых", False, 'white')
work_bench_coin_ring_text3 = font2.render(f"рыб", False, 'white')

space_key_tutorial = font2.render(f"Space, чтобы поймать рыбу", False, 'green')
wasd_key_tutorial = font2.render(f"W A S D, чтобы ходить", False, 'black')
tab_lshift_key_tutorial = font2.render(f"Tab или L_SHIFT, чтобы посмотреть свой улов", False, 'black')
shop_tutorial_1 = font2.render(f"Подойди к магазину", False, 'black')
shop_tutorial_2 = font2.render(f"Кликни на товар, чтобы купить", False, 'black')
shop_tutorial_3 = font2.render(f"Когда закончишь, можeшь отходить", False, 'black')
fish_tutorial_1 = font2.render(f"Подойди к скале", False, 'black')
fish_tutorial_2 = font2.render(f"Нажми Space, чтобы поймать рыбу, ", False, 'black')
fish_tutorial_2_1 = font2.render(f"когда она находится в зелёновом квадрате ", False, 'black')
fish_tutorial_3 = font2.render(f"Пока ты не купил хорошую леску, рыба может сорваться.", False, 'black')
fish_tutorial_3_1 = font2.render(f"Попробуй ещё раз", False, 'black')
fish_tutorial_4 = font2.render(f"Молодец, а теперь поймай в сумме 10 красных рыб", False, 'black')
shop_tutorial_5 = font2.render(f"Ты можешь продать каждую ", False, 'black')
shop_tutorial_5_1 = font2.render(f"красную рыбу за 1 монету", False, 'black')
shop_tutorial_6 = font2.render(f"Теперь, когда у тебя 10 монет, ", False, 'black')
shop_tutorial_6_1 = font2.render(f"ты можешь купить улучшенную леску", False, 'black')
tutorial_end = font2.render(f"На этом туториал заканчивается", False, 'black')
tutorial_end2 = font2.render(f"Продавай рыбы и покупай улучшения", False, 'black')
tutorial_end3 = font2.render(f"Удачи! (клик по экрану для продолжения )", False, 'black')

shop_sfx = pg.mixer.Sound("buy.wav")
shop_sfx.set_volume(0.30)
shop_sfx_open = pg.mixer.Sound("open_shop.wav")
shop_sfx_open.set_volume(0.50)
shop_sfx_close = pg.mixer.Sound("close_shop.mp3")
shop_sfx_close.set_volume(0.50)
fish_catch_sfx = pg.mixer.Sound("fish_catch_sfx.wav")
fish_catch_sfx.set_volume(0.80)
fish_caught_sfx = pg.mixer.Sound("fish_caught_sfx.wav")
fish_caught_sfx.set_volume(0.80)
fish_getaway_sfx = pg.mixer.Sound("fish_getaway_sfx.wav")
fish_getaway_sfx.set_volume(0.80)
current_time = pg.time.get_ticks()
frame_duration_entity = 200
frame_duration_fish = 500
frame_index_entity = (current_time // frame_duration_entity) % 3
frame_index_fish = (current_time // frame_duration_fish) % 2

background = pg.transform.scale(pg.image.load("tile_ground_between_mix.png").convert(), (150, 150))
background_mix = pg.transform.scale(pg.image.load("tile_ground_new.png").convert(), (150, 150))
background_mix2 = pg.transform.scale(pg.image.load("tile_ground_mix2_new.png").convert(), (150, 150))
water_much_background = pg.transform.scale(pg.image.load("much_Water.png").convert(), (350, 150))
lava_much_background = pg.transform.scale(pg.image.load("much_Lava.png").convert(), (350, 150))
background_Shop = pg.transform.scale(pg.image.load("tile_shop.png").convert(), (100, 50))
crafting_bench = pg.transform.scale(pg.image.load("workbench.png").convert(), (50, 50))

volcano_left = pg.transform.scale(pg.image.load("volcano_side.png").convert(), (150, 150))
volcano_upside = pg.transform.scale(pg.image.load("volcano_upside.png").convert(), (150, 150))
volcano_up = pg.transform.scale(pg.image.load("volcano_up.png").convert(), (150, 150))
volcano_upright = pg.transform.scale(pg.image.load("volcano_upleft.png").convert(), (150, 150))
volcano_right = pg.transform.scale(pg.image.load("volcano_side2.png").convert(), (150, 150))
volcano_mix = pg.transform.scale(pg.image.load("volcano_mix.png").convert(), (150, 150))
volcano_down = pg.transform.scale(pg.image.load("volcano_down.png").convert(), (150, 150))
volcano_downleft = pg.transform.scale(pg.image.load("volcano_downleft.png").convert(), (150, 150))
volcano_downright = pg.transform.scale(pg.image.load("volcano_downright.png").convert(), (150, 150))

missions_sign = pg.transform.scale(pg.image.load("sign.png").convert(), (40, 40))
missions_sign_rect = pg.Rect((500, 250, 540, 290))
shop_menu = pg.transform.scale(pg.image.load("shop_menu.png").convert(), (150, 600))
shop_red_fish = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_1.png"), (100, 100))
shop_fishing_line = pg.transform.scale(pg.image.load(f"fishing_line.png"), (100, 100))
shop_fishing_line_small = pg.transform.scale(pg.image.load(f"fishing_line.png"), (50, 50))

shop_fish_bait = pg.transform.scale(pg.image.load(f"fish_bait.png"), (100, 100))
shop_fish_bait_small = pg.transform.scale(pg.image.load(f"fish_bait.png"), (50, 50))

shop_loot_magnet = pg.transform.scale(pg.image.load(f"loot_magnet.png"), (100, 100))
shop_loot_magnet_small = pg.transform.scale(pg.image.load(f"loot_magnet.png"), (50, 50))

ring = pg.transform.scale(pg.image.load(f"ring.png"), (130, 80))
ring_small = pg.transform.scale(pg.image.load(f"ring.png"), (50, 50))

discount_card = pg.transform.scale(pg.image.load(f"discount card.png"), (130, 80))
discount_card_small = pg.transform.scale(pg.image.load(f"discount card.png"), (50, 50))

lucky_coin = pg.transform.scale(pg.image.load(f"Lucky_Coin.png"), (50, 50))

coin_ring = pg.transform.scale(pg.image.load(f"Coin_Ring.png"), (130, 80))
coin_ring_small = pg.transform.scale(pg.image.load(f"Coin_Ring.png"), (50, 50))

endless_crown = pg.transform.scale(pg.image.load(f"img.png"), (50, 30))
endless_crown_rect = pg.Rect((50, 0, 80, 30))

fishing_menu = pg.transform.scale(pg.image.load("fishing_menu_new.png").convert(), (600, 100))
fishing_pole = pg.transform.scale(pg.image.load("Fish-rod.png").convert(), (100, 100))
fishing_pole_small = pg.transform.scale(pg.image.load("Fish-rod.png").convert(), (50, 50))
fish_arrow = pg.transform.scale(pg.image.load("arrow_fish_menu.png").convert(), (50, 50))

clam_1 = pg.transform.scale(pg.image.load(f"fishes/clam/Background.png"), (50, 50))
clam_small = pg.transform.scale(pg.image.load(f"fishes/clam/Background.png"), (25, 25))
clam_2 = pg.transform.scale(pg.image.load(f"fishes/clam/Слой 1.png"), (50, 50))
clam_3 = pg.transform.scale(pg.image.load(f"fishes/clam/Слой 2.png"), (50, 50))
clam_pearl = pg.transform.scale(pg.image.load(f"fishes/clam/Слой 3.png"), (100, 100))
clam_pearl_small = pg.transform.scale(pg.image.load(f"fishes/clam/Слой 3.png"), (25, 25))
clam_ = [clam_1, clam_2, clam_3]

red_fish_1 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_1.png"), (50, 50))
red_fish_small = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_1.png"), (25, 25))
red_fish_2 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_2.png"), (50, 50))
red_fish_3 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_3.png"), (50, 50))
red_fish_4 = pg.transform.scale(pg.image.load(f"fishes/red/red_fish_4.png"), (50, 50))
red_fish_ = [red_fish_1, red_fish_2, red_fish_3, red_fish_4]

coin_fish_1 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 1.png"), (50, 50))
coin_fish_small = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 1.png"), (25, 25))
coin_fish_2 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 2.png"), (50, 50))
coin_fish_3 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 3.png"), (50, 50))
coin_fish_4 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 4.png"), (50, 50))
coin_fish_5 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 5.png"), (50, 50))
coin_fish_6 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 6.png"), (50, 50))
coin_fish_7 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 7.png"), (50, 50))
coin_fish_8 = pg.transform.scale(pg.image.load(f"fishes/coin/Слой 8.png"), (50, 50))
coin_fish_ = [coin_fish_1, coin_fish_2, coin_fish_3, coin_fish_4, coin_fish_5, coin_fish_6, coin_fish_7, coin_fish_8]

gold_fish = pg.transform.scale(pg.image.load(f"fishes/gold fish.png"), (50, 50))
gold_fish_small = pg.transform.scale(pg.image.load(f"fishes/gold fish.png"), (25, 25))

obsidian_fish = pg.transform.scale(pg.image.load(f"fishes/obsidian fish.png"), (50, 50))
lava_fish = pg.transform.scale(pg.image.load(f"fishes/lava fish.png"), (50, 50))
lava_jellyfish = pg.transform.scale(pg.image.load(f"fishes/lava_jellyfish.png"), (50, 50))

shop_rect = pg.Rect((250, 50, 350, 100))
shop_surf = pg.Surface((100, 20))
shop_rect = shop_surf.get_rect(topleft=(250, 30))

crafting_bench_rect = pg.Rect((450, 50, 550, 100))
crafting_bench_surf = pg.Surface((50, 50))
crafting_bench_rect = shop_surf.get_rect(topleft=(450, 50))

fishing_pole_rect = pg.Rect((0, 0, 150, 150))
red_fish_shop_rect = pg.Rect((0, 150, 300, 150))
fish_line_shop_rect = pg.Rect((0, 250, 130, 250))
fish_bait_shop_rect = pg.Rect((0, 470, 180, 600))
loot_magnet_shop_rect = pg.Rect((0, 300, 150, 400))
pearl_shop_rect = pg.Rect((0, 0, 150, 150))

discount_card_rect = pg.Rect((0, 0, 150, 150))
ring_rect = pg.Rect((0, 150, 300, 150))
lucky_coin_ring_rect = pg.Rect((0, 300, 150, 400))

fishing_point_surf = pg.Surface((50, 50))
fishing_point_rect = fishing_point_surf.get_rect(topleft=(290, 499))
fish_point_rect = pg.Rect((300, 400, 300, 450))
fish_point_surf = pg.Surface((50, 100))
fish_point_rect = fishing_point_surf.get_rect(topleft=(270, 300))

ready_red_rect = pg.Rect((40, 100, 60, 110))
ready_red_surf = pg.Surface((70, 20))
ready_red_rect = ready_red_surf.get_rect(topleft=(40, 100))

ready_gold_rect = pg.Rect((40, 200, 60, 210))
ready_gold_surf = pg.Surface((70, 20))
ready_gold_rect = ready_gold_surf.get_rect(topleft=(40, 200))

ready_clam_rect = pg.Rect((40, 300, 60, 310))
ready_clam_surf = pg.Surface((70, 20))
ready_clam_rect = ready_clam_surf.get_rect(topleft=(40, 300))
x = 300
y = 600 // 2
pg.display.update()
shop_state = 'none'
stage = 1
open_shop_menu = False
open_craft_menu = False
open_missions_menu = False
fishing_pole_bought = False  # remove
fishing_line_bought = True
fish_bait_bought = True
loot_magnet_bought = True
discount_card_crafted = True
ring_crafted = True
pearl_bought = True
lucky_coin_fished = True
lucky_coin_ring_crafted = True
fishing_state = True
is_tutorial = True
game_over = False
continue_ = False
tutorial_state = '1'
entity1 = Entity(x, y)
fish1 = Fish(-50, 350, gold_fish, 1.5)
red_fish_mission = HealthBar(35, 80, 80)
gold_fish_mission = HealthBar(35, 180, 80)
clam_mission = HealthBar(35, 280, 80)
fish_point_color = 'green'
all_sprite = pg.sprite.Group(entity1, fish1)
grass_tile1_rect = pg.surface.Surface((50, 50))
while run:
    mouse_x, mouse_y = pg.mouse.get_pos()
    mouse_rect = pg.Surface((5, 5))
    mouse_rect = mouse_rect.get_rect(topleft=(mouse_x, mouse_y))
    clock.tick(60)
    entity1.stay_still()
    keys = pg.key.get_pressed()
    screen.fill('black')
    if stage == 1:
        if mission_red_count == 30:
            red_mission_tier = font.render(f"+", False, 'gray')
        elif mission_red_count == 25:
            red_mission_tier = font2.render(f"III", False, 'yellow')
        elif mission_red_count == 20:
            red_mission_tier = font2.render(f"II", False, 'yellow')
        elif mission_red_count == 15:
            red_mission_tier = font2.render(f"I", False, 'yellow')

        if mission_gold_fish_count == 30:
            gold_fish_mission_tier = font.render(f"+", False, 'gray')
        elif mission_gold_fish_count == 25:
            gold_fish_mission_tier = font2.render(f"III", False, 'yellow')
        elif mission_gold_fish_count == 20:
            gold_fish_mission_tier = font2.render(f"II", False, 'yellow')
        elif mission_gold_fish_count == 15:
            gold_fish_mission_tier = font2.render(f"I", False, 'yellow')

        if mission_clam_count == 30:
            clam_mission_tier = font.render(f"+", False, 'gray')
        elif mission_clam_count == 25:
            clam_mission_tier = font2.render(f"III", False, 'yellow')
        elif mission_clam_count == 20:
            clam_mission_tier = font2.render(f"II", False, 'yellow')
        elif mission_clam_count == 15:
            clam_mission_tier = font2.render(f"I", False, 'yellow')

        fish_list_1 = font2.render(f"Красная рыба x{red_fish_count}", False, 'purple')
        fish_list_2 = font2.render(f"Монета x{coin_fish_count}", False, 'purple')
        fish_list_3 = font2.render(f"Моллюск x{clam_count}", False, 'purple')
        fish_list_3_1 = font2.render(f"Жемчужина x{pearl_count}", False, 'purple')
        fish_list_4 = font2.render(f"Золотая Рыбка x{gold_fish_count}", False, 'purple')
        if mission_red_count == 30:
            mission1_text = font2.render(f"Поймайте 25", False, 'white')
        else:
            mission1_text = font2.render(f"Поймайте {mission_red_count}", False, 'white')
        if mission_gold_fish_count == 30:
            mission2_text = font2.render(f"Поймайте 25", False, 'white')
        else:
            mission2_text = font2.render(f"Поймайте {mission_gold_fish_count}", False, 'white')
        if mission_clam_count == 30:
            mission3_text = font2.render(f"Поймайте 25", False, 'white')
        else:
            mission3_text = font2.render(f"Поймайте {mission_clam_count}", False, 'white')
        screen.blit(background_mix2, (0, 400))
        screen.blit(background_mix2, (0, 300))
        screen.blit(background_mix2, (0, 150))
        screen.blit(background_mix2, (0, 0))
        screen.blit(background_mix2, (150, 400))
        screen.blit(background_mix2, (150, 300))
        screen.blit(background_mix2, (150, 150))
        screen.blit(background_mix2, (150, 0))
        screen.blit(background_mix2, (300, 400))
        screen.blit(background_mix2, (300, 300))
        screen.blit(background_mix2, (300, 150))
        screen.blit(background_mix2, (300, 0))
        screen.blit(background_mix2, (450, 300))
        screen.blit(background_mix2, (450, 150))
        screen.blit(background_mix2, (450, 0))
        screen.blit(background_mix2, (450, 400))
        screen.blit(background, (0, 400))
        screen.blit(background, (150, 400))
        screen.blit(background, (300, 400))
        screen.blit(background, (450, 400))
        screen.blit(water_much_background, (0, 550))
        screen.blit(water_much_background, (350, 550))
        if entity1.rect.y >= 465:
            entity1.rect.y = 465
        if entity1.rect.y < 0:
            entity1.rect.y = 0
        if entity1.rect.x < 0:
            entity1.rect.x = 0
        if entity1.rect.x > 560:
            entity1.rect.x = 560
    elif stage == 2:

        lava_fish_text = font2.render(f"Лавовая рыба x{lava_fish_count}", False, 'purple')
        obsidian_fish_text = font2.render(f"Обсидиановая рыба x{obsidian_fish_count}", False, 'purple')
        lava_jellyfish_count = font2.render(f"Моллюск x{clam_count}", False, 'purple') .....

        screen.blit(volcano_left, (0, 300))
        screen.blit(volcano_left, (0, 150))
        screen.blit(volcano_upside, (0, 0))

        screen.blit(volcano_mix, (150, 300))
        screen.blit(volcano_mix, (150, 150))
        screen.blit(volcano_up, (150, 0))

        screen.blit(volcano_mix, (300, 300))
        screen.blit(volcano_mix, (300, 150))
        screen.blit(volcano_up, (300, 0))
        screen.blit(volcano_right, (450, 300))
        screen.blit(volcano_right, (450, 150))
        screen.blit(volcano_upright, (450, 0))

        screen.blit(volcano_downleft, (0, 400))
        screen.blit(volcano_down, (150, 400))
        screen.blit(volcano_down, (300, 400))
        screen.blit(volcano_downright, (450, 400))

        screen.blit(lava_much_background, (0, 550))
        screen.blit(lava_much_background, (350, 550))
        if entity1.rect.y >= 495:
            entity1.rect.y = 495
        if entity1.rect.y < 0:
            entity1.rect.y = 0
        if entity1.rect.x < 0:
            entity1.rect.x = 0
        if entity1.rect.x > 560:
            entity1.rect.x = 560
    if fishing_pole_bought:
        screen.blit(fishing_pole_small, (530, 540))
    if fishing_line_bought:
        screen.blit(shop_fishing_line_small, (470, 540))
    if fish_bait_bought:
        screen.blit(shop_fish_bait_small, (420, 540))
    if loot_magnet_bought:
        screen.blit(shop_loot_magnet_small, (370, 540))
    if discount_card_crafted:
        screen.blit(discount_card_small, (320, 540))
    if ring_crafted:
        if not lucky_coin_ring_crafted:
            screen.blit(ring_small, (265, 540))
    if lucky_coin_fished:
        if not lucky_coin_ring_crafted:
            screen.blit(lucky_coin, (210, 540))
    if lucky_coin_ring_crafted:
        screen.blit(coin_ring_small, (265, 540))
    if discount_card_crafted:
        shop_text_fish_bait = font.render(f"8 монет", False, 'white')
        shop_text_loot_magnet = font.render(f"10 монет", False, 'white')
    else:
        shop_text_fish_bait = font.render(f"15 монет", False, 'white')
        shop_text_loot_magnet = font.render(f"20 монет", False, 'white')

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_shop_menu:
            if fishing_pole_rect.collidepoint(event.pos) and not fishing_pole_bought:
                print('Удочка куплена!')
                fishing_pole_bought = True
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_shop_menu:
            if fish_line_shop_rect.collidepoint(event.pos) and not fishing_line_bought and coin_fish_count >= 10:
                print('Улучшенная леска куплена!')
                fishing_line_bought = True
                coin_fish_count -= 10
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_shop_menu:
            if discount_card_crafted:
                if fish_bait_shop_rect.collidepoint(event.pos) and not fish_bait_bought and coin_fish_count >= 8:
                    print('Приманка куплена!')
                    fish_bait_bought = True
                    coin_fish_count -= 8
                    shop_sfx.play()
            else:
                if fish_bait_shop_rect.collidepoint(event.pos) and not fish_bait_bought and coin_fish_count >= 15:
                    print('Приманка куплена!')
                    fish_bait_bought = True
                    coin_fish_count -= 15
                    shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_shop_menu:
            if discount_card_crafted:
                if loot_magnet_shop_rect.collidepoint(event.pos) and not loot_magnet_bought and coin_fish_count >= 10:
                    print('Магнит лута куплена!')
                    loot_magnet_bought = True
                    coin_fish_count -= 10
                    shop_sfx.play()
            else:
                if loot_magnet_shop_rect.collidepoint(event.pos) and not loot_magnet_bought and coin_fish_count >= 20:
                    print('Магнит лута куплена!')
                    loot_magnet_bought = True
                    coin_fish_count -= 20
                    shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_shop_menu:
            if ring_crafted:
                if red_fish_shop_rect.collidepoint(event.pos) and not red_fish_count <= 0:
                    print('Рыба продана!')
                    red_fish_count -= 1
                    coin_fish_count += 5
                    shop_sfx.play()
            else:
                if red_fish_shop_rect.collidepoint(event.pos) and not red_fish_count <= 0:
                    print('Рыба продана!')
                    red_fish_count -= 1
                    coin_fish_count += 1
                    shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_shop_menu:
            if ring_crafted:
                if pearl_shop_rect.collidepoint(event.pos) and not clam_count <= 0 and not coin_fish_count < 3:
                    print('Жемчужина куплена!')
                    pearl_count += 1
                    pearl_bought = True
                    clam_count -= 1
                    coin_fish_count -= 3
                    shop_sfx.play()
            else:
                if pearl_shop_rect.collidepoint(event.pos) and not clam_count <= 0 and not coin_fish_count < 5:
                    print('Жемчужина куплена!')
                    pearl_count += 1
                    pearl_bought = True
                    clam_count -= 1
                    coin_fish_count -= 5
                    shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_craft_menu:
            if discount_card_rect.collidepoint(
                    event.pos) and pearl_count >= 1 and coin_fish_count >= 5 and not discount_card_crafted:
                print('Скидочная карта сделана!')
                pearl_count -= 1
                discount_card_crafted = True
                coin_fish_count -= 5
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_craft_menu:
            if ring_rect.collidepoint(event.pos) and pearl_count >= 10 and coin_fish_count >= 5 and not ring_crafted:
                print('Кольцо сделано!')
                pearl_count -= 10
                ring_crafted = True
                coin_fish_count -= 5
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_craft_menu:
            if lucky_coin_ring_rect.collidepoint(
                    event.pos) and pearl_count >= 50 and gold_fish_count >= 15 and not lucky_coin_ring_crafted:
                print('Кольцо Всемирной Власти сделано!')
                pearl_count -= 50
                lucky_coin_ring_crafted = True
                gold_fish_count -= 15
                shop_sfx.play()
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and is_tutorial and tutorial_state == '5.2':
            print('Туториал окончен!')
            is_tutorial = False
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_missions_menu:
            if ready_red_rect.collidepoint(event.pos) and 30 > mission_red_count <= total_red_fish_count:
                mission_red_count += 5
                red_fish_mission.width -= 25
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_missions_menu:
            if ready_gold_rect.collidepoint(event.pos) and 30 > mission_gold_fish_count <= total_gold_fish_count:
                mission_gold_fish_count += 5
                gold_fish_mission.width -= 25
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and open_missions_menu:
            if ready_clam_rect.collidepoint(event.pos) and 30 > mission_clam_count <= total_clam_count:
                mission_clam_count += 5
                clam_mission.width -= 25
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and game_over:
            continue_ = True
            game_over = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE and entity1.rect.y >= 465:
            if is_tutorial:
                fish_point_color = 'black'
            else:
                fish_point_color = 'brown'
            fish_catch_sfx.play()
            pg.time.set_timer(pg.USEREVENT, 200)
        if event.type == pg.USEREVENT:
            fish_point_color = 'green'

    if keys[pg.K_w] and not game_over:
        entity1.move_up()
    if keys[pg.K_s] and not game_over:
        entity1.move_down()
    if keys[pg.K_d] and not game_over:
        entity1.move_right()
    if keys[pg.K_a] and not game_over:
        entity1.move_left()

    if fish1.rect.x >= 620:
        fishing_state = False
        fish1.rect.x = -50
        fish_getaway_sfx.play()
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

    if fish1.image == clam_1 or fish1.image == clam_2 or fish1.image == clam_3:
        frame_index = (current_time // frame_duration) % 3
        fish1.image = clam_[frame_index]
        if fish_bait_bought:
            fish1.speed = 6
        else:
            fish1.speed = 3

    if fish1.image == gold_fish:
        if fish_bait_bought:
            fish1.speed = 14
        else:
            fish1.speed = 7

    if fish1.image == lucky_coin:
        if fish_bait_bought:
            fish1.speed = 1
        else:
            fish1.speed = 0.5
    if fish1.image == lava_fish:
        fish1.speed = 9
    if fish1.image == obsidian_fish:
        fish1.speed = 7
    if fish1.image == lava_jellyfish:
        fish1.speed = 5
    if fish1.rect.x == -50:
        if stage == 1:
            if not loot_magnet_bought:
                if is_tutorial:
                    fish1.image = red_fish_1

                else:
                    if random.randint(1, 10) > 3:
                        fish1.image = red_fish_1
                    if random.randint(1, 10) == 3:
                        fish1.image = clam_1
                    if random.randint(1, 10) < 4:
                        fish1.image = coin_fish_1
            else:
                if ring_crafted:
                    if not lucky_coin_fished:
                        if random.randint(1, 10) == 1:
                            fish1.image = lucky_coin
                        elif random.randint(1, 10) <= 3:
                            fish1.image = red_fish_1
                        elif random.randint(1, 10) <= 3:
                            fish1.image = clam_1
                        elif random.randint(1, 10) <= 5:
                            fish1.image = coin_fish_1
                        else:
                            if not gold_fish_count > 15:
                                fish1.image = gold_fish
                    else:
                        if random.randint(1, 10) <= 5 and not coin_fish_count > 150:
                            fish1.image = red_fish_1

                        elif random.randint(1,
                                            10) > 5 and not clam_count > 50 and not pearl_count > 50 and not pearl_count + clam_count > 50:
                            fish1.image = clam_1

                        else:
                            if not gold_fish_count > 15:
                                fish1.image = gold_fish
                else:
                    if random.randint(1, 10) <= 3:
                        fish1.image = red_fish_1

                    elif random.randint(1, 10) <= 3:
                        fish1.image = clam_1

                    elif random.randint(1, 10) <= 5:
                        fish1.image = coin_fish_1

                    else:
                        if not gold_fish_count > 15:
                            fish1.image = gold_fish
        elif stage == 2:
            if random.randint(1, 20) < 5:
                fish1.image = lava_fish
            elif random.randint(1, 20) > 15:
                fish1.image = obsidian_fish
            else:
                fish1.image = lava_jellyfish
        fish1.rect.x = -50
    if entity1.rect.y >= 465 and stage == 1:

        if fishing_pole_bought and fishing_state:
            screen.blit(fishing_menu, (0, 300))
            screen.blit(fish_arrow, (270, 390))
            screen.blit(fish_point_surf, (270, 300))
            fish_point_surf.fill(fish_point_color)
            current_time = pg.time.get_ticks()
            frame_duration = 300
            frame_index = (current_time // frame_duration) % 2

            if frame_index == 1 and fishing_state:
                fish1.fish_update()

            if frame_index == 2 and fish1.image == gold_fish:
                fish1.fish_update()
    elif entity1.rect.y >= 495 and stage == 2:
        if fishing_pole_bought and fishing_state:
            screen.blit(fishing_menu, (0, 300))
            screen.blit(fish_arrow, (270, 390))
            screen.blit(fish_point_surf, (270, 300))
            fish_point_surf.fill(fish_point_color)
            current_time = pg.time.get_ticks()
            frame_duration = 300
            frame_index = (current_time // frame_duration) % 2

            fish1.lava_fish_update()
    else:
        fish1.rect.x = -50
    if fish1.rect.colliderect(fish_point_rect):

        if fish_point_color == 'black' or fish_point_color == 'brown':

            if not fishing_line_bought:

                if random.randint(1, 2) == 2:
                    fish1.rect.x = -50

                    if is_tutorial:
                        if tutorial_state == '4.3':
                            tutorial_state = '4.4'

                    if fish1.image == red_fish_1 or fish1.image == red_fish_2 or fish1.image == red_fish_3 or fish1.image == red_fish_4:
                        red_fish_count += 1
                        total_red_fish_count += 1
                        fish_point_color = 'red'
                        fish_caught_sfx.play()

                    if fish1.image == coin_fish_1 or fish1.image == coin_fish_2 or fish1.image == coin_fish_3 or fish1.image == coin_fish_4 or fish1.image == coin_fish_5 or fish1.image == coin_fish_6 or fish1.image == coin_fish_7 or fish1.image == coin_fish_8:
                        coin_fish_count += 1
                        fish_point_color = 'red'
                        fish_caught_sfx.play()

                    if fish1.image == clam_1 or fish1.image == clam_2 or fish1.image == clam_3:
                        clam_count += 1
                        fish_point_color = 'red'
                        fish_caught_sfx.play()

                    if fish1.image == gold_fish:
                        gold_fish_count += 1
                        total_gold_fish_count += 1
                        fish_point_color = 'red'
                        fish_caught_sfx.play()

                else:
                    fish_getaway_sfx.play()
                    print('Рыба сорвалась с лески!')
                    fish1.fish_update()
                    fish_point_color = 'blue'

                    if tutorial_state == '4.3' or tutorial_state == '4.2':
                        tutorial_state = '4.3'
            else:
                fish1.rect.x = -50

                if fish1.image == red_fish_1 or fish1.image == red_fish_2 or fish1.image == red_fish_3 or fish1.image == red_fish_4:
                    red_fish_count += 1
                    total_red_fish_count += 1
                    red_fish_mission.width += 5
                    fish_caught_sfx.play()

                if fish1.image == coin_fish_1 or fish1.image == coin_fish_2 or fish1.image == coin_fish_3 or fish1.image == coin_fish_4 or fish1.image == coin_fish_5 or fish1.image == coin_fish_6 or fish1.image == coin_fish_7 or fish1.image == coin_fish_8:
                    coin_fish_count += 1
                    fish_caught_sfx.play()

                if fish1.image == clam_1 or fish1.image == clam_2 or fish1.image == clam_3:
                    clam_count += 1
                    fish_caught_sfx.play()

                if fish1.image == gold_fish:
                    gold_fish_count += 1
                    total_gold_fish_count += 1
                    gold_fish_mission.width += 5
                    fish_caught_sfx.play()
                if fish1.image == lucky_coin:
                    lucky_coin_fished = True
                if fish1.image == lava_fish:
                    lava_fish_count += 1
                if fish1.image == obsidian_fish:
                    obsidian_fish_count += 1
                if fish1.image == lava_jellyfish:
                    lava_jellyfish_count += 1
    if not fishing_point_rect.colliderect(entity1):
        fishing_state = True

    if shop_rect.colliderect(entity1) and stage == 1 and (
            tutorial_state == '3.2' or tutorial_state == '3.3' or tutorial_state == '5' or tutorial_state == '5.1' or tutorial_state == '5.2'):
        open_shop_menu = True

    else:
        screen.blit(shop_text_fish_pole, (1000, 1000))
        open_shop_menu = False
        if shop_state == 'open':
            shop_state = 'none'
            shop_sfx_close.play()

    if crafting_bench_rect.colliderect(entity1) and not is_tutorial and pearl_bought and stage == 1:
        open_craft_menu = True

    else:
        open_craft_menu = False

    if open_shop_menu:
        screen.blit(shop_menu, (0, 0))

        if shop_state == 'none':
            shop_sfx_open.play()
            shop_state = 'open'

        if not fish_bait_bought:
            screen.blit(shop_fish_bait, (30, 465))
            screen.blit(shop_text_fish_bait, (25, 560))
            if mouse_rect.colliderect(fish_bait_shop_rect):
                screen.blit(fish_bait_text, (100, 500))

        if not fishing_line_bought:
            screen.blit(shop_fishing_line, (30, 350))
            screen.blit(shop_text_fish_line, (25, 440))
            if mouse_rect.colliderect(fish_line_shop_rect):
                screen.blit(fish_line_text, (100, 400))

        else:
            if not loot_magnet_bought:
                screen.blit(shop_loot_magnet, (30, 350))
                screen.blit(shop_text_loot_magnet, (25, 440))
                if mouse_rect.colliderect(loot_magnet_shop_rect):
                    screen.blit(loot_magnet_text, (100, 400))

        if not fishing_pole_bought:
            screen.blit(fishing_pole, (23, 30))
            screen.blit(shop_text_fish_pole, (15, 130))
            if mouse_rect.colliderect(fishing_pole_rect):
                screen.blit(fish_pole_text, (50, 30))
        else:
            if not clam_count <= 0:
                screen.blit(clam_pearl, (23, 30))
                screen.blit(shop_text_pearl, (8, 130))

        if not red_fish_count <= 0:
            screen.blit(shop_red_fish, (20, 200))
            screen.blit(shop_text_red_fish, (20, 300))

        else:
            screen.blit(fishing_pole, (1000, 1000))
            screen.blit(shop_text_fish_pole, (1000, 1000))

    if open_craft_menu:
        screen.blit(shop_menu, (0, 0))

        if not discount_card_crafted:
            screen.blit(discount_card, (10, 20))
            screen.blit(work_bench_discount_card_text1, (5, 100))
            screen.blit(work_bench_ring_text2, (5, 120))
            if mouse_rect.colliderect(discount_card_rect):
                screen.blit(discount_card_text, (130, 20))

        if not ring_crafted:
            screen.blit(ring, (6.5, 150))
            screen.blit(work_bench_ring_text1, (5, 235))
            screen.blit(work_bench_ring_text2, (5, 255))
            if mouse_rect.colliderect(ring_rect):
                screen.blit(ring_text, (130, 150))

        if ring_crafted and lucky_coin_fished and not lucky_coin_ring_crafted:
            screen.blit(coin_ring, (10, 350))
            screen.blit(work_bench_lucky_coin_ring_text1, (10, 440))
            screen.blit(work_bench_coin_ring_text2, (10, 460))
            screen.blit(work_bench_coin_ring_text3, (10, 480))
            if mouse_rect.colliderect(lucky_coin_ring_rect):
                screen.blit(lucky_coin_ring_text, (0, 330))
    if open_missions_menu:
        screen.blit(shop_menu, (0, 0))
        screen.blit(mission1_text, (5, 50))
        screen.blit(red_fish_small, (125, 50))
        screen.blit(red_mission_tier, (135, 80))
        if mission_red_count == 30:
            screen.blit(mission_text_max, (27, 100))
        elif total_red_fish_count < mission_red_count:
            screen.blit(mission_text1, (27, 100))
        else:
            screen.blit(mission_text2, (40, 100))
        screen.blit(mission2_text, (5, 150))
        screen.blit(gold_fish_small, (125, 150))
        screen.blit(gold_fish_mission_tier, (135, 180))
        red_fish_mission.update()
        all_sprite.add(red_fish_mission)
        gold_fish_mission.update()
        all_sprite.add(gold_fish_mission)
        clam_mission.update()
        all_sprite.add(clam_mission)
        if mission_gold_fish_count == 30 or gold_fish_mission_tier == font.render(f"+", False, 'gray'):
            screen.blit(mission_text_max, (27, 200))
        elif total_gold_fish_count < mission_gold_fish_count:
            screen.blit(mission_text1, (27, 200))
        else:
            screen.blit(mission_text2, (40, 200))
        screen.blit(mission3_text, (5, 250))
        screen.blit(clam_small, (125, 250))
        screen.blit(clam_mission_tier, (135, 280))

        if mission_clam_count == 30 or clam_mission_tier == font.render(f"+", False, 'gray'):
            screen.blit(mission_text_max, (27, 300))
        elif total_clam_count < mission_clam_count:
            screen.blit(mission_text1, (27, 300))
        else:
            screen.blit(mission_text2, (40, 300))
    else:
        all_sprite.remove(red_fish_mission)
        all_sprite.remove(gold_fish_mission)
        all_sprite.remove(clam_mission)
    if is_tutorial:
        screen.blit(skip_tutorial, (20, 580))

        if keys[pg.K_ESCAPE] and keys[pg.K_SPACE]:
            is_tutorial = False
            fishing_line_bought = True
            fishing_pole_bought = True
            tutorial_state = '5.2'

        if tutorial_state == '1':
            screen.blit(wasd_key_tutorial, (170, 450))

            if keys[pg.K_w] or keys[pg.K_a] or keys[pg.K_d] or keys[pg.K_s]:
                tutorial_state = '2'

        if tutorial_state == '2':
            screen.blit(tab_lshift_key_tutorial, (70, 450))

            if keys[pg.K_TAB] or keys[pg.K_LSHIFT]:
                tutorial_state = '3.1'

        if tutorial_state == '3.1' or tutorial_state == '3.2' or tutorial_state == '3.3':
            screen.blit(background_Shop, (250, 40))

            if tutorial_state == '3.1':
                screen.blit(shop_tutorial_1, (170, 450))
                if entity1.rect.colliderect(shop_rect):
                    tutorial_state = '3.2'

            if tutorial_state == '3.2':
                screen.blit(shop_tutorial_2, (170, 450))
                if fishing_pole_bought:
                    tutorial_state = '3.3'

            if tutorial_state == '3.3':
                screen.blit(shop_tutorial_3, (170, 450))
                if not entity1.rect.colliderect(shop_rect):
                    tutorial_state = '4.1'
        if tutorial_state == '4.1' or tutorial_state == '4.2' or tutorial_state == '4.3' or tutorial_state == '4.4':

            if tutorial_state == '4.1':
                screen.blit(fish_tutorial_1, (170, 450))
                if entity1.rect.y >= 465:
                    tutorial_state = '4.2'

            if tutorial_state == '4.2':
                screen.blit(fish_tutorial_2, (70, 250))
                screen.blit(fish_tutorial_2_1, (70, 270))

            if tutorial_state == '4.3':
                screen.blit(fish_tutorial_3, (20, 250))
                screen.blit(fish_tutorial_3_1, (20, 270))

            if tutorial_state == '4.4':
                screen.blit(fish_tutorial_4, (20, 250))
                if red_fish_count >= 10:
                    tutorial_state = '5'

        if tutorial_state == '5' or tutorial_state == '5.1' or tutorial_state == '5.2':
            screen.blit(background_Shop, (250, 40))

            if tutorial_state == '5':
                if entity1.rect.colliderect(shop_rect):
                    tutorial_state = '5.1'
                else:
                    screen.blit(shop_tutorial_1, (170, 450))

            if tutorial_state == '5.1':
                if fishing_line_bought:
                    tutorial_state = '5.2'
                if red_fish_count == 0 and coin_fish_count >= 10:
                    screen.blit(shop_tutorial_6, (170, 430))
                    screen.blit(shop_tutorial_6_1, (170, 450))

                else:
                    screen.blit(shop_tutorial_5, (170, 430))
                    screen.blit(shop_tutorial_5_1, (170, 450))

            if tutorial_state == '5.2':
                screen.blit(tutorial_end, (70, 410))
                screen.blit(tutorial_end2, (70, 430))
                screen.blit(tutorial_end3, (70, 450))
    else:
        if stage == 1:
            screen.blit(background_Shop, (250, 40))

    if pearl_bought and stage == 1:
        screen.blit(crafting_bench_surf, (450, 50))
        screen.blit(crafting_bench, (450, 50))

    if game_over:
        screen.blit(game_over_text, (150, 300))
        screen.blit(game_over_text2, (150, 380))
        entity1.rect.x = 300
        entity1.rect.y = 350
        if keys[pg.K_ESCAPE]:
            run = False
    if lucky_coin_ring_crafted:
        if not continue_:
            game_over = True
        else:
            game_over = False
            if stage == 1:
                screen.blit(missions_sign, (500, 250))
    all_sprite.draw(screen)
    all_sprite.update()
    if pearl_bought and stage == 1:
        screen.blit(work_bench_text1, (433, 20))
        screen.blit(work_bench_text2, (430, 23))
    if (keys[pg.K_LSHIFT] or keys[pg.K_TAB]) and tutorial_state != '1' and not game_over:
        if stage == 1:
            screen.blit(fish_list_1, (400, 130))
            screen.blit(red_fish_small, (370, 120))
            screen.blit(fish_list_2, (400, 150))
            screen.blit(coin_fish_small, (370, 145))
            if clam_count != 0:
                screen.blit(fish_list_3, (400, 170))
                screen.blit(clam_small, (370, 168))
            if gold_fish_count != 0:
                screen.blit(fish_list_4, (400, 210))
                screen.blit(gold_fish_small, (370, 210))
            if pearl_count != 0:
                screen.blit(fish_list_3_1, (400, 190))
                screen.blit(clam_pearl_small, (370, 190))
        elif stage == 2:

    if lucky_coin_ring_crafted:
        if not continue_:
            game_over = True
        else:
            game_over = False
            screen.blit(endless_crown, (50, 5))
            if mouse_rect.colliderect(endless_crown_rect):
                screen.blit(endless_game, (100, 5))
            if stage == 1:
                screen.blit(missions_text1, (490, 228))
                screen.blit(missions_text2, (488, 230))
            if entity1.rect.colliderect(missions_sign_rect) and stage == 1:
                open_missions_menu = True
            else:
                open_missions_menu = False
    if stage == 1 and mission_red_count == 30 and mission_gold_fish_count == 30 and mission_clam_count == 30:
        if entity1.rect.x <= 0:
            stage = 2
            entity1.rect.x = 550
    if stage == 2:
        if entity1.rect.x > 550:
            stage = 1
            entity1.rect.x = 5

    pg.display.update()
pg.quit()
