'''
Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
1 -> 2 -> 2 -> 1
s
f
p_s

1 -> 2 -> 2 -> 1 -> None
    p_s   s
                     f

  1 <- 2     2 -> 1 -> None
 /    prev   s
None  p_s               f
'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # define prev_slow to keep the previous status of the slow pointer
        prev_slow = slow
        # define prev pointer which is used to do reverse later
        prev = None
        # use slow, fast pointers to find out the middle
        while fast and fast.next:
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        prev_slow.next = None
        # if fast is not None, then it means the length is odd, otherwise length is even.
        if fast:
            slow = slow.next
        while slow:
            _next = slow.next
            slow.next = prev
            prev = slow
            slow = _next
        while prev and head:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
