# just doing brute force just to say i could at least do that in an interview

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [-1] * len(queries)

        for i, q in enumerate(queries):

            for start, end in intervals:
                length = end - start + 1
                if start <= q <= end and (result[i] == -1 or result[i] > length):
                    result[i] = length
        
        return result
