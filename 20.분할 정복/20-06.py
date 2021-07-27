N, M = map(int, input().split())
A = [list(map(int, input().split())) for i in range(N)]
M, K = map(int, input().split())
B = [list(map(int, input().split())) for i in range(M)]
answer = [[0 for i in range(K)]for i in range(N)]

for n in range(N) :
    for k in range(K) :
        for m in range(M) :
            answer[n][k] += A[n][m] * B[m][k]

for i in answer :
    for j in i :
        print(j, end = ' ')
    print()