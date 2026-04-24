class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2c = {'2': "abc",
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz"}

        result = []

        current = []
        def backtrack(i):
            if i >= len(digits):
                result.append("".join(current))
                return
            
            chars = d2c[digits[i]]
            for c in chars:
                current.append(c)
                backtrack(i + 1)
                current.pop()
        
        if digits:
            backtrack(0)
        return result