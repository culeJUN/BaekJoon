time = int(input())

for i in range(time) :
    K, N = map(int, input().split())
    up  = 1
    down = 1
    for i in range(K) :
        up *= (N - i)
        down *= (K - i)

    print(up // down)