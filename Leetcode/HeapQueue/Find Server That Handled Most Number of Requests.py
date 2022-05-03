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


from sortedcontainers import SortedList
class Solution:
    def getNextServer(self, index , sortedAvailableServers):
        nextIndexToRightOfServer = sortedAvailableServers.bisect_left(index)
        # Since We need to find next server availble greater than this index
        if nextIndexToRightOfServer != len(sortedAvailableServers):
            return sortedAvailableServers[nextIndexToRightOfServer]
        # No server greater than index found , means move in cycle and find the lowest avaiable server now
        lowestIdServerAvailable = sortedAvailableServers.bisect_left(0)
        return sortedAvailableServers[lowestIdServerAvailable]

    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        heap = []
        # This heap will be use to make servers as free , the first server to become free will be top element of heap

        sortedAvailableServers = SortedList([i for i in range(k)])
        # This sorted available server list will be used to assign the load to new server , more comment in function

        count = collections.defaultdict(int)
        # This count dictionary will be used to record the count of request each server has handled, will be used in calculating result

        for i in range(len(arrival)):
            arrivalTime,loadTime = arrival[i], load[i]
            # ArrivalTime and loadTime , SimpleStuff

            # Check if any server has become free now, since top of heap will contain the first server which will get free
            # we just compare top server free time with currentTime and mark the server as free if possible
            while len(heap) > 0 and heap[0][0] <= arrivalTime:
                _,serverId = heapq.heappop(heap)
                # after marker this server free add it to list of free Servers
                sortedAvailableServers.add(serverId)

            #Check for any server Available
            if len(sortedAvailableServers) == 0:
                # Drop this Request because no server available
                continue

            # Get the assigned serverId for this Request
            assignedServer = self.getNextServer(i%k,sortedAvailableServers)

            count[assignedServer] += 1 # increase requestcount of this server by 1
            sortedAvailableServers.remove(assignedServer) # remove this server from list of free server
            heapq.heappush(heap,(arrivalTime+loadTime,assignedServer)) # insert this server in heap with free time as arrivalTime+loadTime

        # get the max request servered by any server
        maxRequestServedCount = max(count.values())
        result = []

        #iterate and pick all servers which servered maxRequest
        for serverId in count:
            if count[serverId] == maxRequestServedCount:
                result.append(serverId)

        return result
