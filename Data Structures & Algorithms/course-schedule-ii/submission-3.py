class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c: [] for c in range(numCourses)}
        for course, pre in prerequisites:
            adj[course].append(pre)
        
        visited = set() # correctly processed and is valid
        cycle = set() # nodes seen in current dfs stack
        order = []
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for n in adj[course]:
                if not dfs(n):
                    return False
            cycle.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return order