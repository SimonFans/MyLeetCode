'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job.
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.

Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job.
Profit obtained 150 = 20 + 70 + 60.

Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6
'''

import heapq
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # define a heap piority queue
        queue = []
        # initial a max profit value
        maxProfit = 0
        sorted_job_lst = list(zip(startTime, endTime, profit))
        sorted_job_lst.sort(key = lambda x: x[0])
        # Get the total number of jobs
        n = len(sorted_job_lst)
        # Loop through each job, queue format: [(endTime, profit + maxProfit)]
        for i in range(n):
            while queue and sorted_job_lst[i][0] >= queue[0][0]:
                currentProfit = heapq.heappop(queue)[1]
                maxProfit = max(maxProfit, currentProfit)
            heapq.heappush(queue, (sorted_job_lst[i][1], maxProfit + sorted_job_lst[i][2]))

        #Take out the rest of sum profits in the queue and compare
        while queue:
            restProfit = heapq.heappop(queue)[1]
            maxProfit = max(maxProfit, restProfit)
        return maxProfit

# Time: O(NlogN)
# Space: O(N)
