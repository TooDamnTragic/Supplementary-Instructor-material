package com.gui;


import java.io.File;

import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ToggleButton;
import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.Priority;
import javafx.scene.layout.VBox;
import javafx.scene.media.Media;
import javafx.scene.media.MediaPlayer;
import javafx.stage.Stage;
import javafx.util.Duration;

/**
 * "Spotify-like" music player using JavaFX basics.
 */
public class SpotifyLikePlayer extends Application {

    // -- Day/Night mode colors --
    //Maybe add more colors for themes
    // ---------------------------

    private static final String DAY_BACKGROUND = "-fx-background-color: white;";
    private static final String DAY_TEXT_COLOR = "-fx-text-fill: black;";
    private static final String NIGHT_BACKGROUND = "-fx-background-color: #333333;";
    private static final String NIGHT_TEXT_COLOR = "-fx-text-fill: white;";

    // Array of songs (file paths) -- be sure these exist on your machine!
    private String[] songFiles = {
        "src/main/java/com/gui/media/music/FEN.mp3",
        "src/main/java/com/gui/media/music/Doom.mp3",
        "src/main/java/com/gui/media/music/Oops.mp3"
    };

    // Parallel arrays for song info (could also make a small Song class)
    private String[] songTitles = { 
        "FE!N", 
        "The Only Thing They Fear Is You", 
        "Oops!!!" 
    };
    private String[] artistNames = { 
        "Travis Scott ft Playboi Carti", 
        "Mick Gordon", 
        "Yung Gravy"
    };
    
    private String[] albumName = {
        "UTOPIA",
        "Doom Eternal OST",
        "Oops!!!"
    };

    private String[] albumCovers = {
        "src/main/java/com/gui/media/images/cover1.png",
        "src/main/java/com/gui/media/images/cover2.png",
        "src/main/java/com/gui/media/images/cover3.png"
    };

    // Keep track of which song is currently playing
    private int currentIndex = 0;

    // Media + MediaPlayer
    private MediaPlayer mediaPlayer;

    // UI Controls
    private Label titleLabel;
    private Label artistLabel;
    private Label progressLabel;
    private ImageView albumArtView;

    private ToggleButton dayNightToggle;

    @Override
    public void start(Stage stage) {
        stage.setTitle("Spotify-Like Player");

        
        // Day/Night Toggle
        // ---------------------------

        HBox topBar = new HBox();
        topBar.setStyle(DAY_BACKGROUND);  // Start in day mode by default

        dayNightToggle = new ToggleButton("Night Mode");
        dayNightToggle.setOnAction(e -> toggleDayNightMode());
        topBar.getChildren().add(dayNightToggle);

        
        // Album Art, Song Title, Artist
        // ---------------------------
        
        VBox centerBox = new VBox();
        centerBox.setSpacing(10);
        centerBox.setStyle(DAY_BACKGROUND); // match day mode initially

        albumArtView = new ImageView();
        albumArtView.setFitWidth(200);
        albumArtView.setFitHeight(200);
        albumArtView.setPreserveRatio(true);

        titleLabel = new Label("Song Title");
        titleLabel.setStyle(DAY_TEXT_COLOR + "-fx-font-size: 18px; -fx-font-weight: bold;");


        artistLabel = new Label("Artist Name");
        artistLabel.setStyle(DAY_TEXT_COLOR + "-fx-font-size: 14px;");

        centerBox.getChildren().addAll(albumArtView, titleLabel, artistLabel);


        // Make the center box stretch:
        VBox.setVgrow(albumArtView, Priority.ALWAYS);

        
        // Playback Controls + Progress
        // ---------------------------
        HBox bottomBar = new HBox();
        bottomBar.setSpacing(10);
        bottomBar.setStyle(DAY_BACKGROUND);
        bottomBar.setPadding(new javafx.geometry.Insets(10));

        Button prevButton = new Button("Prev");
        Button playButton = new Button("Play");
        Button pauseButton = new Button("Pause");
        Button nextButton = new Button("Next");

        progressLabel = new Label("0:00 / 0:00");
        progressLabel.setStyle(DAY_TEXT_COLOR);

        
        
        // Networking all the buttons to the backend
        prevButton.setOnAction(e -> handlePrevious());
        playButton.setOnAction(e -> handlePlay());
        pauseButton.setOnAction(e -> handlePause());
        nextButton.setOnAction(e -> handleNext());

        bottomBar.getChildren().addAll(prevButton, playButton, pauseButton, nextButton, progressLabel);

        // Setups
        // ---------------------------
        BorderPane root = new BorderPane();
        root.setTop(topBar);
        root.setCenter(centerBox);
        root.setBottom(bottomBar);
        Scene scene = new Scene(root, 400, 400);
        stage.setScene(scene);
        stage.show();

        loadTrack(currentIndex);
    }

    /**
     * Load a specific track by index, create media player, and update the UI.
     */
    private void loadTrack(int index) {
        if (mediaPlayer != null) {
            mediaPlayer.stop();
        }

        // Ensure valid index
        currentIndex = (index + songFiles.length) % songFiles.length;

        // Create new Media & MediaPlayer
        File mp3File = new File(songFiles[currentIndex]);
        Media media = new Media(mp3File.toURI().toString());
        mediaPlayer = new MediaPlayer(media);

        // Update album art, song title, artist
        titleLabel.setText(songTitles[currentIndex]);
        artistLabel.setText(artistNames[currentIndex]);
        Image cover = new Image("file:" + albumCovers[currentIndex]);
        albumArtView.setImage(cover);

        // Reset progress
        progressLabel.setText("0:00 / 0:00");

        // Get duration
        mediaPlayer.setOnReady(() -> {
            Duration total = mediaPlayer.getMedia().getDuration();
            String totalStr = formatTime(total);
            progressLabel.setText("0:00 / " + totalStr);
        });

        // Keep track of currentTime to update progress
        mediaPlayer.currentTimeProperty().addListener((obs, oldTime, newTime) -> {
            Duration total = mediaPlayer.getTotalDuration();
            if (total != null && !total.isUnknown()) {
                String currentStr = formatTime(newTime);
                String totalStr = formatTime(total);
                progressLabel.setText(currentStr + " / " + totalStr);
            }
        });
    }

    /**
     * Code to format a Duration as M:SS (e.g., 3:05).
     */
    private String formatTime(Duration duration) {
        if (duration == null || duration.isUnknown()) {
            return "0:00";
        }
        int seconds = (int) duration.toSeconds();
        int minutes = seconds / 60;
        int secs = seconds % 60;
        return String.format("%d:%02d", minutes, secs);
    }

    // -------------------------------
    // Event Handlers for Buttons
    // -------------------------------
    private void handlePrevious() {
        // Decrement index and reload track
        loadTrack(currentIndex - 1);
        mediaPlayer.play();
    }

    private void handlePlay() {
        if (mediaPlayer != null) {
            mediaPlayer.play();
        }
    }

    private void handlePause() {
        if (mediaPlayer != null) {
            mediaPlayer.pause();
        }
    }

    private void handleNext() {
        // Increment index and reload track
        loadTrack(currentIndex + 1);
        mediaPlayer.play();
    }



    /**
     * Toggle between Day and Night mode by updating the style.
     */
    private void toggleDayNightMode() {
        boolean nightMode = dayNightToggle.isSelected();
        if (nightMode) {
            dayNightToggle.setText("Day Mode");
            setOverallTheme(NIGHT_BACKGROUND, NIGHT_TEXT_COLOR);
        } else {
            dayNightToggle.setText("Night Mode");
            setOverallTheme(DAY_BACKGROUND, DAY_TEXT_COLOR);
        }
    }

    /**
     * Updates the background/text color for the entire UI.
     */
    private void setOverallTheme(String backgroundStyle, String textStyle) {
        // Top bar
        dayNightToggle.getParent().setStyle(backgroundStyle); 
        dayNightToggle.setStyle(textStyle);
        
        // Center region (titleLabel, artistLabel, albumArtView's container)
        titleLabel.getParent().setStyle(backgroundStyle);
        titleLabel.setStyle(textStyle + "-fx-font-size: 18px; -fx-font-weight: bold;");
        artistLabel.setStyle(textStyle + "-fx-font-size: 14px;");

        // Bottom bar
        progressLabel.getParent().setStyle(backgroundStyle);
        progressLabel.setStyle(textStyle);
        
        // Also re-style any other buttons in bottomBar if needed
        // We can loop or do them individually
        HBox bottomBar = (HBox) progressLabel.getParent();
        for (javafx.scene.Node node : bottomBar.getChildren()) {
            if (node instanceof Button) {
                node.setStyle(textStyle);
            }
        }
    }

    // Main
    // ---------------------------
    public static void main(String[] args) {
        launch(args);
    }
}
