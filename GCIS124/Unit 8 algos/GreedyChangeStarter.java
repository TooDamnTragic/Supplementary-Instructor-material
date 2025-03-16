import java.util.ArrayList;
import java.util.List;

public class GreedyChangeStarter {
    enum Currency { DOLLAR, QUARTER, DIME, NICKEL, PENNY }

    // TODO: Implement the makeChange method
    public static List<Currency> makeChange(double price, double payment) {
        List<Currency> change = new ArrayList<>();
        // Logic for calculating change goes here
        return change;
    }

    public static void main(String[] args) {
        double price = 2.32;
        double payment = 5.00;
        List<Currency> result = makeChange(price, payment);
        System.out.println("Change: " + result);
    }
}
