import java.util.Scanner;

public class BSTConsole {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        BST<Integer> tree = new BST<>();

        printHelp();
        while (true) {
            System.out.print("> ");
            String command = sc.next();

            if (command.equalsIgnoreCase("insert")) {
                int value = sc.nextInt();
                boolean success = tree.insert(value);
                if (success) {
                    System.out.println("Inserted " + value);
                } else {
                    System.out.println("Value " + value + " already exists in the tree.");
                }

            } else if (command.equalsIgnoreCase("contains")) {
                int value = sc.nextInt();
                if (tree.contains(value)) {
                    System.out.println("Tree contains " + value);
                } else {
                    System.out.println("Tree does NOT contain " + value);
                }

            } else if (command.equalsIgnoreCase("delete")) {
                int value = sc.nextInt();
                boolean removed = tree.delete(value);
                if (removed) {
                    System.out.println("Deleted " + value);
                } else {
                    System.out.println("Value " + value + " not found in tree.");
                }

            } else if (command.equalsIgnoreCase("inorder")) {
                System.out.println("In-Order: " + tree.toInOrderString());

            } else if (command.equalsIgnoreCase("preorder")) {
                System.out.println("Pre-Order: " + tree.toPreOrderString());

            } else if (command.equalsIgnoreCase("postorder")) {
                System.out.println("Post-Order: " + tree.toPostOrderString());

            } else if (command.equalsIgnoreCase("size")) {
                System.out.println("Size: " + tree.size());

            } else if (command.equalsIgnoreCase("help")) {
                printHelp();

            } else if (command.equalsIgnoreCase("exit")) {
                break;

            } else {
                System.out.println("Unrecognized command. Type 'help' for a list of commands.");
            }
        }

        System.out.println("Exiting...");
        sc.close();
    }

    private static void printHelp() {
        System.out.println("Available commands:");
        System.out.println(" insert <value>   : Insert an integer into the BST");
        System.out.println(" contains <value> : Check if an integer is in the BST");
        System.out.println(" delete <value>   : Remove an integer from the BST");
        System.out.println(" inorder          : Print in-order traversal");
        System.out.println(" preorder         : Print pre-order traversal");
        System.out.println(" postorder        : Print post-order traversal");
        System.out.println(" size             : Show how many elements in the BST");
        System.out.println(" help             : Show this help message");
        System.out.println(" exit             : Exit the program");
    }
}
