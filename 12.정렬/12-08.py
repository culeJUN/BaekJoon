n = int(input())
word_list = []
for i in range(n) :
    word = input()
    word_len = len(word)
    word_list.append((word, word_len))

word_list.sort(key = lambda x : (x[1], x[0]))

for i in range(n - 1) :
    if word_list[i] == word_list[i + 1] :
        word_list[i] = 0
    
for i in word_list :
    if i != 0 :
        print(i[0])