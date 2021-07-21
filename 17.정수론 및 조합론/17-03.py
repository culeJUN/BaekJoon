import sys

def gcd(a, b) :
    if a % b == 0 :
        return b
    else :
        return gcd(b, a % b)

x, y = map(int, sys.stdin.readline().split())
small = gcd(x, y)
large = x * y // small

print(small)
print(large)