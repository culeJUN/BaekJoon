city = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))
cheap = oil[0]
total = 0

for i in range(len(length)) :
    if oil[i] < cheap :
        cheap = oil[i]
    total += cheap * length[i]

print(total)