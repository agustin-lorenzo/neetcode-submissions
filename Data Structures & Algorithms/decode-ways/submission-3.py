class Solution:
    def numDecodings(self, s: str) -> int:
        result = 0
        memo = {}
        
        def backtrack(i):
            nonlocal result
            if i >= len(s):
                return 1
            
            if s[i] == "0":
                return 0
            
            if i in memo:
                return memo[i]

            # double digit choice
            result = backtrack(i + 1)
            if i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and i + 1 < len(s) and s[i + 1] in "0123456")):
                result += backtrack(i + 2)

            memo[i] = result
            return result
        
        return backtrack(0)