class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prev):
            if (r not in range(R) or
                c not in range(C) or
                (r, c) in visited or
                heights[r][c] < prev):
                return
            
            newH = heights[r][c]
            visited.add((r, c))
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
        
        return list(pac & atl)