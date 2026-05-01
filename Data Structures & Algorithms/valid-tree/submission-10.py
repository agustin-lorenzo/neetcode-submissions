class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {node: [] for node in range(n)}
        for node, neighbor in edges:
            adj[node].append(neighbor)
            adj[neighbor].append(node)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False

            visited.add(node) # NOT "CORRECTLY" PROCESSED, JUST PROCESSED AT ANY POINT -> CYCLE DETECTED
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            
            return True
        
        if not dfs(0, None):
            return False
        
        return len(visited) == n