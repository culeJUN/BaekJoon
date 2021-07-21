num = int(input())
time = list(map(int, input().split()))
sum = 0
time.sort()

for i in range(num) :
    for j in range(i + 1) :
        sum += time[j]

print(sum)