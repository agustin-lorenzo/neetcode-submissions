class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for n in nums:
            counter = 1
            current = n - 1
            while current in numSet:
                counter += 1
                current -= 1
            longest = max(longest, counter)

        return longest