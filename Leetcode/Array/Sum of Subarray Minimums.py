'''
Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
'''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        # 对于每一个数字，找左，右侧分别比它大的数字个数，分别记录
        # 例如 arr = [3,2], 当遍历到3，左侧和右侧比3大的都是0个，所以最后(0+1)*(0+1)*3 = 3
        # 当遍历到2， 左侧比2大的有一个3， 右侧比2大的有0个，所以最后(1+1)*(0+1)*2 = 4
        # 最后结果把上面的加起来就是3+4 = 7
        # 基本初始化
        n = len(arr)
        mod = 10**9 + 7
        # 找到左边比当前数字大的存到一个list
        left = [0] * n
        s1 = []
        for i, num in enumerate(arr):
            count = 1
            while s1 and s1[-1][0] > num:
                count += s1.pop()[1]
            left[i] = count
            # [数字，比当前数字大的个数]
            s1.append([num, count])
        # 找到右边比当前数字大的存到一个list
        right = [0] * n
        s2 = []
        for i, num in enumerate(arr[::-1]):
            count = 1
            while s2 and s2[-1][0] >= num:
                count += s2.pop()[1]
            right[i] = count
            # [数字，比当前数字大的个数]
            s2.append([num, count])
        # 最后加起来
        res = 0
        for a, l, r in zip(arr, left, right[::-1]):
            res += a*l*r
        return res%mod
