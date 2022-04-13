'''
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
'''

from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # edge case:
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        word_len = len(beginWord)
        # generate a dictionary, key is mutation exprssion, value is the word
        word_mutation = defaultdict(list)
        for word in wordList:
            for i in range(word_len):
                word_mutation[word[:i]+ '*' + word[i+1:]].append(word)
        # BFS establish a queue
        queue = deque([(beginWord, 1)])
        # note down if the word has been visited
        visited = {beginWord: True}
        while queue:
            curr_word, step = queue.popleft()
            #对初始单词进行变种
            for i in range(word_len):
                curr_word_mutate = curr_word[:i] + '*' + curr_word[i+1:]
                #查看当前变种是否是wordList变种字典中的一个key
                for word in word_mutation[curr_word_mutate]:
                    #当前变种对应的单词和结束单词相同，返回步数+1
                    if word == endWord:
                        return step + 1
                    #当前变种对应的单词第一次出现，则记录一下，后期遇到不再加入到queue中去
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, step + 1))
                #第一次变种后将此时变种key对应list设为空，因为对应的单词都加入到queue了
                word_mutation[curr_word_mutate] = []
        return 0

# Time: O(M^2*N) M is the length of each word, N is the total number of words in the wordList
# Space: O(M^2*N)
