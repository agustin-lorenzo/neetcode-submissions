class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair of values: temp, index(day)
        result = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                _, prevIdx = stack.pop()
                result[prevIdx] = i - prevIdx
            stack.append([t, i])
        
        return result
            