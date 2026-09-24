class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
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
            for n in adj[course]:
                if not dfs(n):
                    return False
            path.remove(course)

            visited.add(course)
            return True
                
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True