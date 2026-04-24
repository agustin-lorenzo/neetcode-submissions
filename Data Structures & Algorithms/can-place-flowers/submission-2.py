class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 1:
                continue
            
            left = 0 if i == 0 else flowerbed[i - 1]
            right = 0 if i == len(flowerbed) - 1 else flowerbed[i + 1]

            if not left and not right:
                flowerbed[i] = 1
                n -= 1
        
        return n <= 0