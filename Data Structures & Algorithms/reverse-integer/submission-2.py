class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        result = int(str(abs(x))[::-1]) * sign

        if result < -2147483648 or result > 2147483647:
            return 0
        
        return result