SHIFT_FOR_PHOTO = 20
CELL_SIZE = 80


class Spot:

    def __init__(self, piece, row, col):
        self.piece = piece
        self.row = row
        self.col = col

    def __str__(self):
        print(f"piece: {self.piece}, row:{self.row}, col: {self.col}")
