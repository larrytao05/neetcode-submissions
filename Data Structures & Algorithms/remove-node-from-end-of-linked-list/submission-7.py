# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = end = head
        prev = cur
        n -= 1
        while n:
            end = end.next
            n -= 1
        
        while end.next:
            prev = cur
            cur = cur.next
            end = end.next
        print(cur.val)
        print(end.val)
        if cur == head:
            return head.next
        if prev:
            prev.next = cur.next
        cur.next = None
        return head
        
