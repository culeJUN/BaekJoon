import sys

stair = []
data = []
total = int(sys.stdin.readline())
for i in range(total) :
    stair.append(int(sys.stdin.readline()))

data.append(stair[0])
if total >= 2 :
    data.append(max(stair[0] + stair[1], stair[1]))
if total >= 3 :
    data.append(max(stair[0] + stair[2], stair[1] + stair[2]))
for i in range(3, total) :
    data.append(max(data[i - 2] + stair[i], data[i - 3] + stair[i - 1] + stair[i]))

sys.stdout.write(str(data[-1]))