import sys
input = sys.stdin.readline

n = int(input())
data = [0, 0, 1, 1]

for i in range(4, n + 1) :
    data.append(data[i - 1] + 1)

    if i % 2  == 0 :
        data[i] = min(data[i], data[i // 2] + 1)

    if i % 3 == 0 :
        data[i] = min(data[i], data[i // 3] + 1)

print(data[n])