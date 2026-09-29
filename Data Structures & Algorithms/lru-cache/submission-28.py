class Node:

    def __init__(self, key, value):
        self.key, self.val = key, value
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.tail, self.head = Node(0, 0), Node(0, 0)
        self.tail.next, self.head.prev = self.head, self.tail

    def remove(self, node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p
    
    def insert(self, node):
        p, n = self.head.prev, self.head
        p.next, node.prev = node, p
        node.next, n.prev = n, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.tail.next
            self.remove(lru)
            del self.cache[lru.key]