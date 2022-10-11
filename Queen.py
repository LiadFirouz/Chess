from Piece import Piece
import main


class Queen(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/w_queen.png'
        else:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/b_queen.png'

    def img(self):
        return self.image

    def move(self, board):
        y = self.y - main.SHIFT_FOR_PHOTO
        x = self.x - main.SHIFT_FOR_PHOTO
        stack = []

        f_x = x
        f_y_p = y + main.CELL_SIZE
        f_y_m = y - main.CELL_SIZE
        bump_into_x_p = False
        bump_into_x_m = False
        while f_y_p <= 560 or f_y_m >= 0:
            if f_y_p <= 560 and not bump_into_x_p:
                stack.append((f_x, f_y_p))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][
                    main.InitGame.find_cell_by_dot(self, f_y_p)].piece is not None:
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][
                        main.InitGame.find_cell_by_dot(self, f_y_p)].piece.white is self.white:
                        stack.pop()
                    bump_into_x_p = True
            f_y_p += main.CELL_SIZE

            if f_y_m >= 0 and not bump_into_x_m:
                stack.append((f_x, f_y_m))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][
                    main.InitGame.find_cell_by_dot(self, f_y_m)].piece is not None:
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][
                        main.InitGame.find_cell_by_dot(self, f_y_m)].piece.white is self.white:
                        stack.pop()
                    bump_into_x_m = True
            f_y_m -= main.CELL_SIZE

            f_y = y
            f_x_p = x + main.CELL_SIZE
            f_x_m = x - main.CELL_SIZE
            bump_into_y_p = False
            bump_into_y_m = False
            while f_x_p <= 560 or f_x_m >= 0:
                if f_x_p <= 560 and not bump_into_y_p:
                    stack.append((f_x_p, f_y))
                    if board[main.InitGame.find_cell_by_dot(self, f_x_p)][
                        main.InitGame.find_cell_by_dot(self, f_y)].piece is not None:
                        if board[main.InitGame.find_cell_by_dot(self, f_x_p)][
                            main.InitGame.find_cell_by_dot(self, f_y)].piece.white is self.white:
                            stack.pop()
                        bump_into_y_p = True
                f_x_p += main.CELL_SIZE

                if f_x_m >= 0 and not bump_into_y_m:
                    stack.append((f_x_m, f_y))
                    if board[main.InitGame.find_cell_by_dot(self, f_x_m)][
                        main.InitGame.find_cell_by_dot(self, f_y)].piece is not None:
                        if board[main.InitGame.find_cell_by_dot(self, f_x_m)][
                            main.InitGame.find_cell_by_dot(self, f_y)].piece.white is self.white:
                            stack.pop()
                        bump_into_y_m = True
                f_x_m -= main.CELL_SIZE

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
        f_x = x + main.CELL_SIZE
        f_y_p = y + main.CELL_SIZE
        f_y_m = y - main.CELL_SIZE
        bump_into_x_p = False
        bump_into_x_m = False
        while f_x <= 560:
            if f_y_p <= 560 and not bump_into_x_p:
                stack.append((f_x, f_y_p))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][
                    main.InitGame.find_cell_by_dot(self, f_y_p)].piece is not None:
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][
                        main.InitGame.find_cell_by_dot(self, f_y_p)].piece.white is self.white:
                        stack.pop()
                    bump_into_x_p = True
                f_y_p += main.CELL_SIZE

            if f_y_m >= 0 and not bump_into_x_m:
                stack.append((f_x, f_y_m))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][
                    main.InitGame.find_cell_by_dot(self, f_y_m)].piece is not None:
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][
                        main.InitGame.find_cell_by_dot(self, f_y_m)].piece.white is self.white:
                        stack.pop()
                    bump_into_x_m = True
                f_y_m -= main.CELL_SIZE
            f_x += main.CELL_SIZE

        f_x = x - main.CELL_SIZE
        f_y_p = y + main.CELL_SIZE
        f_y_m = y - main.CELL_SIZE
        bump_into_x_p = False
        bump_into_x_m = False
        while f_x >= 0:
            if f_y_p <= 560 and not bump_into_x_p:
                stack.append((f_x, f_y_p))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][
                    main.InitGame.find_cell_by_dot(self, f_y_p)].piece is not None:
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][
                        main.InitGame.find_cell_by_dot(self, f_y_p)].piece.white is self.white:
                        stack.pop()
                    bump_into_x_p = True
                f_y_p += main.CELL_SIZE

            if f_y_m >= 0 and not bump_into_x_m:
                stack.append((f_x, f_y_m))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][
                    main.InitGame.find_cell_by_dot(self, f_y_m)].piece is not None:
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][
                        main.InitGame.find_cell_by_dot(self, f_y_m)].piece.white is self.white:
                        stack.pop()
                    bump_into_x_m = True
                f_y_m -= main.CELL_SIZE
            f_x -= main.CELL_SIZE


        """y = self.y
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
                    stack.append((f_x, f_y))"""

        return stack

    def piece_name(self):
        return "Queen"
