# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        head2 = prev
        cur = head
        head = head.next
        while head and head2:
            cur.next = head2
            head2 = head2.next
            cur = cur.next

            cur.next = head
            head = head.next
            cur = cur.next

        
        while head:
            cur.next = head
            head = head.next
            cur = cur.next
        
        while head2:
            cur.next = head2
            head2 = head2.next
            cur = cur.next
