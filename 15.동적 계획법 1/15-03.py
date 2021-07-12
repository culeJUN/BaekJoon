import sys

data = [0] * 1000001

data[1] = 1
data[2] = 2

n = int(sys.stdin.readline())
for i in range(3, n + 1) :
    data[i] = (data[i - 1] + data[i - 2]) %15746

print(data[n])