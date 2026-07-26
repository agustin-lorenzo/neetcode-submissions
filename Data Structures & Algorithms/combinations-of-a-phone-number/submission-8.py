class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        d2c = {'2': "abc",               
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz"}
        result = []
        combo = []

        def backtrack(i):
            if i == len(digits):
                result.append("".join(combo))
                return
            
            for c in d2c[digits[i]]:
                combo.append(c)
                backtrack(i + 1)
                combo.pop()
        
        backtrack(0)
        return result
