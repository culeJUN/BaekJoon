import sys

def gcd(a, b) :
    if a % b == 0 :
        return b
    else :
        return gcd(b, a % b)

def lcm(a, b) :
    return a * b // gcd(a, b)

num = int(sys.stdin.readline())
for i in range(num) :
    x, y = map(int, sys.stdin.readline().split())
    print(lcm(x, y))