import sys

def heapSort(unsorted):                     # max heap 트리로 배열의 순서를 바꿔줘서 오름차순으로 정렬
    n = len(unsorted)
    for i in range(n // 2 - 1, -1, -1):     # 최대 힙을 구하는 반복문
        heapify(unsorted, i, n)
 
    for i in range(n - 1, 0, -1):           #오름 차순으로 정렬하는 부분
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]     # 자리를 바꿔줌으로서 젤 큰 값을 맨 뒤로 보내주게 된다
        heapify(unsorted, 0, i)                                 # 맨 뒤로 보낸 값 빼고 다시 max heap으로 바꿔준다
 
    return unsorted
 
def heapify(unsorted, index, heap_size):    # 리스트를 max heap 형태로 바꾸는 함수
    largest = index                         # 루트 노드를 largest에 저장
    left_index = 2 * index + 1              
    right_index = 2 * index + 2             
 
    # 만약 왼쪽 인덱스가 힙 사이즈보다 작고, 트리 왼쪽 값이 트리에서 가장 큰 값보다 크다면 왼쪽 인덱스를 largest로 바꾼다
    # left_index가 2*index+1이여서 리스트의 범위를 벗어나는 경우가 있기 때문에 확인 해야 한다
    if left_index < heap_size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
 
    # 오른쪽도 마찬가지로 해준다
    if right_index < heap_size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
 
    # largest가 기존에 예상했던 index가 아니라면 largest와 index의 자리를 바꿔준다, 즉 트리의 노드를 바꿔주는 것
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, heap_size)
 
 
m = int(input())
arr = []
for i in range(m):
    arr.append(int(sys.stdin.readline()))

arr = heapSort(arr)
for i in range(m):
    sys.stdout.write(str(arr[i]) + '\n')