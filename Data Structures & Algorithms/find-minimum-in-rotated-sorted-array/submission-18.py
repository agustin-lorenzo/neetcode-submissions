class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            minimum = min(nums[m], minimum)
            if nums[m] > nums[r]: # in left/larger portion -> move right
                l = m + 1
            else: # in right/smaller portion
                r = m - 1

        return minimum