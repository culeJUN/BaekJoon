x = int(input())
num = list(map(int, input().split()))
data = [1] * x 

for i in range(1, x) :
    for j in range(i) :
        if num[j] < num[i] :
            data[i] = max(data[i], data[j] + 1)

print(max(data))