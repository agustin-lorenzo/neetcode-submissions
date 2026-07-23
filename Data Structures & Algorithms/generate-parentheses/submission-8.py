class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combo = []

        def backtrack(nOpen, nClose):
            if nClose == n:
                result.append("".join(combo))
                return
            
            if nClose < nOpen:
                combo.append(')')
                backtrack(nOpen, nClose + 1)
                combo.pop()
            
            if nOpen < n:
                combo.append('(')
                backtrack(nOpen + 1, nClose)
                combo.pop()
        
        backtrack(0, 0)
        return result