import sys
input = sys.stdin.readline

n = int(input())
N = list(sorted(map(int, input().split())))     # 값 받자마자 정렬
m = int(input())
M = list(map(int, input().split()))

def binary(i, N, start, end) :
    if start > end :                            # 순서가 이상하면 0
        return 0
    m = (start + end) // 2                      # 중간값 지정
    if i == N[m] :                              # 같으면 1
        return 1
    elif i < N[m] :                             # 중간값보다 작으면
        return binary(i, N, start, m - 1)           # 중간보다 작은 범위에서 다시 검색
    else :                                      # 중간값보다 크면
        return binary(i, N, m + 1, end)             # 중간보다 큰 범위에서 다시 검색

for i in M :
    start = 0                                   # 시작
    end = len(N) - 1                            # 마지막
    print(binary(i, N, start, end))