import sys

# 가로 체크
def horizontal(x, val):
    if val in sudoku[x]:
        return False
    return True

# 세로 체크
def vertical(y, val):
    for i in range(9):
        if val == sudoku[i][y]:
            return False
    return True

# 3x3 체크
def bythree(x, y, val):
    x = x//3 * 3
    y = y//3 * 3
    for i in range(3):
        for j in range(3):
            if val == sudoku[x+i][y+j]:
                return False
    return True


def DFS(index):
    if index == len(zero):
        for row in sudoku:
            for n in row:
                print(n, end=" ")
            print()
        return
    else:
        for i in range(1, 10):
            x = zero[index][0]
            y = zero[index][1]

            if horizontal(x, i) and vertical(y, i) and bythree(x, y, i):
                sudoku[x][y] = i
                DFS(index+1)
                sudoku[x][y] = 0


sudoku = []
for i in range(9) :
    sudoku.append(list(map(int, sys.stdin.readline().split())))

zero = []
for i in range(9) :
    for j in range(9) :
        if sudoku[i][j] == 0 :
            zero.append((i, j))
            
DFS(0)
print()
print(sudoku)