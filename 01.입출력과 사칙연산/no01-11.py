a = int(input())
b = int(input())

r1 = a * (b % 10)
r2 = a * (b % 100 // 10)
r3 = a * (b // 100)
result = a * b

print(r1)
print(r2)
print(r3)
print(result)