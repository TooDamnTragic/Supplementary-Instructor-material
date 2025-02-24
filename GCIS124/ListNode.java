
    class ListNode {
        int val;
        ListNode next;
        
        ListNode(int val) {
            this.val = val;
            this.next = null;
        }
    }
    
    class ReverseLinkedList {
    
        public static ListNode reverseList(ListNode head) {
            //Implement the logic to reverse the linked list.
            return head;
        }
        

        public static ListNode createLinkedList(int[] values) {
            if (values == null || values.length == 0) {
                return null;
            }
            
            ListNode head = new ListNode(values[0]);
            ListNode current = head;
            
            for (int i = 1; i < values.length; i++) {
                current.next = new ListNode(values[i]);
                current = current.next;
            }
            
            return head;
        }

    public static void printLinkedList(ListNode head) {
        ListNode current = head;
        
        while (current != null) {
            System.out.print(current.val);
            if (current.next != null) {
                System.out.print(" -> ");
            }
            current = current.next;
        }
        System.out.println(" -> null");
    }
    


    
    public static void main(String[] args) {
        // Create a linked list 1 -> 2 -> 3 -> 4 -> 5 -> null
        ListNode head = createLinkedList(new int[]{1, 2, 3, 4, 5});
        
        System.out.println("Original List:");
        printLinkedList(head);
        
        // Reverse the linked list
        head = reverseList(head);
        
        System.out.println("\nReversed List:");
        printLinkedList(head);
    }
}




// public static ListNode reverseList(ListNode head) {
//     ListNode prev = null;
//     ListNode current = head;
//     while (current != null) {
//         // Temporarily store the next node
//         ListNode next = current.next;
        
//         // Reverse the current node's pointer
//         current.next = prev;
        
//         // Move prev and current one step forward
//         prev = current;
//         current = next;
//     }
    
//     // prev will end up at the new head of the reversed list
//     return prev;
// }