public class PrintNumbers {
    public static void main(String[] args) {
        // Using Standard For Loop
        for (int i = 0; i <= 10; i++) {
            System.out.println(i);
        }

        // Reverse For Loop
        for (int i = 10; i >= 0; i--) {
            System.out.println(10 - i);
        }

        // For Loop with Conditional Break
        for (int i = 0; ; i++) {
            if (i > 10) break;
            System.out.println(i);
        }

        // For Loop with Step Variable
        for (int i = 0, step = 1; i <= 10; i += step) {
            System.out.println(i);
        }

        // Using Standard While Loop
        int i = 0;
        while (i <= 10) {
            System.out.println(i);
            i++;
        }

        // While Loop with Decrement
        i = 10;
        while (i >= 0) {
            System.out.println(10 - i);
            i--;
        }

        // While Loop with Break
        i = 0;
        while (true) {
            if (i > 10) break;
            System.out.println(i);
            i++;
        }

        // Using Standard Do-While Loop
        i = 0;
        do {
            System.out.println(i);
            i++;
        } while (i <= 10);

        // Do-While Loop with Break
        i = 0;
        do {
            if (i > 10) break;
            System.out.println(i);
            i++;
        } while (true);

        // Using IntStream with Range
        java.util.stream.IntStream.rangeClosed(0, 10).forEach(System.out::println);

        // Using Stream with Lambda Expression
        java.util.stream.Stream.iterate(0, n -> n + 1)
            .limit(11)
            .forEach(System.out::println);

        // Simple Recursion
        printNumbers(0);

        // Tail Recursion
        printNumbers(0, 10);

        // For Loop with Label
        outer:
        for (int j = 0; j <= 10; j++) {
            System.out.println(j);
            continue outer;
        }

        // Using a List
        java.util.List<Integer> numbers = java.util.Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        for (int num : numbers) {
            System.out.println(num);
        }

        // Using Iterator
        java.util.Iterator<Integer> iterator = numbers.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }
    }

    // Simple Recursion
    public static void printNumbers(int i) {
        if (i > 10) return;
        System.out.println(i);
        printNumbers(i + 1);
    }

    // Tail Recursion
    public static void printNumbers(int current, int end) {
        if (current > end) return;
        System.out.println(current);
        printNumbers(current + 1, end);
    }
}
