class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        seen = set(nums)

        for n in nums:
            counter = 1
            curr = n - 1
            while curr in seen:
                counter += 1
                curr -= 1
            longest = max(counter, longest)
        
        return longest