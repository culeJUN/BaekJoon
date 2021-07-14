N = int(input())
data = [[0] * 10 for i in range(N + 1)]

for i  in range(1, 10) :
    data[1][i] = 1

for i in range(2, N + 1) :
    for j in range(10) :
        if j == 0 :
            data[i][j] = data[i - 1][1]
        elif j == 9 :
            data[i][j] = data[i - 1][8]
        else :
            data[i][j] = data[i - 1][j - 1] + data[i - 1][j + 1]

print(sum(data[N]) % 1000000000)