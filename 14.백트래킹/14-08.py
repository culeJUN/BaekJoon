import sys

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        start, link = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    start += a[i][j]
                elif not select[i] and not select[j]:
                    link += a[i][j]
        ans = min(ans, abs(start - link))

    for i in range(idx, n):
        if select[i]:
            continue
        select[i] = 1
        dfs(i + 1, cnt + 1)
        select[i] = 0


n = int(sys.stdin.readline())       #몇명?
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]       #점수

select = [0 for i in range(n)]      #팀 선택 ex) (0, 0, 1, 1)
ans = 9999999999999999999
dfs(0, 0)
print(ans)