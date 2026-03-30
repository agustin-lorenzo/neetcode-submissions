class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)

        while len(minHeap) > 1:
            stone1, stone2 = -heapq.heappop(minHeap), -heapq.heappop(minHeap)
            if stone1 > stone2:
                stone1 -= stone2
                heapq.heappush(minHeap, -stone1)
            elif stone2 > stone1:
                stone2 -= stone1
                heapq.heappush(minHeap, -stone2)

        if len(minHeap) > 0:
            return -minHeap[0]
        else:
            return 0

