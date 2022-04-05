# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use fast pointer and slow pointer
        if not head:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            # Example: 1 -> null or 1 -> 2 -> null
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

# Time : O(n), n denotes the total number of nodes in the linkedlist.
# Space: O(1)
