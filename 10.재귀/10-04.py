def hanoi(x, line1, line3, line2) :
    if x == 1 :
        print(line1, line3)

    else :
        hanoi(x - 1, line1, line2, line3) 
        print(line1, line3)
        hanoi(x - 1, line2, line3, line1)

x = int(input())
print(2 ** x - 1)
hanoi(x, 1, 3, 2)