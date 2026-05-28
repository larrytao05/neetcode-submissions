class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        curInterval = intervals[0]
        res = []
        for i in range(1,len(intervals)):
            if curInterval[1] < intervals[i][0]:
                res.append(curInterval)
                curInterval = intervals[i]
            else:
                curInterval[0] = min(curInterval[0], intervals[i][0])
                curInterval[1] = max(curInterval[1], intervals[i][1])
        res.append(curInterval)

        return res