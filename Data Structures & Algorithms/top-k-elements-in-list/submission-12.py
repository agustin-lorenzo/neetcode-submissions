class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for n, f in freq.items():
            buckets[f].append(n)

        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result