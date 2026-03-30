class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliments = {}
        
        for i, n in enumerate(nums):
            if n in compliments:
                return [compliments[n], i]
            else:
                compliment = target - n
                compliments[compliment] = i
        
