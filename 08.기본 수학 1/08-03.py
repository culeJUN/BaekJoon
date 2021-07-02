num = int(input())
a = 1
b = 1
line = 0
end = 0
count = 0
while True :
    if line % 2 == 1 :
        if num <= end :
            for i in range(line) :
                a = line - i
                b = i + 1
                count += 1
                if count == num :
                    break
        else :
            count += line
            line += 1
            end += line
    else :
        if num <= end :
            for i in range(line) :
                a = i + 1
                b = line - i
                count += 1
                if count == num :
                    break
        else :
            count += line
            line += 1
            end += line

    if count == num :
        print(str(a) + '/' + str(b))
        break