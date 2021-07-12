import sys

n = int(sys.stdin.readline())
array = [[0 for _ in range(3)] for __ in range(n)]
table = [[0 for _ in range(3)] for __ in range(n)]
for i in range(n):
    array[i][0], array[i][1], array[i][2] = list(map(int, sys.stdin.readline().split()))

for i in range(n):  # i = 0 일때는 그냥 array맨 윗줄 복붙 그 이후부터는 위에서부터 안겹치게 누적
    table[i][0] = min(table[i - 1][1], table[i - 1][2]) + array[i][0]       
    table[i][1] = min(table[i - 1][0], table[i - 1][2]) + array[i][1]
    table[i][2] = min(table[i - 1][0], table[i - 1][1]) + array[i][2]

print(min(table[n - 1][0], table[n - 1][1], table[n - 1][2]))