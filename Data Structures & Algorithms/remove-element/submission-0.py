class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        for n in nums:
            if n != val:
                result.append(n)

        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)