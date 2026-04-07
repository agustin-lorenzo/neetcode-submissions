class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]

        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            minimum = min(minimum, nums[m])
            if nums[m] > nums[r]: # in left, larger portion
                l = m + 1
            else:
                r = m - 1
        
        return minimum