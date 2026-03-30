class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = defaultdict(int)

        for i, n in enumerate(nums):
            if n in comps:
                return [comps[n], i]
            c = target - n
            comps[c] = i