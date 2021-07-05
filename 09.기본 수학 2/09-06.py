N = 10000
prime = [False, False] + [True for i in range(N - 1)]
for i in range(2, N + 1) :
    for j in range(2 * i, N + 1, i) :
        prime[j] = False

time = int(input())
for i in range(time) :
    x = int(input())
    for i in range(x // 2, 0, -1) :
        if prime[i] == True and prime[x - i] == True :
            print(str(i) + ' ' + str(x - i))
            break