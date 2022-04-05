'''
Input
["WordDistance", "shortest", "shortest"]
[[["practice", "makes", "perfect", "coding", "makes"]], ["coding", "practice"], ["makes", "coding"]]
Output
[null, 3, 1]
'''

from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.location = defaultdict(list)
        # Hashmap: stores key, value pair. key is the word, and value is the index
        # the index is already sorted with for loop
        for i, w in enumerate(wordsDict):
            self.location[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        # Get the searched word index list from the predefined dictionary
        loc1 = self.location[word1]
        loc2 = self.location[word2]
        # two pointers to point on each index list
        p1, p2 = 0,0
        short_dist = float('Inf')
        while p1 < len(loc1) and p2 < len(loc2):
            short_dist = min(short_dist, abs(loc1[p1]-loc2[p2]))
            if loc1[p1] < loc2[p2]:
                p1 += 1
            else:
                p2 += 1
        return short_dist
