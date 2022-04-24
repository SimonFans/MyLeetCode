'''
arr_list = [[3,6,9],[1,2,3],[9,10,12]]
Answer: [1, 2, 3, 3, 6, 9, 9, 10, 12]
'''

import heapq
arr_list = [[3,6,9],[1,2,3],[9,10,12]]
# minHeap
minHeap = []
res = []
for arr in arr_list:
    if arr:
        heapq.heappush(minHeap, (arr[0],arr[1:]))
while minHeap:
    num, next_arr = heapq.heappop(minHeap)
    res.append(num)
    if next_arr:
        heapq.heappush(minHeap, (next_arr[0], next_arr[1:]))
print(res)
