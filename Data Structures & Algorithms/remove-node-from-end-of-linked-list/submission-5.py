# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        if not head.next:
            return None
        while n:
            n -= 1
            cur = cur.next
        res = head
        if not cur:
            return head.next
        while cur and cur.next:
            cur = cur.next
            res = res.next
        res.next = res.next.next
        return head