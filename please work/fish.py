import pygame as pg

pg.init()


class Fish(pg.sprite.Sprite):
    def __init__(self, x, y, image, speed):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed

    def fish_update(self):
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 2
        if frame_index == 1:
            self.rect.x += self.speed
