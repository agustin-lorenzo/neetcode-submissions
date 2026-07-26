class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        order = []
        visited = set()
        path = set()

        def dfs(course):
            if course in visited:
                return True
            if course in path:
                return False
            
            path.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            path.remove(course)
            visited.add(course)
            order.append(course)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return order