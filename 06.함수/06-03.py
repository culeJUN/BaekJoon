def calc(a) :
    list_num = list(map(int, str(a)))
    if len(list_num) == 1 :
        return 1
    
    flag = list_num[0] - list_num[1]
    for i in range(len(list_num)-1) :
        if list_num[i] - list_num[i + 1] == flag :
            continue  
        else :
            return 0          
    return 1

num = int(input())
count = 0

for i in range(1, num + 1) :
    if calc(i) == 1 :
        count += 1

print(count)