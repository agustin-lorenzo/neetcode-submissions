class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = defaultdict(int)
        maxCount = 0

        for n in nums:
            counts[n] += 1
            if counts[n] > counts[maxCount]:
                maxCount = n
        
        return maxCount