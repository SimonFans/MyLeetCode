import heapq
from collections import deque
heap = deque()
heapq.heapify(heap)
heapq.heappush(heap, (1,2))
heapq.heappop(heap)
