class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in nums:
            prev = n - 1
            length = 1
            while prev in seen:
                length += 1
                prev -= 1
            longest = max(length, longest)

        return longest