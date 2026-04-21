class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def helper(arr, l, m, r):
            left, right = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def merge(arr, l, r):
            if l == r:
                return arr
            
            m = (l + r) // 2
            merge(arr, l, m)
            merge(arr, m + 1, r)
            helper(arr, l, m, r)
            return arr
        
        return merge(nums, 0, len(nums) - 1)