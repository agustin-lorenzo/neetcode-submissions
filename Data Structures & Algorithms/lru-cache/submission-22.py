class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.tail, self.head = ListNode(0, 0), ListNode(0, 0)
        self.tail.next, self.head.prev = self.head, self.tail

    def remove(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node: ListNode) -> None:
        prev, nxt = self.head.prev, self.head
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.tail.next
            self.remove(lru)
            del self.cache[lru.key]
