class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                previ, prevt = stack.pop()
                result[previ] = i - previ
            stack.append([i, t])
        
        return result