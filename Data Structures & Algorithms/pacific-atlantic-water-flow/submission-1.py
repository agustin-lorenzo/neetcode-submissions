class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pacific, atlantic = set(), set()

        def dfs(r, c, visited, prevH):
            if ((r, c) in visited or
                r < 0 or c < 0 or r == R or c == C or
                heights[r][c] < prevH):
                return
            visited.add((r, c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])

        for c in range(C):
            dfs(0, c, pacific, heights[0][c])
            dfs(R - 1, c, atlantic, heights[R - 1][c])

        for r in range(R):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, C - 1, atlantic, heights[r][C - 1])
        
        result = []
        for r in range(R):
            for c in range(C):
                if (r, c) in pacific and (r, c) in atlantic:
                    result.append([r, c])
        return result
