import sys
input = sys.stdin.readline

while True :
    stack = []
    command = input()
    if command == '.' :
        break

    for i in range(len(command) - 1) :
        if command[i] == '(' :
            stack.append('(')

        elif command[i] == '[' :
            stack.append('[')

        elif command[i] == ')' :
            if len(stack) == 0 :
                break
            elif stack[-1] == '(' :
                del stack[-1]
            else :            
                break
            
        elif command[i] == ']' :
            if len(stack) == 0 :
                break
            elif stack[-1] == '[' :
                del stack[-1]
            else :
                break

    if stack == [] :
        print('YES')
    else :
        print('NO')