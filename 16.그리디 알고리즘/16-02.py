num = int(input())
time = []
for i in range(num):
    start, end = map(int, input().split())
    time.append([start, end])
time = sorted(time, key=lambda a: a[1])     #끝나는 시간 기준 올림차순정렬
last = 0                #끝나는 시간 저장
cnt = 0
for i, j in time:       #타임 리스트에 저장된 시작, 종료 시간이 i랑 j에 저장됨
    if i >= last:           #시작시간이 끝나는 시간보다 뒤면 회의 예약 완료
        cnt += 1
        last = j
print(cnt)