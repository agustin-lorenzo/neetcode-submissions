class TimeMap:

    def __init__(self):
        self.tMap = defaultdict(list)


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.tMap[key]
        if not values or timestamp < values[0][1]:
            return ""
        
        result = values[0][0]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result