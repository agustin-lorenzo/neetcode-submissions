class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for n in nums:
            counter = 1
            current = n - 1
            while current in seen:
                counter += 1
                current -= 1
            longest = max(counter, longest)

        return longest