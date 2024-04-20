import pygame as pg
from entity import Entity

pg.init()

clock = pg.time.Clock()
run = True

screen = pg.display.set_mode((600, 600))

font = pg.font.SysFont("None", 80)
text = font.render(f"Free", False, 'white')

walk_sound = pg.mixer.Sound("sounds/audio-editor-output.mp3")
shop_sfx = pg.mixer.Sound("sounds/buy.wav")
shop_sfx.set_volume(0.30)
background = pg.transform.scale(pg.image.load("tiles/tile_ground_between_mix.png").convert(), (150, 150))
background_mix = pg.transform.scale(pg.image.load("tiles/tile_ground_new.png").convert(), (150, 150))
background_mix2 = pg.transform.scale(pg.image.load("tiles/tile_ground_mix2_new.png").convert(), (150, 150))
water_much_background = pg.transform.scale(pg.image.load("tiles/much_Water.png").convert(), (350, 150))

background_Shop = pg.transform.scale(pg.image.load("tiles/tile_shop.png").convert(), (100, 50))
shop_menu = pg.transform.scale(pg.image.load("menus/shop_menu.png").convert(), (150, 600))
fishing_menu = pg.transform.scale(pg.image.load("menus/fishing_menu.png").convert(), (600, 100))
fishing_pole = pg.transform.scale(pg.image.load("items/fish-rod.png").convert(), (100, 100))
fish_arrow = pg.transform.scale(pg.image.load("menus/arrow_fish_menu.png").convert(), (50, 50))
shop_rect = pg.Rect((250, 50, 350, 100))
shop_surf = pg.Surface((100, 20))
shop_rect = shop_surf.get_rect(topleft=(250, 40))
fishing_pole_rect = pg.Rect((0, 0, 50, 50))

fishing_pole_surf = pg.Surface((100, 100))
fishing_pole_rect = fishing_pole_surf.get_rect(topleft=(20, 20))

fishing_point_surf = pg.Surface((50, 50))
fishing_point_rect = fishing_point_surf.get_rect(topleft=(290, 499))

x = 300
y = 600 // 2
pg.display.update()
open_menu = False
fishing_pole_bought = False
fishing_state = False
entity1 = Entity(x, y)

all_sprite = pg.sprite.Group(entity1)
grass_tile1_rect = pg.surface.Surface((50, 50))

while run:
    entity1.stay_still()
    keys = pg.key.get_pressed()
    screen.fill('black')

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
    if keys[pg.K_w]:
        entity1.move_up()
    if keys[pg.K_s]:
        entity1.move_down()
    if keys[pg.K_d]:
        entity1.move_right()
    if keys[pg.K_a]:
        entity1.move_left()

    if entity1.rect.y > 465:
        entity1.rect.y = 465
    if entity1.rect.y < 0:
        entity1.rect.y = 0
    if entity1.rect.x < 0:
        entity1.rect.x = 0
    if entity1.rect.x > 560:
        entity1.rect.x = 560
    if fishing_point_rect.colliderect(entity1) and fishing_pole_bought:
        screen.blit(fishing_menu, (0, 300))
        screen.blit(fish_arrow, (270, 390))
    if shop_rect.colliderect(entity1):
        open_menu = True
    else:
        screen.blit(text, (1000, 1000))
        open_menu = False
    if open_menu:
        screen.blit(shop_menu, (0, 0))
        if not fishing_pole_bought:
            screen.blit(fishing_pole, (25, 30))
            screen.blit(text, (20, 130))
        else:
            screen.blit(fishing_pole, (1000, 1000))
            screen.blit(text, (1000, 1000))

    all_sprite.draw(screen)
    all_sprite.update()

    pg.display.update()
pg.quit()
