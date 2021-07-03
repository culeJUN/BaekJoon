x = int(input())
y = int(input())
num = []

for i in range(x, y + 1) :
    flag = 1
    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                flag = 0
                break
        if flag :
            num.append(i)

if num == [] :
    print(-1) 
else :
    print(sum(num))
    print(min(num))