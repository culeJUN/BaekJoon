import sys
input = sys.stdin.readline

def square(x, y, n) :
    global red, blue, white
    check = paper[x][y]
    for i in range(x, x + n) :
        for j in range(y, y + n) :
            if check != paper[i][j] :
                check = 999
                break

    if check == 999 :
        square(x, y, n // 3)
        square(x, y + n // 3, n // 3)
        square(x, y + 2 * (n // 3), n // 3)
        square(x + n // 3, y, n // 3)
        square(x + n // 3, y + n // 3, n // 3)
        square(x + n // 3, y + 2 * (n // 3), n // 3)
        square(x + 2 * (n // 3), y, n // 3)
        square(x + 2 * (n // 3), y + n // 3, n // 3)
        square(x + 2 * (n // 3), y + 2 * (n // 3), n // 3)

    elif check == -1 :
        red += 1

    elif check == 0 :
        white += 1

    elif check == 1 :
        blue += 1

line = int(input())
paper = [list(map(int,input().split())) for i in range(line)]
white, blue, red = 0, 0, 0
square(0, 0, line)
print(red)
print(white)
print(blue)