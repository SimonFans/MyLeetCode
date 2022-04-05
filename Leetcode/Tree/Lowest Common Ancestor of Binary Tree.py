'''
root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
       3
     5    1
   6  2  0  8
     7 4
return  3 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # bottom up
        def helper(node):
            if not node:
                return False
            left = helper(node.left)
            right = helper(node.right)
            mid = node == p or node == q
            # return final result
            if mid + left + right == 2:
                self.ans = node
            return mid or left or right

        self.ans = None
        helper(root)
        return self.ans


#         # Add root to the stack
#         stack = [root]

#         # dictionary to keep track of parent node
#         parent = {root: None}

#         # loop stops until we found out p & q
#         while p not in parent or q not in parent:
#             node = stack.pop(0)
#             if node.left:
#                 stack.append(node.left)
#                 parent[node.left] = node
#             if node.right:
#                 stack.append(node.right)
#                 parent[node.right] = node

#         # create a set to keep the ancestor of node p
#         ancestors = set()

#         # process all ancestors for node p using parent pointers
#         while p:
#             ancestors.add(p)
#             p = parent[p]

#         while q not in ancestors:
#             q = parent[q]

#         return q
