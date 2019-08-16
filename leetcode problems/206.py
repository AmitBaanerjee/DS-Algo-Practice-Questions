# 206. Reverse Linked List
#
# Reverse a singly linked list.
#
# Example:
#
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode previous=null;
        ListNode current=head;
        while(current!=null){
            ListNode temp=current.next;
            current.next=previous;
            previous=current;
            current=temp;
        }
        return previous;
    }
}
