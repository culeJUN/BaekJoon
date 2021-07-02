total = int(input()) 
n = total // 5 + 1
num = []
for i in range(n) :
    x = total // 5 - i
    if (total - 5 * x) % 3 != 0 :
        continue
    y = (total - 5 * x) // 3
    num.append(x + y)
    
if num != [] :
    print(min(num))
else :
    print(-1)