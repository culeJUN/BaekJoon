import sys

T = int(input())

for i in range(T) :
    x, y = map(int, sys.stdin.readline().split())
    print(x + y)