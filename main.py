import tkinter
from _curses import window

import pygame
from tkinter import *

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
WHITE_PLAYER = False


class InitGame:

    def __init__(self, width, height):
        self.surface_width = width
        self.surface_height = height
        self.board = self.init_board()

    def init_board(self):
        """initialize the game board in the matrix"""
        board = [[Spot.Spot(Piece.Piece, row, col) for row in range(8)] for col in range(8)]

        for row in range(8):
            x = (SHIFT_FOR_PHOTO + 80 * row)
            for col in range(8):
                y = (SHIFT_FOR_PHOTO + 80 * col)
                board[row][col].piece = None
                isWhite = False

                if col == 1:
                    board[row][col].piece = Pawn.Pawn(x, y, True, False)
                if col == 6:
                    board[row][col].piece = Pawn.Pawn(x, y, False, False)

                if col == 0 or col == 7:
                    if col == 0:
                        isWhite = True
                    if row == 0 or row == 7:
                        board[row][col].piece = Rook.Rook(x, y, isWhite, False)
                    if row == 1 or row == 6:
                        board[row][col].piece = Knight.Knight(x, y, isWhite, False)
                    if row == 2 or row == 5:
                        board[row][col].piece = Bishop.Bishop(x, y, isWhite, False)

                if col == 0 and row == 3:
                    board[row][col].piece = King.King(x, y, True, False)
                if col == 0 and row == 4:
                    board[row][col].piece = Queen.Queen(x, y, True, False)

                if col == 7 and row == 3:
                    board[row][col].piece = King.King(x, y, False, False)
                if col == 7 and row == 4:
                    board[row][col].piece = Queen.Queen(x, y, False, False)

        # self.print_board_in_CLI(board)
        self.draw(board)
        return board

    def draw(self, board):
        "draw the pieces on the game board"
        self.display_surface = pygame.display.set_mode((self.surface_width, self.surface_height))
        pygame.display.set_caption('Chess Game')
        image = pygame.image.load(r'/home/liadfirouz/PycharmProjects/Chess/img/chess_board.png')
        self.display_surface.blit(pygame.transform.scale(image, (self.surface_width, self.surface_height)), (0, 0))
        # self.print_board_in_CLI(board)
        for col in range(board.__len__()):
            for row in range(board.__len__()):
                if board[row][col].piece is not None:
                    image = pygame.image.load(board[row][col].piece.img())
                    self.display_surface.blit(pygame.transform.scale(image, (55, 55)),
                                              (board[row][col].piece.x, board[row][col].piece.y))
        # self.print_board_in_CLI(board)

    def print_board_in_CLI(self, board):
        """print the matrix in the CLI"""
        print("BOARD:")
        for col in range(8):
            for row in range(8):
                if board[row][col].piece is not None:
                    print(board[row][col].piece.piece_name(), end='| ')
                else:
                    print("none", end='|')
            print('\n')
        print("_________________________________________________________")

    def find_cell_by_dot(self, dot):
        """find the position click of the mouse on the board"""
        for i in range(0, 640, CELL_SIZE):
            if i <= dot <= (i + CELL_SIZE) - 1:
                return i // CELL_SIZE

    def get_cell_center_by_positions(self, row, col):
        x = row * CELL_SIZE
        y = col * CELL_SIZE
        return x, y

    def select_possible_next_move(self, board, x, y, player_color):
        "color the selected cell by click"
        green_frame = pygame.image.load(r'/home/liadfirouz/PycharmProjects/Chess/img/green_frame.png')
        self.display_surface.blit(pygame.transform.scale(green_frame, (CELL_SIZE, CELL_SIZE)), (x, y))

    def replacement_window(self):
        "selection window for switching the pawn"

        root = Tk()
        root.title("Switch your pawn")
        root.resizable(width=False, height=False)
        #x = root.winfo_x()/2
        #root.geometry("+%d+%d" % (x, y))
        root.eval('tk::PlaceWindow . center')
        v = tkinter.StringVar()

        Radiobutton(root,font='Helvetica 20 bold italic', text="Queen", variable=v, value="Queen", indicator=0, bg='#33383b', fg='white', command=root.destroy, height=5, width=10).pack( side=LEFT)
        Radiobutton(root,font='Helvetica 20 bold italic', text="Rook", variable=v, value="Rook", indicator=0, bg='#33383b', fg='white', command=root.destroy, height=5, width=10).pack(side=LEFT)
        Radiobutton(root,font='Helvetica 20 bold italic', text="Bishop", variable=v, value="Bishop", indicator=0, bg='#33383b', fg='white', command=root.destroy, height=5, width=10).pack( side=LEFT)
        Radiobutton(root,font='Helvetica 20 bold italic', text="Knight", variable=v, value="Knight", indicator=0, bg='#33383b', fg='white', command=root.destroy, height=5, width=10).pack( side=LEFT)

        mainloop()
        return v.get()


def main():
    WIDTH, HEIGHT = 640, 640
    init_game_obj = InitGame(WIDTH, HEIGHT)
    run = True
    clicked = False
    piece_row = None
    piece_col = None
    possible_moves = []

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
                row = init_game_obj.find_cell_by_dot(pos[0])
                col = init_game_obj.find_cell_by_dot(pos[1])

                if init_game_obj.board[row][col].piece is not None and \
                        (clicked and init_game_obj.board[row][col].piece.white == init_game_obj.board[piece_row][
                            piece_col].piece.white):
                    clicked = False
                    piece_row = row
                    piece_col = col
                    init_game_obj.draw(init_game_obj.board)
                    pygame.display.update()

                if not clicked:
                    piece_row = row
                    piece_col = col
                    if init_game_obj.board[row][col].piece is not None:
                        moves = init_game_obj.board[row][col].piece.move(init_game_obj.board)

                        while moves:
                            (x, y) = moves.pop()
                            init_game_obj.select_possible_next_move(init_game_obj.board, x, y,
                                                                    init_game_obj.board[row][col].piece.white)
                        clicked = True

                elif clicked:
                    (x, y) = init_game_obj.get_cell_center_by_positions(row, col)
                    possible_moves = [*set(init_game_obj.board[piece_row][piece_col].piece.move(init_game_obj.board))]

                    for i in possible_moves:
                        if (x, y) == i:
                            init_game_obj.board[row][col].piece = init_game_obj.board[piece_row][piece_col].piece
                            init_game_obj.board[piece_row][piece_col].piece.update_pos(x + SHIFT_FOR_PHOTO, y + SHIFT_FOR_PHOTO)
                            init_game_obj.board[piece_row][piece_col].piece = None
                            init_game_obj.draw(init_game_obj.board)
                            clicked = False

                            if init_game_obj.board[row][col].piece.piece_name() == "Pawn" and (col == 0 or col == 7):
                                change_to = init_game_obj.replacement_window()
                                if change_to == "Queen":
                                    init_game_obj.board[row][col].piece = Queen.Queen(x + SHIFT_FOR_PHOTO, y + SHIFT_FOR_PHOTO, init_game_obj.board[row][col].piece.white, False)
                                if change_to == "Bishop":
                                    init_game_obj.board[row][col].piece = Bishop.Bishop(x + SHIFT_FOR_PHOTO, y + SHIFT_FOR_PHOTO, init_game_obj.board[row][col].piece.white, False)
                                if change_to == "Rook":
                                    init_game_obj.board[row][col].piece = Rook.Rook(x + SHIFT_FOR_PHOTO, y + SHIFT_FOR_PHOTO, init_game_obj.board[row][col].piece.white, False)
                                if change_to == "Knight":
                                    init_game_obj.board[row][col].piece = Knight.Knight(x + SHIFT_FOR_PHOTO, y + SHIFT_FOR_PHOTO, init_game_obj.board[row][col].piece.white, False)
                                init_game_obj.draw(init_game_obj.board)
                                clicked = False

                    init_game_obj.draw(init_game_obj.board)
                    pygame.display.update()

            # Draws the surface object to the screen.
        pygame.display.update()


if __name__ == '__main__':
    main()
