class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combo = []

        def dfs(nOpen, nClose):
            if nClose == n:
                result.append("".join(combo))
                return
            
            if nClose < nOpen:
                combo.append(')')
                dfs(nOpen, nClose + 1)
                combo.pop()
            
            if nOpen < n:
                combo.append('(')
                dfs(nOpen + 1, nClose)
                combo.pop()
        
        dfs(0, 0)
        return result