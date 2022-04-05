'''
Input: root = [4,2,5,1,3], target = 3.714286, k = 2
     4
   2    5
 1   3
Output: [4,3]
'''
给一个target值，想找出离这个target值最近的K个点.
inorder traversal + heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        heap = []
        ans = []
        def inOrderTraversal(node, target):
            if not node:
                return
            inOrderTraversal(node.left, target)
            heapq.heappush(heap, (abs(node.val-target), node.val))
            inOrderTraversal(node.right, target)
        inOrderTraversal(root, target)
        while k:
            ans.append(heapq.heappop(heap)[1])
            k-=1
        return ans
