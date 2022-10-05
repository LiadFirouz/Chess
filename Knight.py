from Piece import Piece
import main

class Knight(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)
        if isWhite:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/w_knight.png'
        else:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/b_knight.png'

    def img(self):
        return self.image

    def move(self, board):
        y = self.y
        x = self.x
        stack = []

        for f_y in range(0, 640, 80):
            for f_x in range(0, 640, 80):

                if (x - main.SHIFT_FOR_PHOTO + (2 * main.CELL_SIZE)) == f_x or (x - main.SHIFT_FOR_PHOTO - (2 * main.CELL_SIZE)) == f_x:
                    if (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) == f_y or (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) == f_y:
                        stack.append((f_x, f_y))
                if (y - main.SHIFT_FOR_PHOTO + (2 * main.CELL_SIZE)) == f_y or (y - main.SHIFT_FOR_PHOTO - (2 * main.CELL_SIZE)) == f_y:
                    if (x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) == f_x or (x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) == f_x:
                        stack.append((f_x, f_y))

        #print(stack)
        return stack

    def piece_name(self):
        return "Knight"