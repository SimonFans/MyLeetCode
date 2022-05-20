'''
https://leetcode.com/problems/alien-dictionary/

Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"

Input: words = ["z","x"]
Output: "zx"

Input: words = ["z","x","z"]
Output: ""
Explanation: The order is invalid, so return "".

思路： 给一个list of strings, 要求推断出来最后的string。 前后比较每个word in the list, 当字母不同时
可以想象成前面的字母->后面的字母，形成一个graph。 用拓扑逻辑+ BFS去解这题
'''

from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # topological sorting
        # 记录每个unique字符in-degree的个数
        in_degree = defaultdict(int)
        for word in words:
            for c in word:
                in_degree[c] = 0
        # {start : <end1, end2>}
        adj_list = defaultdict(set)
        # words     = ["wrt","wrf","er","ett", "rftt"]
        # words[1:] = ["wrf","er","ett","rftt"]
        # 只有4个pairs
        for first_word, second_word in zip(words, words[1:]):
            for c1, c2 in zip(first_word, second_word):
                if c1 != c2:
                    # update the adjacent list
                    if c2 not in adj_list[c1]:
                        adj_list[c1].add(c2)
                    # add 1 to the in_degree[c2]
                        in_degree[c2] += 1
                    break
            # After inner for loop ends, check this else condition
            # first_word = 'wac', second_word = 'wa'
            else:
                if len(second_word) < len(first_word): return ''
        # bfs
        ans = []
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            curr = queue.popleft()
            ans.append(curr)
            for c in adj_list[curr]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    queue.append(c)
        # If not all letters are in output, that means there was a cycle
        if len(ans) < len(in_degree): return ''
        return ''.join(ans)

# Time: O(C) where C is the total number of all the words in the input list, added togehter
# Space: O(# of unique letters)
