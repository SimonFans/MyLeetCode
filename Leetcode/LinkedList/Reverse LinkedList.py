# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
none  1 ->   2 --->
prev  c    temp

none <- 1    2 --->
prev    c   temp

none <- 1     2 --->
        c    temp
        prev

none <- 1     2 --->
        prev temp
              c
'''

# Time: O(n) n: list's length. Space: O(1)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr, nxt = None, head, head
        while curr:
            # 保留当前node下一个位置的地址
            nxt = curr.next
            # 当前位置指向前一个node prev
            curr.next = prev
            # 当前位置成为新的prev
            prev = curr
            # 当前位置移到下一个位置
            curr = nxt
        return prev




''' (2) This is the second way to do this problem using recursion
1 -> 2 -> 3 -> N
1 -> 2 <- 3
     h    p
'''
# Time: O(N)  Space: O(N)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # empty linkedlist or only 1
        if (not head) or (not head.next):
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
