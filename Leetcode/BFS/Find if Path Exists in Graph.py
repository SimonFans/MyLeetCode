'''
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
'''

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # BFS
        neighbor = collections.defaultdict(list)
        # {0:[1,2], 1:[0,2], 2:[0,1]}
        for n1, n2 in edges:
            neighbor[n1].append(n2)
            neighbor[n2].append(n1)
        queue = collections.deque([source])
        visited = set()
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            visited.add(node)
            for n in neighbor[node]:
                if n not in visited:
                    queue.append(n)
        return False

        # DFS
        neighbor = collections.defaultdict(list)
        for n1, n2 in edges:
            neighbor[n1].append(n2)
            neighbor[n2].append(n1)
        visited = set()
        def dfs(node, end, visited):
            if node == end:
                return True
            if node in visited:
                return False
            visited.add(node)
            for n in neighbor[node]:
                if dfs(n,end, visited):
                    return True
            return False
        return dfs(source, destination, visited)
