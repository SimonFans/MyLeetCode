'''
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
'''

思路：首先按会议的起始时间升序排序。 放入第一个开始的会议的结束时间。循环剩下的会议，
如果发现下一个会议的开始时间在heap[0]之后即最早的会议结束时间(因为heap里存储的都是会议结束时间),则heap pop即去掉之前最先开完的会议结束时间，
反之，则代表之前的所有会议都还没结束。最后再将当前的会议结束时间放入heap。遍历完所有会议后，heap的长度就是要多少个会议室。

import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        heap = []
        #sort the list based on start time
        intervals.sort(key = lambda x: x[0])

        # heap push the first meeting end time
        heapq.heappush(heap, intervals[0][1])

        # if next start time >= the minimum end time, then it means there's a meeting completes
        # we can pop the minimum end time from the heap
        for interval in intervals[1:]:
            if heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])
        # Finally we can count how many end time left in the heap, that's the answer
        return len(heap)
