'''
Given the head of a linked list, rotate the list to the right by k places.
Example:
Input:
1 -> 2 -> 3 -> 4 -> 5

After rotate the list to the right by 2 places
Output:
4 -> 5 -> 1 -> 2 -> 3
'''

思路： 因为k可能大于长度或者小于长度，可以通过模值运算来决定从左到右移动几位。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if head is null
        if not head:
            return head

        # get the length of linkedlist
        length, tail = 1, head
        while tail.next:
            tail = tail.next
            length += 1

        # if k > length and k < length
        k = k % length
        if k == 0:
            return head

        cur = head
        for _ in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        # cur.next = tail.next
        cur.next = None
        tail.next = head

        return newHead
