import sys

size = int(sys.stdin.readline())
layer = [[]for i in range(size)]
for i in range(size) :
    layer[i] = list(map(int, sys.stdin.readline().split()))

for i in range(1, size) :
    for j in range(i + 1) :
        if j == i :
            layer[i][j] += layer[i - 1][j - 1] 
        elif j == 0 :
            layer[i][j] += layer[i - 1][j]
        else :
            layer[i][j] += max(layer[i - 1][j - 1], layer[i - 1][j]) 

sys.stdout.write(str(max(layer[size - 1])))