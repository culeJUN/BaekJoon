num = int(input())
count = 0

for i in range(num) :
    word = input()
    temp = []
    for j in range(len(word)) :
        if word[j] in temp :
            if word[j] == temp[-1] :
                if j == len(word) - 1:
                    count += 1
                    temp.clear()
                continue
            else :
                temp.clear()
                break 
        else :
            temp.append(word[j])
            if j == len(word) - 1:
                count += 1
                temp.clear()
            continue
            
print(count)