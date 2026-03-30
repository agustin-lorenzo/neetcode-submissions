class TimeMap:

    def __init__(self):
        self.tmap = {}        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.tmap:
            self.tmap[key] = []
        self.tmap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.tmap or timestamp < self.tmap[key][0][-1]:
            return ""

        values = self.tmap[key]
        l, r = 0, len(values) - 1
        result = values[0][0]
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result