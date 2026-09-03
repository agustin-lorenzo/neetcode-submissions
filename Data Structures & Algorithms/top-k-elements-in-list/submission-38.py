from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        for n, f in freq.items():
            buckets[f].append(n)
        
        result = []
        for b in buckets[::-1]:
            for n in b:
                result.append(n)
                if len(result) == k:
                    return result