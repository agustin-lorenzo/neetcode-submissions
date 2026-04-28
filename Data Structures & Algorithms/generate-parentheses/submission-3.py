class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        combo = []
        def backtrack(numOpen, numClose):
            if numOpen == numClose == n:
                result.append("".join(combo))
                return
            
            if numOpen < n:
                combo.append('(')
                backtrack(numOpen + 1, numClose)
                combo.pop()
            
            if numClose < numOpen:
                combo.append(')')
                backtrack(numOpen, numClose + 1)
                combo.pop()
        
        backtrack(0, 0)
        return result