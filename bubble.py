import pygame as pg

pg.init()
pg.mixer.init()

explosion_anim = [pg.transform.scale(pg.image.load(f'animations/bubbles/Слой {i}.png').convert(), (25, 25)) for i in range(2, 11)]


class Bubble(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("screamer.jpg").convert(), (15, 15))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 2
        self.image = explosion_anim[frame_index]
