import sys
input = sys.stdin.readline

num = int(input())
for i in range(num) :
    stack = []
    command = input()
    for i in range(len(command) - 1) :
        if command[i] == '(' :
            stack.append(1)
        else :
            if stack == [] :
                stack.append(-1)
                break
            del stack[-1]

    if stack == [] :
        print('YES')
    else :
        print('NO')