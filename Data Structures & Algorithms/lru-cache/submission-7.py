class Node:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.prev = self.tail
        self.tail.next = self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):
        prev = self.head.prev
        prev.next, node.prev = node, prev
        self.head.prev, node.next = node, self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.cap:
            lru = self.tail.next
            self.remove(lru)
            del self.cache[lru.key]