class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        numSet = set()
        for n in nums:
            numSet.add(n)

        longest = 1
        for n in nums:
            current = 1
            j = n + 1
            while j in numSet:
                current += 1
                longest = max(longest, current)
                j += 1
        
        return longest
