class Solution:
    def findMin(self, nums: List[int]) -> int:
        smallest = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            smallest = min(smallest, nums[m])
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1

        return smallest