'''
题意： 判断能否将此数组等分成k份，并且每一份和相等,输出分组的结果
Example 1:
Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Input: nums = [1,2,3,4], k = 3
Output: false

O(k* 2^N) k: # of subsets, N: # of numbers in the array
O(N)
'''

class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        def backtrack(count: int, curr_sum: int) -> bool:
        # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True
            # Current subset-sum exceeds target sum, no need to proceed further.
            if curr_sum > target_sum:
                return False
            # When current subset sum reaches target sum then one subset is made.
            # Increment count and reset current subset sum to 0.
            if curr_sum == target_sum:
                return backtrack(count + 1, 0)
            # Try not picked elements to make some combinations.
            for j in range(n):
                if not taken[j]:
            # Include this element in current subset.
                    taken[j] = True
            # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(count, curr_sum + arr[j]):
                        return True
            # Backtrack step.
                    taken[j] = False
            # We were not able to make a valid combination after picking
            # each element from the array, hence we can't make k subsets.
            return False
        total_array_sum = sum(arr)
        n = len(arr)
        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k
        taken = [False] * n
        return backtrack(0, 0)

##### cache optimization
class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        n = len(arr)

        total_array_sum = sum(arr)

        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k

        # Sort in decreasing order.
        arr.sort(reverse=True)

        taken = ['0'] * n

        memo = {}

        def backtrack(index, count, curr_sum):
            n = len(arr)

            taken_str = ''.join(taken)
            print(taken_str)

            # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True

            # No need to proceed further.
            if curr_sum > target_sum:
                return False

            # If we have already computed the current combination.
            if taken_str in memo:
                return memo[taken_str]

            # When curr sum reaches target then one subset is made.
            # Increment count and reset current sum.
            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]

            # Try not picked elements to make some combinations.
            for j in range(index, n):
                if taken[j] == '0':
                    # Include this element in current subset.
                    taken[j] = '1'
                    # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True
                    # Backtrack step.
                    taken[j] = '0'

            # We were not able to make a valid combination after picking
            # each element from the array, hence we can't make k subsets.
            memo[taken_str] = False
            return memo[taken_str]

        return backtrack(0, 0, 0)
