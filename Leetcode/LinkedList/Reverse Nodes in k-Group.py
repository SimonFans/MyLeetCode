'''
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

Input: 1 - 2 - 3 - 4 - 5
Result: 2 - 1 - 4 - 3 - 5
'''

class Solution(object):
    def reverseKGroup(self, head, k):
        count, node = 0, head
        while node and count < k:
            node = node.next
            count += 1
        if count < k: return head
        new_head, prev = self.reverse(head, count)
        head.next = self.reverseKGroup(new_head, k)
        return prev

    def reverse(self, head, count):
        prev, cur, nxt = None, head, head
        while count > 0:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count -= 1
        return (cur, prev)
