import javafx.scene.control.Button;
import javafx.event.EventHandler;
import javafx.scene.input.MouseEvent;

public class TicTacToeController {
    private TicTacToeModel model;
    private TicTacToeView view;

    public TicTacToeController(TicTacToeModel model, TicTacToeView view) {
        this.model = model;
        this.view = view;
        attachHandlers();
    }

    /**
     * Attach handlers so that when a user clicks a button, we call model.makeMove(...)
     */
    private void attachHandlers() {
        Button[][] cells = view.getButtonGrid();
        for (int row = 0; row < TicTacToeModel.SIZE; row++) {
            for (int col = 0; col < TicTacToeModel.SIZE; col++) {
                Button cell = cells[row][col];
                cell.setOnMouseClicked(new EventHandler<MouseEvent>() {
                    @Override
                    public void handle(MouseEvent event) {
                        // Retrieve the row/col from the button’s userData
                        int[] rc = (int[]) cell.getUserData();
                        int r = rc[0];
                        int c = rc[1];

                        // TODO: Call the model to make a move at (r, c)
                        // model.makeMove(r, c);

                        // The model will notify the view automatically (Observer pattern).
                    }
                });
            }
        }
    }
}
