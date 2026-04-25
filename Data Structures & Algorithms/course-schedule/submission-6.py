class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)

        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            
            visited.add(course)
            for pre in adj[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            adj[course] = []            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True