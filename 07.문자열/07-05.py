import copy

s = input().upper()
alphabet = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
check = []
result = 0

for i in range(len(s)) :
    alphabet[ord(s[i]) - 65] += 1
        
check = copy.deepcopy(alphabet)
check.sort(reverse = True)

if check[0] == check[1] :
    print('?')
else :
    result = alphabet.index(max(alphabet))
    print(chr(result + 65))