class Piece:

    def __init__(self, x, y, isWhite, isKilled):
        self.x = x
        self.y = y
        self.killed = isKilled
        self.white = isWhite
        self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_pawn.png'

    def img(self):
        return self.image

    def move(self):
        pass
