class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        1. start binary search, compute mid value
        2. check for pivot
        3. move pointers appropriately
        '''
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]