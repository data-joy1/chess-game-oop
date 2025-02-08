document.addEventListener("DOMContentLoaded", async function () {
    const boardContainer = document.getElementById("chessboard");
    let selectedSquare = null; // Track selected piece

    // Fetch board data from Flask API
    async function loadBoard() {
        const response = await fetch("http://127.0.0.1:5000/get_board");
        const board = await response.json();
        renderBoard(board);
    }

    // Render board on screen
    function renderBoard(board) {
        boardContainer.innerHTML = ""; // Clear previous board
        for (let y = 0; y < 8; y++) {
            for (let x = 0; x < 8; x++) {
                const square = document.createElement("div");
                square.classList.add("square", (x + y) % 2 === 0 ? "light" : "dark");
                square.dataset.position = `${x},${y}`;
                square.textContent = board[y][x] !== "." ? board[y][x] : "";

                square.addEventListener("click", () => handleSquareClick(square, x, y));
                boardContainer.appendChild(square);
            }
        }
    }

    // Handle piece selection & movement
    async function handleSquareClick(square, x, y) {
        if (!selectedSquare) {
            selectedSquare = { x, y };
            square.classList.add("selected"); // Highlight selected piece
        } else {
            // Send move request to Flask
            const response = await fetch("http://127.0.0.1:5000/move_piece", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ move_from: [selectedSquare.x, selectedSquare.y], move_to: [x, y] })
            });

            const result = await response.json();
            if (result.success) {
                await loadBoard(); // Reload board after a successful move
            } else {
                alert(result.message);
            }

            selectedSquare = null; // Reset selection
        }
    }

    // Load board when page loads
    loadBoard();
});
