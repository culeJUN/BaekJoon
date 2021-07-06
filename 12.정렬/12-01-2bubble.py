time = int(input())
num = []

for i in range(time) :
    num.append(int(input()))

for i in reversed(range(time)) :
    for j in range(i) :
        if num[j] > num[j + 1] :
            num[j], num[j + 1] = num[j + 1], num[j]
    
for i in range(time) :
    print(num[i])