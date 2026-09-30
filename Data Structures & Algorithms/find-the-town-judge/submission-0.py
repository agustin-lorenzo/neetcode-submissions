class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for n1, n2 in trust:
            outgoing[n1] += 1
            incoming[n2] += 1
        
        for i in range(1, n + 1):
            if outgoing[i] == 0 and incoming[i] == (n - 1):
                return i
        
        return -1
