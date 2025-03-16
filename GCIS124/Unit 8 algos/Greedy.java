import java.util.ArrayList;
import java.util.List;

/*

Problem: Return the optimal set of coins for $2.26
(DOLLAR, QUARTER, DIME, NICKEL, PENNY)

*/



public class Greedy {
    enum Currency { DOLLAR, QUARTER, DIME, NICKEL, PENNY }

    public static List<Currency> makeChange(double price, double payment) {
        double change = payment - price;
        List<Currency> result = new ArrayList<>();
        double[] values = {1.00, 0.25, 0.10, 0.05, 0.01};
        Currency[] currencies = Currency.values();

        for (int i = 0; i < values.length; i++) {
            while (change >= values[i]) {
                result.add(currencies[i]);
                change -= values[i];
                change = Math.round(change * 100.0) / 100.0;  // Rounding fix
            }
        }

        return result;
    }


    public static void main(String[] args) {
        System.out.println("Change for $2.26: " + makeChange(0, 2.26));
    }
}
