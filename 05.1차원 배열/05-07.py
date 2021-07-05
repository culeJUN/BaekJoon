num = int(input())

for i in range(num) :
    inf = list(map(int, input().split()))
    sumary = sum(inf) - inf[0]
    average = sumary / inf[0]
    people = 0
    
    for j in range(1, len(inf)) :
        if inf[j] > average :
            people += 1

    average = people / inf[0] * 100
    print('%0.3f' % float(average) + '%')