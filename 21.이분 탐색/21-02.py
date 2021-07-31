from sys import stdin
n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = map(int,stdin.readline().split())

def binary(n, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if n == N[m]:
        return N[start:end+1].count(n)
    elif n < N[m]:
        return binary(n, N, start, m-1)
    else:
        return binary(n, N, m+1, end)

count = {}
for n in N:
    start = 0
    end = len(N) - 1
    if n not in count:
        count[n] = binary(n, N, start, end)

print(' '.join(str(count[x]) if x in count else '0' for x in M ))