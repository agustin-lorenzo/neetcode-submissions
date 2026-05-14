class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            temp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            result = max(result, currMax)

        return result