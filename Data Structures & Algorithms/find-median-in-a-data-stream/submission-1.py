class MedianFinder:

    def __init__(self):
        # two equal size heaps, large, small, minheap, maxheap
        # larger portion is minheap, gets smallest element from larger half of array
        # smaller portion is maxheap, gets largest element from smallest half of array
        # both are as close to the median as possible
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # make sure every num in small is <= every num in large
        if (self.small and self.large and 
            -self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return (-self.small[0] + self.large[0]) / 2
        