START_UP_FUNCTION = 0
OPTION_CHOOSE = 3
SET_NEW_POINT = 4
PARTY = 5
PARTY_2 = 6
PRINT_USER = 50
CLEAR = 97
WAIT = 98
EXIT = 99


class Message:
    def __init__(self, command, data=0):
        self.data = data
        self.command = command

    def __repr__(self) -> str:
        return "Message(data=({0}), command=({1}))".format(self.data, self.command)
