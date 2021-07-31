from sys import stdin
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int,stdin.readline().split())

def binary(i, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if i == N[m]:
        return N[start:end+1].count(i)
    elif i < N[m]:
        return binary(i, N, start, m-1)
    else:
        return binary(i, N, m+1, end)

count = {}
for i in N:
    start = 0
    end = len(N) - 1
    if i not in count:
        count[i] = binary(i, N, start, end)

print(' '.join(str(count[x]) if x in count else '0' for x in M ))