time = int(input())

for i in range(time) :    
    num, s = input().split()
    for i in s :
        print(i * int(num), end = '')
    print()