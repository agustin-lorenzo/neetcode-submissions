class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            result += i + 1
            result -= nums[i]
        
        return result