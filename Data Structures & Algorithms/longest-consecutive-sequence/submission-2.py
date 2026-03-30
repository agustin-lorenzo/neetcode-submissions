class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums is None or len(nums) == 0:
            return 0

        maxSequence = 1
        numsSet = set(nums)

        for num in nums:
            currentCounter = 1
            if num - 1 not in numsSet:
                rightNeighbor = num + 1
                while rightNeighbor in numsSet:
                    currentCounter += 1
                    rightNeighbor += 1
            maxSequence = max(currentCounter, maxSequence)

        return maxSequence
                