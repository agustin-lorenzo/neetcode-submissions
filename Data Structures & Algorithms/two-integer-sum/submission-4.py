class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}

        for i, n in enumerate(nums):
            c = target - n
            if c in compliments:
                return [compliments[c], i]
            
            compliments[n] = i