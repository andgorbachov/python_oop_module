from random import randint
from exceptions import EnemyDown
from exceptions import GameOver
import settings


# Mag
# Fighter
# Robber


class Enemy(object):
    level = 0
    lives = 3

    def __init__(self, level):
        self.level = level

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise EnemyDown


class Player(object):
    lives = 3
    score = 0
    allowed_attacks = 0

    def __init__(self, name):
        self.name = name

    @staticmethod
    def fight(attack, defense):             # 1, 2, 3
        round_result = 0
        if attack == defense:
            round_result = 0
        elif attack == 1 and defense == 2:
            round_result = 1                    # 0, -1, 1
        elif attack == 1 and defense == 3:
            round_result = -1
        elif attack == 2 and defense == 1:
            round_result = -1
        elif attack == 2 and defense == 3:
            round_result = 1
        elif attack == 3 and defense == 1:
            round_result = 1
        elif attack == 3 and defense == 2:
            round_result = -1
        return round_result

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise GameOver

    def attack(self, enemy_obj):
        while True:
            print(settings.enter_attack_message)
            player_attack = input()
            if player_attack in ('1', '2', '3'):
                break
        enemy_attack = enemy_obj.select_attack()
        result = self.fight(int(player_attack), enemy_attack)
        if result == 0:
            print(settings.draw_message)
        elif result == 1:
            print(settings.win_message)
            self.score += 1
            enemy_obj.decrease_lives()
        else:
            print(settings.defeat_message)
            self.decrease_lives()

    def defence(self, enemy_obj):
        while True:
            print(settings.enter_defense_message)
            player_defence = input()
            if player_defence in ('1', '2', '3'):
                break
        enemy_attack = enemy_obj.select_attack()
        result = self.fight(int(player_defence), enemy_attack)
        if result == 0:
            print(settings.draw_message)
        elif result == 1:
            print(settings.win_message)
            self.score += 1
            enemy_obj.decrease_lives()
        else:
            print(settings.defeat_message)
            self.decrease_lives()
