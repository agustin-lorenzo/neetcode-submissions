class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {n: [] for n in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node)            
            for n2 in adj[node]:
                if n2 == parent:
                    continue
                if not dfs(n2, node):
                    return False
            return True
        
        if not dfs(0, -1) or len(visited) != n:
            return False
        return True