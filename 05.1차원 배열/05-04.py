left = []
count = 1

for i in range(10) :
    x = int(input())
    x = x % 42
    left.append(x)

left.sort()

for i in range(9) :
    if left[i] != left[i + 1] :
        count += 1

print(count)