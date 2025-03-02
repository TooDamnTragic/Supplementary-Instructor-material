import javafx.scene.layout.GridPane;
import javafx.scene.control.Button;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import java.util.Observer;
import java.util.Observable;

public class TicTacToeView extends GridPane implements Observer {

    private TicTacToeModel model;
    // 2D array of Buttons to represent each cell
    private Button[][] buttons;

    public TicTacToeView(TicTacToeModel model) {
        this.model = model;
        this.model.addObserver(this);
        initView();
    }

    private void initView() {
        buttons = new Button[TicTacToeModel.SIZE][TicTacToeModel.SIZE];
        for (int row = 0; row < TicTacToeModel.SIZE; row++) {
            for (int col = 0; col < TicTacToeModel.SIZE; col++) {
                Button cell = new Button();
                cell.setMinSize(80, 80);
                cell.setFont(Font.font(24));
                // For demonstration, store (row, col) in userData
                cell.setUserData(new int[]{row, col});

                // The controller typically sets onAction or onMouseClicked,
                // but you can do it here or in the controller.

                // Add the button to the grid:
                this.add(cell, col, row);
                buttons[row][col] = cell;
            }
        }
        // Initial sync with model data
        updateBoard();
    }

    /**
     * This method repaints the board based on the model state.
     */
    private void updateBoard() {
        int[][] boardData = model.getBoard();
        for (int row = 0; row < TicTacToeModel.SIZE; row++) {
            for (int col = 0; col < TicTacToeModel.SIZE; col++) {
                int val = boardData[row][col];
                Button cell = buttons[row][col];

                if (val == 0) {
                    cell.setText("");
                } else if (val == 1) {
                    cell.setText("X");
                    cell.setTextFill(Color.BLUE);
                } else if (val == 2) {
                    cell.setText("O");
                    cell.setTextFill(Color.RED);
                }
            }
        }
    }

    /**
     * Observer callback: Whenever the model changes (notifyObservers()),
     * this method is called.
     */
    @Override
    public void update(Observable o, Object arg) {
        updateBoard();

        // (Optional) You could display a message if the game is over:
        if (model.isGameOver()) {
            int w = model.getWinner();
            if (w == 0) {
                System.out.println("It's a draw!");
            } else if (w == 1) {
                System.out.println("X wins!");
            } else if (w == 2) {
                System.out.println("O wins!");
            }
        }
    }

    /**
     * Provides public access to the button array in case the controller
     * wants to attach event handlers directly.
     */
    public Button[][] getButtonGrid() {
        return buttons;
    }
}
