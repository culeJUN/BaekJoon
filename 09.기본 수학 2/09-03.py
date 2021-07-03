x = int(input())
num = []
while True :
    if x == 1 : 
        break
    for i in range(2, x + 1) :
        if x % i == 0 :
            x = x // i
            num.append(i)
            break
    
for i in num :
    print(i)