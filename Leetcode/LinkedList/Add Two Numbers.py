'''
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        curr = dummy
        _carry = 0
        # There's at least 1 node in each linkedlist, so no need to put edge case at the beginning
        while l1 or l2:
            first = l1.val if l1 else 0
            second = l2.val if l2 else 0
            _val = (first + second + _carry)%10
            _carry = (first + second + _carry)//10
            curr.next = ListNode(_val)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        # check if carry == 1, if so, add a listnode with value 1
        if _carry == 1:
            curr.next = ListNode(1)
        return dummy.next
# Time: O(max(m,n)), m is the length of the first linkedlist, n is the length of the second linkedlist
# Space: O(max(m,n)), the length of new list is at most max(m,n) + 1
