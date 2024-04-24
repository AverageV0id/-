import pygame as pg

pg.init()
pg.mixer.init()
screen = pg.display.set_mode((600, 600))

bubble2 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 2.png').convert(), (150, 150))
bubble3 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 3.png').convert(), (150, 150))
bubble4 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 4.png').convert(), (150, 150))
bubble5 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 5.png').convert(), (150, 150))
bubble6 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 6.png').convert(), (150, 150))
bubble7 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 7.png').convert(), (150, 150))
bubble8 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 8.png').convert(), (150, 150))
bubble9 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 9.png').convert(), (150, 150))
bubble10 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 10.png').convert(), (150, 150))
bubble11 = pg.transform.scale(pg.image.load(f'animations/bubbles/Слой 11.png').convert(), (150, 150))
bubble_ = [bubble2, bubble3, bubble4, bubble5, bubble6, bubble7, bubble8, bubble9, bubble10, bubble11]


class Bubble(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("fishes/screamer.jpg").convert(), (15, 15))
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 2
        self.image = bubble_[frame_index]
