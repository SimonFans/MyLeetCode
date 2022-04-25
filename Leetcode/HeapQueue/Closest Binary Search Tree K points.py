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
        def helper(node, target):
            if not node:
                return
            helper(node.left, target)
            # 保存在heap queue里面的就是答案(distance, node val)
            heapq.heappush(heap, (-abs(node.val- target), node.val))
            if len(heap) > k:
                heapq.heappop(heap)
            helper(node.right, target)
        helper(root, target)
        print(heap)
        return [val for _, val in heap]
