import sys
input = sys.stdin.readline

queue = []
front = 0
num = int(input())
for i in range(num) :
    command = input().split()
    if command[0] == 'push' :
        queue.append(command[1])
    
    elif command[0] == 'pop' :
        if len(queue) - front <= 0 :
            print(-1)
        else :
            print(queue[front])
            front += 1

    elif command[0] == 'size' :
        print(len(queue) - front)

    elif command[0] == 'empty' :
        if len(queue) - front <= 0 :
            print(1)
        else : 
            print(0)
    
    elif command[0] == 'front' :
        if len(queue) - front <= 0 :
            print(-1)
        else :
            print(queue[front])
    
    elif command[0] == 'back' :
        if len(queue) - front <= 0  :
            print(-1) 
        else :
            print(queue[-1])