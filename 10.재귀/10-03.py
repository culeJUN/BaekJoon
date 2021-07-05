def draw(x, map) :
    if x < 3 :
        return
    if x == 3 :
        map[1][1] = ' '
    else :
        draw(x // 3, map)
        for i in range(x // 3) :
            for j in range(x // 3) :
                if map[i][j] == ' ' :
                    map[i][j + x // 3] = ' '
                    map[i][j + 2 * x // 3] = ' '
                    map[i + x // 3][j] = ' '
                    map[i + x // 3][j + 2 * x // 3] = ' '
                    map[i + 2 * x // 3][j] = ' '
                    map[i + 2 * x // 3][j + x //3] = ' '
                    map[i + 2 * x // 3][j + 2 * x //3] = ' '
                    
        for i in range(x) :
            for j in range(x) :
                if x // 3 <= i < 2 * (x // 3) and x // 3 <= j < 2 * (x // 3) :
                    map[i][j] = ' '

x = int(input())
map = [['*' for i in range(x)] for i in range(x)]
draw(x, map)

for i in range(x) :
    for j in range(x) :
        print(map[i][j], end = '')
    print()