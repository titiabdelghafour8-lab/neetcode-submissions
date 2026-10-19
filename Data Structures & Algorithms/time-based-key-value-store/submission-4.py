class TimeMap:

    def __init__(self):
        self.dictionnary: dict[List[tuple[int, str]]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dictionnary: self.dictionnary[key] = []
        self.dictionnary[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictionnary:
            return ""
        timed_values = self.dictionnary[key]
        left = 0
        right = len(timed_values) - 1
        if timed_values[0][0] > timestamp:
            return ""
        left_max = left
        while left <= right:
            mid = int((left + right) / 2)
            if timed_values[mid][0] == timestamp:
                return timed_values[mid][1]
            elif timed_values[mid][0] > timestamp:
                right = mid - 1
            else:
                left_max = mid
                left = mid + 1 
        return timed_values[left_max][1]
