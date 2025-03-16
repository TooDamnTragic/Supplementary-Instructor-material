import java.util.ArrayList;
import java.util.List;

public class GreedyChange {
    enum Currency { DOLLAR, QUARTER, DIME, NICKEL, PENNY }

    public static List<Currency> makeChange(double price, double payment) {
        double changeAmount = payment - price;
        List<Currency> change = new ArrayList<>();
        double[] values = {1.00, 0.25, 0.10, 0.05, 0.01};
        Currency[] currencies = Currency.values();

        for (int i = 0; i < values.length; i++) {
            while (changeAmount >= values[i]) {
                change.add(currencies[i]);
                changeAmount -= values[i];
                changeAmount = Math.round(changeAmount * 100.0) / 100.0;  // Fix rounding errors
            }
        }

        return change;
    }

    public static void main(String[] args) {
        double price = 2.32;
        double payment = 5.00;
        List<Currency> result = makeChange(price, payment);
        System.out.println("Change: " + result);
    }
}




// For the Greedy Change-Making Problem:
// How does the greedy algorithm make decisions at each step?
// In what situations would this algorithm fail to find the optimal solution? (Hint: Unconventional coin values)
// What if there was a coin worth 99 cents—how would that impact the solution?
// How could you modify the algorithm to handle non-standard coin values more efficiently?