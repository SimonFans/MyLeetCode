'''
95. Unique Binary Search Trees II
Given an integer n, return all the structurally unique BST's (binary search trees),
which has exactly n nodes of unique values from 1 to n.
Return the answer in any order.
给一个数字n (n>0), 问可以造出多少种不同的binary search tree
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        @lru_cache(None)
        def dfs(left, right):
            if left > right: return [None]
            if left == right: return [TreeNode(left)]
            ans = []
            for root in range(left, right+1):
                # all possible left subtrees if root is choosen to be a root
                left_nodes = dfs(left, root - 1)
                # all possible right subtrees if root is choosen to be a root
                right_nodes = dfs(root+1, right)
                # connect left and right subtrees to the root
                for leftNode in left_nodes:
                    for rightNode in right_nodes:
                        rootNode = TreeNode(root, leftNode, rightNode)
                        ans.append(rootNode)
            return ans
        return dfs(1, n)
