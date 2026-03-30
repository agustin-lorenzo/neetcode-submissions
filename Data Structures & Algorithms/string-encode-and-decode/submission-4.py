class Solution:

    def encode(self, strs):
        result = ""
        for s in strs:
            result += s
            result += "@@"

        return result

    def decode(self, s):
        strs = []
        prev = 0
        for i in range(len(s)):
            if i < len(s) - 1 and s[i] == '@' and s[i + 1] == '@':
                string = s[prev:i]
                strs.append(string)
                i += 2
                prev = i

        return strs
        
