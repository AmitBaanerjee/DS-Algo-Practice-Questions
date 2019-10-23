86. Partition List

Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head==null)
            return null;
        ListNode beforeStart=null;
        ListNode beforeEnd=null;
        ListNode afterStart=null;
        ListNode afterEnd=null;
        ListNode current=head;
        while(current!=null){
            ListNode temp=current.next;
            current.next=null;
            if(current.val<x){
                if(beforeStart==null){
                    beforeStart=current;
                    beforeEnd=beforeStart;
                }
                else{
                    beforeEnd.next=current;
                    beforeEnd=beforeEnd.next;
                }
            }
            else{
                if(afterStart==null){
                    afterStart=current;
                    afterEnd=afterStart;
                }
                else{
                    afterEnd.next=current;
                    afterEnd=afterEnd.next;
                }
            }
            current=temp;
        }
        if (beforeStart==null){
            return afterStart;
        }
        beforeEnd.next=afterStart;
        return beforeStart;
    }
}
