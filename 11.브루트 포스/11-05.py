x = int(input())
six_num = 666
count = 0

while True :
    if '666' in str(six_num) :
        count += 1
    
    if count == x :
        print(six_num)
        break

    six_num += 1