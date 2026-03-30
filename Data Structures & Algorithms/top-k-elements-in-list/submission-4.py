class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = 1 + counts.get(num, 0)
        countsList = list(counts.items())
        countsList = sorted(countsList, key=lambda x: x[1], reverse=True)

        result = []
        for i in range(k):
            result.append(countsList[i][0])
        return result