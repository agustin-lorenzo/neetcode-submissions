class TimeMap:

    def __init__(self):
        self.tMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tMap:
            self.tMap[key] = []
        self.tMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        if key not in self.tMap or timestamp < self.tMap[key][0][1]:
            return result
        
        values = self.tMap[key]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result
