class Solution:
    def reverse(self, x: int) -> int:
        strx = list(str(x))

        l, r = 0, len(strx) - 1
        if strx[l] == '-':
            l += 1
        while l < r:
            strx[l], strx[r] = strx[r], strx[l]
            l += 1
            r -= 1
        
        x = int("".join(strx))
        if x < -2147483648 or x > 2147483647:
            return 0
        
        return x