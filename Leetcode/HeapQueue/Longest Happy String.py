'''
A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string.
If there are multiple longest happy strings, return any of them.
If there is no such string, return the empty string "".

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
'''

import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        mapping = {'a':a, 'b':b, 'c':c}
        maxHeap = []
        for char, num in mapping.items():
            if num != 0:
                heapq.heappush(maxHeap, (num*-1, char))
        char_list = []
        while maxHeap:
            cnt1, char1 = heapq.heappop(maxHeap)
            if len(char_list) >=2 and char_list[-1] == char_list[-2] == char1:
                if not maxHeap:
                    return ''.join(char_list)
                cnt2, char2 = heapq.heappop(maxHeap)
                char_list.append(char2)
                cnt2 += 1
                if cnt2 != 0:
                    heapq.heappush(maxHeap,(cnt2, char2))
                heapq.heappush(maxHeap, (cnt1,char1))
                continue
            char_list.append(char1)
            cnt1 += 1
            if cnt1 != 0:
                heapq.heappush(maxHeap,(cnt1, char1))
        return ''.join(char_list)
