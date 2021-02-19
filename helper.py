import settings
from exceptions import GameOver


class HelperManager(object):
    @staticmethod
    def manage_input(user_inp, play=None, player=None):
        while True:
            if user_inp in (1, 2, 3):
                break
            if user_inp == settings.start_command_message:
                play(player)
                break
            elif user_inp == settings.help_command_message:
                HelperManager.show_commands()
                break
            elif user_inp == settings.show_scores_command_message:
                HelperManager.show_scores()
                break
            elif user_inp == settings.exit_command_message:
                raise GameOver

    @staticmethod
    def show_commands():
        commands = []
        f = open('settings.py', 'r+')
        for i, line in enumerate(f):
            if 'command' in line:
                commands.append(line)
        f.close()
        print(commands)
        return commands

    @staticmethod
    def show_scores():
        scores = []
        f = open('scores.txt', 'r+')
        for i, line in enumerate(f):
            scores.append(line)
        f.close()
        print(scores)
        return scores
