A = int(input())
B = int(input())
C = int(input())
n = A * B * C

list_x = []
for i in str(n) :
    list_x.append(int(i))

list_n = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(len(list_x)) :
    list_n[list_x[i]] += 1

for i in range(len(list_n)) :
    print(list_n[i])
    print()