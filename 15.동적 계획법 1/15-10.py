import sys
input = sys.stdin.readline

x = int(input())
wine = [0] * 10000
total = [0] * 10000
for i in range(x) :
    wine[i] = int(input())

total[0] = wine[0]
total[1] = wine[0] + wine[1]
total[2] = max(total[1], wine[0] + wine[2], wine[1] + wine[2])
for i in range(3, x) :
    total[i] = max(wine[i] + total[i - 2], wine[i] + wine[i - 1] + total[i - 3], total[i - 1])

print(max(total))