from Piece import Piece
import main

class Pawn(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)
        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_pawn.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_pawn.png'

    def img(self):
        return self.image

    def move(self):
        stack = []
        print(self.x, self.y)
        if not self.white:
            pos = (self.x - main.SHIFT_FOR_PHOTO, self.y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE)

        else:
            pos = (self.x - main.SHIFT_FOR_PHOTO, self.y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE)

        stack.append(pos)
        return stack
