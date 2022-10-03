class Piece:

    def __init__(self, x, y, isWhite, isKilled):
        self.x = x
        self.y = y
        self.killed = isKilled
        self.white = isWhite
        self.image = r'C:\Users\LiadF\PycharmProjects\Chess\img\128h\b_pawn.png'

    def img(self):
        return self.image

    def move(self, board):
        pass

    def update_pos(self, x, y):
        self.x = x
        self.y = y

    def print_pos(self):
        print("x:{}, y:{}".format(self.x, self.y))

    def piece_name(self):
        print("")