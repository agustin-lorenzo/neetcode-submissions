class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        current = nums[0]
        for _ in range(k):
            current = -heapq.heappop(nums)
        
        return current