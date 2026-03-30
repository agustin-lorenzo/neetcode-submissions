class Solution:
    def findMin(self, nums: List[int]) -> int:
        result = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            result = min(result, nums[m])
            if nums[m] > nums[r]: # in greater/left portion
                l = m + 1
            else:
                r = m - 1
        
        return result
            