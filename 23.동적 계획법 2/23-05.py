import sys 
input = sys.stdin.readline

N = int(input())
sinkers = list(map(int, input().split()))
M = int(input())
beads = list(map(int, input().split()))
dp = [[0] * 15001 for _ in range(N + 1)]    # 15001 = 추의 무게 총합    # 앞에서부터 n개 썼을때 가능한 무게 = 1
possible = []

def dfs(sinkers, n, now, left, right) :     # (추 종류, 총 n개, 추가한 추, 왼쪽 저울, 오른쪽 저울)
    new = abs(left - right)

    if new not in possible :
        possible.append(new)
    
    if now == n : 
        dp[now][new] = 1
        return 0

    if dp[now][new] == 0 :
        dfs(sinkers, n, now + 1, left + sinkers[now], right)    # 왼쪽에 올리기
        dfs(sinkers, n, now + 1, left, right + sinkers[now])    # 오른쪽에 올리기
        dfs(sinkers, n, now + 1, left, right)                   # 안올리기
        dp[now][new] = 1

dfs(sinkers, N, 0, 0, 0)
for i in range(0, M) :
    if beads[i] in possible :
        print('Y', end = ' ')
    else :
        print('N', end = ' ')