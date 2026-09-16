class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(l, r):
            m = (l + r) // 2
            left, right = nums[l:m+1], nums[m+1:r+1]
            i, j, k = l, 0, 0 # i: start of portion of original array
                              # j: start of left subarray copy
                              # k: start of right subarray copy
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
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(l, r):
            if l >= r:
                return
            m = (l + r) // 2
            mergeSort(l, m)
            mergeSort(m + 1, r)
            merge(l, r)
        
        mergeSort(0, len(nums) - 1)
        return nums