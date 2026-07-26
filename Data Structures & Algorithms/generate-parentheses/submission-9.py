class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = []

        def backtrack(nOpen, nClose):
            if nClose == n:
                result.append("".join(current))
                return
            
            if nClose < nOpen:
                current.append(')')
                backtrack(nOpen, nClose + 1)
                current.pop()
            
            if nOpen < n:
                current.append('(')
                backtrack(nOpen + 1, nClose)
                current.pop()
            
        backtrack(0, 0)
        return result