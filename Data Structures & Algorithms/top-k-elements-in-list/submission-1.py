class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for num in nums:
            freqs[num] += 1

        arr = []
        for key, value in freqs.items():
            arr.append([value, key])
        arr.sort()

        result = []
        for i in range(k):
            result.append(arr.pop()[1])
        return result