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
            self.dmg = random.randint(5, 25)
            if self.dmg < 10:
                print(f'{self.name} промахивается ')
            else:
                current_dmg = self.dmg - objective.defense
                objective.hp -= current_dmg
                print(f'{self.name} атаковал Стража Вулкана\n'
                      f'{objective.name} потерял {current_dmg} здоровья \n'
                      f'У Стража Вулкана осталось {objective.hp} \n')
        else:
            if self.weapon == 'obsidian_sword':
                self.dmg = random.randint(15, 25)
            if self.weapon == 'jelly_fish_sword':
                self.dmg = random.randint(35, 50)
            if self.weapon == 'Volcano':
                self.dmg = random.randint(70, 90)
            current_dmg = self.dmg + 50 - objective.defense
            objective.hp -= current_dmg
            print(f'{self.name} атаковал Стража Вулкана, используя {self.weapon} \n'
                  f'{objective.name} потерял {current_dmg} здоровья \n'
                  f'У Стража Вулкана осталось {objective.hp} \n')

    def pick_move(self, objective):
        if not self.dead:
            if random.randint(1, 5) == 1:
                heal_amount = random.randint(15, 25)
                self.hp += heal_amount
                print(f'{self.name} исцеляет себя на {heal_amount}\n')
                return 'heal'
            if random.randint(1, 5) == 2:
                self.dmg = 30
                current_dmg = self.dmg - objective.defense
                objective.hp -= current_dmg
                print(f'{self.name} атаковал Кота лёгким замахом\n'
                      f'{objective.name} потерял {current_dmg} здоровья \n'
                      f'У Кота осталось {objective.hp} \n')
                return 'light attack'
            if random.randint(1, 5) == 3:
                self.dmg = 50
                current_dmg = self.dmg - objective.defense
                objective.hp -= current_dmg
                print(f'{self.name} атаковал Кота тяжёлым замахом\n'
                      f'{objective.name} потерял {current_dmg} здоровья \n'
                      f'У Кота осталось {objective.hp} \n')
                return 'heavy attack'
            if random.randint(1, 5) == 4:
                self.dmg = 80
                current_dmg = self.dmg - objective.defense

                print(f'{self.name} заряжает луч силы\n'
                      f'Берегись!')
                if random.randint(1, 2) == 1:
                    objective.hp -= current_dmg
                    print(f'{objective.name} попал под луч и потерял 80 здоровья\n')
                    return 'FORCE BEAM'
                else:
                    print(f'{objective.name} увернулся от луча\n')
                    return 'FORCE BEAM'
            if random.randint(1, 5) == 5:
                print(f'{self.name} промахивается\n')
                return 'miss'

    def сheck_for_death(self):
        if self.hp < 0:
            self.dead = True
            print(f'{self.name} проиграл\n')

    def use_potion(self, item):
        if item < 0:
            print(f"У {self.name}а не осталось {item.name}")
        else:
            self.hp += 30
            print(f"{self.name} использовал Зелье Здоровья\n"
                  f"{self.name} востановил 30 Здоровья\n"
                  f"У {self.name}а осталось {self.hp}\n")
