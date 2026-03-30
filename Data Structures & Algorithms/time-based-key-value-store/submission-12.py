class TimeMap:

    def __init__(self):
        self.map = defaultdict(list) # "key": ["value", time]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.map[key]
        if not values or timestamp < values[0][1]:
            return ""

        if timestamp >= values[-1][1]:
            return values[-1][0]
        
        result = values[0][0]
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] < timestamp:
                result = values[m][0]
                l = m + 1
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                return values[m][0]
        
        return result
