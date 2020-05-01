class Player:
    def __init__(self, id, stripList, color):
        self.id = id
        self.lastPosition = -1
        self.currentPosition = -1
        self.stripList = list(stripList)
        self.color = color

    def __repr__(self) -> str:
        return "Player(id={0}, lastPos={1}, pos={2}, stripList={3}, color={4})".format(self.id, self.lastPosition,
                                                                                       self.currentPosition,
                                                                                       self.stripList, self.color)
