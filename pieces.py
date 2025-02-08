class Piece:
    def __init__(self, color):
        self.color = color  # "white" or "black"

    def valid_moves(self, position, board):
        """Return a list of valid moves. Must be overridden in subclasses."""
        raise NotImplementedError("This method should be implemented in child classes.")

    def __str__(self):
        return self.__class__.__name__[0]  # Returns the first letter of the piece name

class Pawn(Piece):
    def valid_moves(self, position, board):
        """Define Pawn movement logic"""
        x, y = position
        moves = []
        direction = -1 if self.color == "white" else 1

        # Move forward
        if board.is_empty((x, y + direction)):
            moves.append((x, y + direction))

        return moves

class Rook(Piece):
    def valid_moves(self, position, board):
        """Define Rook movement logic (horizontal & vertical)"""
        moves = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dx, dy in directions:
            new_x, new_y = position
            while True:
                new_x += dx
                new_y += dy
                if board.is_valid((new_x, new_y)):
                    moves.append((new_x, new_y))
                    if board.has_piece((new_x, new_y)):  # Stop if capturing
                        break
                else:
                    break

        return moves
    
class King(Piece):
    def valid_moves(self, position, board):
        x, y = position
        moves = [(x+dx, y+dy) for dx in [-1, 0, 1] for dy in [-1, 0, 1]
                 if board.is_valid((x+dx, y+dy))]

        # Castling Logic
        if not self.has_moved and not board.is_king_in_check(self.color):
            # Check left side (Queen-side castling)
            if isinstance(board.grid[y][0], Rook) and not board.grid[y][1] and not board.grid[y][2]:
                moves.append((x-2, y))  # Castling move
            # Check right side (King-side castling)
            if isinstance(board.grid[y][7], Rook) and not board.grid[y][5] and not board.grid[y][6]:
                moves.append((x+2, y))

        return moves
