import sys
input = sys.stdin.readline

def square(x, y, n) :
    check = paper[x][y]
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if check != paper[i][j] :
                print('(', end = '')
                square(x, y, n // 2)
                square(x, y + n // 2, n // 2)
                square(x + n // 2, y, n // 2)
                square(x + n // 2, y + n // 2, n // 2)
                print(')', end = '')
                return
    
    if check == 0 :
        print('0', end = '')
        return

    else :
        print('1', end = '')
        return

line = int(input())
paper = [list(map(int,input().strip())) for i in range(line)]
square(0, 0, line)