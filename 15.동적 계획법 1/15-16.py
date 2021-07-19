import sys

(N, K) = map(int, sys.stdin.readline().split())
item = [[0, 0]] 

for i in range(1, N + 1): 
    item.append(list(map(int, sys.stdin.readline().split()))) 

table = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1) : 
    for j in range(1, K + 1) : 
        if j >= item[i][0] : 
            table[i][j] = max(table[i-1][j], table[i-1][j-item[i][0]] + item[i][1]) 
        else : 
            table[i][j] = table[i-1][j] 
            
print(table[N][K])