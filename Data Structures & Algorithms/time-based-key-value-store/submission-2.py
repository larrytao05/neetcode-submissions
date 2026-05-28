from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        lst = self.map[key]
        l,r = 0, len(lst)-1
        while l <= r:
            mid = (l+r)//2
            if timestamp == lst[mid][0]:
                return lst[mid][1]
            if timestamp < lst[mid][0]:
                r = mid-1
            else:
                l = mid+1
        return "" if r < 0 else lst[r][1]
