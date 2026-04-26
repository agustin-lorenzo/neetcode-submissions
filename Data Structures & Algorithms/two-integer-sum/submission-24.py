class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = {} # {previous compliment: previous index}

        for i, n in enumerate(nums):
            if n in comps:
                return [comps[n], i]
            c = target - n
            comps[c] = i