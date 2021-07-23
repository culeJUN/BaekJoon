time = int(input())

for i in range(time):
    case = int(input())    
    clothes_type = {}                       # 딕셔너리
    for j in range(case):
        name, type = input().split()
        if type in clothes_type :
            clothes_type[type] += 1
        else:
            clothes_type[type] = 1
    
    answer = 1    
    for key in clothes_type.keys():
        answer *= clothes_type[key] + 1     # 안입는 거 포함해서 곱해주기
    
    print(answer - 1)                   # 아무것도 안입는거 1 빼주기