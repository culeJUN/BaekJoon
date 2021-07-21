sik = input().split('-')
num = []
for i in sik :
    sum = 0
    short = i.split('+')
    for j in short :
        sum += int(j)
    num.append(sum)

n = num[0]
for i in range(1, len(num)) :
    n -= num[i]

print(n)