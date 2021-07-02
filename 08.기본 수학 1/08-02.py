num = int(input()) 
flag = 0
count = 1

while True :
    if(num > 1) :
        flag += 6
    else :
        break

    num -= flag
    count += 1
    
print(count)