a, b, c = map(int, input().split())
if b < c :
    d = c - b
    x = a // d + 1
else : 
    x = -1
print(x)