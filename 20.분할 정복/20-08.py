import sys
input = sys.stdin.readline
mod = 1000000007

def power(matrix, n) :
    if n == 1 :
        return matrix
    else :
        temp = power(matrix, n // 2) 
        if n % 2 == 0 :
            return multi(temp, temp)
        else :
            return multi(multi(temp, temp), matrix)

def multi(A, B) :
    answer = [[] for _ in range(len(A))]
    for i in range(len(A)) :
        for j in range(len(A)) :
            temp = 0
            for k in range(len(A)) :
                temp += A[i][k] * B[k][j]
            answer[i].append(temp % mod)
    return answer

N = int(input())
fibo_matrix = [[1, 1], [1, 0]]
print(power(fibo_matrix, N)[0][1])