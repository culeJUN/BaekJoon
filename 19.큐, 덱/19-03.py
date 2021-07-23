from collections import deque

N, K = map(int, input().split())
deque = deque([i for i in range(1, N + 1)])
answer = []
for i in range(K - 1) :
    move_num = deque.popleft()
    deque.append(move_num)

print('<', end = '')
while True :
    print(deque.popleft(), end = '')
    if len(deque) == 0 :
        break
    print(', ', end = '')
    for i in range(K - 1) :
        move_num = deque.popleft()
        deque.append(move_num)
print('>')