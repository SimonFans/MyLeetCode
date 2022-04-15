'''
Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
'''

class Solution:
    def compress(self, chars: List[str]) -> int:
        '''
        aabbccc
        '''
        i, count = 0, 1
        n = len(chars)
        for j in range(1, n + 1):
            if j < n and chars[j] == chars[j-1]:
                count += 1
            else:
                chars[i] = chars[j-1]
                i += 1
                if count > 1:
                    for k in str(count):
                        chars[i] = k
                        i += 1
                    count = 1
        # chars = chars[:i]
        return i
