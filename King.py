from Piece import Piece
import main


class King(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/w_king.png'
        else:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/b_king.png'

    def img(self):
        return self.image

    def move(self, board):
        y = self.y
        x = self.x
        stack = []

        for f_x in range(0, 640, 80):
            for f_y in range(0, 640, 80):
                flag = False

                if f_x == (x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_y == (y - main.SHIFT_FOR_PHOTO):
                    flag = True
                if f_y == (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO):
                    flag = True
                if f_x == (x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_y == (y - main.SHIFT_FOR_PHOTO):
                    flag = True
                if f_y == (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO):
                    flag = True
                if f_y == (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE):
                    flag = True
                if f_y == (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE):
                    flag = True
                if f_y == (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE):
                    flag = True
                if f_y == (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE):
                    flag = True

                if flag and board[main.InitGame.find_cell_by_dot(self, f_x)][main.InitGame.find_cell_by_dot(self, f_y)].piece is not None:
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][main.InitGame.find_cell_by_dot(self, f_y)].piece.white is not self.white:
                        stack.append((f_x, f_y))
                elif flag:
                    stack.append((f_x, f_y))

        return stack

    def piece_name(self):
        return "King"
