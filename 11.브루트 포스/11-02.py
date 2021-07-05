x = int(input())
answer = []

for i in range(x) :
    num = i
    number = str(i)
    for j in number :
        num += int(j)
    if num == x :
        answer.append(i)

if answer == [] :
    print(0)
else :
    print(min(answer))