'''
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        idx, res = 0, []
        # 1. Append all ranges that start time < new start time to the res
        while idx < len(intervals) and intervals[idx][0] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1
        # 2. Fit in new interval to the res. edge case: empty list at the beginning
        if not res or newInterval[0] > res[-1][1]:
            res.append(newInterval)
        else:
            res[-1][1] = max(newInterval[1], res[-1][1])
        # 3. Deal with the rest of intervals
        while idx < len(intervals):
            if intervals[idx][0] > res[-1][1]:
                res.append(intervals[idx])
            else:
                res[-1][1] = max(intervals[idx][1], res[-1][1])
            idx += 1
        return res
