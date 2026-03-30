class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i:[] for i in range(n)}
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        visited = set()
        def dfs(n):
            if n not in visited:
                visited.add(n)
            for neighbor in graph[n]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        components = 0
        for i in range(n):
            if i not in visited:
                components += 1
                dfs(i)
        
        return components
