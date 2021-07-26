import sys
input = sys.stdin.readline

def square(x, y, n) :
    global blue, white
    check = paper[x][y]
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if check != paper[i][j] :
                check = -1
                break

    if check == -1 :
        square(x, y, n // 2)
        square(x + n // 2, y, n // 2)
        square(x, y + n // 2, n // 2)
        square(x + n // 2, y + n // 2, n // 2)

    elif check == 1 :
        blue += 1

    elif check == 0 :
        white += 1

line = int(input())
paper = [list(map(int,input().split())) for i in range(line)]
white, blue = 0, 0
square(0, 0, line)
print(white)
print(blue)