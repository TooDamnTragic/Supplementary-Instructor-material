import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import java.util.NoSuchElementException;

public class QueueGUI extends Application {

    // Node class
    private static class Node<E> {
        E value;
        Node<E> next;
        Node(E value) {
            this.value = value;
            this.next = null;
        }
    }

    // A simple node-based queue
    public static class MyQueue<E> {
        private Node<E> front;
        private Node<E> back;
        private int size;

        public MyQueue() {
            front = back = null;
            size = 0;
        }

        public void enqueue(E value) {
            Node<E> newNode = new Node<>(value);
            if (isEmpty()) {
                front = back = newNode;
            } else {
                back.next = newNode;
                back = newNode;
            }
            size++;
        }

        public E dequeue() {
            if (isEmpty()) throw new NoSuchElementException("Queue is empty");
            E val = front.value;
            front = front.next;
            if (front == null) back = null;
            size--;
            return val;
        }

        public boolean isEmpty() {
            return size == 0;
        }

        // Provide a string representation for the UI
        public String toString() {
            // TODO: Return contents of the queue from front to back
            // e.g., "[first, second, third]"
            return "...";
        }
    }

    private MyQueue<String> queue;

    @Override
    public void start(Stage stage) {
        queue = new MyQueue<>();

        TextField inputField = new TextField();
        inputField.setPromptText("Enter item to enqueue");

        Button enqueueBtn = new Button("Enqueue");
        Button dequeueBtn = new Button("Dequeue");
        Label queueLabel = new Label("Queue: [ ]");

        enqueueBtn.setOnAction(e -> {
            // TODO: read text from inputField
            //       enqueue into 'queue'
            //       update queueLabel with queue.toString()
        });

        dequeueBtn.setOnAction(e -> {
            // TODO: dequeue from 'queue' if not empty
            //       handle NoSuchElementException if empty
            //       update queueLabel
        });

        VBox root = new VBox(10, inputField, enqueueBtn, dequeueBtn, queueLabel);
        Scene scene = new Scene(root, 300, 200);
        stage.setScene(scene);
        stage.setTitle("Queue Demo");
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
