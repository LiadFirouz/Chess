from Piece import Piece
import main


class Pawn(Piece):

    def __init__(self, x, y, isWhite, isKilled):
        super().__init__(x, y, isWhite, isKilled)
        if isWhite:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/w_pawn.png'
        else:
            self.image = r'/home/liadfirouz/PycharmProjects/Chess/img/128h/b_pawn.png'

    def img(self):
        return self.image

    def move(self, board):
        stack = []
        f_x = self.x - main.SHIFT_FOR_PHOTO
        f_y = self.y - main.SHIFT_FOR_PHOTO

        if not self.white:
            left = (f_x - main.CELL_SIZE, f_y - main.CELL_SIZE)
            right = (f_x + main.CELL_SIZE, f_y - main.CELL_SIZE)

            if f_y - main.CELL_SIZE > -main.CELL_SIZE and not None:
                if board[main.InitGame.find_cell_by_dot(self, f_x)][main.InitGame.find_cell_by_dot(self, f_y - main.CELL_SIZE)].piece is None:
                    stack.append((f_x, f_y - main.CELL_SIZE))
                if left[0] >= 0:
                    if board[main.InitGame.find_cell_by_dot(self, left[0])][main.InitGame.find_cell_by_dot(self, left[1])].piece is not None and \
                            board[main.InitGame.find_cell_by_dot(self, left[0])][main.InitGame.find_cell_by_dot(self, left[1])].piece.white is not self.white:
                        stack.append(left)
                if  right[0] <= 560:
                    if board[main.InitGame.find_cell_by_dot(self, right[0])][main.InitGame.find_cell_by_dot(self, right[1])].piece is not None and \
                            board[main.InitGame.find_cell_by_dot(self, right[0])][main.InitGame.find_cell_by_dot(self, right[1])].piece is not self.white:
                        stack.append(right)

        else:
            left = (f_x - main.CELL_SIZE, f_y + main.CELL_SIZE)
            right = (f_x + main.CELL_SIZE, f_y + main.CELL_SIZE)

            if f_y + main.CELL_SIZE < 640 and not None:
                if board[main.InitGame.find_cell_by_dot(self, f_x)][main.InitGame.find_cell_by_dot(self, f_y + main.CELL_SIZE)].piece is None:
                    stack.append((f_x, f_y + main.CELL_SIZE))
                if left[0] >= 0:
                    if board[main.InitGame.find_cell_by_dot(self, left[0])][main.InitGame.find_cell_by_dot(self, left[1])].piece is not None and \
                            board[main.InitGame.find_cell_by_dot(self, left[0])][main.InitGame.find_cell_by_dot(self, left[1])].piece.white is not self.white:
                        stack.append(left)
                if right[0] <= 560:
                    if board[main.InitGame.find_cell_by_dot(self, right[0])][main.InitGame.find_cell_by_dot(self, right[1])].piece is not None and \
                            board[main.InitGame.find_cell_by_dot(self, right[0])][main.InitGame.find_cell_by_dot(self, right[1])].piece.white is not self.white:
                        stack.append(right)

        return stack

    def piece_name(self):
        return "Pawn"
