x, y, w, h = map(int, input().split())
list_distance = []

list_distance.append(x)
list_distance.append(w - x)
list_distance.append(y)
list_distance.append(h - y)

print(min(list_distance))