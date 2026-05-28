# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        before = dummy
        firstOut = head
        while firstOut:
            count = 0
            curr = firstOut
            while firstOut and count < k:
                firstOut = firstOut.next
                count += 1
            if count < k:
                return dummy.next
            firstIn = curr
            prev = None
            while count > 0:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                count -= 1
            before.next = prev
            before = firstIn
            firstIn.next = firstOut
        return dummy.next