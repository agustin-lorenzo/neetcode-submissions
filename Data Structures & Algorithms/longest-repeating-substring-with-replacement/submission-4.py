class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # choosing the substring: sliding window algorithm
        # while not valid, update l
        # hashmap contains both character and number of appearances in substring
        # when replacing, only replace chars that are not most freq
        longest = 0
        counts = {}

        l = 0
        for r in range(len(s)):
            c = s[r]
            counts[c] = counts.get(c, 0) + 1

            while not ((r - l + 1) - max(counts.values())) <= k:
                counts[s[l]] -= 1
                l += 1
            
            longest = max(longest, (r - l + 1))
        
        return longest