num, money = map(int, input().split())
type = []
count = 0
for i in range(num) :
    type.append(int(input()))
type.sort(reverse=True)

for i in type :
    if money == 0 :
        break
    count += money // i
    money %= i

print(count)