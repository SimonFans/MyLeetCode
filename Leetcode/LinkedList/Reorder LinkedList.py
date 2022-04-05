'''
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle
        if not head or not head.next:
            return head

        slow, fast = head, head
        prev_slow = slow
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        prev_slow.next = None

        # Reverse 后半段
        prev, curr = None, slow
        while curr:
            _next = curr.next
            curr.next = prev
            prev = curr
            curr = _next

        # Result
        first, second = head, prev
        dummy = ListNode(-1)
        curr = dummy

        while first or second:
            if first:
                curr.next = first
                first = first.next
                curr = curr.next
            if second:
                curr.next = second
                second = second.next
                curr = curr.next
        return dummy.next

Time: O(N)
Find the middle takes O(N), reverse the second part needs N/2 operations,
final merge needs N/2 operations.
Space: O(1)
