import sys
input = sys.stdin.readline

def mul(A, B) :
    answer = [[0] * len(A) for j in range(len(A))]

    for i in range(len(A)) :
        for j in range(len(A)) :
            for k in range(len(A)) :
                answer[i][j] += A[i][k] * B[k][j]
                answer[i][j] %= 1000
    return answer

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for j in range(N)]
answer = [[1 if i == j else 0 for i in range(N)] for j in range(N)]

while B != 1 :
    temp = matrix[:]
    if B % 2 :
        answer = mul(answer, temp)
        B -= 1
    else :
        matrix = mul(temp, temp)
        B //= 2

answer = mul(answer, matrix)
for i in answer :
    for j in i :
        print(j, end = ' ')
    print()
