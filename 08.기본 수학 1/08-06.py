apartment = [[0 for i in range(15)] for j in range(15)]
for i in range(1, 15) :
    apartment[0][i] = i

for floor in range(1, 15) :
    for ho in range(1, 15) :
            apartment[floor][ho] = apartment[floor - 1][ho] + apartment[floor][ho - 1]

num = int(input())
for i in range(num) :
    x = int(input())
    y = int(input())
    print(apartment[x][y])