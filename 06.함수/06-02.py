def calc (a) :
    value = sum(map(int, str(a))) + a
    return value

number = list(range(1, 10001))
num = []
for i in number :
    num.append(calc(i))

for i in number :
    if i in num :
        continue 
    else :
        print(i)