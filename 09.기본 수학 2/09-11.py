import math

time = int(input())
for i in range(time) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    r_l = r1 + r2
    r_s = r1 - r2 
    if r_s < 0 :
        r_s = -1 * r_s

    if r_s < d and d < r_l :
        print(2) 
    elif (r_s == d or d == r_l) and d != 0:
        print(1)
    elif r_l < d or d < r_s :
        print(0)
    else :
        print(-1)