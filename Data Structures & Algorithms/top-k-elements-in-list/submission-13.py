class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. use hashmap to count freqs for all n
        # 2. store nums in bucket array
        # 3. iterate backwards append k times
        freqs = defaultdict(int) # {num: count}
        for n in nums:
            freqs[n] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key, value in freqs.items():
            buckets[value].append(key)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k:
                    return result