class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            summed = numbers[start] + numbers[end]
            if summed > target:
                end -= 1
            elif summed < target:
                start += 1
            else:
                return [start + 1, end + 1]