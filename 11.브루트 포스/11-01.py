N, M = map(int, input().split())
card = list(map(int, input().split()))
list_sum = []

for i in range(N) :
    for j in range(i + 1, N) :
        for k in range(j + 1, N) :
            sum = card[i] + card[j] + card[k]
            if sum <= M :
                list_sum.append(sum)

print(max(list_sum))