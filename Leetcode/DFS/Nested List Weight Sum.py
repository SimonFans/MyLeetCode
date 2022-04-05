'''
Return the sum of each integer in nestedList multiplied by its depth.
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
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
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def removeNestings(nested_list, depth):
            res = 0
            for curr in nested_list:
                # curr is a nested list
                if not curr.isInteger():
                    res += removeNestings(curr.getList(), depth+1)
                # curr is an integer
                else:
                    res += curr.getInteger() * depth
            return res

        depth = 1
        return removeNestings(nestedList, depth)

### optimize saving result to cache

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        _sum = 0
        if not nestedList:
            return 0
        # {level: sum of the values}
        cache = defaultdict(int)
        self.helper(nestedList, 1, cache)
        # print(cache)
        for level, num in cache.items():
            _sum += level * num
        return _sum

    def helper(self, nestedList, level, cache):
        for curr in nestedList:
            if curr.isInteger():
                cache[level] += curr.getInteger()
            else:
                self.helper(curr.getList(), level+1, cache)
        return
