class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        numSet = set(nums)

        for n in nums:
            if n - 1 not in numSet: # start of sequence
                length = 1
                while n + length in numSet:
                    length += 1
                result = max(result, length)
        
        return result