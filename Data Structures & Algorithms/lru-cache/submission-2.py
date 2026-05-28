class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.capacity = capacity
        self.kv = {}
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev,nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    
    def insert(self, node):
        prev,nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.next,node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.kv:
            self.remove(self.kv[key])
            self.insert(self.kv[key])
            return self.kv[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.kv:
            self.remove(self.kv[key])
        self.kv[key] = Node(key,value)
        self.insert(self.kv[key])
        if self.capacity < len(self.kv):
            lru = self.head.next
            self.remove(lru)
            del self.kv[lru.key]