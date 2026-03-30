class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            added = numbers[l] + numbers[r]
            if added > target:
                r -= 1
            elif added < target:
                l += 1
            else:
                return [l + 1, r + 1]
        