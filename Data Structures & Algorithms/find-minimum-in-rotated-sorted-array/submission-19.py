class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] > nums[r]: # in left/larger portion
                l = m + 1
            else:
                r = m - 1
        
        return result