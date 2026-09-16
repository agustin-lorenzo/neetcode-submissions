class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        i = 0
        for color in range(3):
            for j in range(counts[color]):
                nums[i] = color
                i += 1