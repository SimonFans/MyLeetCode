'''
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

       1
    2     3
  4   5

=>
       4
    5     2
        3   1
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(cur):
            if not cur.left:
                return cur
            # print(cur, cur.val, '\n') 注意第一次cur在2的位置不是4的位置
            newRoot = dfs(cur.left)
            cur.left.left = cur.right
            cur.left.right = cur
            cur.left = None
            cur.right = None
            return newRoot

        # edge case : given by example 2
        if not root:
            return None
        return dfs(root)
