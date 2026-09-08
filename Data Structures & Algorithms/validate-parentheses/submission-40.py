class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        c2o = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c in c2o:
                if not stack or stack.pop() != c2o[c]:
                    return False
            else:
                stack.append(c)
        
        return not stack