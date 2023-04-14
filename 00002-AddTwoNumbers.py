# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Logic: Mathematical Approach with Carry Flag
        
        Time: O(max(m,n))
        Space: O(max(m,n))
        """    
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            total = a + b + carry
            if total >= 10:
                carry = 1
                total -= 10
            else:
                carry = 0
            head.next = ListNode(total)
            head = head.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry:
            head.next = ListNode(carry)
        
        return dummy.next
