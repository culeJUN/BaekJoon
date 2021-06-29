n = int(input())
score = list(map(int, input().split()))

high = max(score)
sum = 0

for i in range(n) :
    score[i] = score[i] / high * 100
    sum += score[i]

print(sum / n)