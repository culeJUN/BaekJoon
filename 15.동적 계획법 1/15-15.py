x = int(input())
num = list(map(int, input().split()))
table = [num[0]]

for i in range(x - 1) :
    table.append(max(table[i] + num[i + 1], num[i + 1]))    #앞에 누적수에 지금 수 더한거 보다 그냥 지금 수가 더 크면 지금 수 저장

print(max(table))