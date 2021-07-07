import sys

n = int(sys.stdin.readline())
list_num = []
for i in str(n) :
    list_num.append(int(i))

list_num.sort(reverse = True) 

for i in list_num :
    sys.stdout.write(str(i))