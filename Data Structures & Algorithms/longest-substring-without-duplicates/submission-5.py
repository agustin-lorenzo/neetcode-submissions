class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # left and right pointers start at index 0
        # use hashset to determine when duplicates are encountered
        # when duplicate found, shift left and remove s[l] from set
        seen = set()
        longest = 0
        l = 0

        for r in range(len(s)):
            c = s[r]
            while c in seen:
                seen.remove(s[l])
                l += 1
            seen.add(c)
            longest = max(longest, (r - l + 1))

        return longest        