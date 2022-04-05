'''
Input: nestedList = [[1,1],2,[1,1]]
Output: 8
Explanation: Four 1's with a weight of 1, one 2 with a weight of 2.
1*1 + 1*1 + 2*2 + 1*1 + 1*1 = 8
'''
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#

# DFS: T => O(N), S => O(N) Space complexity is equal to the maximum number of active stack calls during the depth-first search
class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # get the maximum depth
        def findmaxDepth(nestedList):
            depth = 1
            for curr in nestedList:
                if not curr.isInteger():
                    depth = max(depth, 1 + findmaxDepth(curr.getList()))
                    print(depth)
            return depth

        def weightSum(nestedList, depth, maxDepth):
            res = 0
            for curr in nestedList:
                if not curr.isInteger():
                    res += weightSum(curr.getList(), depth +1, maxDepth)
                else:
                    res += curr.getInteger() * (maxDepth - depth + 1)
            return res


        # depth at least is 1
        maxDepth = findmaxDepth(nestedList)
        answer = weightSum(nestedList, 1, maxDepth)
        return answer


#  优化中间存结果
from collections import defaultdict

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        # {level : 数字值的累加和}
        cache = defaultdict(int)
        self.max_level = -1
        self.helper(nestedList, 1, cache)
        total_sum = 0
        for level, num in cache.items():
            total_sum += num * (self.max_level - level + 1)
        return total_sum

    def helper(self, nestedList, level, cache):
        self.max_level = max(self.max_level, level)
        for curr in nestedList:
            if not curr.isInteger():
                self.helper(curr.getList(), level+1, cache)
            else:
                cache[level] += curr.getInteger()
        return



# BFS: 不用找深度，外层数字被累加
# nestedList = [1,[4,[6]]]
# level_sum = 1       total_sum = 1
# level_sum = 1 + 4   total_sum = 1 + (1+4)
# level_sum = (1+4) +6 total_sum = 1 + (1+4) + [(1+4) + 6]

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum
