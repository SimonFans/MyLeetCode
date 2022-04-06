'''
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''
'''
ideas:
[1,2,3]
=> pop
[1,2]
=> pop
[1]
=> nums:[2,3] loop to the second number which is 3
[1,3,2]
=> pop
=> pop
=> pop
[2,1,3]
=> pop
=> pop
[2,3,1]
'''

class Solution:
    def permute(self, nums: 'List[int]') -> 'List[List[int]]':

        def helper(nums, tmp):
            if not len(nums):
                # hard copy
                ans.append(list(tmp))
                return
            for i in range(len(nums)):
                tmp.append(nums[i])
                # 第一个参数放剩下的数字，第二个参数放当前存入的数字
                helper(nums[:i]+nums[i+1:], tmp)
                # backtracking 注意pop
                tmp.pop()
        ans = []
        helper(nums, [])
        return ans

# Time: O(N!)
# Space: O(N!)
