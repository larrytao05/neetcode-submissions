class TimeMap:

    def __init__(self):
        self.vals = defaultdict(list)
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.vals[key].append(timestamp)
        self.times[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        lst = self.vals[key]
        l = 0
        r = len(lst)-1
        while l <= r:
            mid = (l+r)//2
            if lst[mid] > timestamp:
                r = mid - 1
            elif lst[mid] < timestamp:
                l = mid + 1
            else:
                return self.times[timestamp]
        return "" if r < 0 else self.times[lst[r]]


