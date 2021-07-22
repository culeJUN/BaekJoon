def GCD(a, b) :
    if a % b == 0 :
        return b
    else :
        return GCD(b, a % b)

num = int(input())
r = list(map(int, input().split()))

for i in range(1, len(r)) :
    gcd = GCD(r[0], r[i])
    print(str(r[0] // gcd) + '/' + str(r[i] // gcd))