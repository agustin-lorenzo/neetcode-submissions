class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: set() for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].add(pre)

        order = []
        visited = set()
        path = set()

        def dfs(c):
            if c in visited:
                return True
            if c in path:
                return False
            
            path.add(c)
            for pre in adj[c]:
                if not dfs(pre):
                    return False
            path.remove(c)

            visited.add(c)
            order.append(c)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return order