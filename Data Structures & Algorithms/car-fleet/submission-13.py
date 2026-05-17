class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[(target - p) / s, p, s] for p, s in zip(position, speed)]
        cars.sort(key = lambda x: -x[1]) # sort by position

        stack = []
        for a, p, s in cars:
            if not stack or a > stack[-1]:
                stack.append(a)
        
        return len(stack)