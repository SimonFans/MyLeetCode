'''
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Input: nums = [7,7,7,7,7,7,7]
Output: 1
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums = [10,9,2,5,3,7,101,18]
        nums = [0,1,0,3,2,3]

        res = [nums[0]]
        for num in nums[1:]:
            # Start with the second num, if num > 前一个就放进结果list去
            if num > res[-1]:
                res.append(num)
            # 遍历结果list,找到第一个比当前num大的数，num替换掉第一个大的数
            else:
                i = 0
                while res[i] < num:
                    i += 1
                res[i] = num
        return len(res)

# Time: O(N^2)
# Space: O(N)

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for num in nums:
            i = bisect.bisect_left(res, num)
            if i == len(res):
                res.append(num)
            else:
                res[i] = num
        return len(res)

# Time: O(NLogN)
# Space: O(N)
