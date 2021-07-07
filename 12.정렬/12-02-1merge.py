import sys

def merge_sort(array):
    if len(array)<=1:                           #리스트 길이 1보다 작으면 그냥 리턴
        return array
    mid = len(array) // 2                       #가운데 자르기 위한 mid값
    left = merge_sort(array[:mid])              #왼쪽 오른쪽 계속 반 가르기
    right = merge_sort(array[mid:])

    i,j,k = 0,0,0
    while i < len(left) and j < len(right):     #left와 right에 값이 아직 있다면
        if left[i] < right[j]:                  #left랑 right 비교후 작은 수 array에 저장
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k+=1
    
    if i==len(left):                            #left나 right에 값이 없다면 남은 값들 array에 저장
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
    elif j==len(right):
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
            
    return array

n=int(input())
num = []
for i in range(n):
    num.append(int(sys.stdin.readline()))

num = merge_sort(num)
for i in num:
    sys.stdout.write(str(i) + '\n')