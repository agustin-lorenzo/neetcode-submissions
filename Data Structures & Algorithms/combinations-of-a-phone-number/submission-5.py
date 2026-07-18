class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        num2char = {'2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz'}

        result = []
        combo = []

        def dfs(i):
            if i == len(digits):
                result.append("".join(combo))
                return
            
            for c in num2char[digits[i]]:
                combo.append(c)
                dfs(i + 1)
                combo.pop()
            
        dfs(0)
        return result