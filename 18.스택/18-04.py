while True:
    s = input()
    if s == '.':
        break
    stack = []
    temp = True
    for i in s:
        if i == '(' or i == '[':
            stack.append(i)

        elif i == ')':
            if not stack or stack[-1] != '(':       # 스택이 비어있거나 마지막이 '('이 아니라면
                temp = False
                break
            elif stack[-1] == '(':
                stack.pop()

        elif i == ']':
            if not stack or stack[-1] != '[':       # 스택이 비어있거나 마지막이 '['이 아니라면
                temp = False
                break
            elif stack[-1] == '[':
                stack.pop()

    if temp == True and not stack:
        print('yes')
    else:
        print('no')