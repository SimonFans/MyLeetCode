'''
You are given an array of intervals, where intervals[i] = [starti, endi] and each starti is unique.

The right interval for an interval i is an interval j such that startj >= endi and startj is minimized. Note that i may equal j.

Return an array of right interval indices for each interval i. If no right interval exists for interval i, then put -1 at index i

Input: intervals = [[3,4],[2,3],[1,2]]
Output: [-1,0,1]
Explanation: There is no right interval for [3,4].
The right interval for [2,3] is [3,4] since start0 = 3 is the smallest start that is >= end1 = 3.
The right interval for [1,2] is [2,3] since start1 = 2 is the smallest start that is >= end2 = 2.
'''

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def insertIndex(start_time, target):
            lo, hi = 0, len(start_time) - 1
            while lo + 1 < hi:
                mid = (lo + hi)//2
                if start_time[mid] < target:
                    lo = mid
                else:
                    hi = mid
            if target <= start_time[lo]:
                return lo
            elif target <= start_time[hi]:
                return hi
            else:
                return len(start_time)

        sorted_by_start = []
        ans = [-1] * len(intervals)
        for index, interval in enumerate(intervals):
            sorted_by_start.append([interval[0],interval[1], index])
        # [[start_time, end_time, previous_index], [], ...]
        sorted_by_start.sort(key = lambda s: s[0])
        # only select start time, which is used to do binary search to find insertion index
        start_time = [s for s, e, i in sorted_by_start]
        for s, e, i in sorted_by_start:
            pos = insertIndex(start_time, e)
            # Below method will return the insertion position without writing the binary search method
            # pos = bisect.bisect_left(start_time, e)
            # if return insert position == len(start_time), then it's outbound of the start_time, no need to update the ans list, leave it as -1
            if pos < len(start_time):
                # get and update the previous index to the answer list
                ans[i] = sorted_by_start[pos][2]
        return ans

# Time: O(nlogn)
# Space: O(n)
