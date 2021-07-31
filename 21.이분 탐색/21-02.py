import sys
input = sys.stdin.readline

n = int(input())
N = list(sorted(map(int, input().split())))
m = int(input())
M = list(map(int, input().split()))

def binary(i, N, start, end) :
    if start > end :
        return 0 
    m = (start + end) // 2
    if i == N[m] :
        return N[start:end + 1].count(i)
    elif i < N[m] :
        return binary(i, N, start, m - 1)
    else :
        return binary(i, N, m + 1, end)

count = {}
for i in N :
    start = 0
    end = len(N) - 1
    if i not in count :
        count[i] = binary(i, N, start, end)
        
print(' '.join(str(count[x]) if x in count else '0' for x in M)) 