class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neigh in adj[node]:
                if neigh == parent:
                    continue
                if not dfs(neigh, node):
                    return False
            return True
        
        if not dfs(0, None):
            return False
        
        return len(visited) == n