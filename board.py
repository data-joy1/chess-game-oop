from pieces import King

class Board:
    def __init__(self):
        self.grid = [[None] * 8 for _ in range(8)]  # 8x8 chessboard
        self.king_positions = {"white": (4, 7), "black": (4, 0)}  # Track king positions

    def is_king_in_check(self, color):
        """Check if the king is in check"""
        king_position = self.king_positions[color]
        
        # Check if any opponent piece can attack the king
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece and piece.color != color:
                    if king_position in piece.valid_moves((col, row), self):
                        return True
        return False

    def move_piece(self, from_pos, to_pos):
        """Move piece and update king position if needed"""
        piece = self.grid[from_pos[1]][from_pos[0]]
        self.grid[to_pos[1]][to_pos[0]] = piece
        self.grid[from_pos[1]][from_pos[0]] = None
        
        # Update king position if moved
        if isinstance(piece, King):
            self.king_positions[piece.color] = to_pos
    
    def place_piece(self, piece, position):
        """Place a piece on the board"""
        x, y = position
        self.grid[y][x] = piece

    def is_empty(self, position):
        """Check if a position is empty"""
        x, y = position
        return self.grid[y][x] is None

    def has_piece(self, position):
        """Check if a position contains a piece"""
        x, y = position
        return self.grid[y][x] is not None

    def is_valid(self, position):
        """Check if a position is within board limits"""
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8

    def display(self):
        """Print the board"""
        for row in self.grid:
            print(" | ".join([str(piece) if piece else "." for piece in row]))
            print("-" * 25)
