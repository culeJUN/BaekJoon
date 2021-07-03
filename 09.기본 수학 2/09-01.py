num = [i for i in range(1, 1001)]

for i in range(1000) :
    n = num[i]
    if n < 2 :
        del num[i]
        num.insert(i, 0)
    for j in range(2, n) :
        if n % j == 0 :
            del num[i]
            num.insert(i, 0)

time = int(input()) 
x = list(map(int, input().split()))
count = 0

for i in x :
    if i in num :
        count+= 1

print(count)