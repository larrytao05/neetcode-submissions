class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()

        
        i = 0
        while i < len(intervals):
            s,e = intervals[i]
            while i+1 < len(intervals) and e >= intervals[i+1][0]:
                i += 1
                _,n_e = intervals[i]
                e = max(e, n_e)
            res.append([s,e])
            i += 1
        return res
