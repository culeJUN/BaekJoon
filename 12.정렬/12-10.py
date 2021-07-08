import sys

n = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
num_list = sorted(list(set(num)))                       #작은 수 부터 정렬(중복 제거하고)
dic = {num_list[i] : i for i in range(len(num_list))}   #num_list길이 만큼 작은 수 : 몇번째로 작은지 라는 딕셔너리

for i in num:
    sys.stdout.write(str(dic[i]) + ' ')