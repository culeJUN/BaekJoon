num, money = map(int, input().split())
type = []
count = 0
for i in range(num) :
    type.append(int(input()))


while True :
    if money == 0 :
        break

    if money % type[-1] == money :
        type.pop()
    else :
        count += money // type[-1]
        money -= type[-1] * (money // type[-1])
        type.pop()

print(count)