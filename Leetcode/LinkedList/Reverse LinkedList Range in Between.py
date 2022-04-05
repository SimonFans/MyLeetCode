# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
dummy -> 1 ->   2 ->  3 -> 4 -> 5
         prev  curr

              None
                 \
dummy -> 1 ->     2 <-  3     <- 4      <- 5
         prev              newHead    curr

                  ----------------------
                  |                    |
dummy -> 1      2 <-  3     <- 4       5
         prev              newHead    curr
         |                       |
         ------------------------
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # 锁定left之前的node位置
        for i in range(left-1):
            prev = prev.next
        # 定位left node
        curr = prev.next
        # reverse
        newHead = None
        for i in range(right-left+1):
            _next = curr.next
            curr.next = newHead
            newHead = curr
            curr = _next
        #最后整合
        # 2 link 5, 1 link 4
        prev.next.next = curr
        prev.next = newHead
        return dummy.next

Time: O(N) Space: O(1)
