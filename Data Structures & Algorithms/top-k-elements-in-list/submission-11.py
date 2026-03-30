class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]

        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        
        for num, freq in counts.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result