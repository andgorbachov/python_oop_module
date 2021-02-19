from exceptions import EnemyDown
from exceptions import GameOver
from helper import HelperManager
from models import Player
from models import Enemy
import settings


def play(player):
    level = 1
    enemy = Enemy(level)
    while True:
        player.attack(enemy)
        player.defence(enemy)


if __name__ == '__main__':
    print(settings.enter_name_message)
    player_name = input()
    gamePlayer = Player(player_name)
    try:
        print(settings.welcome_message)
        while True:
            user_input = input()
            HelperManager.manage_input(user_input, play, gamePlayer)
    except GameOver:
        print(settings.game_over_message)
        f = open('scores.txt', 'a+')
        f.write(f'Player - {gamePlayer.name}: Scores - {gamePlayer.score}\n')
        f.close()
        print(f'{settings.result_message}{gamePlayer.score}')
    except EnemyDown:
        # level += 1
        gamePlayer.score += 5
        f = open('scores.txt', 'a+')
        f.write(f'Player - {gamePlayer.name}: Scores - {gamePlayer.score}\n')
        f.close()
        print(f'You won!. {settings.result_message}{gamePlayer.score}')
    except KeyboardInterrupt:
        pass
    finally:
        print(settings.good_bye_message)
