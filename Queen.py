from Piece import Piece
import main


class Queen(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_queen.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_queen.png'

    def img(self):
        return self.image

    def move(self):
        y = self.y
        x = self.x
        stack = []

        for f_x in range(0, 640, 80):
            for f_y in range(0, 640, 80):

                if abs(f_x + f_y) == (x - (2 * main.SHIFT_FOR_PHOTO) + y):
                    stack.append((f_x, f_y))
                if abs(f_x - f_y) == abs(x - y):
                    if (x <= y and f_x <= f_y) or (x >= y and f_x >= f_y):
                        stack.append((f_x, f_y))
                if f_x == (x - main.SHIFT_FOR_PHOTO) or f_y == (y - main.SHIFT_FOR_PHOTO):
                    stack.append((f_x, f_y))

        return stack
