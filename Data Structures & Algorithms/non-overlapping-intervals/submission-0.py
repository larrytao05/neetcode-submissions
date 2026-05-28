class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        res = 0
        curInt = intervals[0]
        for i in range(1,len(intervals)):
            if curInt[1] <= intervals[i][0]:
                curInt = intervals[i]
            else:
                res += 1
                if curInt[1] <= intervals[i][1]:
                    continue
                else:
                    curInt = intervals[i]
        return res