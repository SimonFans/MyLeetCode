class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        ## APPROACH : SLIDING WINDOW ##
        # Logic #
        # 1. Increase the window if the substring is valid else,
        # 2. slide the window with the same length. No need to shrink the window
        '''
        freqDict = defaultdict(int)
        maxLength = 0
        start, end = 0, 0
        maxFreq = 0

        while end < len(s):
            freqDict[s[end]] += 1
            # maxFreq may be invalid at some points, but this doesn't matter
            # maxFreq will only store the maxFreq reached till now
            maxFreq = max(maxFreq, freqDict[s[end]])
            # if logic: 窗口长度-当前窗口内出现最多次的字符数，剩下的位置如果多于可替换字符数
            if end - start + 1 - maxFreq > k:
                freqDict[s[start]] -= 1
                start += 1
            else:
                maxLength = max(maxLength, end-start+1)
            end += 1
        return maxLength
