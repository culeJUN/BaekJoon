line = int(input())
A2B = []
for _ in range(line):
    A, B = map(int, input().split())
    A2B.append([A,B])

A2B = sorted(A2B, key = lambda x: x[0])

result = [[] for _ in range(line)]
for i in range(line):
    if i == 0:
        result[i].append(A2B[i][1])
    else:
        for j in range(0, i):
            if result[j][-1] < A2B[i][1]:
                if len(result[i]) - 1 < len(result[j]):
                    result[i] = result[j] + [A2B[i][1]]
                    
        if not result[i]:
            result[i].append(A2B[i][1])

maximum = 0
for i in range(line):
    maximum = max(maximum, len(result[i]))
print(line - maximum)