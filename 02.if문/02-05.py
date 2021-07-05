h, m = input().split()
h = int(h)
m = int(m)

if m >= 45 :
    m -= 45
    print(str(h) + ' ' + str(m))
else :
    if h == 0 :
        h = 23
    else :
        h -= 1
    m += 15    
    print(str(h) + ' ' + str(m))
    print()