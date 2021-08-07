import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
data = [0]

for i in range(n) :
    low = 0
    high = len(data) - 1
    while low <= high :
        mid = (low + high) // 2
        if data[mid] < A[i] :
            low = mid + 1
        else :
            high = mid - 1
    if low >= len(data) :
        data.append(A[i])
    else :
        data[low] = A[i]

print(len(data) - 1)