class ListNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.right = self.right
        self.right.left = self.left
        self.keys = {}

    def get(self, key: int) -> int:
        if key in self.keys:
            val = self.keys[key][1]
            self.use(key)
            return val
        return -1

    def put(self, key: int, value: int) -> None:    
        if key not in self.keys:
            self.size += 1
            node = ListNode(key, self.left, self.left.right)
            self.left.right.left = node
            self.left.right = node
            self.keys[key] = [node, value]
        else:
            self.keys[key][1] = value
            self.use(key)
        if self.size > self.capacity:
            self.evict()

    def use(self, key):
        node,val = self.keys[key]
        tmp = node.left
        node.right.left = node.left
        tmp.right = node.right

        tmp = self.left.right
        self.left.right = node
        node.right = tmp
        node.left = self.left
        tmp.left = node
    
    def evict(self):
        key = self.right.left.val
        del self.keys[key]
        self.right.left = self.right.left.left
        self.right.left.right = self.right
        self.size -= 1


        
