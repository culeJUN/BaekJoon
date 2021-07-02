a , b, v = map(int, input().split())
count = 0

if (v - a) % (a - b) == 0 :
    count = (v - a) // (a - b) + 1
else :
    count = (v - a) // (a - b) + 2
    
print(count)
