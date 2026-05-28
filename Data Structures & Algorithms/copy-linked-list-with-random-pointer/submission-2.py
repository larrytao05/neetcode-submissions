"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        seen = {None: None}
        curr = head
        while curr:
            seen[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            if curr.next:
                seen[curr].next = seen[curr.next]
            if curr.random:
                seen[curr].random = seen[curr.random]
            curr = curr.next
        return seen[head]
        