# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        curr2 = l2
        carry = 0
        newh = ListNode(0)
        newCurr = newh
        while curr1 and curr2:
            res = curr1.val + curr2.val + carry
            carry = res // 10
            newCurr.next = ListNode((res % 10))
            newCurr = newCurr.next
            curr1 = curr1.next
            curr2 = curr2.next
        while curr1:
            res = curr1.val + carry
            carry = res // 10
            newCurr.next = ListNode((res % 10))
            newCurr = newCurr.next
            curr1 = curr1.next
        while curr2:
            res = curr2.val + carry
            carry = res // 10
            newCurr.next = ListNode((res % 10))
            newCurr = newCurr.next
            curr2 = curr2.next
        if carry:
            newCurr.next = ListNode(carry)
        return newh.next