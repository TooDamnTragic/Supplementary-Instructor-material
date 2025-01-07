package com.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;

import javafx.application.Application;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.Priority;
import javafx.scene.layout.RowConstraints;
import javafx.scene.layout.StackPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;

public class JeopardyGame extends Application {

    private static final int ROWS = 5;
    private static final int COLS = 5;
    private String[] categories = new String[COLS];
    private String[][] questions = new String[ROWS][COLS];
    private String[][] answers = new String[ROWS][COLS];
    private Button[][] buttons = new Button[ROWS][COLS];

    private Stage primaryStage;
    private Scene mainScene;

    @Override
    public void start(Stage primaryStage) {
        this.primaryStage = primaryStage;
        loadCSVData();

        GridPane gridPane = new GridPane();
        gridPane.setAlignment(Pos.CENTER);
        gridPane.setGridLinesVisible(false);
        gridPane.setHgap(5);
        gridPane.setVgap(5);

        for (int i = 0; i < COLS; i++) {
            ColumnConstraints colConstraints = new ColumnConstraints();
            colConstraints.setHgrow(Priority.ALWAYS);
            colConstraints.setPercentWidth(100.0 / COLS);
            gridPane.getColumnConstraints().add(colConstraints);
        }
        for (int i = 0; i <= ROWS; i++) { // ROWS + 1 to include category labels
            RowConstraints rowConstraints = new RowConstraints();
            rowConstraints.setVgrow(Priority.ALWAYS);
            rowConstraints.setPercentHeight(100.0 / (ROWS + 1));
            gridPane.getRowConstraints().add(rowConstraints);
        }
// Set up categories
for (int col = 0; col < COLS; col++) {
    Label categoryLabel = new Label(categories[col]);
    categoryLabel.setTextFill(Color.web("#4A628A"));
    categoryLabel.setFont(Font.font("Courier New", FontWeight.BOLD, 16));
    categoryLabel.setAlignment(Pos.CENTER);
    categoryLabel.setStyle("-fx-background-color: #DFF2EB;");
    categoryLabel.setWrapText(true);
    categoryLabel.setMaxWidth(Double.MAX_VALUE);
    categoryLabel.setMaxHeight(Double.MAX_VALUE);
    
    GridPane.setHgrow(categoryLabel, Priority.ALWAYS);
    GridPane.setVgrow(categoryLabel, Priority.ALWAYS);
    
    gridPane.add(categoryLabel, col, 0);
}

// Set up buttons
// color theme:
// #DFF2EB
// #B9E5E8
// #7AB2D3
// #4A628A
// rgb(223, 242, 235)
// rgb(185, 229, 232)
// rgb(122, 178, 211)
// rgb(74, 98, 138)
for (int row = 1; row <= ROWS; row++) {
    for (int col = 0; col < COLS; col++) {
        int pointValue = row * 100;
        Button button = new Button("$" + pointValue);
        button.setTextFill(Color.web("#DFF2EB"));
        button.setFont(Font.font("Courier New", FontWeight.BOLD, 24));
        button.setStyle("-fx-background-color: #7AB2D3;");
        button.setMaxWidth(Double.MAX_VALUE);
        button.setMaxHeight(Double.MAX_VALUE);
        final int r = row - 1;
        final int c = col;
        button.setOnAction(event -> expandButton(button, questions[r][c], answers[r][c], c + 1, r + 1));
        buttons[r][c] = button;

        GridPane.setHgrow(button, Priority.ALWAYS);
        GridPane.setVgrow(button, Priority.ALWAYS);

        gridPane.add(button, col, row);
    }
}

        gridPane.setStyle("-fx-background-color: black;");
        BorderPane root = new BorderPane(gridPane);
        mainScene = new Scene(root, 800, 600);

        primaryStage.setTitle("Jeopardy Game");
        primaryStage.setScene(mainScene);
        primaryStage.show();
    }

    private void expandButton(Button button, String questionText, String answerText, int categoryIndex, int questionIndex) {
        StackPane stackPane = new StackPane();
        if (categoryIndex == 1){
            stackPane.setStyle("-fx-background-color: gold;");
        }
        else if (categoryIndex == 2){
            stackPane.setStyle("-fx-background-color: tomato;");
        }
        else if (categoryIndex == 3){
            stackPane.setStyle("-fx-background-color: mediumorchid;");
        }
        else if (categoryIndex == 4){
            stackPane.setStyle("-fx-background-color: paleturquoise;");
        }
        else{
            stackPane.setStyle("-fx-background-color: lavender;");
        }


        // Create a VBox to hold the image and the text
        VBox contentBox = new VBox(10); // spacing of 10
        contentBox.setAlignment(Pos.CENTER);

        // Load question image
        String questionImageBaseName = categoryIndex + "-Q" + questionIndex;
        Image questionImage = loadImage(questionImageBaseName);

        if (questionImage != null) {
            ImageView imageView = new ImageView(questionImage);
            imageView.setPreserveRatio(true);
            imageView.setFitWidth(primaryStage.getWidth() * 0.8); // scale image to 80% of width
            contentBox.getChildren().add(imageView);
        }

        Label label = new Label(questionText);
        label.setTextFill(Color.BLACK);
        label.setFont(Font.font("Courier New", FontWeight.BOLD, 36));
        label.setWrapText(true);
        label.setAlignment(Pos.CENTER);
        contentBox.getChildren().add(label);

        stackPane.getChildren().add(contentBox);

        Scene scene = new Scene(stackPane, primaryStage.getWidth(), primaryStage.getHeight());

        // Click count to track the number of clicks on the question screen
        final int[] clickCount = {1};

        stackPane.setOnMouseClicked(event -> {
            clickCount[0]++;
            if (clickCount[0] == 2) {
                // Show the answer

                // Clear the contentBox
                contentBox.getChildren().clear();

                // Load answer image
                String answerImageBaseName = categoryIndex + "-A" + questionIndex;
                Image answerImage = loadImage(answerImageBaseName);

                if (answerImage != null) {
                    ImageView imageView = new ImageView(answerImage);
                    imageView.setPreserveRatio(true);
                    imageView.setFitWidth(primaryStage.getWidth() * 0.8); // scale image to 80% of width
                    contentBox.getChildren().add(imageView);
                }

                // Update label text to answer
                label.setText(answerText);
                contentBox.getChildren().add(label);
            } else if (clickCount[0] == 3) {
                // Return to main scene and gray out the button
                button.setDisable(true);
                button.setStyle("-fx-background-color: forestgreen;");
                button.setText("");
                primaryStage.setScene(mainScene);
            }
        });

        primaryStage.setScene(scene);
    }

    private Image loadImage(String baseFilename) {
        String[] extensions = {".png", ".jpeg", ".jpg"};
        for (String ext : extensions) {
            String filename = "/" + baseFilename + ext;
            InputStream is = getClass().getResourceAsStream(filename);
            if (is != null) {
                return new Image(is);
            }
        }
        return null;
    }

    private void loadCSVData() {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(
                getClass().getResourceAsStream("/jeopardy_data.csv")))) {
            String line;
            int row = 0;
            int questionRow = 0;
            int answerRow = 0;

            // Read categories
            if ((line = br.readLine()) != null) {
                categories = line.split(",");
            }

            while ((line = br.readLine()) != null) {
                String[] data = line.split(",");
                if (row % 2 == 0) {
                    // Questions
                    questions[questionRow++] = data;
                } else {
                    // Answers
                    answers[answerRow++] = data;
                }
                row++;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
