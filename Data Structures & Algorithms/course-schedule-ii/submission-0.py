class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c:[] for c in range(numCourses)}

        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        # 3 possible states:
        # visited: course has been added to output
        # visiting: course not added to output, but added to cycle
        # unvisited: course isn't in output or in current cycle path

        output = []
        visited, cycle = set(), set()
        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for pre in prereq[course]:
                if not dfs(pre):
                    return False
                
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output