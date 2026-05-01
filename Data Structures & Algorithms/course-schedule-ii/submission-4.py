class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        result = []
        
        visited = set() # correctly processed nodes
        cycle = set() # current path
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            cycle.remove(course)
            visited.add(course)
            result.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return result
