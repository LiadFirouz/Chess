import pygame

import Bishop
import King
import Knight
import Pawn
import Piece
import Queen
import Rook
import Spot

pygame.init()

SHIFT_FOR_PHOTO = 10
CELL_SIZE = 80


class InitGame:

    def __init__(self, width, height):
        self.surface_width = width
        self.surface_height = height

        # self.display_surface = pygame.display.set_mode((self.surface_width, self.surface_height))
        # pygame.display.set_caption('Chess Game')
        # image = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\chess_board.png')
        # self.display_surface.blit(pygame.transform.scale(image, (self.surface_width, self.surface_height)), (0, 0))

        self.board = self.init_board()
        # self.print_board(board=self.board)

    def init_board(self):
        "initialize the game board in the matrix"

        board = [[Spot.Spot(Piece.Piece, row, col) for col in range(8)] for row in range(8)]

        for row in range(8):
            x = (SHIFT_FOR_PHOTO + 80 * row)
            for col in range(8):
                y = (SHIFT_FOR_PHOTO + 80 * col)
                board[row][col].piece = None
                isWhite = False

                if row == 1:
                    board[row][col].piece = Pawn.Pawn(x, y, True, False)
                if row == 6:
                    board[row][col].piece = Pawn.Pawn(x, y, False, False)

                if row == 0 or row == 7:
                    if row == 0:
                        isWhite = True
                    if col == 0 or col == 7:
                        board[row][col].piece = Rook.Rook(x, y, isWhite, False)
                    if col == 1 or col == 6:
                        board[row][col].piece = Knight.Knight(x, y, isWhite, False)
                    if col == 2 or col == 5:
                        board[row][col].piece = Bishop.Bishop(x, y, isWhite, False)

                if row == 0 and col == 3:
                    board[row][col].piece = King.King(x, y, True, False)
                if row == 0 and col == 4:
                    board[row][col].piece = Queen.Queen(x, y, True, False)

                if row == 7 and col == 3:
                    board[row][col].piece = King.King(x, y, False, False)
                if row == 7 and col == 4:
                    board[row][col].piece = Queen.Queen(x, y, False, False)

        self.draw(board)
        return board

    def draw(self, board):
        "draw the pieces on the game board"
        self.display_surface = pygame.display.set_mode((self.surface_width, self.surface_height))
        pygame.display.set_caption('Chess Game')
        image = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\chess_board.png')
        self.display_surface.blit(pygame.transform.scale(image, (self.surface_width, self.surface_height)), (0, 0))

        for row in range(board.__len__()):
            for col in range(board.__len__()):
                if board[row][col].piece is not None:
                    image = pygame.image.load(board[row][col].piece.img())
                    self.display_surface.blit(pygame.transform.scale(image, (55, 55)),
                                              (board[row][col].piece.y, board[row][col].piece.x))

    def print_board(self, board):
        "print the matrix in the CLI"
        print("new BOARD:")
        print("------------------------------------")
        for row in board:
            for obj in row:
                if obj is not None:
                    print(obj.piece.x, obj.piece.y)

    def find_Cell_by_dot(self, dot):
        "find the position click of the mouse on the board"
        for i in range(0, 640, CELL_SIZE):
            if i < dot <= i + CELL_SIZE:
                return i // CELL_SIZE

    def get_cell_center_pos(self, row, col):
        x = row * CELL_SIZE
        y = col * CELL_SIZE
        return x, y

    def possible_move_colored_cell(self, board, row, col):
        "color the selected cell by click"
        # x, y = (self.get_cell_center_pos(row, col))
        # print("{},{}".format(x, y))
        green_frame = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\green_fram.png')
        self.display_surface.blit(pygame.transform.scale(green_frame, (CELL_SIZE, CELL_SIZE)), (col, row))


def main():
    WIDTH, HEIGHT = 640, 640
    init_game_obj = InitGame(WIDTH, HEIGHT)
    run = True
    hasClicked = False
    # init_game_obj.print_board(init_game_obj.board)
    while run:

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.

        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = init_game_obj.find_Cell_by_dot(pos[0])
                row = init_game_obj.find_Cell_by_dot(pos[1])
                # print(init_game_obj.board[row][col].piece.print_pos())
                if init_game_obj.board[row][col].piece is not None:

                    if hasClicked:
                        init_game_obj.draw(init_game_obj.board)
                        pygame.display.update()
                        hasClicked = False

                    piece_row = row
                    piece_col = col
                    stack = init_game_obj.board[row][col].piece.move()

                    while stack:
                        (x, y) = stack.pop()
                        init_game_obj.possible_move_colored_cell(board=init_game_obj.board, row=y, col=x)

                    hasClicked = True

                if hasClicked and init_game_obj.board[row][col].piece is None:
                    (x, y) = init_game_obj.get_cell_center_pos(row, col)

                    init_game_obj.board[piece_row][piece_col].piece.x = x + SHIFT_FOR_PHOTO
                    init_game_obj.board[piece_row][piece_col].piece.y = y + SHIFT_FOR_PHOTO

                    init_game_obj.board[row][col].piece = init_game_obj.board[piece_row][piece_col].piece
                    init_game_obj.board[piece_row][piece_col].piece = None

                    print(init_game_obj.board[row][col].piece.print_pos())
                    init_game_obj.draw(init_game_obj.board)
                    hasClicked = False
        # Draws the surface object to the screen.
        pygame.display.update()


if __name__ == '__main__':
    main()
