class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set()
        path = set()

        def dfs(node):
            # DON'T DO IF NOT NODE: 0 WILL BE AN INPUT!
            if node in visited:
                return True
            if node in path:
                return False
            
            path.add(node)
            for neighbor in adj[node]:
                if not dfs(neighbor):
                    return False

            path.remove(node)
            visited.add(node)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
