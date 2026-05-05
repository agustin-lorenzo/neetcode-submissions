class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for n1, n2 in prerequisites:
            adj[n1].append(n2)

        order = []
        visited = set()
        cycle = set()
        def dfs(course):
            if course in visited:
                return True
            
            if course in cycle:
                return False
            
            cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []

        return order