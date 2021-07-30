import sys
n = int(sys.stdin.readline())
points = []
for _ in range(n) :
    points.append(tuple(map(int, sys.stdin.readline().split())))
points = list(set(points))          # set으로 중복 제거
points.sort(key=lambda x: x[0])     # x 좌표 기준 정렬

def distance(a, b) :
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def short(m) :
    if len(m) == 2 :
        return distance(m[0], m[1])
    elif len(m) == 3 :
        return min(distance(m[0], m[1]), distance(m[1], m[2]), distance(m[0], m[2]))
    else :
        mid = len(m) // 2
        minimum = min(short(m[:mid]), short(m[mid:]))           # 분할 정복으로 양쪽에서 구해지는 거리 최소값을 minimum에 저장

        # 여기서 부터는 가운데에서 나뉜 애들 양 옆의 거리를 측정
        temp = []
        for i in range(len(m)) :
            if (m[i][0] - m[mid][0]) ** 2 < minimum :              # x 좌표의 차이가 minimum 보다 작으면 후보군에 저장
                temp.append(m[i])

        if len(temp) >= 2 :                                     # 일단 값이 2개 이상 있어야 거리가 존재
            temp.sort(key=lambda x: x[1])                           # y값 기준 정렬
            for i in range(len(temp) - 1) :                         
                for j in range(i + 1, len(temp)) :                      
                    if (temp[i][1] - temp[j][1]) ** 2 > minimum :               # i와 j의 y 좌표가 최소 거리보다 크면 break
                        break
                    elif temp[i][0] < m[mid][0] and temp[j][0] < m[mid][0] :    # i와 j의 x좌표가 중간 좌표보다 작으면 이미 검사했던거라 pass
                        continue
                    elif temp[i][0] >= m[mid][0] and temp[j][0] >= m[mid][0] :  # i와 j의 x좌표가 중간 좌표보다 크면 이미 검사했던거라 pass
                        continue
                    minimum = min(minimum, distance(temp[i], temp[j]))          # 위 세 경우가 다 아니라면 최소값이랑 좌표거리 비교후 저장
        return minimum
if n != len(points) :           # 중복이 있다는 뜻! 즉 최소 거리는 0이 된다.
    print(0)
else :                 
    print(short(points))