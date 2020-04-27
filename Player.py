class Player:
    def __init__(self, id, stripList, color):
        self.id = id
        self.currentPosition = 0
        self.stripList = list(stripList)
        self.color = color

    def __repr__(self) -> str:
         return "Player(id={0}, pos={1}, stripList={2}, color={3})".format(self.id, self.currentPosition, self.stripList, self.color)

