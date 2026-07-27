from heapq import heapify, heappush, heappop

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k
        heapify(self.nums)

        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val: int) -> int:
        heappush(self.nums, val)

        if len(self.nums) > self.k:
            heappop(self.nums)

        return self.nums[0]