n = int(input())
information = []

for i in range(n) :
    age, name = input().split()
    age = int(age)
    information.append((age, name, i))

information.sort(key = lambda x : (x[0], x[2]))

for i in information :
    print(i[0], i[1])