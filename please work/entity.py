import pygame as pg
import time

pg.init()
pg.mixer.init()
walk_sound = pg.mixer.Sound("audio-editor-output.mp3")
walk_sound.set_volume(0.5)
up_1 = pg.image.load(f'../please work/up_1.png')
up_2 = pg.image.load(f'../please work/up_2.png')
up_ = [up_1, up_2]
idle_1 = pg.image.load(f'idle_1.png')
idle_2 = pg.image.load(f'idle_2.png')
idle_ = [idle_1, idle_2]
down_1 = pg.image.load(f'down_1.png')
down_2 = pg.image.load(f'down_2.png')
down_ = [down_1, down_2]
left_1 = pg.image.load(f'left_1.png')
left_2 = pg.image.load(f'left_2.png')
left_ = [left_1, left_2]
right_1 = pg.image.load(f'right_1.png')
right_2 = pg.image.load(f'right_2.png')
right_ = [right_1, right_2]
golem_frame_1 = pg.transform.scale(pg.image.load(f"fight/frame_1.png"), (50, 50))
golem_frame_2 = pg.transform.scale(pg.image.load(f"fight/frame_2.png"), (50, 50))
golem_frame_3 = pg.transform.scale(pg.image.load(f"fight/frame_3.png"), (50, 50))
golem_frame_4 = pg.transform.scale(pg.image.load(f"fight/frame_4.png"), (50, 50))
golem_frame_5 = pg.transform.scale(pg.image.load(f"fight/frame_5.png"), (50, 50))
golem_frame_ = [golem_frame_1, golem_frame_2, golem_frame_3, golem_frame_4, golem_frame_5]
clock = pg.time.Clock()
clock.tick(60)


class Entity(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pg.transform.scale(pg.image.load("fishes/screamer.jpg").convert(), (45, 45))
        self.rect = self.image.get_rect(center=(x, y))
        self.vector_y = 0
        self.vector_x = 0

    def update(self):
        self.rect.y += self.vector_y
        self.rect.x += self.vector_x

    def stay_still_player(self):
        self.vector_y = 0
        self.vector_x = 0
        current_time = pg.time.get_ticks()
        frame_duration_player = 300
        frame_index_player = (current_time // frame_duration_player) % 2
        self.image = idle_[frame_index_player]

    def stay_still_golem(self):
        self.vector_y = 0
        self.vector_x = 0
        current_time = pg.time.get_ticks()
        frame_duration_golem = 300
        frame_index_golem = (current_time // frame_duration_golem) % 5
        self.image = golem_frame_[frame_index_golem]

    def move_up(self):
        self.vector_y = -3
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 2
        self.image = up_[frame_index]
        if self.image == up_[1] and self.rect.y >= 1:
            walk_sound.play(loops=0, fade_ms=500)

    def move_down(self):
        self.vector_y = + 3
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 2
        self.image = down_[frame_index]
        if self.image == down_[1] and self.rect.y <= 440:
            walk_sound.play(loops=0, fade_ms=500)

    def move_left(self):
        self.vector_x = -3
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 2
        self.image = left_[frame_index]
        if self.image == left_[1] and self.rect.x >= 1:
            walk_sound.play(loops=0, fade_ms=500)

    def move_right(self):
        self.vector_x = + 3
        current_time = pg.time.get_ticks()
        frame_duration = 300
        frame_index = (current_time // frame_duration) % 2
        self.image = right_[frame_index]
        if self.image == right_[1] and self.rect.x < 559:
            walk_sound.play(loops=0, fade_ms=500)
