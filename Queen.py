from Piece import Piece


class Queen(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_queen.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_queen.png'

    def img(self):
        return self.image
