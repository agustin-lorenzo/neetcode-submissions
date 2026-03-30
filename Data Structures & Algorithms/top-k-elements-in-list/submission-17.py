class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = defaultdict(int)
        for n in nums:
            freqs[n] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in freqs.items():
            buckets[value].append(key)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                if len(result) == k:
                    return result
                result.append(n)
        
        return result