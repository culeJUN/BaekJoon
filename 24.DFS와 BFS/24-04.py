import sys
sys.setrecursionlimit(10000)        # 재귀 깊이 한정
input = sys.stdin.readline
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y) :
        maps[x][y] = 0
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < m) :            
                if maps[nx][ny] == 1 :
                    dfs(nx, ny)

for _ in range(t) :
    n, m, num = map(int, input().split())
    maps = [[0] * m for _ in range(n)]  
    count = 0
    for _ in range(num):
        a,b = map(int,input().split())
        maps[a][b] = 1

    for i in range(n) :
        for j in range(m) :
            if maps[i][j] == 1 :
                count += 1
                dfs(i, j)
                
    print(count)