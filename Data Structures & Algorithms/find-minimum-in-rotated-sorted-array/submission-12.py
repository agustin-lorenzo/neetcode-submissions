class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]

        while l <= r:
            m = (l + r) // 2
            result = min(nums[m], result)
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return result