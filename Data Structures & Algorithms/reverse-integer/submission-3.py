class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        remain = abs(x)
        
        while remain:
            digit = remain % 10
            res = (res * 10) + digit
            remain //= 10
            
        # Re-apply sign
        res = res if x >= 0 else -res
        
        # Boundary check
        if res < -2147483648 or res > 2147483647:
            return 0
        return res