import pygame as pg

health_bar_1 = pg.transform.scale(pg.image.load("healthbar/Слой 2.png").convert(), (200, 200))
health_bar_2 = pg.transform.scale(pg.image.load("healthbar/Слой 3.png").convert(), (200, 200))
health_bar_3 = pg.transform.scale(pg.image.load("healthbar/Слой 4.png").convert(), (200, 200))
health_bar_4 = pg.transform.scale(pg.image.load("healthbar/Слой 5.png").convert(), (200, 200))
health_bar_5 = pg.transform.scale(pg.image.load("healthbar/Слой 6.png").convert(), (200, 200))
health_bar_6 = pg.transform.scale(pg.image.load("healthbar/Слой 8.png").convert(), (200, 200))


class HealthBar(pg.sprite.Sprite):
    def __init__(self, x, y, health):
        super().__init__()
        self.width = 300
        self.image = pg.surface.Surface((self.width, 10))
        self.health = health

    def update(self):
        if self.health >= 100:
            self.image = health_bar_1
        if self.health >= 80:
            self.image = health_bar_2
        if self.health >= 60:
            self.image = health_bar_3
        if self.health >= 40:
            self.image = health_bar_4
        if self.health >= 20:
            self.image = health_bar_5
