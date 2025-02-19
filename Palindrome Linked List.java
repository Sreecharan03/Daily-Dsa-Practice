Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    ListNode reverse(ListNode node){
        ListNode prev = null;
        ListNode curr = node;
        while(curr!=null){
                ListNode next = curr.next;
            curr.next = prev;
            prev =curr;
            curr = next;
        }
        return prev;
    }
    public boolean isPalindrome(ListNode head) {
        ListNode tmp=head,fast=head,slow=head;
        while(fast!=null && fast.next!=null){
            fast = fast.next.next;
            slow = slow.next;
        }
        slow = reverse(slow);

        while(slow!=null){
            if(tmp.val!=slow.val)return false;
            slow=slow.next;
            tmp = tmp.next;
        }
        return true;
    }
}
