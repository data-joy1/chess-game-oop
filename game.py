from board import Board
from pieces import Pawn, Rook

class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"

        # Place sample pieces for testing
        self.board.place_piece(Pawn("white"), (0, 6))
        self.board.place_piece(Pawn("black"), (0, 1))
        self.board.place_piece(Rook("white"), (0, 7))

    def switch_turn(self):
        """Switch player turns"""
        self.turn = "black" if self.turn == "white" else "white"

    def play(self):
        """Game loop"""
        while True:
            self.board.display()
            print(f"{self.turn}'s turn")

            # Get move input
            move_from = tuple(map(int, input("Move from (x y): ").split()))
            move_to = tuple(map(int, input("Move to (x y): ").split()))

            # Move piece (basic logic)
            piece = self.board.grid[move_from[1]][move_from[0]]
            if piece and piece.color == self.turn:
                if move_to in piece.valid_moves(move_from, self.board):
                    self.board.grid[move_from[1]][move_from[0]] = None
                    self.board.place_piece(piece, move_to)
                    self.switch_turn()
                else:
                    print("Invalid move. Try again.")
            else:
                print("No valid piece selected. Try again.")
