class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanStr = ""
        for c in s:
            if c.isalnum():
                cleanStr += c
            
        l, r = 0, len(cleanStr) - 1
        while l <= r:
            if cleanStr[l].lower() != cleanStr[r].lower():
                return False
            l += 1
            r -= 1

        return True