from Piece import Piece
import main


class King(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_king.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_king.png'

    def img(self):
        return self.image

    def move(self, board):
        col = main.InitGame.find_cell_by_dot(self, self.y)
        row = main.InitGame.find_cell_by_dot(self, self.x)
        stack = []



        """ for f_x in range(0, 640, 80):
            for f_y in range(0, 640, 80):
                

                if f_x == (x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_y == (y - main.SHIFT_FOR_PHOTO):
                    stack.append((f_x, f_y))
                if f_y == (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO):
                    stack.append((f_x, f_y))
                if f_x == (x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_y == (y - main.SHIFT_FOR_PHOTO):
                    stack.append((f_x, f_y))
                if f_y == (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_x == (x - main.SHIFT_FOR_PHOTO):
                    stack.append((f_x, f_y))
                if f_y == (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_x == (
                        x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE):
                    stack.append((f_x, f_y))
                if f_y == (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_x == (
                        x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE):
                    stack.append((f_x, f_y))

                if f_y == (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) and f_x == (
                        x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE):
                    stack.append((f_x, f_y))
                if f_y == (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) and f_x == (
                        x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE):
                    stack.append((f_x, f_y))"""
        return stack

    def piece_name(self):
        return "King"
