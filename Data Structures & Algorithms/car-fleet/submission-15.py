class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arrivals = [[p, s] for p, s in zip(position, speed)]
        arrivals.sort(reverse = True) # want to process closer to target (higher p, decending order) first
        stack = []

        for p, s in arrivals:
            t = (target - p) / s
            stack.append(t)

            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)