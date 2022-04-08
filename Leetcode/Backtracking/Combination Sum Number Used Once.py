'''
Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]
'''

class Solution:

    # 和上一道题类似。只不过这道题要求candidate中的每个数只能使用一次。也是使用dfs。
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        def helper(start, path, remain):
            if remain == 0:
                ans.append(path)
                return

            for i in range(start, len(candidates)):
                # if [1 1 1] , target = 2 then second part 1 1 will not run
                #       s i
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                # if current value is greater than the remain value then no need to continue
                if candidates[i] > remain:
                    break
                helper(i + 1, path + [candidates[i]], remain - candidates[i])

        # aviod over counting
        candidates.sort()
        ans = []
        helper(0, [], target)
        return ans
