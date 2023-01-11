'''
Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid is filled with water.
- Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land. We have 1 island.
- Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land. We still have 1 island.
- Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land. We have 2 islands.
- Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land. We have 3 islands.
'''

'''
题目：
每加一个岛，计算一次当前不相邻的island数目,此题要用union-find解法
Time: O(m*n + L) m: rows, n: cols, L: # of operations to process positions,
union opeartions take O(1)
Space: O(m*n)
'''
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # Return final result.
        ans = []
        island = Union()
        # 每加一个岛，计算一下当前岛数是否有变化，将答案加入ans list.
        for p in map(tuple, positions):
            if p not in island.id:
                island.add(p)
                for np in [(0,1),(0,-1),(1,0),(-1,0)]:
                    q = (p[0] + np[0], p[1] + np[1])
                    # 任何一个方向有岛则call unite method
                    if q in island.id:
                        island.unite(p, q)
            ans += [island.count]
        return ans

class Union(object):
	def __init__(self):
		# 记录island连着哪个父island
		self.id = {}
		# 记录当前island有多少个connections
		self.id_links = {}
		# count island的数目
		self.count = 0

	def add(self, p):
		# {curr_pos: curr_pos or parent_pos}
		self.id[p] = p
		# {curr_pos: number}
		self.id_links[p] = 1
		self.count += 1

	def unite(self, p, q):
		# 在unite之前判断一下当前p和q是否分别连接别的岛，找到他们的父节点
		parent_p, parent_q = self.root(p), self.root(q)
		# 如果自己连自己，直接返回，不需要执行接下来的unite
		if parent_p == parent_q:
			return
		# 连接数少的投靠连接数多的，然后将少的连接数再加到多的连接数上去，合算
		if self.id_links[parent_p] > self.id_links[parent_q]:
			parent_p, parent_q = parent_q, parent_p
		self.id[parent_p] = parent_q
		self.id_links[parent_q] += self.id_links[parent_p]
		# unite后减1
		self.count -= 1

	def root(self, curr):
		# 如果当前位置连着别的位置,则从当前位置追溯到最远的父节点
		while curr != self.id[curr]:
			curr = self.id[curr]
		return curr
