234. Palindrome Linked List

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        Stack<Integer> s= new Stack<Integer>();
        ListNode slow=head;
        ListNode fast=head;
        while(fast!=null && fast.next!=null){
            s.push(slow.val);
            slow=slow.next;
            fast=fast.next.next;
        }
        //odd size linked list
        if(fast!=null){
            slow=slow.next;
        }
        while(slow!=null){
            int num=s.pop();
            if(num!=slow.val){
                return false;
            }
            slow=slow.next;
        }
    return true;
    }
}
