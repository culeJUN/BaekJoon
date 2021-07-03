N = 123456 * 2 + 1
num = [i for i in range(1, N + 1)]
for i in range(2, int(N ** 0.5) + 1):
    if num[i] != 0:
        for j in range(2 * i, N, i):
            num[j] = 0

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if num[i] != 0 :
            cnt += 1
    print(cnt)

while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)