import sys 
from collections import Counter

time = int(sys.stdin.readline())
list_num = []
for i in range(time) :
    list_num.append(int(sys.stdin.readline()))

list_num.sort()
print(round(sum(list_num) / time))
print(list_num[time // 2])

count = Counter(list_num).most_common()
if len(count) > 1 and count[0][1]==count[1][1]: #최빈값 2개 이상
    print(count[1][0])
else:
    print(count[0][0])

print(max(list_num) - min(list_num))