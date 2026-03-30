class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1

        while start < end:
            added = numbers[start] + numbers[end]
            if added == target:
                return [start+1, end+1]
            elif added > target:
                end -= 1
            elif added < target:
                start += 1
