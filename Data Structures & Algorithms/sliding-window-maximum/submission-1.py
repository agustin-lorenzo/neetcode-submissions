class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = collections.deque()
        l, r = 0, 0 # represent window

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # remove left value from window when out of bounds
            if l > q[0]: # left end of q is out of left bound
                q.popleft()
            
            if (r + 1) >= k:
                result.append(nums[q[0]])
                l += 1            
            r += 1
        
        return result
            
