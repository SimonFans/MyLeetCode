'''
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
'''

思路： 从左往右遍历，如果右边的数大小比左边的大，则一直删到左边的数不小于右边的数，即始终保持最左边的数最大。
每次加入heap的时候存成(index, val). 每一次for循环，最后检查是否heap中当前最左边数字index加上窗口长度k等于当前index，
如果等于，则pop出heap中最左边的数字。然后另一个条件是如果当前index大于窗口长度-1，则将最左边的数字加入到结果list中去

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Either len(nums) or k = 0, then return []
        if len(nums) * k == 0:
            return []
        # If the maximum allowed window size is 1,  then return current nums
        if k == 1:
            return nums
        ans = []
        # deque is a list
        dq = collections.deque()
        # start to loop through the array
        for cur_index in range(len(nums)):
            # only keep the largest number, be careful here it's pop not popleft
            while dq and dq[-1][1] < nums[cur_index]:
                dq.pop()
            dq.append((cur_index, nums[cur_index]))
            # If the difference between the current index and the most left index in dq == max window size, pop the mostleft one in the dq
            if cur_index - dq[0][0] == k:
                dq.popleft()
            # When current index beyond the window right boundary, start to record the answer
            if cur_index >= k - 1:
                ans.append(dq[0][1])
        return ans

# Time: O(N)
# Space: O(N)
