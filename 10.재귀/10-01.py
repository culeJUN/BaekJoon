def pactorial(i) :
    if i == 0 :
        return 1
    if i == 1 :
        return 1
    return i * pactorial(i - 1)

x = int(input())
print(pactorial(x))