
public class BST<E extends Comparable<E>> {
    private Node<E> root;
    private int size;

    // Node class definition
    private static class Node<T> {
        T value;
        Node<T> left, right;
        Node(T v) {
            value = v;
            left = right = null;
        }
    }

    public BST() {
        this.root = null;
        this.size = 0;
    }

    /**
     * Inserts the given value into the BST if it is not already present.
     * Returns true if insertion happened, false if it was a duplicate.
     */
    public boolean insert(E value) {
        if (root == null) {
            root = new Node<>(value);
            size++;
            return true;
        }
        // TODO: Insert into the correct subtree using a helper function
        //       If value is found, do not insert a duplicate; return false.
        //       If inserted, size++, return true.
        root = insertRecursive(root, value);
        // We’ll need a way to distinguish between a successful insert 
        // and “already exists.” One approach is to track if insertion occurred
        // in the helper. For now, assume always insertion is successful 
        // or do a check before reassigning root. Implementation is flexible.
        return true;
    }

    private Node<E> insertRecursive(Node<E> current, E value) {
        if (current == null) {
            size++; // new node
            return new Node<>(value);
        }
        int cmp = value.compareTo(current.value);
        if (cmp < 0) {
            current.left = insertRecursive(current.left, value);
        } else if (cmp > 0) {
            current.right = insertRecursive(current.right, value);
        } else {
            // value already exists; do NOT insert a duplicate
            // Optional: throw an exception or handle it in some way
        }
        return current;
    }

    /**
     * Returns true if this BST contains the given value.
     */
    public boolean contains(E value) {
        // TODO: Implement using a loop or recursion
        return false;
    }

    /**
     * Deletes the specified value from the BST, if it exists.
     * Returns true if deletion succeeded, false if value was not found.
     */
    public boolean delete(E value) {
        // (Optional) If you don’t want to implement delete, you can skip this
        // If implementing, you should track whether the value was found or not.
        if (!contains(value)) {
            return false;
        }
        root = deleteRecursive(root, value);
        size--;
        return true;
    }

    private Node<E> deleteRecursive(Node<E> current, E value) {
        // TODO: Implement the standard BST deletion logic:
        // 1) Search for the value in left/right subtrees
        // 2) If not found, return current (no changes).
        // 3) If found:
        //    - If current has one child or none, replace with the child.
        //    - If current has two children, find inorder successor/predecessor, 
        //      copy its value to current, then delete it from the subtree.
        return current;
    }

    /**
     * Returns the number of elements currently in the BST.
     */
    public int size() {
        return size;
    }

    /**
     * Returns an in-order traversal of the BST as a String.
     * Example for an integer tree: "1 3 5 7 9"
     */
    public String toInOrderString() {
        StringBuilder sb = new StringBuilder();
        inOrder(root, sb);
        return sb.toString().trim();
    }

    private void inOrder(Node<E> node, StringBuilder sb) {
        if (node == null) return;
        inOrder(node.left, sb);
        sb.append(node.value).append(" ");
        inOrder(node.right, sb);
    }

    /**
     * Returns a pre-order traversal of the BST as a String.
     */
    public String toPreOrderString() {
        StringBuilder sb = new StringBuilder();
        preOrder(root, sb);
        return sb.toString().trim();
    }

    private void preOrder(Node<E> node, StringBuilder sb) {
        // TODO: Root → Left → Right
    }

    /**
     * Returns a post-order traversal of the BST as a String.
     */
    public String toPostOrderString() {
        StringBuilder sb = new StringBuilder();
        postOrder(root, sb);
        return sb.toString().trim();
    }

    private void postOrder(Node<E> node, StringBuilder sb) {
        // TODO: Left → Right → Root
    }
}
