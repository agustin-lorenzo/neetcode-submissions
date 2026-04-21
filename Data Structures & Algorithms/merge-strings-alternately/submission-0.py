class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""

        length = min(len(word1), len(word2))
        i = 0
        while i < length:
            result += word1[i]
            result += word2[i]
            i += 1
        
        if len(word1) > len(word2):
            result += word1[i:]
        if len(word2) > len(word1):
            result += word2[i:]

        return result