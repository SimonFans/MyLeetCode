'''
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]
Explanation:
Window position                Median
---------------                -----
[1  3  -1] -3  5  3  6  7        1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7        3
 1  3  -1  -3 [5  3  6] 7        5
 1  3  -1  -3  5 [3  6  7]       6
'''

# Time: O(NLogk)

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        curr_lst = []
        res = []
        for i, num in enumerate(nums):
            # 将number插入curr_lst,并且保证curr_lst in order
            bisect.insort(curr_lst, num)
            # if beyond the window size
            if i >= k:
                # 按照先后顺序找到数组中对应的index,然后从curr_lst删除
                j = bisect.bisect_left(curr_lst, nums[i-k])
                curr_lst.pop(j)
            # 当符合窗口计算条件
            if i >= k - 1:
                # k is odd number
                if k & 1 == 1:
                    res.append(curr_lst[k//2])
                else:
                    res.append((curr_lst[(k-1)//2] + curr_lst[k//2])/2)
        return res
