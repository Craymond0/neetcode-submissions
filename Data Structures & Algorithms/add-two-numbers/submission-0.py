# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        cur = dummy

        while l1 and l2:

            operand = l1.val + l2.val + carry
            carry = operand // 10
            digit = operand % 10
            
            cur.next = ListNode(digit)
            cur = cur.next

            l1 = l1.next
            l2 = l2.next
        
        while l1:
            operand = l1.val + carry 
            carry = operand // 10
            digit = operand % 10

            cur.next = ListNode(digit)
            cur = cur.next
            l1 = l1.next
    
        while l2:
            operand = l2.val + carry
            carry = operand // 10
            digit = operand % 10

            cur.next = ListNode(digit)
            cur = cur.next

            l2 = l2.next

        if carry:
            cur.next = ListNode(carry)
            cur = cur.next


        return dummy.next


