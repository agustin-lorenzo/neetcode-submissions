class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            counts[n] = counts.get(n, 0) + 1
        for n, c in counts.items():
            freq[c].append(n)
        
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
