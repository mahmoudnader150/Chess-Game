from const import *
from square import Square
from piece import *
from move import Move


class Board:

    def __init__(self):
        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]

        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def calc_moves(self, piece, row, col):
        '''
           calculate all possible (valid) moves of an specific piece on a specific position
        '''
        def knight_moves():
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1),
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = (possible_move)

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_enemy(piece.color):
                        # create squares to the new move
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create new move
                        move = Move(initial, final)
                        piece.add_move(move)

        def pawn_moves():
            # steps
            steps = 1 if piece.moved else 2

            # vertical moves
            start = row+piece.dir
            end = row+(piece.dir*(1+steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # create a new move
                        move = Move(initial, final)
                        piece.add_move(move)
                    # blocked
                    else:
                        break
                # not in range
                else:
                    break
            # diagonal moves
            possible_move_row = row+piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_enemy_piece(piece.color):
                        # create initial and final move squares
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # create a new move
                        move = Move(initial, final)
                        # append new move
                        piece.add_move(move)

        if isinstance(piece, Pawn):
            pawn_moves()

        elif isinstance(piece, Knight):
            knight_moves()

        elif isinstance(piece, Bishop):
            pass

        elif isinstance(piece, Rook):
            pass

        elif isinstance(piece, Queen):
            pass

        elif isinstance(piece, King):
            pass

    def _create(self):
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col)

    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)
        # all pawns :)
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(
                row_pawn, col, Pawn(color))
        self.squares[5][0] = Square(
            5, 0, Pawn(color))
        # knights
        self.squares[row_other][1] = Square(
            row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(
            row_other, 6, Knight(color))

        # bishops
        self.squares[row_other][2] = Square(
            row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(
            row_other, 5, Bishop(color))

        # rooks
        self.squares[row_other][0] = Square(
            row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(
            row_other, 7, Rook(color))

        # queen
        self.squares[row_other][3] = Square(
            row_other, 3, Queen(color))

        # king
        self.squares[row_other][4] = Square(
            row_other, 4, King(color))
