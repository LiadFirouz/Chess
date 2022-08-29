from Piece import Piece


class Bishop(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_bishop.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_bishop.png'

    def img(self):
        return self.image
