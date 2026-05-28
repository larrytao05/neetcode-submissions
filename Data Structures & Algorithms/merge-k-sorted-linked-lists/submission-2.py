# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        dummy = ListNode(0)
        curr = dummy
        empty = 0
        while empty < k:
            minVal = math.inf
            ind = -1
            empty = 0
            for i in range(k):
                l = lists[i]
                if not l:
                    empty += 1
                    if empty == k:
                        break
                    continue
                if l.val < minVal:
                    minVal = l.val
                    ind = i
            if minVal != math.inf:
                curr.next = ListNode(minVal)
                curr = curr.next
                lists[ind] = lists[ind].next
        return dummy.next
            
                
                