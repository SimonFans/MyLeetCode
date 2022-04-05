'''
Input: n = 1
Output: 10
Explanation: We need to dial a number of length 1, so placing the knight over any numeric cell of the 10 cells is sufficient.

Input: n = 2
Output: 20
Explanation: All the valid number we can dial are [04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]
'''

class Solution:
    def knightDialer(self, n: int) -> int:
	# paths represents every key we can go to from given key
	# -1 is starting condition, we can start from any key
    # cache {1:4} means one step jump to pad number 4 has 3 ways, cache {2:0} means two steps jump to pad 0 has x ways

        paths = {-1: [0,1,2,3,4,5,6,7,8,9], 0: [4,6], 1: [6,8], 2: [7,9],
		3: [4,8], 4: [0,3,9], 5: [], 6: [0,1,7], 7: [2,6], 8: [1,3], 9: [2,4] }

        return self.helper(paths, n, -1, {}) % (10 ** 9 + 7)

    def helper(self, paths, step, number, cache):
        if (step, number) in cache:
            return cache[(step, number)]
        if step == 0:
            return 1
        count = 0
        for num in paths[number]:
            count += self.helper(paths, step - 1, num, cache)
        cache[(step, number)] = count
        return count
