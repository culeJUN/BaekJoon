import sys
input = sys.stdin.readline
stack = []

num = int(input())
for i in range(num) :
    command = int(input())
    if command != 0 :
        stack.append(command)
    else :
        del stack[-1]

print(sum(stack))