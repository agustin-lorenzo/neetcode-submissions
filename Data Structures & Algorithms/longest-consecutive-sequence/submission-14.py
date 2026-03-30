class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            current = n - 1
            counter = 1
            while current in numSet:
                current -= 1
                counter += 1
            longest = max(longest, counter)

        return longest
            