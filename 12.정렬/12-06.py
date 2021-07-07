import sys

n = int(sys.stdin.readline())
list_point = []
for i in range(n) :
    list_point.append(list(map(int, sys.stdin.readline().split())))

list_point.sort()

for i in range(len(list_point)) :
    print(str(list_point[i][0]) + ' ' + str(list_point[i][1]))