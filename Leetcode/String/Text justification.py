'''
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justifica
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        i = 0
        while i < len(words):
            size = 0
            begin = i
            # move pointer i to the position where the word will start at the next line
            while i < len(words):
                newsize = len(words[i]) if size == 0 else size + len(words[i]) + 1
                if newsize <= maxWidth:
                    size = newsize
                    i += 1
                else:
                    break
            # calulate how many spaces can be filled
            spaceCount = maxWidth - size
            # i - begin: how many words in a line
            # i - begin - 1: count the number of space between words
            # This if condition will run when the current line is not only one word (and) it's not the last line
            if i - begin - 1 > 0 and i < len(words):
                # total # of space divided by the number of spaces
                everyCount = spaceCount / (i - begin - 1)
                # check if spaces can be distributed evenly which means if the remainder is 0
                spaceCount %= (i - begin - 1)
            # If only one word in the current line or it's the last line
            else:
                everyCount = 0
            # define a pointer j at the position begin
            j = begin
            s = ''
            while j < i:
                if j > begin:
                    # +1 here is because 之前计算size的时候已加的1在这里要重加
                    s += ' ' * (int(everyCount) + 1)
                    # 不是最后一行的话
                    if spaceCount > 0 and i < len(words):
                        s += ' '
                        spaceCount -= 1
                # first time add the first word directly
                s += words[j]
                j += 1
            #
            s += ' ' * spaceCount
            ans.append(s)
        return ans
