class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def dfs(current, numOpen, numClose):
            if numOpen == n and numClose == n:
                result.append(current)
                return
            
            if numOpen < n:
                newStr = current + "("
                dfs(newStr, numOpen + 1, numClose)
            
            if numClose < n and numClose < numOpen:
                newStr = current + ")"
                dfs(newStr, numOpen, numClose + 1)

        dfs("", 0, 0)
        return result
            
            
