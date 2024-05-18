import pygame as pg
import random

pg.init()
pg.mixer.init()


class Player:

    def __init__(self, name, health, defense, weapon):
        self.name = name
        self.hp = health
        self.dmg = 15
        self.defense = defense
        self.dead = False
        self.weapon = weapon

    def attack_using_weapon(self, objective):
        if self.weapon == 'None':
            self.dmg = 5
            current_dmg = self.dmg - objective.defense
            objective.hp -= current_dmg
            print(f'{self.name} атаковал {objective.name}, используя лапки \n'
                  f'{objective.name} потерял {current_dmg} здоровья \n'
                  f'Осталось у {objective.name} осталось {objective.hp} \n')
        if self.weapon == 'obsidian_sword':
            self.dmg = random.randint(15, 25)
        if self.weapon == 'jelly_fish_sword':
            self.dmg = random.randint(35, 50)
        if self.weapon == 'Volcano':
            self.dmg = random.randint(70, 90)
        current_dmg = self.dmg + 50 - objective.defense
        objective.hp -= current_dmg
        print(f'{self.name} атаковал {objective.name}, используя {self.weapon} \n'
              f'{objective.name} потерял {current_dmg} здоровья \n'
              f'У {objective.name} осталось {objective.hp} \n')

    def pick_move(self, objective):
        if random.randint(1, 5) == 1:
            return 'block'
        if random.randint(1, 5) == 2:
            return 'dodge'
        if random.randint(1, 5) == 3:
            self.dmg = 20
            current_dmg = self.dmg - objective.defense
            objective.hp -= current_dmg
            print(f'{self.name} атаковал {objective.name} лёгким замахом\n'
                  f'{objective.name} потерял {current_dmg} здоровья \n'
                  f'У {objective.name} осталось {objective.hp} \n')
            return 'light attack'
        if random.randint(1, 5) == 4:
            self.dmg = 45
            current_dmg = self.dmg - objective.defense
            objective.hp -= current_dmg
            print(f'{self.name} атаковал {objective.name} тяжёлым замахом\n'
                  f'{objective.name} потерял {current_dmg} здоровья \n'
                  f'У {objective.name} осталось {objective.hp} \n')
            return 'heavy attack'
        if random.randint(1, 5) == 5:
            self.dmg = 80
            current_dmg = self.dmg - objective.defense
            objective.hp -= current_dmg
            print(f'{self.name} заряжает луч силы\n'
                  f'Берегись!')
            return 'FORCE BEAM'

    def сheck_for_death(self):
        if self.hp <= 0:
            print(f'{self.name} умер \n')
            self.dead = True

    def use(self, item):
        self.hp += item.hp
        print(f"{self.name}, использовал {item.name}")
