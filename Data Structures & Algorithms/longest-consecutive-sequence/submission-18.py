class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            counter = 1
            while n - 1 in numSet:
                counter += 1
                n = n - 1
            longest = max(longest, counter)
        
        return longest