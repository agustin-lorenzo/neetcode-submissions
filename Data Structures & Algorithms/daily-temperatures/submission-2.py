class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack, push val = [temp, idx] as we encounter them
        # current = temp[i]: pop from stack as long temp > stack.pop()
        # to get the number of days, i - val[1] <- append to result list
        result = [0] * len(temperatures)
        stack = [] # [t, idx]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                prevDay = stack.pop()
                result[prevDay[1]] = i - prevDay[1]

            stack.append([t, i])
        
        return result