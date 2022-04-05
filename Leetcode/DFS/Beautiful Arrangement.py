'''
Input: n = 2
Output: 2
Explanation:
The first beautiful arrangement is [1,2]:
    - perm[1] = 1 is divisible by i = 1
    - perm[2] = 2 is divisible by i = 2
The second beautiful arrangement is [2,1]:
    - perm[1] = 2 is divisible by i = 1
    - i = 2 is divisible by perm[2] = 1
'''

题目例子： 找有多少种组合，满足（1）当前位置的值%当前位置index=0 或者（2）当前位置index%当前位置的值=0
'''
Example:
assume N = 3, index is based on 1

 [1,2,3] ok
 [1,3,2] no 3&2 !=0 2%3!=0
 [2,1,3] ok
 [2,3,1] no 3&2 !=0 2%3!=0
 [3,1,2] no 3&2 !=0 2%3!=0
 [3,2,1] ok

 return ans = 3
'''

class Solution:
    def countArrangement(self, n: int) -> int:
        # backtracking recursion
        # lst: all possible choices at the current position
        # index: current position
        def helper(lst, index):
            # when list is empty means之前的选择都填满了
            if len(lst) == 0:
                return 1
            ans = 0
            for i in range(len(lst)):
                # 当前填入的数字满足这两个条件才继续填下一个位置，否则当前位置换下一个数字
                if lst[i]%index == 0 or index%lst[i] == 0:
                    ans += helper(lst[:i] + lst[i+1:], index + 1)
            return ans

        # create a list to include numbers from 1 to n, such as [1,2]
        lst = [i for i in range(1,n+1)]
        return helper(lst, 1)
