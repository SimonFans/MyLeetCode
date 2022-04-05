'''
Input: nums = [1,1,2,2,2,3]
Output: [3,1,1,2,2,2]
Explanation: '3' has a frequency of 1, '1' has a frequency of 2, and '2' has a frequency of 3.

Input: nums = [2,3,1,3,2]
Output: [1,3,3,2,2]
Explanation: '2' and '3' both have a frequency of 2, so they are sorted in decreasing order.
'''

from collections import defaultdict
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        num_cnt = defaultdict(int)
        cnt_num_lst = defaultdict(list)
        for num in nums:
            num_cnt[num] += 1
        for num, cnt in num_cnt.items():
            cnt_num_lst[cnt].append(num)
        sorted_cnt = sorted(cnt_num_lst.keys())
        for cnt in sorted_cnt:
            val_lst = cnt_num_lst[cnt]
            val_lst.sort(reverse=True)
            for num in val_lst:
                ans.extend(cnt*[num])
        return ans


    # def frequencySort(self, A):
    #     count = collections.Counter(A)
    #     return sorted(A, key=lambda x: (count[x], -x))
