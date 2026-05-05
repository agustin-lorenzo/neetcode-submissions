class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prevH):
            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                heights[r][c] < prevH):
                return
            
            visited.add((r, c))
            newH = max(prevH, heights[r][c])
            dfs(r + 1, c, visited, newH)
            dfs(r - 1, c, visited, newH)
            dfs(r, c + 1, visited, newH)
            dfs(r, c - 1, visited, newH)

        for r in range(R):
            dfs(r, 0, pac, float("-inf"))
            dfs(r, C - 1, atl, float("-inf"))
        
        for c in range(C):
            dfs(0, c, pac, float("-inf"))
            dfs(R - 1, c, atl, float("-inf"))
        
        return [[r, c] for r, c in (pac & atl)]