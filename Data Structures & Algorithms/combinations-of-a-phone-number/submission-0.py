class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
            
        num2letter = {'2': "ABC", '3': "DEF", '4': "GHI", '5': "JKL", '6': "MNO", '7': "PQRS", '8': "TUV", '9': "WXYZ"}
        result = []

        def backtrack(prev, i):
            if i >= len(digits):
                result.append(prev)
                return

            letters = num2letter[digits[i]]

            for l in letters:
                added = (prev + l).lower()
                backtrack(added, i + 1)
            
        backtrack("", 0)
        return result
