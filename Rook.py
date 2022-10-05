from Piece import Piece
import main


class Rook(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)

        if isWhite:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/w_rook.png'
        else:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/b_rook.png'

    def img(self):
        return self.image

    def move(self, board):
        y = self.y - main.SHIFT_FOR_PHOTO
        x = self.x - main.SHIFT_FOR_PHOTO
        stack = []

        f_x = x + main.CELL_SIZE
        bump_into_x = False
        while f_x <= 560:
            if not bump_into_x:
                stack.append((f_x, y))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][main.InitGame.find_cell_by_dot(self, y)].piece is not None:
                    bump_into_x = True
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][main.InitGame.find_cell_by_dot(self, y)].piece.white is self.white:
                        stack.pop()
            f_x += main.CELL_SIZE

        f_x = x - main.CELL_SIZE
        bump_into_x = False
        while f_x >= 0:
            if not bump_into_x:
                stack.append((f_x, y))
                if board[main.InitGame.find_cell_by_dot(self, f_x)][
                    main.InitGame.find_cell_by_dot(self, y)].piece is not None:
                    bump_into_x = True
                    if board[main.InitGame.find_cell_by_dot(self, f_x)][
                        main.InitGame.find_cell_by_dot(self, y)].piece.white is self.white:
                        stack.pop()
            f_x -= main.CELL_SIZE

        f_y = y + main.CELL_SIZE
        bump_into_y = False
        while f_y <= 560:
            if not bump_into_x:
                stack.append((x, f_y))
                if board[main.InitGame.find_cell_by_dot(self, x)][
                    main.InitGame.find_cell_by_dot(self, f_y)].piece is not None:
                    bump_into_y = True
                    if board[main.InitGame.find_cell_by_dot(self, x)][
                        main.InitGame.find_cell_by_dot(self, f_y)].piece.white is self.white:
                        stack.pop()
            f_y += main.CELL_SIZE

        f_y = y - main.CELL_SIZE
        bump_into_y = False
        while f_y >= 0:
            if not bump_into_y:
                stack.append((x, f_y))
                if board[main.InitGame.find_cell_by_dot(self, x)][
                    main.InitGame.find_cell_by_dot(self, f_y)].piece is not None:
                    bump_into_y = True
                    if board[main.InitGame.find_cell_by_dot(self, x)][
                        main.InitGame.find_cell_by_dot(self, f_y)].piece.white is self.white:
                        stack.pop()
            f_y -= main.CELL_SIZE

        return stack


    def piece_name(self):
        return "Rook"
