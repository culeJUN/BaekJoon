line = int(input())

for i in range(line) :
    for j in range(line - i - 1, 0, -1) :
        print(' ', end = '')
    for k in range(0, i + 1) :
        print('*', end = '')
    print()