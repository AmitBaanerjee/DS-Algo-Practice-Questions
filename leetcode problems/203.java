203. Remove Linked List Elements
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeElements(ListNode head, int val) {
        ListNode temp=new ListNode(0);
        //temp.next=head;
        ListNode current=head;
        ListNode prev=temp;
        while(current!=null){
            if (current.val==val)
                prev.next=current.next;

            else{
                prev.next=current;
                prev=prev.next;
            }
            current=current.next;
        }
        return temp.next;
    }
}
