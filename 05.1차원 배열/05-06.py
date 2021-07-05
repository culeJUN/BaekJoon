num = int(input())

for i in range(num) :
    answer = input()
    score = 0
    total = 0

    for j in range(len(answer)) :
        if answer[j] == 'O' :
            score += 1
            total += score
        elif answer[j] == 'X' :
            score = 0

    print(total)