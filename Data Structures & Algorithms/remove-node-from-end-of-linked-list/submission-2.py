# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        curr = head
        i = 0
        prev = None
        fast = head
        l = 1
        while fast.next:
            l += 1
            fast = fast.next
        
        while i < (l-n):
            prev = curr
            curr = curr.next
            i += 1
        if not curr.next:
            prev.next = None
        else:
            if not prev:
                tmp = curr.next
                curr.next = None
                return tmp
            prev.next = curr.next
        return head
