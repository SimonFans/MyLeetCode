# Input: nums = [1,1,1,1,1], target = 3
# Output: 5
# Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
# -1 + 1 + 1 + 1 + 1 = 3
# +1 - 1 + 1 + 1 + 1 = 3
# +1 + 1 - 1 + 1 + 1 = 3
# +1 + 1 + 1 - 1 + 1 = 3
# +1 + 1 + 1 + 1 - 1 = 3

# 传统解法，不用memo超时
class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        return self.dp(nums, S, index, curr_sum,[])

    def dp(self, nums, target, index, curr_sum, temp):

        if index < 0 and curr_sum == target:
            print(temp)
            return 1
        if index < 0:
            return 0
        positive = self.dp(nums, target, index-1, curr_sum + nums[index], temp + [nums[index]])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index], temp + [-nums[index]])
        return positive + negative

# optimize
class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        self.memo = {}
        return self.dp(nums, S, index, curr_sum,[])

    def dp(self, nums, target, index, curr_sum, temp):
        if (index, curr_sum) in self.memo:
            return self.memo[(index, curr_sum)]

        if index < 0 and curr_sum == target:
            return 1
        if index < 0:
            return 0

        positive = self.dp(nums, target, index-1, curr_sum + nums[index], temp + [nums[index]])
        negative = self.dp(nums, target, index-1, curr_sum + -nums[index], temp + [-nums[index]])
        self.memo[(index, curr_sum)] = positive + negative
        return self.memo[(index, curr_sum)]

# Print result
class Solution:
    def findTargetSumWays(self, nums, S):
        index = len(nums) - 1
        curr_sum = 0
        return self.dp(nums, S, index, curr_sum,[])

    def dp(self, nums, target, index, curr_sum, temp):
        if index < 0 and curr_sum == target:
            print(temp)
            return 1
        if index < 0:
            return 0
        self.dp(nums, target, index-1, curr_sum + nums[index], temp + [nums[index]])
        self.dp(nums, target, index-1, curr_sum + -nums[index], temp + [-nums[index]])
