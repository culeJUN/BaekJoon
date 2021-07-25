from collections import deque
import sys
input = sys.stdin.readline

case = int(input())
for i in range(case) :
    reverse = 0
    error = 0
    command = input()
    num = int(input())
    list_num = deque(input()[1:-2].split(","))
    if list_num[0] == '' :              # 비어있는 덱이면 ''이라고 들어오는거 방지
        list_num.pop()  
        
    for j in command :
        if j == 'R' :                       # 매번 뒤집지 말고 그냥 뒤집었는지 확인
            reverse += 1

        elif j == 'D' :
            if len(list_num) == 0 :
                print('error')
                error = 1                       # 에러 체크
                break

            elif reverse % 2 == 0 :             # 안뒤집었다면 맨앞 pop
                list_num.popleft()

            elif reverse % 2 == 1 :             # 뒤집었다면 맨뒤 pop
                list_num.pop()

    if reverse % 2 == 1 :                # 마지막에 뒤집어져있어야 된다면 뒤집어 주기
        list_num.reverse()

    if not error :
        print('[', end = '')
        for k in range(len(list_num)) :
            print(list_num[k], end = '')
            if k != len(list_num) - 1 :
                print(',', end = '')
        print(']')