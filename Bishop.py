from Piece import Piece
import main


class Bishop(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\w_bishop.png'
        else:
            self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_bishop.png'

    def img(self):
        return self.image

    def move(self):
        y = self.y
        x = self.x
        stack = []

        for f_x in range(0, 640, 80):
            for f_y in range(0, 640, 80):
                print("{} == {}".format(f_x + f_y, x + y))
                if self.white and (f_x - f_y == abs(x - y) or f_x + f_y == abs(x - y)):
                    stack.append((f_x, f_y))
                elif not self.white and (f_y - f_x == abs(x - y) or f_x + f_y == (x + y - (2 * main.SHIFT_FOR_PHOTO))):
                    stack.append((f_x, f_y))

        """stack.append(self.top_right(x, y))
        stack.append(self.bottom_right(x, y))
        #stack.append(self.top_left(x, y))
        stack.append(self.bottom_left(x, y))

        # if not self.white:
        while y <= 640 and x <= 640:
            stack.append((y - main.CELL_SIZE, x - main.CELL_SIZE))
            stack.append((y + main.CELL_SIZE, x - main.CELL_SIZE))

            y += 80
            x += 80
        else:
            stack.append((self.y + main.CELL_SIZE, self.x + main.CELL_SIZE))
            stack.append((self.y - main.CELL_SIZE, self.x + main.CELL_SIZE))"""
        print(stack)
        return stack

    """def top_right(self, x, y):

        if 10 <= x >= 650 or 10 <= y >= 650:
            return
        else:
            return self.top_right(x + main.CELL_SIZE, y - main.CELL_SIZE)
    def top_left(self, x, y):

        if 10 <= x >= 650 or 10 <= y >= 650:
            return
        else:
            return self.top_left(x - main.CELL_SIZE, y - main.CELL_SIZE)

    def bottom_right(self, x, y):

        if 10 <= x >= 650 or 10 <= y >= 650:
            return
        else:
            return self.bottom_right(x + main.CELL_SIZE, y + main.CELL_SIZE)

    def bottom_left(self, x, y):

        if 10 <= x >= 650 or 10 <= y >= 650:
            return
        else:
            return self.bottom_left(x - main.CELL_SIZE, y + main.CELL_SIZE)"""
