from const import *
from square import Square
from piece import *


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        # all pawns :)
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(
                row_pawn, col, Pawn('pawn', color, 1))

        # knights
        self.squares[row_other][1] = Square(
            row_other, 1, Knight('knight', color, 3.0))
        self.squares[row_other][6] = Square(
            row_other, 6, Knight('knight', color, 3.0))

        # bishops
        self.squares[row_other][2] = Square(
            row_other, 2, Bishop('bishop', color, 3.001))
        self.squares[row_other][5] = Square(
            row_other, 5, Bishop('bishop', color, 3.001))

        # rooks
        self.squares[row_other][0] = Square(
            row_other, 0, Rook('rook', color, 5.0))
        self.squares[row_other][7] = Square(
            row_other, 7, Rook('rook', color, 5.0))

        # queen
        self.squares[row_other][3] = Square(
            row_other, 3, Queen('queen', color, 9.0))

        # king
        self.squares[row_other][4] = Square(
            row_other, 4, King('king', color, 9.0))
