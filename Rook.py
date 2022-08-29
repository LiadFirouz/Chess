from Piece import Piece


class Rook(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_rook.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_rook.png'

    def img(self):
        return self.image
