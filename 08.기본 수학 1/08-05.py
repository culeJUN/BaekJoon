num = int(input())

for i in range(num) :
    H, W, N = map(int, input().split())
    floor = 1
    room_num = 1
    while True :
        if H < N :
            N -= H
            room_num += 1
        else : 
            break
    floor = N
    print('%d'%floor + '%02d'%room_num)