class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set()
        path = set()

        def dfs(c):
            if c in visited:
                return True
            if c in path:
                return False
            
            path.add(c)
            for n in adj[c]:
                if not dfs(n):
                    return False
            path.remove(c)

            visited.add(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True