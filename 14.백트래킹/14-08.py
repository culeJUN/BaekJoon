import sys

def dfs(idx, cnt):
    global ans
    if cnt == n // 2:
        team_a, team_b = 0, 0
        for i in range(n):
            for j in range(n):
                if select[i] and select[j]:
                    team_a += a[i][j]
                elif not select[i] and not select[j]:
                    team_b += a[i][j]
        ans = min(ans, abs(team_a - team_b))

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