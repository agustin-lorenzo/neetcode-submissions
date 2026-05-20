class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head, self.tail = Node(0, 0), Node(0, 0)
        self.head.prev, self.tail.next = self.tail, self.head
    
    def insert(self, node: Node) -> None:
        prev, nxt = self.head.prev, self.head
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node
    
    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
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
