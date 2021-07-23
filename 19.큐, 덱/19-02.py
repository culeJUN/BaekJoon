from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while True :
    if len(deque) == 1 :
        break
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])