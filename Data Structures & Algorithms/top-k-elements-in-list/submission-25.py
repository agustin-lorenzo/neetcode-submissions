class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i, n in enumerate(nums):
            freq[n] = freq.get(n, 0) + 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in freq.items():
            buckets[value].append(key)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result