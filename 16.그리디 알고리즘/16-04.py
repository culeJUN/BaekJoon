sik = input().split('-')        # 제일 큰 수를 뺴야 되므로 -기준으로 분리
num = []
for i in sik :
    sum = 0
    short = i.split('+')            # 분리된 식들 계산하기 위해 분리
    for j in short :
        sum += int(j)                   # 더하기
    num.append(sum)

n = num[0]
for i in range(1, len(num)) :       # 더해 놓은 것들 서로 빼주기
    n -= num[i]                         

print(n)