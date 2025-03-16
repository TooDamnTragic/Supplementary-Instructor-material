import java.util.List;

class Item {
    int weight, value;

    Item(int weight, int value) {
        this.weight = weight;
        this.value = value;
    }
}

public class Knapsack {
    public static int packKnapsack(List<Item> items, int capacity) {
        return backtrack(items, 0, capacity, 0);
    }

    private static int backtrack(List<Item> items, int index, int remainingCapacity, int currentValue) {
        if (index == items.size()) {
            return currentValue;
        }

        Item currentItem = items.get(index);

        // Option 1: Exclude the current item
        int exclude = backtrack(items, index + 1, remainingCapacity, currentValue);

        // Option 2: Include the current item (only if it fits)
        int include = 0;
        if (currentItem.weight <= remainingCapacity) {
            include = backtrack(
                items,
                index + 1,
                remainingCapacity - currentItem.weight,
                currentValue + currentItem.value
            );
        }

        return Math.max(exclude, include);
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







// For the Knapsack Problem:
// How does backtracking ensure that every possible combination is considered?
// What if two items have the same weight and value? How would that affect the algorithm's choices?
// Could a greedy algorithm efficiently solve this problem as well? If so, when?
// How would you improve the backtracking solution to avoid redundant calculations?