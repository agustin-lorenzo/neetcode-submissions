class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for n in nums:
            sequence = 1
            current = n
            while current - 1 in seen:
                sequence += 1
                current -= 1
            longest = max(longest, sequence)
        
        return longest