from flask import Flask, jsonify, request
from flask_cors import CORS
from game import Game

app = Flask(__name__)
CORS(app)  # Allows frontend to call backend

# Initialize chess game
chess_game = Game()

# Sample Chessboard Representation (8x8 Grid)
chessboard = [
    ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ["P", "P", "P", "P", "P", "P", "P", "P"],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", ".", ".", "."],
    ["p", "p", "p", "p", "p", "p", "p", "p"],
    ["r", "n", "b", "q", "k", "b", "n", "r"]
]

@app.route("/get_board", methods=["GET"])
def get_board():
    """Returns the current state of the chessboard"""
    return jsonify(chessboard)

@app.route("/move_piece", methods=["POST"])
def move_piece():
    """Handles piece movement"""
    data = request.json
    move_from = tuple(data["move_from"])
    move_to = tuple(data["move_to"])

    # Validate move
    piece = chess_game.board.grid[move_from[1]][move_from[0]]
    if piece and piece.color == chess_game.turn:
        if move_to in piece.valid_moves(move_from, chess_game.board):
            chess_game.board.grid[move_from[1]][move_from[0]] = None
            chess_game.board.place_piece(piece, move_to)
            chess_game.switch_turn()
            return jsonify({"success": True, "message": "Move successful!"})
    
    return jsonify({"success": False, "message": "Invalid move!"})

if __name__ == "__main__":
    app.run(debug=True)
