'''
Input: words = ["ab","bc"], s = "aabcd"
Output: "a<b>abc</b>d"
Explanation: Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Input: words = ["ab","cb"], s = "aabcd"
Output: "a<b>ab</b>cd"
'''

class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        '''
        1. loop through the string and mark 1 in a list whenever there's a matching in words list.
        2. loop through the string, and add bold tagging based on the 01 bold list
        '''

        bold = [0] * len(s)
        for word in words:
            start = 0
            # abc len(S) = 3
            # 012
            while start < len(s):
                index = s.find(word, start)
                # if we found the matched word because otherwise it will return -1
                if index >= 0:
                    # update the bold list
                    bold[index:index+len(word)] = [1] * len(word)
                    start = index + 1
                else:
                    break
        # create a list for result
        res = []
        for i, c in enumerate(s):
            # a b c
            # _   _
            # bold[i-1]: if bold c, b is not, add '<b>' between b and c
            if bold[i] and (i==0 or not bold[i-1]):
                res.append('<b>')
            res.append(c)

            if bold[i] and (i== len(s) - 1 or not bold[i+1]):
                res.append('</b>')
        return ''.join(res)

Time: O(N)
Space: O(N)
