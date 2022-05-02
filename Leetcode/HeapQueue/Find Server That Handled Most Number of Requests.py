'''
Leetcode: 1606
Input: k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3]
Output: [1]
Explanation:
All of the servers start out available.
The first 3 requests are handled by the first 3 servers in order.
Request 3 comes in. Server 0 is busy, so it's assigned to the next available server, which is 1.
Request 4 comes in. It cannot be handled since all servers are busy, so it is dropped.
Servers 0 and 2 handled one request each, while server 1 handled two requests. Hence server 1 is the busiest server.
'''

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        cnt = [0] * k
        busy = []
        # available servers id
        available = [i for i in range(k)]
        # For each incoming requests
        for r in range(len(arrival)):
            # check if there's any servers can be added into the available heap
            while busy and busy[0][0] <= arrival[r]:
                _, server = heapq.heappop(busy)
                heapq.heappush(available, r + (server - r)%k)
            if available:
                avai_server = heapq.heappop(available)%k
                heapq.heappush(busy, (arrival[r] + load[r], avai_server))
                cnt[avai_server] += 1
        target = max(cnt)
        return [i for i in range(k) if cnt[i] == target]
