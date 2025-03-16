import java.util.List;

public class KnapsackStarter {


    // TODO: Implement the packKnapsack method

    
    public static int packKnapsack(List<Item> items, int capacity) {
        // Logic for backtracking solution
        return 0;
    }

    public static void main(String[] args) {
        List<Item> items = List.of(
            new Item(2, 10),
            new Item(5, 30),
            new Item(3, 15),
            new Item(6, 40)
        );

        int capacity = 10;
        int maxValue = packKnapsack(items, capacity);
        System.out.println("Maximum Value: " + maxValue);
    }
}


class Item {
    int weight, value;

    Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }
}
