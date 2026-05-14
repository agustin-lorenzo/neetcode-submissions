class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)

        for i in range(n + 1):
            count = 0
            number = i
            while number > 0:
                count += number % 2
                number >>= 1
            output[i] = count
        
        return output