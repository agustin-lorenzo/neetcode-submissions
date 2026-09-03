class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        order = []
        adj = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set()
        path = set()
        def dfs(course):
            if course in visited:
                return True
            
            if course in path:
                return False
            
            path.add(course)
            for neigh in adj[course]:
                if not dfs(neigh):
                    return False            
            path.remove(course)

            visited.add(course)
            order.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return order