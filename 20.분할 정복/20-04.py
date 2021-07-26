def power(x, y) :
    if(y == 1) :
        return x % C
    else :
        temp = power(x, y // 2)
        if y % 2 == 0 :
            return temp * temp % C
        else :
            return temp * temp * x % C

A, B, C = map(int, input().split())
answer = power(A, B)
print(answer)