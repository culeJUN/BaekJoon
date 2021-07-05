time = int(input())
person = []

for i in range(time) :
    person.append(input().split())

level = []

for i in range(time) :
    count = 1
    for j in range(time) :
        if person[i][0] < person[j][0] and person[i][1] < person[j][1] :
            count += 1
    level.append(count)

for i in range(time) :
    print(level[i], end = ' ')