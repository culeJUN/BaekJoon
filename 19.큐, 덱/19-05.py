import sys
input = sys.stdin.readline

deque = []
num = int(input())
for i in range(num) :
    command = input().split()
    if command[0] == 'push_front' :
        deque.insert(0, command[1])

    elif command[0] == 'push_back' :
        deque.append(command[1])

    elif command[0] == 'pop_front' :
        if deque == [] :
            print(-1)
        else :
            print(deque[0])
            del deque[0] 

    elif command[0] == 'pop_back' :
        if deque == [] :
            print(-1)
        else :
            print(deque[-1])
            del deque[-1] 

    elif command[0] == 'size' :
        print(len(deque))

    elif command[0] == 'empty' :
        if deque == [] :
            print(1)
        else :
            print(0)

    elif command[0] == 'front' :
        if deque == [] :
            print(-1)
        else :
            print(deque[0])

    elif command[0] == 'back' :
        if deque == [] :
            print(-1)
        else :
            print(deque[-1])