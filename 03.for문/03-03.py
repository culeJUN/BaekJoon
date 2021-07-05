n = int(input())
sum = 0

if n % 2 == 0 :
    sum = (1 + n) * (n // 2)
else :
    sum = (1 + n) * (n // 2) + (n // 2 + 1)

print(sum)