START_UP_FUNCTION=0
SHOW_ALL = 1
RAINBOW = 2
PRINT_USER=98
EXIT=99


class Message:
    def __init__(self, command, player=0):
        self.player=player
        self.command = command
