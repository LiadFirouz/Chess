from Piece import Piece
import main

class Knight(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)
        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_knight.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_knight.png'

    def img(self):
        return self.image

    def move(self):
        y = self.y
        x = self.x
        stack = []

        for f_x in range(0, 640, 80):
            for f_y in range(0, 640, 80):

                if f_x == ((y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) or (y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE)) and f_y == ((x - main.SHIFT_FOR_PHOTO - (2 * main.CELL_SIZE)) or (x - main.SHIFT_FOR_PHOTO + (2 * main.CELL_SIZE))):
                    stack.append((f_x, f_y))
                if f_x == ((y - main.SHIFT_FOR_PHOTO + (2 * main.CELL_SIZE)) or (y - main.SHIFT_FOR_PHOTO - (2 * main.CELL_SIZE))) and f_y == ((x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) or (x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE)):
                    stack.append((f_x, f_y))

                if f_x == ((x - main.SHIFT_FOR_PHOTO + main.CELL_SIZE) or (x - main.SHIFT_FOR_PHOTO - main.CELL_SIZE)) and f_y == ((y - main.SHIFT_FOR_PHOTO - (2 * main.CELL_SIZE)) or (y - main.SHIFT_FOR_PHOTO + (2 * main.CELL_SIZE))):
                    stack.append((f_y, f_x))
                if f_x == ((x - main.SHIFT_FOR_PHOTO + (2 * main.CELL_SIZE)) or (x - main.SHIFT_FOR_PHOTO - (2 * main.CELL_SIZE))) and f_y == ((y - main.SHIFT_FOR_PHOTO - main.CELL_SIZE) or (y - main.SHIFT_FOR_PHOTO + main.CELL_SIZE)):
                    stack.append((f_y, f_x))

        print(stack)
        return stack
