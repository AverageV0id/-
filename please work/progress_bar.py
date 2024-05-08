import pygame as pg


class HealthBar(pg.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.width = width
        self.image = pg.surface.Surface((self.width, 10))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.image = pg.surface.Surface((self.width, 10))
        self.image.fill("green")