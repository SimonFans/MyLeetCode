'''
Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Input: s = "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
'''

class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt_groups = [1]
        # count if the current and previous numbers are continous then +1 else append a new 1
        for i in range(1, len(s)):
            if s[i-1] == s[i]:
                cnt_groups[-1] += 1
            else:
                cnt_groups.append(1)
        ans = 0
        # if 0011 => 2种， min([2,2]) = 2, => 01 or 0011
        # if 001 => 1种, min([2,1]) = 1, => 01
        # iterate another for loop, result += min(prev, current)
        for i in range(1, len(cnt_groups)):
            ans += min(cnt_groups[i-1], cnt_groups[i])
        return ans
