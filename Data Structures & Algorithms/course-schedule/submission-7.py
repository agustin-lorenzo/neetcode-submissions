class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set() # correctly processed
        cycle = set() # current path being processed, TBD
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
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
                