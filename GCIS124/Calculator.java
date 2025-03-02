import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Calculator extends Application {

    private TextField display;

    // (Optional) You can store pending operation info here:
    // private double leftOperand;
    // private String operator; // "+", "-", "*", "/"

    @Override
    public void start(Stage stage) {
        display = new TextField();
        display.setEditable(false);

        GridPane grid = new GridPane();
        // Use grid.add(node, colIndex, rowIndex) to place buttons
        // TODO: Create buttons (0-9, +, -, *, /, =)
        //       and add them to the grid in a layout that resembles a calculator.

        // Example for button '1' at row=1, col=0:
        /*
        Button btn1 = new Button("1");
        btn1.setOnAction(e -> {
            // TODO: Append '1' to the display
        });
        grid.add(btn1, 0, 1);
        */

        // TODO: Add event handlers that:
        //  - append digits to display
        //  - store and handle the current operation
        //  - compute results when '=' is clicked

        // Combine everything into a Scene:
        GridPane root = new GridPane();
        // You can place display at the top in row 0, spanning columns:
        root.add(display, 0, 0);
        // And place the grid of buttons in row 1:
        root.add(grid, 0, 1);

        Scene scene = new Scene(root, 300, 400);
        stage.setTitle("My Calculator");
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
