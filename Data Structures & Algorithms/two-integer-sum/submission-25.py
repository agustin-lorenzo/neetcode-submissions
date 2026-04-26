class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {} # {previous compliment: previous index}

        for i, n in enumerate(nums):
            c = target - n
            if c in comps:
                return [comps[c], i]
            
            comps[n] = i