class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):
            currEnd = res[-1][1]

            if intervals[i][0] <= currEnd:
                currEnd = max(currEnd, intervals[i][1])
                res[-1][1] = currEnd
            else:
                res.append(intervals[i])
        
        return res