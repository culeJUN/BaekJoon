n = int(input())
stack = []
operation = []
count = 1
temp = True
for i in range(n):
    num = int(input())
    while count <= num:
        stack.append(count)
        operation.append('+')
        count += 1
        
    if stack[-1] == num:
        stack.pop()
        operation.append('-')
    else:
        temp = False

if temp == False:
    print('NO')
else:
    for i in operation:
        print(i)