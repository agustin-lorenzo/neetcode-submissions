class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current = -1

        for i in range(len(arr) - 1, -1, -1):
            nxt = max(current, arr[i])
            arr[i] = current
            current = nxt
        
        return arr