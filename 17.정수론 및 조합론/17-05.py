num = int(input())
list_num = []
for i in range(num) :
    list_num.append(int(input()))
list_num.sort()

for i in range(2, list_num[1]) :
    left = list_num[0] % i
    flag = 0
    for j in range(1, len(list_num)) :
        if left != list_num[j] % i :
            flag = 1
            break
    if flag == 0 :
        print(i, end = ' ')