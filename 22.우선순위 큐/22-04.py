import sys 
import heapq
input= sys.stdin.readline

n = int(input())
heap_left = []          # 최대 힙
heap_right = []         # 최소 힙
for i in range(n) :
    num = int(input())
    if len(heap_left) == len(heap_right) :
        heapq.heappush(heap_left, (-num, num))
    else :
        heapq.heappush(heap_right, (num, num))
        
    if len(heap_left) > 0 and len(heap_right) > 0 and heap_left[0][1] > heap_right[0][1] :
        max_val = heapq.heappop(heap_left)[1]
        min_val = heapq.heappop(heap_right)[1]
        heapq.heappush(heap_left, (-min_val, min_val))
        heapq.heappush(heap_right, (max_val, max_val))
    
    print(heap_left[0][1])