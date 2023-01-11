'''
You are given the root of a binary search tree (BST),
where the values of exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
        1
    3       N
   N 2

Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.
        3                 2
    1       4           1   4
          2                3
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def recoverTree(self, root: 'TreeNode') -> 'None':
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: return None
        stack = []
        pre, first, second = None, None, None
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                #If right child < root then found the problem
                if pre and root.val < pre.val:
                    if first == None:
                        first = pre
                    second = root
                pre = root
                root = root.right

        first.val, second.val = second.val, first.val
