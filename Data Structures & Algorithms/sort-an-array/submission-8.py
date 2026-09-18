class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def conquer(l, r):
            m = (l + r) // 2
            left, right = nums[l:m+1], nums[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] < right[k]:
                    nums[i] = left[j]
                    j += 1
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                i += 1
                j += 1
            while k < len(right):
                nums[i] = right[k]
                i += 1
                k += 1
        
        def divide(l, r):
            if l >= r:
                return
            m = (l + r) // 2
            divide(l, m)
            divide(m + 1, r)
            conquer(l, r)
        
        divide(0, len(nums) - 1)
        return nums