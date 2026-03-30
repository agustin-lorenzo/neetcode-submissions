class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        for i in range(len(nums)):
            if nums[i] in compliments:
                return [compliments[nums[i]], i]
            else:
                compliment = target - nums[i]
                compliments[compliment] = i
