'''
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""
'''

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        if len(strs)==0:
            return ""
        if "" in strs:
            return ""
        first_string = strs[0]
        for i in range(len(first_string)): # Take first string as template
            for next_string in strs[1:]: # from second to the last
                if i == len(next_string) or first_string[i] != next_string[i]:
                    return first_string[0:i]
        # if the string only have one character like ['a'] then return 'a'
        return first_string

Time: O(S), S is the sum of all characters in all strings.
Space: O(1)

# bianry search
'''
explain:
strs = ["flower","flow","flight"]
shortest length is 4 => flow
low = 0, high = 3, mid = 1. fl, fl, fl... so low = mid+1 = 1+1 = 2. Because 2<=3, so recompute mid = 2 extract flo,flo, fli return False.
high = mid - 1 = 2-1 = 1 while loop stops. return strs[0] substring from 0 to low
'''

class Solution:
    def longestCommonPrefix(self, strs: 'List[str]') -> 'str':
        def helper(strs, mid):
            str1 = strs[0][0:mid+1]
            for i in range(1,len(strs)):
                if not strs[i].startswith(str1):
                    return False
            return True

        if not strs or not strs[0]:
            return ""
        minLen = float('Inf')
        for _str in strs:
            minLen = min(len(_str), minLen)
        low = 0
        high = minLen - 1
        while low <= high:
            mid = (low + high) //2
            if helper(strs, mid):
                low = mid + 1
            else:
                high = mid - 1
        return strs[0][0:low]

Time : O(S*log(m)), where m is the length of n equal strings. S is the sum of all characters in all strings.
Space: O(1)
