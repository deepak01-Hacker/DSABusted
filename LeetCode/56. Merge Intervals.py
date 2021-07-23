class Solution(object):
    def merge(self, intervals):
        if len(intervals) == 0:
            return []

        ans = []
        intervals.sort()
        ans.append([])
        ans[-1].append(intervals[0][0])
        maxs = intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0] > maxs:
                ans[-1].append(maxs)
                ans.append([])
                ans[-1].append(intervals[i][0])
            if intervals[i][1] > maxs:
                maxs = intervals[i][1]
        ans[-1].append(maxs)
        return ans
