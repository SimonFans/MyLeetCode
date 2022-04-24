'''
Given a string s,
rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.

Input: s = "aab"
Output: "aba"

Input: s = "aaab"
Output: ""
'''

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        # if it's an empty string
        if not s:
            return ''
        # define a result string
        res = ''
        # format [(count: 'char'), (count: 'char') ...]
        cnt_char = [(-cnt, char) for char, cnt in dict(Counter(s)).items()]
        # define a heap
        heap = []
        # Iterate through cnt_char list, add into the heap
        for pair in cnt_char:
            heapq.heappush(heap, pair)
        # 保证heap里至少要有两对,不然每次需要拿出两个来的话会报错
        while len(heap) > 1:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)
            # add to the result string
            res += char1
            res += char2
            # if abs(freq) > 1, then it means it has more than 1 characters, add it back to the heap
            if abs(freq1) > 1:
                heapq.heappush(heap, (freq1 + 1, char1))
            # if abs(freq) > 1, then it means it has more than 1 characters, add it back to the heap
            if abs(freq2) > 1:
                heapq.heappush(heap, (freq2 + 1, char2))
        # 如果heap里还剩一个，看当前剩下字符的count如果大于1，则代表不可能，返回''. 否则加上当前字符
        # 如果heap为空，则不执行这个if，直接返回result string
        if heap:
            freq, char = heap[0]
            if abs(freq) > 1:
                return ''
            res += char
        return res
