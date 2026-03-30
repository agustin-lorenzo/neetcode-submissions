class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        current = []
        def backtrack(i):
            if i >= len(nums):
                result.append(current.copy())
                return

            # include nums[i]
            current.append(nums[i])
            backtrack(i + 1)
            
            # exclude nums[i]
            current.pop()
            backtrack(i + 1)

        backtrack(0)
        return result
