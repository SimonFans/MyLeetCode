# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
         1
    2         3
 4     5

Input: root = [1,2,3,4,5]
Output: [[4,5,3],[2],[1]]

思路：dfs到最深层，左右返回当前node height = 1+ max(left, right). 如果当前height值==组后结果list的长度，说明
需要append一个空list到结果list中去。 之后相同的height就append到结果list对应的index中去
'''
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def getHeight(node):
            # The lowest level is -1
            if not node:
                return -1
            height = 1 + max(getHeight(node.left), getHeight(node.right))
            if height == len(res):
                res.append([])
            res[height].append(node.val)
            return height
        res = []
        getHeight(root)
        return res
