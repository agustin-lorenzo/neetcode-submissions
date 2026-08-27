class ListNode:

    def __init__(self, key, value):
        self.key, self.val = key, value
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):        
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = ListNode(0, 0), ListNode(0, 0)
        self.head.prev, self.tail.next = self.tail, self.head

    def insert(self, node: ListNode) -> None:
        prev, nxt = self.head.prev, self.head
        prev.next, node.prev = node, prev
        node.next, nxt.prev = nxt, node

    def remove(self, node: ListNode) -> None:
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

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
