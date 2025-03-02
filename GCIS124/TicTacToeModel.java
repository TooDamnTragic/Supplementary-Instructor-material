import java.util.Observable;

public class TicTacToeModel extends Observable {
    // We’ll represent the board as a 2D int array:
    // 0 = empty, 1 = player X, 2 = player O
    private int[][] board;
    private int currentPlayer;
    private boolean gameOver;
    private int winner; // 0 if no winner, 1 = X, 2 = O

    public static final int SIZE = 3;

    public TicTacToeModel() {
        board = new int[SIZE][SIZE];
        currentPlayer = 1; // Let player X start
        gameOver = false;
        winner = 0;
    }

    /**
     * Returns the current board state.
     */
    public int[][] getBoard() {
        return board;
    }

    /**
     * Returns which player's turn it is:
     * 1 = X, 2 = O
     */
    public int getCurrentPlayer() {
        return currentPlayer;
    }

    /**
     * Attempts to place the current player's mark at (row, col).
     * If valid, place the mark, check for a winner or draw,
     * and switch the current player.
     */
    public void makeMove(int row, int col) {
        if (gameOver) {
            // Game is over, no moves allowed
            return;
        }

        // TODO: Validate (row, col) is in range and board[row][col] is empty
        // If valid:
        //    board[row][col] = currentPlayer;
        //    checkGameState(row, col);
        //    if (!gameOver) switchPlayer();

        // If the move is valid, notify observers:
        setChanged();
        notifyObservers();
    }

    /**
     * Check if the last move caused a win or a draw.
     */
    private void checkGameState(int row, int col) {
        // TODO: Implement logic to check the row, column, and possibly diagonals
        // to see if this move caused the current player to win.

        // If there is a winner:
        //    gameOver = true;
        //    winner = currentPlayer;
        //
        // Or if the board is full with no winner, set gameOver = true; winner = 0 (draw)
    }

    private void switchPlayer() {
        currentPlayer = (currentPlayer == 1) ? 2 : 1;
    }

    public int getWinner() {
        return winner;
    }

    public boolean isGameOver() {
        return gameOver;
    }

    /**
     * Optional: Let the user reset the board.
     */
    public void resetGame() {
        // TODO: Clear the board, reset currentPlayer to 1 (X), gameOver to false, winner to 0
        // Then notify observers again
        setChanged();
        notifyObservers();
    }
}
