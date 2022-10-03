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

    def move(self, board):
        stack = []
        pos_x = self.x - main.SHIFT_FOR_PHOTO
        pos_y = self.y - main.SHIFT_FOR_PHOTO

        if not self.white:
            left = (pos_x - main.CELL_SIZE, pos_y - main.CELL_SIZE)
            right = (pos_x + main.CELL_SIZE, pos_y - main.CELL_SIZE)

            if pos_y - main.CELL_SIZE > -main.CELL_SIZE and not None:
                if board[main.InitGame.find_cell_by_dot(self, pos_x)][
                    main.InitGame.find_cell_by_dot(self, pos_y - main.CELL_SIZE)].piece is None:
                    stack.append((pos_x, pos_y - main.CELL_SIZE))
                if board[main.InitGame.find_cell_by_dot(self, left[0])][
                    main.InitGame.find_cell_by_dot(self, left[1])].piece is not None and not main.WHITE_PLAYER:
                    stack.append(left)
                if board[main.InitGame.find_cell_by_dot(self, right[0])][
                    main.InitGame.find_cell_by_dot(self, right[1])].piece is not None and not main.WHITE_PLAYER:
                    stack.append(right)

        else:
            left = (pos_x - main.CELL_SIZE, pos_y + main.CELL_SIZE)
            right = (pos_x + main.CELL_SIZE, pos_y + main.CELL_SIZE)
            if pos_y + main.CELL_SIZE < 640 and not None:
                if board[main.InitGame.find_cell_by_dot(self, pos_x)][
                    main.InitGame.find_cell_by_dot(self, pos_y + main.CELL_SIZE)].piece is None:
                    stack.append((pos_x, pos_y + main.CELL_SIZE))
                if board[main.InitGame.find_cell_by_dot(self, left[0])][
                    main.InitGame.find_cell_by_dot(self, left[1])].piece is not None and not main.WHITE_PLAYER:
                    stack.append(left)
                if board[main.InitGame.find_cell_by_dot(self, right[0])][
                    main.InitGame.find_cell_by_dot(self, right[1])].piece is not None and not main.WHITE_PLAYER:
                    stack.append(right)

        return stack

    def piece_name(self):
        return "Pawn"
