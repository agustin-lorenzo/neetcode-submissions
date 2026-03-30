class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # [1, 2, 3, 4]
        #     ^  ^
        start = 0
        end = len(numbers) - 1

        while start < end:
            summed = numbers[start] + numbers[end]
            if summed == target:
                return [start + 1, end + 1]
            elif summed < target:
                start += 1
            elif summed > target:
                end -= 1
