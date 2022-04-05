'''
Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
'''

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        e_schedule = []
        for s in schedule:
            for i in s:
                e_schedule.append([i.start, i.end])
        e_schedule.sort(key = lambda x: x[0])
        ans, endMax = [], e_schedule[0][1]

        for interval in e_schedule[1:]:
            if interval[0] <= endMax and interval[1] > endMax:
                endMax = interval[1]
            elif interval[0] > endMax:
                ans.append(Interval(endMax, interval[0]))
                endMax = interval[1]
        return ans
