time = int(input())
num = []

for i in range(time) :
    num.append(int(input()))

num.sort()

for i in range(time) :
    print(num[i])
    print()