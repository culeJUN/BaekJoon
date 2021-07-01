x, y = input().split()
x = list(x)
y = list(y)
x.reverse()
y.reverse()
x_ = ""
y_ = ""

for i in x :
    x_ += i

for i in y :
    y_ += i

if int(x_) > int(y_) :
    print(x_)
else :
    print(y_)