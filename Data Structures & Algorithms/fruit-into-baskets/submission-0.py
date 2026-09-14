class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        result = 0

        l = 0
        for r in range(len(fruits)):
            window[fruits[r]] += 1
            while len(window) > 2:
                window[fruits[l]] -= 1
                if window[fruits[l]] == 0:
                    del window[fruits[l]]
                l += 1
            
            result = max(result, (r - l + 1))
        
        return result