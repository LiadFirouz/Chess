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

        self.display_surface = pygame.display.set_mode((self.surface_width, self.surface_height))
        pygame.display.set_caption('Chess Game')
        image = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\img\chess_board.png')
        self.display_surface.blit(pygame.transform.scale(image, (self.surface_width, self.surface_height)), (0, 0))

        self.board = self.init_board()

    # self.draw_pieces(board=self.board)

    def init_board(self):

        piece = None
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
                    board[row][col].piece = Queen.Queen(x, y, True, False)
                if row == 0 and col == 4:
                    board[row][col].piece = King.King(x, y, True, False)

                if row == 7 and col == 3:
                    board[row][col].piece = King.King(x, y, False, False)
                if row == 7 and col == 4:
                    board[row][col].piece = Queen.Queen(x, y, False, False)

        self.draw(board)
        return board

    def draw(self, board):
        for row in range(board.__len__()):
            for col in range(board.__len__()):
                if board[row][col].piece is not None:
                    image = pygame.image.load(board[row][col].piece.img())
                    self.display_surface.blit(pygame.transform.scale(image, (55, 55)),
                                              (board[row][col].piece.y, board[row][col].piece.x))


    def print_board(self, board):
        print("------------------------------------")
        print("new BOARD:")
        for row in board:
            for obj in row:
                print(obj.__str__())

    def find_Cell(self, dot):
        for i in range(0, 640, CELL_SIZE):
            if i < dot <= i + CELL_SIZE:
                return i // CELL_SIZE

    def choose_cell(self, board, row, col):
        green_frame = pygame.image.load(r'C:\Users\LiadF\PycharmProjects\chessgame\green_fram.png')
        self.display_surface.blit(pygame.transform.scale(green_frame, (CELL_SIZE, CELL_SIZE)),
                                  (
                                      board[row][col].piece.y - SHIFT_FOR_PHOTO,
                                      board[row][col].piece.x - SHIFT_FOR_PHOTO))


def main():
    WIDTH, HEIGHT = 640, 640
    init_game_obj = InitGame(WIDTH, HEIGHT)
    run = True
    #init_game_obj.print_board(init_game_obj.board)
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
                col = init_game_obj.find_Cell(pos[0])
                row = init_game_obj.find_Cell(pos[1])

                if init_game_obj.board[row][col].piece is not None:
                    init_game_obj.choose_cell(board=init_game_obj.board, row=row, col=col)

                    # Draws the surface object to the screen.
        pygame.display.update()


if __name__ == '__main__':
    main()
