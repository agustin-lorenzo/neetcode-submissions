class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        fast, slow = 0, 0        
        while fast < len(nums):
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while slow2 < len(nums):
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow
