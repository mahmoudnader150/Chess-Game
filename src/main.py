import pygame
import sys

from const import *
from game import Game
from square import Square
from move import Move
import tkinter as tk


def white_gui():
    root = tk.Tk()
    root.title("Chess Game")

    frame = tk.Frame(root, width=300, height=200)
    frame.pack()

    label = tk.Label(frame, text="White wins!", font=("Arial", 24))
    label.pack(pady=50)

    root.mainloop()


def black_gui():
    root = tk.Tk()
    root.title("Chess Game")

    frame = tk.Frame(root, width=300, height=200)
    frame.pack()

    label = tk.Label(frame, text="Black wins!", font=("Arial", 24))
    label.pack(pady=50)

    root.mainloop()


class Main:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()

    def mainloop(self):

        screen = self.screen
        game = self.game
        board = self.game.board
        dragger = self.game.dragger

        while True:
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)

            game.show_pieces(screen)
            game.show_hover(screen)
            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():

                # click
                if event.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse(event.pos)

                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE

                    print(dragger.mouseX, clicked_col)
                    print(dragger.mouseY, clicked_row)

                    # if clicked square has piece?
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        # valid piece (color)?
                        if piece.color == game.next_player:
                            board.calc_moves(
                                piece, clicked_row, clicked_col, bool=True)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            # show methods
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_pieces(screen)
                # mouse motion
                elif event.type == pygame.MOUSEMOTION:
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] // SQSIZE
                    game.set_hover(motion_row, motion_col)
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        # show methods
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        game.show_hover(screen)
                        dragger.update_blit(screen)

                # click release
                elif event.type == pygame.MOUSEBUTTONUP:

                    if dragger.dragging:
                        dragger.update_mouse(event.pos)

                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        # creat possible move
                        initial = Square(dragger.initial_row,
                                         dragger.initial_col)

                        final = Square(released_row,
                                       released_col)

                        move = Move(initial, final)

                        # valid move
                        if board.valid_move(dragger.piece, move):
                            captured = board.squares[released_row][released_col].has_piece(
                            )

                            board.move(dragger.piece, move)
                            game.play_sound(captured)
                            board.set_true_en_passant(dragger.piece)
                            # show
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_pieces(screen)

                            if board.white_win():
                                game.next_turn()
                                pygame.quit()
                               # sys.exit()
                                white_gui()
                                sys.exit()
                            elif board.black_win():
                                game.next_turn()
                                pygame.quit()
                               # sys.exit()
                                black_gui()
                                sys.exit()

                            # NXT TURN
                            game.next_turn()

                    dragger.undrag_piece()
                # key press (theme)
                elif event.type == pygame.KEYDOWN:
                    # change theme
                    if(event.key == pygame.K_t):
                        game.change_theme()
                    if event.key == pygame.K_r:
                        game.reset()
                        screen = self.screen
                        game = self.game
                        board = self.game.board
                        dragger = self.game.dragger
                # quit app
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main = Main()
main.mainloop()
