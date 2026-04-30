class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combo = []

        def dfs(numOpen, numClose):
            if numClose == n:
                result.append("".join(combo))
                return
            
            if numOpen < n:
                combo.append('(')
                dfs(numOpen + 1, numClose)
                combo.pop()

            if numClose < numOpen:
                combo.append(')')
                dfs(numOpen, numClose + 1)
                combo.pop()
            
        dfs(0, 0)
        return result