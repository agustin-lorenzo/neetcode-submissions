from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]
        for num, freq in freqs.items():
            buckets[freq].append(num)
        
        result = []
        for bucket in buckets[::-1]:
            for n in bucket:
                result.append(n)
                if len(result) == k:
                    return result