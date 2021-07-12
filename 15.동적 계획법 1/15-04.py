data = [0] * 101
data[0] = 0
data[1] = 1
data[2] = 1
data[3] = 1

def pado(x) :
    if data[x] :
        return pado[x]
    else :
        data[x] = pado(x - 2) + pado(x - 3)

n = int(input())
for i in range(n) :
    x = int(input())
    for j in range(4, x + 1) :
        if data[x] :
            continue
        else :
            data[j] = data[j - 2] + data[j - 3]
    print(data[x])