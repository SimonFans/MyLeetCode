'''
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...].
The 5th missing positive integer is 9.

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
'''

# Use one time loop
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        # [4,6]  k = 3, return 3
        if k <= arr[0] - 1:
            return k
        # arr[0]的右侧还要找几个k
        k = k - (arr[0] - 1)
        # search kth missing between the array numbers,
        # missing ? numbers = arr[i+1] - arr[i] - 1, example: [3,6], missing 6-3-1 = 2, which is 4 & 5
        for i in range(len(arr) - 1):
            curr_missing_cnt = arr[i+1] - arr[i] - 1
            if k <= curr_missing_cnt:
                return arr[i] + k
            k -= curr_missing_cnt
        # this case, the missing number > arr[-1]: example => [4,6]  k = 5, return 7
        return arr[-1] + k

# Time: O(N), the worst case is to pass all array elements
# Space: O(1)

# Use binary search
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l, r = 0, len(arr) - 1
        while l <= r:
            p = (l + r) //2
            # 应该是当前对应的实际值
            # [1,3,4] p=1. arr[p] = 3
            # [1,2,3]      实际arr[p] = 2
            if arr[p] - (p+1) < k:
                l = p + 1
            else:
                r = p - 1
        return l + k

# Time: O(logN), where N is a number of elements in the input array
# Space: O(1) 
