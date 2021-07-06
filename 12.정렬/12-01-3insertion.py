time = int(input())
num = []

for i in range(time) :
    num.append(int(input()))

for i in range(1, time) :
    for j in range(i, 0, -1) :
        if num[j] < num[j - 1] :
            num[j], num[j - 1] = num[j - 1], num[j]
        else :
            break

    
for i in range(time) :
    print(num[i])