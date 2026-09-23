class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        maxL, maxR = 0, 0
        total = 0

        while l < r:
            if height[l] < height[r]:
                maxL = max(maxL, height[l])
                l += 1
                total += max(0, maxL - height[l])
            else:
                maxR = max(maxR, height[r])
                r -= 1
                total += max(0, maxR - height[r])
        
        return total