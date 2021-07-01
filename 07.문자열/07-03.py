s = list(input())
alphabet = []
for i in range(26) :
    alphabet.append(-1)

for i in range(len(s)) :
    if alphabet[ord(s[i])-97] == -1 :
        alphabet[ord(s[i])-97] = i

for i in alphabet :
    print(i, end = ' ')