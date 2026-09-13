class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        combo = []

        def backtrack(i):
            if i == len(nums):
                result.append(combo.copy())
                return
            
            combo.append(nums[i])
            backtrack(i + 1)

            combo.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return result