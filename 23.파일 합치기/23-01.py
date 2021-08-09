import sys
input = sys.stdin.readline

n = int(input())
for i in range(n) :
    num = int(input())
    file = [0] + list(map(int, input().split()))
    sum = [0 for _ in range(num + 1)]
    for i in range(1, num + 1) :
        sum[i] = sum[i - 1] + file[i]
    
    DP = [[0 for _ in range(num + 1)] for _ in range(num + 1)]
    for i in range(2, num + 1) :            # 2개씩 묶는거 부터 시작
        for j in range(1, num + 2 - i) :
            DP[j][j+i-1] = min([DP[j][j+k] + DP[j+k+1][j+i-1] for k in range(i-1)]) + (sum[j+i-1] - sum[j-1])       #이걸 어케 생각하지...
    
    print(DP[1][-1])