class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            if nums[m] > nums[r]: # in left/larger portion
                # check m relative to target
                if target < nums[l] or nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            
            else:
                if target > nums[r] or nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

        return -1