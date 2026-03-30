class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []

        l = 0
        r = k - 1
        while r < len(nums):
            currentMax = max(nums[l:r+1])
            result.append(currentMax)
            l += 1
            r += 1
        
        return result 