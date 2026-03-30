class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left and right pointers init at 0
        # increment right, save new chars to seen [value, index]
        # use hashmap to find duplicates, increment left pointer
        charSet = set()
        l = 0
        result = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            result = max(result, r - l + 1)

        return result