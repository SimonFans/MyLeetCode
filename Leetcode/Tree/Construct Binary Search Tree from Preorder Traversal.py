'''
Input: preorder = [8,5,1,7,10,12]
Output: [8,5,10,1,7,null,12]
        8
    5       10
 1    7   N   12

Input: preorder = [1,3]
Output: [1,null,3]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def helper(lower, upper):
            # define a global variable here!!! 不会倒退，只会向前
            nonlocal idx

            # After the last node was visited, idx == len(preorder) because idx+1 before calling left & right
            if idx == len(preorder):
                return None
            # binary search tree feature
            if not lower <= preorder[idx] <= upper:
                return None
            root = TreeNode(preorder[idx])
            idx += 1
            root.left = helper(lower, root.val)
            root.right = helper(root.val, upper)
            return root

        idx = 0
        return helper(float('-Inf'), float('Inf'))

'''
Time: O(N)
Space: O(N)
'''
