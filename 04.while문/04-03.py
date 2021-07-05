num = int(input())
count = 0
temp = num

while 1 :
    front = temp // 10
    back = temp % 10
    last = (front + back) % 10
    result = (10 * back) + last
    count += 1
    if result == num :
        break
    temp = result

print(count)
print()